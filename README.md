# 📝 गोड आठवणी (Sweet Memories) — A Simple Flask Blog

> A nostalgic and elegant blogging platform built with ❤️ using Flask.

---

## ✨ Features

<table>
<tr><td>🔐 <strong>User Authentication</strong></td><td>📑 <strong>Post Management</strong></td><td>💬 <strong>Engagement Tools</strong></td></tr>
<tr>
<td>
<ul>
<li>Register, Login, Logout</li>
<li>Password hashing for security</li>
<li>Remember Me functionality</li>
<li>Forgot Password (email logic placeholder)</li>
</ul>
</td>
<td>
<ul>
<li>Create, Edit, Delete Posts</li>
<li>Rich text editor (Quill.js)</li>
<li>View posts with timestamps</li>
</ul>
</td>
<td>
<ul>
<li>Like / Unlike posts</li>
<li>Comment on posts</li>
<li>View counts for likes & comments</li>
</ul>
</td>
</tr>
</table>

---

<table>
<tr><td>🔍 <strong>Content Discovery</strong></td><td>👤 <strong>User Profiles</strong></td><td>👷️ <strong>Admin Dashboard</strong></td></tr>
<tr>
<td>
<ul>
<li>Homepage feed</li>
<li>Full-text Search</li>
<li>Pagination</li>
</ul>
</td>
<td>
<ul>
<li>Username, email, join date</li>
</ul>
</td>
<td>
<ul>
<li>Promote to admin</li>
<li>Delete any post or comment</li>
<li>Role-based access (only admins)</li>
</ul>
</td>
</tr>
</table>

---

## 📱 Responsive UI

* Built with Bootstrap 5
* Clean, mobile-first layout

## 🔔 Flash Messaging

* Instant feedback on user actions

---

## 🛠️ Technologies Used

* <strong>Backend:</strong> Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, Flask-JWT-Extended
* <strong>Frontend:</strong> HTML5, CSS3, Bootstrap 5, Quill.js
* <strong>Utilities:</strong> Python 3.x, pip, .env config
* <strong>Security:</strong> Werkzeug for password hashing

---

## Glims 🖼️

----
### 🟢 Live User Activity Animation
[Screencast From 2025-07-28 20-21-21.webm](https://github.com/user-attachments/assets/56a3413b-920a-4527-85fe-f6a7734d5e0b)


-----
### 🏡 Homepage with Posts

<img width="1836" height="921" alt="Screenshot From 2025-07-28 19-52-28" src="https://github.com/user-attachments/assets/cc6b2921-d879-44f7-b8e7-8cd22c0f018d" />

-----
### 📝 User Registration
<img width="1836" height="921" alt="Screenshot From 2025-07-28 19-52-51" src="https://github.com/user-attachments/assets/a676c0e4-af60-47ed-b219-2481a0997c16" />

-----
### ➡️ User Login
<img width="1836" height="921" alt="Screenshot From 2025-07-28 19-52-43" src="https://github.com/user-attachments/assets/51474cb5-b561-4bbc-bf3e-cf37fa0a0ba1" />

-----
### 📁 CRUD OPERATIONS 
<img width="1836" height="921" alt="Screenshot From 2025-07-28 20-11-25" src="https://github.com/user-attachments/assets/e5c7467d-3d63-4445-8bd3-f54ea07bf20d" />

----
<img width="1836" height="921" alt="Screenshot From 2025-07-28 19-53-51" src="https://github.com/user-attachments/assets/ad51c02d-af17-4931-930c-57fa3cf8dd05" />

----
<img width="1836" height="921" alt="Screenshot From 2025-07-28 19-54-00" src="https://github.com/user-attachments/assets/1a4efdd7-175d-4609-a309-e066dbf8775d" />

----
<img width="1836" height="921" alt="Screenshot From 2025-07-28 19-54-14" src="https://github.com/user-attachments/assets/a086fd60-eb2b-4203-8acf-0fe434c1c418" />

----

## 🚀 Getting Started

### 📦 Prerequisites

* Python 3.8+
* pip
* SQLite (default) or PostgreSQL/MySQL

### 🧱 Installation

```bash
git clone <your-repo-url>
cd blog
python3 -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```

📄 Create `.env` file:

```env
SECRET_KEY='your_secret_key'
SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
JWT_SECRET_KEY='your_jwt_secret_key'
```

### 🧬 Database Setup

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

(Optional) Seed sample data:

```bash
python seed.py
```

---

## ▶️ Running the App

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 👨‍💼 Usage

* Register & Login
* Create a new blog post
* Like/Unlike posts
* Comment & interact
* Search posts by keywords
* Admins can moderate content and users

---

## 🧑‍💼 Admin Access

1. Use seeded admin credentials or promote a user.
2. Once logged in as admin, navigate to <strong>Admin Dashboard</strong> from navbar.

---

## 📆 Folder Structure (optional)

```bash
📂 blog/
🕺️ app/
🕺️ templates/
🕺️ static/
🕺️ models.py
🕺️ routes.py
🕺️ forms.py
seed.py
run.py
requirements.txt
```

---

## 🤝 Contributing

Feel free to fork and submit PRs!
💬 Suggestions and feedback are welcome.

---

## 📜 License

MIT License. See `LICENSE` file for full details.

---

## 💖 Built With Love

[![Built with love by Rahul](https://img.shields.io/badge/Built%20with%20%E2%9D%A4%EF%B8%8F%20by-Rahul-ff69b4.svg)](https://github.com/your-github-profile)
