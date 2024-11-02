
# CRUD Flask MySQL Application

This is a basic CRUD (Create, Read, Update, Delete) application built using Python's Flask framework and MySQL for the database.

## Features

- **Create**: Add new records to the MySQL database.
- **Read**: View all records in a list.
- **Update**: Edit existing records.
- **Delete**: Remove records from the database.

## Requirements

- Python 3.x
- Flask
- MySQL
- MySQL Connector for Python

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd CRUD_APP
   ```

2. **Set up the database**:

   - Create a new MySQL database:
     ```sql
     CREATE DATABASE crud_app;
     ```
   - Import the schema:
     ```bash
     mysql -u username -p crud_app < schema.sql
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database connection**:
   Update the database connection settings in `app.py` to match your MySQL credentials:
   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'your_username'
   app.config['MYSQL_PASSWORD'] = 'your_password'
   app.config['MYSQL_DB'] = 'crud_app'
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the application**:
   Open your browser and go to `http://127.0.0.1:5000`.

## File Structure

- `app.py`: Main application file with Flask routes and logic.
- `schema.sql`: SQL file to set up the MySQL database.
- `templates/`: Contains HTML files for the frontend.

## Usage

1. **Create**: Use the form to add new entries to the database.
2. **View**: See a list of all entries on the homepage.
3. **Edit**: Click the edit button next to an entry to modify its details.
4. **Delete**: Use the delete button to remove an entry.
