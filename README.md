# smart-notes-app

A simple Flask-based note-taking application with user authentication.

## Setup Instructions

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up MySQL database:
   - Create a MySQL database named `smart_notes`
   - Run the SQL commands in `database_setup.sql`
   - Update the database credentials in `app.py`

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and go to `http://localhost:5000`

## Features

- User registration and login
- Create and view personal notes
- Secure password hashing
- Session management

## Database Configuration

Update the database connection settings in `app.py`:
```python
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="smart_notes"
)
```