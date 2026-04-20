# 🚀 Quotes Scraper Service

### 📌 Overview

This project is a full system that scrapes quotes from a website, stores them in PostgreSQL, and exposes them via a FastAPI API.

---

### 🧱 Architecture

* **Scraper Layer** → collects data
* **Database Layer** → PostgreSQL with SQLAlchemy
* **API Layer** → FastAPI endpoints
* **Service Layer** → systemd
* **Packaging** → deb package

---

### 🚀 Features

Web scraping (quotes, authors, tags)
PostgreSQL database
REST API using FastAPI
Background scraping
systemd service (auto start)
deb package for easy deployment

---

🔄 Data Flow

The system follows a structured data pipeline from data collection to user access:

Website (quotes.toscrape.com)
        ↓
Scraper Script (scraper.py)
        ↓
Data Cleaning & Structuring
        ↓
PostgreSQL Database
        ↓
FastAPI Application
        ↓
API Endpoints (/quotes)
        ↓
User (Browser / Client)

---

🧠 Explanation

1. Data Source
   The system collects data from an external website containing quotes, authors, and tags.

2. Scraper Layer
   A Python script uses "requests" and "BeautifulSoup" to fetch and parse HTML content.

3. Data Processing
   Extracted data is cleaned and structured into a consistent format before storage.

4. Database Layer
   Clean data is stored in a PostgreSQL database using SQLAlchemy ORM.

5. API Layer
   FastAPI exposes the stored data through RESTful endpoints.

6. Service Layer
   The application runs as a background service using systemd, ensuring continuous availability.

7. User Access
   Users can access the data via a browser or API tools like Postman.

---

### ⚙️ Installation

 sudo dpkg -i package.deb

---

### ▶️ Run manually

 uvicorn app.main:app --host 127.0.0.1  --port 8000

---

### 📂 Project Structure

```text
quotes_service/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── api.py           # API routes (endpoints)
│   ├── scraper.py       # Web scraping script
│   ├── models.py        # SQLAlchemy ORM models
│   └── database.py      # Database connection setup
│
├── scripts/
│   └── start.sh         # Script to start the app
│
├── service/
│   └── quotes.service   # systemd service file
│
├── package/
│   ├── DEBIAN/
│   │   ├── control      # Package metadata
│   │   └── postinst     # Auto-start script after install
│   ├── opt/
│   │   └── quotes_service/  # Installed app location
│   └── etc/
│       └── systemd/
│           └── system/
│               └── quotes.service
│
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

### 🚀 API Endpoints

| Method | Endpoint                | Description               |
| ------ | ----------------------- | ------------------------- |
| GET    | `/quotes`               | Retrieve all quotes       |
| GET    | `/quotes/{id}`          | Retrieve a specific quote |
| GET    | `/quotes/author/{name}` | Retrieve quotes by author |

---

### 🔐 Port

 Runs on:
 http://localhost:8000


---

### 📦 Deployment

 Packaged as .deb and runs automatically using systemd.

### 🔁 Service Commands

```bash
sudo systemctl start quotes
sudo systemctl stop quotes
sudo systemctl restart quotes
sudo systemctl status quotes
```
