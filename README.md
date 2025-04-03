# Portfolio Website

This is a personal portfolio website built using Flask, PostgreSQL, and HTML/CSS. The website showcases projects, skills, and provides a contact form for visitors.

## 🚀 Features
- **Home Page** – Introduction and overview.
- **About Page** – Details about education and experience.
- **Skills Page** – List of technical skills.
- **Projects Page** – Showcases various projects.
- **Contact Page** – Users can send messages via a contact form.
- **Database Integration** – Stores contact form messages in a PostgreSQL database.

## 🛠 Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Hosting**: Render.com

## 🔧 Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ArisuAbhilash/Portfolio-website
cd Portfolio-website
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add:
```
DB_HOST=your_db_host
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_PORT=your_db_port
PHONE_NUMBER=your_phone_number
EMAIL=your_email
```

### 5️⃣ Run the Application
```sh
flask run
```
Visit `http://127.0.0.1:5000` in your browser.

## 🌐 Deployment on Render
1. Push your code to GitHub.
2. Create a new Web Service on [Render](https://render.com/).
3. Select your GitHub repo and set the build command:
   ```sh
   pip install -r requirements.txt
   ```
4. Set the **Start Command**:
   ```sh
   gunicorn app:app
   ```
5. Add environment variables in Render's dashboard.
6. Deploy and get your live website link!

## 📩 Contact
If you face any issues, feel free to reach out:
- **Email**: arisuconnect@gmail.com
- **LinkedIn**: www.linkedin.com/in/abhilash-maurya-365a941b8

---
⭐ *If you find this project helpful, consider giving it a star!* ⭐

