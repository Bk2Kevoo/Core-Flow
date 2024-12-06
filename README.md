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
- **React.js** (for the frontend)
- **Python** (for the backend)
- **Pipenv** (for virtual environment management)

---

### 🍴 Fork and Clone

1. **Fork the repository** by clicking the "Fork" button in the top-right corner of the repository page.
2. **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/your-username/CoreFlow.git
    ```

---

### 🐍 Backend Setup (Flask)

1. **Navigate to the server folder**:
    ```
    cd CoreFlow/server
    ```

2. **Install dependencies**:
    ```
    pipenv install && pipenv shell
    ```

3. **Initialize the database**:
    ```
    flask db init
    ```

4. **Seed the database**:
    ```
    python seed.py
    ```

5. **Run the Flask server**:
    ```
    flask run
    ```

---

### ⚛️ Frontend Setup (React)

1. Open a new terminal and navigate to the client directory:
    ```
    cd ../client
    ```

2. **Install dependencies**:
    ```
    npm install
    ```

3. **Run the React application**:
    ```
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
