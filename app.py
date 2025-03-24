from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SMau@1",
    database="contact_form_db"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        query = "INSERT INTO contacts (name, email, subject, message) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, email, subject, message))
        db.commit()

        flash('Message sent successfully!', 'success')
        return redirect('/contact')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)