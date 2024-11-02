import os
from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', students=data)


@app.route('/add', methods=['POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        flash('Student Added successfully')
        return redirect(url_for('index'))



@app.route('/update', methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE students SET name=%s, email=%s, phone=%s WHERE id=%s", (name, email, phone, id))
        flash('Student Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('index'))


 
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id = %s", (id,))
    mysql.connection.commit()
    flash('Student Removed Successfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)