from flask import Flask, render_template, request, redirect, flash
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Load the secret key from .env

# Database connection function
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("host"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            dbname=os.getenv("dbname"),
            port=int(os.getenv("port")),
        )
        return conn
    except psycopg2.OperationalError as e:
        print("❌ Database Connection Failed:", e)
        return None  # Return None to handle the failure gracefully

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

        # Connect to the database
        conn = get_db_connection()
        if conn is None:
            flash("⚠️ Database is currently unavailable. Please contact us via:\n📧 arisuconnect@gmail.com\n📞 +91-6306181422.", 'danger')
            return redirect('/contact')

        try:
            cursor = conn.cursor()
            query = "INSERT INTO contacts (name, email, subject, message) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, email, subject, message))
            conn.commit()

            flash('✅ Message sent successfully!', 'success')

        except psycopg2.Error as e:
            print("❌ Database Query Failed:", e)
            flash("⚠️ There was an error processing your request. Please contact us via:\n📧 arisuconnect@gmail.com\n📞 +91-6306181422.", 'danger')

        finally:
            if conn:
                cursor.close()
                conn.close()

        return redirect('/contact')

    return render_template('contact.html')

# Custom error handler for 500 errors
@app.errorhandler(500)
def handle_internal_server_error(e):
    print(f"❌ Internal Server Error: {e}")  # Log error for debugging
    return render_template("error"), 500  # Custom error page

if __name__ == '__main__':
    app.run(debug=True)