from flask import Flask, render_template


app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')


# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)