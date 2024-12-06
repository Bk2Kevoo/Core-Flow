# 🌊 Core Flow

Core Flow is a web application designed to streamline user registration and authentication processes using Flask on the backend and React on the frontend.

---

## ✨ Features

- 🔒 User registration and authentication.
- ⚡ Dynamic front-end interface with React.
- 🛡️ Secure back-end server implemented in Flask.

---

## 🛠️ Technologies Used

- **Frontend**: React, CSS
- **Backend**: Flask, Python
- **Database**: SQLite (or any database compatible with Flask SQLAlchemy)

---

## 🚀 Installation and Setup

### 📋 Prerequisites
Make sure you have the following installed:
- **Node.js** (for the frontend)
- **Python** (for the backend)
- **Pipenv** (for virtual environment management)

---

### 🐍 Backend Setup (Flask)

1. **Navigate to the server folder**:
    ```bash
    cd CoreFlow/server
    ```

2. **Install dependencies**:
    ```bash
    pipenv install
    ```

3. **Initialize the database**:
    ```bash
    flask db init
    ```

4. **Seed the database**:
    ```bash
    python seed.py
    ```

5. **Run the Flask server**:
    ```bash
    flask run
    ```

---

### ⚛️ Frontend Setup (React)

1. Open a new terminal and navigate to the client directory:
    ```bash
    cd ../client
    ```

2. **Install dependencies**:
    ```bash
    npm install
    ```

3. **Run the React application**:
    ```bash
    npm start
    ```

---

## 🔍 Usage

1. Start by registering a new user through the React front-end.
2. Authenticate the registered user to access the main features.
3. The database is pre-seeded with test data to explore the application functionality.

---

## 🤝 Contributing

We welcome contributions to **Core Flow**! Please submit pull requests to share your improvements or report issues via the repository's issue tracker.

---
