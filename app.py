from flask import Flask, render_template, request, redirect, session, flash
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # Change this
    database="smart_notes"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                       (username, email, password))
        db.commit()
        flash("Registered successfully! Please login.")
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode()).hexdigest()
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect('/dashboard')
        else:
            flash("Invalid credentials.")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    cursor.execute("SELECT * FROM notes WHERE user_id = %s", (session['user_id'],))
    notes = cursor.fetchall()
    return render_template('dashboard.html', notes=notes, username=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if 'user_id' not in session:
        return redirect('/login')
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cursor.execute("INSERT INTO notes (user_id, title, content) VALUES (%s, %s, %s)",
                       (session['user_id'], title, content))
        db.commit()
        flash("Note added successfully!")
        return redirect('/dashboard')
    
    return render_template('add_note.html')

if __name__ == '__main__':
    app.run(debug=True)
    return redirect('/')

@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if 'user_id' not in session:
        return redirect('/login')
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        cursor.execute("INSERT INTO notes (user_id, title, content) VALUES (%s, %s, %s)",
                       (session['user_id'], title, content))
        db.commit()
        flash("Note added successfully!")
        return redirect('/dashboard')
    
    return render_template('add_note.html')

if __name__ == '__main__':
    app.run(debug=True)