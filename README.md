# 🚀 FastAPI Blog Engine

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57)
![Status](https://img.shields.io/badge/Status-Active-success)

> High-performance REST API for a modern blogging platform, built with FastAPI, SQLAlchemy, and JWT authentication.

---

## 🌟 Overview
A production-ready backend API that handles **user authentication** and **blog management** using JWT security, ORM-based database access, and Pydantic validation.

---

## 🛠️ Tech Stack
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- OAuth2 + JWT
- Bcrypt

---

## ✨ Features
- Secure user signup & login
- JWT authorization
- Blog creation & retrieval
- User–blog relationships
- Modular router architecture
- Dependency injection

---

## 📂 Project Structure
```
FastAPI-Blog-App
├── routers/
│   ├── blog.py
│   ├── user.py
│   └── authentication.py
├── main.py
├── models.py
├── schemas.py
├── database.py
├── hashing.py
├── oauth2.py
├── user_token.py
└── requirements.txt
```

---

## ⚡ Getting Started
```
git clone https://github.com/yourusername/fastapi-blog.git
cd fastapi-blog
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn sqlalchemy python-multipart python-jose[cryptography] passlib[bcrypt]
uvicorn main:app --reload
```

---

## 🔌 API Docs
- Swagger UI: /docs
- ReDoc: /redoc

---

## 🚧 Future Improvements
- Docker support
- Unit testing
- Cloud deployment
- Blog update/delete

---

### 👨‍💻 Created by a Developer @ FAST-NUCES
### If you found this project helpful, give it a ⭐️ star on GitHub!
