from flask import Flask, render_template, request, redirect, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="dpg-cvm0flngi27c73ah9li0-a",
        user="root",
        password="GSOeyeEkuIsPL6LFnsRPtcfYZAikQLEC",
        dbname="contact_form_db_he0f",
        port="5432"
    )
        
    return conn

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

        # Connect to the database and insert contact information
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO contacts (name, email, subject, message) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, email, subject, message))
        conn.commit()

        cursor.close()
        conn.close()

        flash('Message sent successfully!', 'success')
        return redirect('/contact')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)