from collections import defaultdict
from user import User

import secrets, time, hashlib, re


class AuthService:
    """Handles authentication, registration, rate limiting, and session management."""

    def __init__(self):
        self.users_db = {}  # In-memory user database (email -> User)
        self.token_store = {}  # Temporary storage for password reset tokens
        self.request_attempts = defaultdict(list)  # Tracks login/signup attempts {email/IP: [timestamps]}
        self._populate_initial_data()

    def _populate_initial_data(self):
        """Populate the database with 3 records for testing."""
        self.register("alice", "alice@example.com", "Secure123!")
        self.register("bob", "bob@example.com", "Password$456")
        self.register("charlie", "charlie@example.com", "Hello@World1")

    def _rate_limit(self, identifier, limit=5, time_window=120):
        """
        Implements a simplified rate limiting:
        - Allows `limit` attempts per `time_window` seconds.
        - If limit exceeded, deny access temporarily.
        """
        now = time.time()

        # Remove outdated attempts
        self.request_attempts[identifier] = [t for t in self.request_attempts[identifier] if now - t < time_window]

        # If exceeded short-term limit (5 attempts in 2 minutes), deny access temporarily
        if len(self.request_attempts[identifier]) >= limit:
            return False, "Too many attempts. Please wait before trying again."

        # Log new attempt
        self.request_attempts[identifier].append(now)
        return True, None

    @staticmethod
    def _hash_password(password):
        """Securely hash a password using PBKDF2."""
        salt = secrets.token_hex(16)
        hash_value = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100000)
        return f"{salt}${hash_value.hex()}"

    @staticmethod
    def _verify_password(stored_hash, password):
        """Verify a password against the stored hash."""
        salt, stored_hash_value = stored_hash.split("$")
        hash_value = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100000)
        return stored_hash_value == hash_value.hex()

    @staticmethod
    def _is_valid_email(email):
        """Validate email format using regex."""
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_pattern, email) is not None

    @staticmethod
    def _is_strong_password(password):
        """Check if the password meets security requirements."""
        return (
                len(password) >= 8 and
                any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in password)
        )

    def register(self, username, email, password):
        """Register a new user with security checks."""
        allowed, message = self._rate_limit(email)
        if not allowed:
            return message
        if email in self.users_db:
            return "Email already registered."
        if any(user.username == username for user in self.users_db.values()):
            return "Username already taken."
        if not self._is_valid_email(email):
            return "Invalid email format."
        if not self._is_strong_password(password):
            return "Password must be strong."

        password_hash = self._hash_password(password)
        self.users_db[email] = User(username, email, password_hash)
        return "Account successfully created."

    def login(self, identifier, password):
        """Authenticate a user with account locking and session creation."""
        allowed, message = self._rate_limit(identifier)
        if not allowed:
            return message
        user = self.users_db.get(identifier) or next((u for u in self.users_db.values() if u.username == identifier),
                                                     None)
        if not user:
            return "User not found."
        if user.is_locked():
            return "Account is locked. Try again later."

        if not self._verify_password(user.password_hash, password):
            user.increment_failed_attempts()
            return "Invalid password."

        user.reset_failed_attempts()
        token = user.create_session()
        return f"Login successful. Token: {token}"

    def logout(self, token):
        """Logout a user by invalidating their session."""
        for user in self.users_db.values():
            if user.logout(token):
                return "Logout successful."
        return "Invalid token."

    def reset_password(self, email, old_password, new_password):
        """Reset password with rate limiting."""
        allowed, message = self._rate_limit(email)
        if not allowed:
            return message

        if email not in self.users_db:
            return "User not found."

        user = self.users_db[email]
        if not self._verify_password(user.password_hash, old_password):
            return "Old password is incorrect."
        if user.old_password_hash and self._verify_password(user.old_password_hash, new_password):
            return "New password cannot be the same as the last password."
        if not self._is_strong_password(new_password):
            return "Password must be strong."

        user.update_password(self._hash_password(new_password))
        return "Password reset successful."



