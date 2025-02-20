import time
import secrets

class User:
    """Represents a user with authentication properties and methods to manage its state."""

    def __init__(self, username, email, password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.old_password_hash = None
        self.failed_attempts = 0
        self.locked_until = None
        self.sessions = {}  # Active sessions: {token: expiry_timestamp}

    def is_locked(self):
        """Check if the user account is locked."""
        return self.locked_until and time.time() < self.locked_until

    def increment_failed_attempts(self):
        """Increment failed login attempts and lock the account if necessary."""
        self.failed_attempts += 1
        if self.failed_attempts >= 10:
            self.locked_until = time.time() + 600  # Lock for 10 minutes

    def reset_failed_attempts(self):
        """Reset failed login attempts."""
        self.failed_attempts = 0
        self.locked_until = None

    def update_password(self, new_hashed_password):
        """Update the user's password, storing the old one to prevent reuse."""
        self.old_password_hash = self.password_hash
        self.password_hash = new_hashed_password

    def create_session(self):
        """Generate a session token and set an expiration time (2 hours)."""
        token = secrets.token_urlsafe(32)
        self.sessions[token] = time.time() + 7200
        return token

    def validate_session(self, token):
        """Check if a session token is valid and active."""
        if token in self.sessions and time.time() < self.sessions[token]:
            return True
        if token in self.sessions:
            del self.sessions[token]  # Remove expired session
        return False

    def logout(self, token):
        """Invalidate a specific session token."""
        if token in self.sessions:
            del self.sessions[token]
            return True
        return False