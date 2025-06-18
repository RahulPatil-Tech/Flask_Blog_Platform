<h1 align="center">📝गोड आठवणी </h1>

<p align="center">
  A secure, modern, and responsive blog application built with <strong>Flask</strong>, <strong>MySQL</strong>, and <strong>Bootstrap</strong> 🌐🛡️  
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Framework-Flask-blue.svg" />
  <img src="https://img.shields.io/badge/Database-MySQL-orange" />
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
  <img src="https://img.shields.io/badge/Made%20by-Rahul-blueviolet" />
</p>

---

## 🌟 Overview

Welcome! I'm **Rahul**, and this is a full-featured blogging platform where users can share posts, engage via comments and likes, and manage content with ease. Built using Flask, it includes secure **JWT authentication**, **role-based access control**, and an intuitive **Bootstrap UI** for seamless experience across all devices.

---

## 🚀 Key Features

- 🔐 **JWT Authentication** – Secure login and registration  
- 🛂 **Role-based Permissions** – Admin vs. user privileges  
- 📝 **Post Management** – Create, update, delete blog posts  
- 💬 **Comments & Likes** – Interact and engage with content  
- 🧑‍💻 **Admin Dashboard** – Manage users and content  
- 📱 **Responsive Design** – Mobile-first layout using Bootstrap 5  
- 🧩 **Modular Architecture** – Scalable and maintainable Flask structure  

---

## 🧠 Tech Stack

- **Backend**: Flask, SQLAlchemy, Flask-JWT-Extended  
- **Database**: MySQL  
- **Frontend**: Bootstrap 5, Jinja2  
- **Utilities**: Python-dotenv, Flask-Migrate, Flask-CORS  

---

## 📁 Project Structure
```
flask_blog/
│
├── app/
│   ├── __pycache__/        # Compiled Python files
│   ├── models/             # SQLAlchemy ORM models
│   ├── routes/             # API and web route handlers
│   ├── templates/          # Jinja2 HTML templates
│   ├── utils/              # Helper functions (e.g., JWT/auth)
│   ├── __init__.py         # Application factory
│   └── extensions.py       # Third-party extensions (e.g., db, JWT)
│
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── run.py                  # App entry point (Flask runner)
```

---

## ⚙️ Getting Started

### 🔹 Create Virtual Environment
```
python -m venv venv**  
source venv/bin/activate  (Windows: venv\\Scripts\\activate)
```
### 🔹 Install Requirements

```pip install -r requirements.txt```

### 🔹 Configure Environment Variables

Create a `.env` file in the root directory:
```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
JWT_SECRET_KEY=your-jwt-secret
```

### 🔹 Run Migrations & Start Server

**flask db init**  
**flask db migrate**  
**flask db upgrade**  
**flask run**

---

## 🖼️ UI Previews

| Home Page | Blog Post | After Login |
|-----------|-----------|-------------|
| ![Home](https://github.com/user-attachments/assets/a4c49613-adb8-4508-b50e-ba01b3fac300) | ![Post](https://github.com/user-attachments/assets/b2e6b7fa-5c69-423d-9225-aaa8d545fdd3) | ![Dashboard](https://github.com/user-attachments/assets/b3425ef8-8d6c-44c4-988c-d09c14717163) |

---

## 🛠️ Roadmap

- [ ] 🔄 Post Pagination  
- [ ] 🖋️ Rich Text Editor (WYSIWYG)  
- [ ] 🔍 Post Search and Filters  
- [ ] 🧑 Profile Image & Bio  
- [ ] 🔐 Password Reset + Email Verification  
- [ ] 🚀 Deployment on Render / Railway  

---

## 🎯 Future Enhancements

- 💡 GPT-based writing assistance  
- 🌍 Multilingual support (i18n)  
- 📊 Admin analytics dashboard  
- 📄 Export posts as PDF  
- 🧪 Unit & integration tests  

---

## 📜 License

This project is licensed under the **MIT License**.  
Use it freely, modify as needed, and don’t forget to credit!

---

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/)  
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)  
- [Bootstrap](https://getbootstrap.com/)  
- [Python Dotenv](https://pypi.org/project/python-dotenv/)  

---

## 👨‍💻 Contact

📧 Email: rp3252154@gmail.com  
🌐 [Portfolio]([https://your-portfolio-link.com](https://github.com/RahulPatil-Tech))  
🐙 [GitHub]([https://github.com/yourusername](https://github.com/RahulPatil-Tech))  
💼 [LinkedIn]([https://linkedin.com/in/yourlinkedin](https://www.linkedin.com/in/rahul-patil-4bb533209/))

---

> Built with ❤️ and Flask by **Rahul**
