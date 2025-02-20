# Class Activity 7: AI-Powered Testing and Development Evaluation

## **Project Goals**
In this activity, students will:
- Practice **unit testing** and **integration testing**.
- Explore the **capabilities and limitations of AI** in test generation.
- Apply **Test-Driven Development (TDD)** principles to improve software reliability.

By the end of this activity, students will have **analyzed AI-generated tests**, **compared AI-written vs. human-written implementations**, and **gained insights into AI’s strengths and weaknesses in software development**.


## **Program**
The activity is divided into two main parts. Students will generate test cases using **AI tools** and compare them with their manually written tests.

### Part 1
AI-generated test cases for a **Tic-Tac-Toe** implementation and compare them with the manually written tests from Activity 3.

### Requirements

#### 1. Understand the Provided Code
The provided Tic-Tac-Toe implementation consists of the following files:
- `tic_tac_toe/tic_tac_toe.py` 
- `tic_tac_toe/test_tic_tac_toe.py`

There are three classes in `tic_tac_toe.py` file:
- `Player` – class that implements a player with name and tracks the number of wins.
- `Board` – class that implements game and board logic.
- `Game` – class that implements initialize the board and players.

Review the provided code and identify key functions that require testing:

#### 2. Generate AI-Based Test Cases
Use **AI tools** (ChatGPT, Copilot, etc.) to generate test cases.
- Use the prompts provided in `test_tic_tac_toe.py` to generate tests:
- Copy and paste AI-generated test cases into:
  - `test_tic_tac_toe.py`
#### 3. Run and Evaluate the Tests
- Execute and evaluate and report the test coverage. 
  - If AI-generated tests fail, try to identify and fix any issues in the tests (if necessary).
  - Modify or add missing test cases to improve coverage.
- Share your thoughts and reflections in a `reflections.txt` file::
  - How did AI-generated tests compare to manually written tests?
  - Were the tests valid, well-structured, and useful?
  - Did AI correctly identify edge cases?
  - Did AI generate any incorrect tests that failed?
  - What are the strengths and weaknesses of using AI for test generation?

### Part 2
AI-generated test cases for a simplified **Authentication Service** with these features. 

- In this authentication system, users can register for a new account with a unique username and a unique and valid email format. 
- The system requires users to provide a complex password with upper case and lowercase letter, numbers and minimum 8 character.
- Each user has a rate limitation for sending requests (identified by their username or email) which is set to be a default values of 5 requests in the last 2 minutes.
- After 10 failed loging attempts in a 1-hour window, the user account will be locked.
- After a successful login the user have an active session with a token that expires after two hours.

### Requirements
#### 1. Understand the Provided Code
The provided Tic-Tac-Toe implementation consists of the following files:
- `auth_service/auth_service.py` 
- `auth_service/user.py`

There are two classes in Authentication Service implementation:
- `AuthService` – class that implements a simplified login and signup functionalities and store users data in an in memory dictionary.
- `User` – class that implements a user.

Review the provided code and identify key functions that require testing.
#### 2. Generate AI-Based Test Cases
Use **AI tools** (ChatGPT, Copilot, etc.) to generate test cases.
- Use the prompts provided in `test_auth_service.py` to generate tests:
- Copy and paste AI-generated test cases into:
  - `test_auth_service.py`
#### 3. Run and Evaluate the Tests
- Execute and evaluate and report the test coverage. 
  - If AI-generated tests fail, try to identify and fix any issues in the tests (if necessary).
  - Add at least 5 more test cases to improve coverage.
- Share your thoughts and reflections in a `reflections.txt` file:
  - How did AI-generated tests compare to manually written tests?
  - Were the tests valid, well-structured, and useful?
  - Did AI correctly identify edge cases?
  - Did AI generate any incorrect tests that failed?
  - What are the strengths and weaknesses of using AI for test generation?

### Submission Details
If you are using git from the command line, execute the following commands:
1. After accepting the assignment invitation, copy the clone URL
2. Type `git clone clone URL`
3. cd into your new assignment directory
4. After working on your files
5. When you’re ready, type the following commands:
     ```sh
    git add .
    git commit -m “your commit message”
    git push
     ```