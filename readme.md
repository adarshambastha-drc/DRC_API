# 🚀 DRC Systems Employee API (Mock Data Generator)

A robust FastAPI application that generates infinite, random employee data for **DRC Systems**. This API is designed to simulate real-world data scenarios, including random null values and "Smart" composite IDs, making it perfect for testing data pipelines, frontend dashboards, or error handling logic.

## ✨ Features

* **⚡ Real-time Generation:** Data is generated on the fly; no database required.
* **🆔 Smart Composite IDs:** Generates meaningful IDs (e.g., `DRC-2023-AI-84920`) based on joining year and department.
* **🎲 Random Nulls:** ~20% of fields randomly return `null` to test error handling and data cleaning scripts.
* **♾️ Infinite Scaling:** Request as many records as you need via query parameters.
* **🌍 Realistic Data:** Uses the `Faker` library for realistic names, dates, emails, and phone numbers.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **FastAPI** (Web Framework)
* **Uvicorn** (ASGI Server)
* **Faker** (Data Generation)

---

## 🚀 Live Demo

*(Once you deploy to Render, paste your URL here)*
**Base URL:** `https://<your-app-name>.onrender.com`

---

## 💻 How to Run Locally

Follow these steps to run the API on your own machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/](https://github.com/)<your-username>/drc-employee-api.git
cd drc-employee-api