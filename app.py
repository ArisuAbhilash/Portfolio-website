from flask import Flask, render_template, request, redirect, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
        host="dpg-cvm0flngi27c73ah9li0-a",
        user="root",
        password="GSOeyeEkuIsPL6LFnsRPtcfYZAikQLEC",
        dbname="contact_form_db_he0f",
        port="5432",
        )
        return conn
    except psycopg2.OperationalError as e:
        print("❌ Database Connection Failed:", e)
        return None
    
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
        if conn is None:
            flash('⚠️ There was an error processing your request.'
            '\n Please reach out via: \n'
            '📧 arisuconnect@gmail.com \n 📞 +91-6306181422.', 'danger')

        try:
            cursor = conn.cursor()

            query = "INSERT INTO contacts (name, email, subject, message) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, email, subject, message))
            conn.commit()

            cursor.close()
            conn.close()

        except psycopg2.Error as e:
            print("❌ Database Query Failed:", e)
            flash('⚠️ There was an error processing your request.'
            '\n Please reach out via: \n'
            '📧 arisuconnect@gmail.com \n 📞 +91-6306181422.', 'danger')
       
        finally:
            if conn:
                conn.close()
                flash('Message sent successfully!', 'success')
        return redirect('/contact')
    
    return render_template('contact.html')

# Custom error handler for 502 and other errors
@app.errorhandler(502)
@app.errorhandler(500)
@app.errorhandler(Exception)
def handle_error(e):
    print(f"❌ Server Error: {e}")  # Log the error for debugging
    return render_template("error.html"), 500  # Show custom error page




if __name__ == '__main__':
    app.run(debug=True)