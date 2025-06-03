<h1 align="center">📝 Flask Blog Platform</h1>

<p align="center">
  A modern, secure, and responsive blog platform built with <strong>Flask</strong>, <strong>MySQL</strong>, and <strong>Bootstrap</strong> ✨  
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20With-Flask-blue.svg" />
  <img src="https://img.shields.io/badge/Database-MySQL-orange" />
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
  <img src="https://img.shields.io/badge/By-Rahul-blueviolet" />
</p>

---

## 🌟 Introduction

Hi, I’m **Rahul** 👋  
This is a full-stack blog platform where users can write and share posts, comment on others’ content, and like posts. Admins can manage content site-wide, while everything runs securely behind JWT auth and role-based permissions. Designed for modern development and full-stack learners.

---

## 🚀 Features

✅ **JWT Authentication** – Login & registration with token security  
✅ **Role-based Access** – Admins vs regular users  
✅ **Blog Post Management** – Create, update, delete posts  
✅ **Comments & Likes** – User interactions  
✅ **Admin Dashboard** – Control content across the platform  
✅ **Responsive UI** – Mobile-first Bootstrap design  
✅ **Clean Code Architecture** – Modular Flask app  

---

## 🧠 Tech Stack

- **Framework**: Flask  
- **Database**: MySQL + SQLAlchemy  
- **Frontend**: Bootstrap 5 + Jinja2  
- **Authentication**: Flask-JWT-Extended  
- **Tools**: Python-dotenv, Flask-Migrate, Flask-CORS  

---

## 📁 Folder Structure

```
flask_blog/
│
├── app/
│ ├── routes/ # Views and API routes
│ ├── models/ # SQLAlchemy models
│ ├── templates/ # Jinja2 HTML templates
│ ├── static/ # CSS, JS, images
│ └── utils/ # JWT & auth helpers
├── migrations/ # DB migration files
├── requirements.txt
├── config.py
├── run.py
└── .env

```


---

## ⚙️ Setup Instructions

### ✅ Create a Virtual Environment

***
python -m venv venv  
source venv/bin/activate  # or venv\Scripts\activate  
***

### ✅ Install Dependencies

***
pip install -r requirements.txt  
***

### ✅ Set Up Environment Variables

Create a `.env` file in the root directory:

***
FLASK_APP=run.py  
FLASK_ENV=development  
SECRET_KEY=your-secret-key  
DATABASE_URL=mysql+pymysql://user:password@localhost/dbname  
JWT_SECRET_KEY=your-jwt-secret  
***

### ✅ Run Migrations & Start App

***
flask db init  
flask db migrate  
flask db upgrade  
flask run  
***

---

## 📸 UI Previews

| Home Page | Admin Dashboard | Blog Post |
|-----------|------------------|-----------|
| ![Home](screenshots/home.png) | ![Admin](screenshots/admin.png) | ![Post](screenshots/post.png) |

---

## 🛠 TODO Roadmap

- [ ] Add post pagination  
- [ ] Add WYSIWYG/Rich Text Editor  
- [ ] Implement post search and filters  
- [ ] Profile image & bio editor  
- [ ] Add password reset and email verification  
- [ ] Deploy on Render / Railway  

---

## 💡 Future Goals

- 🧠 GPT-based post suggestions  
- 🌐 i18n: Multilingual support  
- 📊 Admin analytics dashboard  
- 🧾 PDF export of posts  
- 🧪 Unit + integration test suite  

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share!

---

## 🙌 Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
- [Bootstrap](https://getbootstrap.com/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)

---

## 🧑‍💻 Connect with Me

📧 Email: rahul@example.com  
🌐 [Portfolio](https://your-portfolio-link.com)  
🐙 [GitHub](https://github.com/yourusername)  
💼 [LinkedIn](https://www.linkedin.com/in/yourlinkedin)  

> Made with 💙 by **Rahul**
