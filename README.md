
# Flask CRUD Application with MySQL

This is a basic Flask application implementing CRUD (Create, Read, Update, Delete) functionality using a MySQL database to manage a list of students. This app includes routes to add, edit, view, and delete student records with basic HTML templates for rendering data.

## Features

- **Create**: Add a new student record.
- **Read**: View a list of all student records.
- **Update**: Modify existing student details.
- **Delete**: Remove student records.

## Requirements

- Python 3.x
- Flask
- Flask-MySQLdb
- MySQL

## Setup

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd CRUD_APP
   ```

2. **Create and Configure the Database**

Copy paste the content of `schema.sql` into mysql workbench and run it

3. **Set Up Environment Variables**

Create a `.env` file in the root directory with your MySQL credentials:
   ```env
   MYSQL_HOST=localhost
   MYSQL_USER=your_username
   MYSQL_PASSWORD=your_password
   MYSQL_DB=school_db
   ```

4. **Install dependencies**

Create a requirements.txt file with the following content

```
Flask==3.0.3
Flask-MySQLdb==2.0.0

```
Then, run:
   ```
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```
   python app.py
   ```

6. **Access the application**:
   Open your browser and go to `http://127.0.0.1:5000`.

## File Structure

- `app.py`: Main application file with Flask routes and MySQL configurations.
- `templates/`: Contains HTML templates for displaying and managing student records.
  - `index.html`: Lists students and provides options for adding, updating, and deleting records.

## Usage

- **Homepage (`/`)**: Displays a list of students.
- **Add Student (`/add`)**: POST endpoint to add a new student.
- **Update Student (`/update`)**: POST endpoint to update a student’s details.
- **Delete Student (`/delete/<id>`)**: DELETE endpoint to remove a student.

## Example CRUD Operations

### Add a Student

1. Go to the homepage, fill in the student details in the form, and submit.
2. After submission, the new student record will appear on the homepage list.

### Update a Student

1. Click the "Edit" button next to the student record.
2. Modify the student's details and submit the form.
3. The homepage will refresh with updated details.

### Delete a Student

1. Click the "Delete" button next to a student.
2. The student record will be removed from the database.

