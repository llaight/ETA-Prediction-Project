# 🚚 Delivery ETA Prediction System

A full-stack project for **predicting delivery estimated time of arrival (ETA)** using machine learning and Flask API, with PostgreSQL for data storage and a simple frontend for interaction.

---

## 🔧 Features
- 🤖 **ML Model (Linear Regression)** to predict delivery ETA based on distance and time features  
- 🛠️ **Flask API** for ETA prediction and logging delivery data  
- 🗄️ **PostgreSQL** database to store ETA logs including driver and order info  
- 🌐 Simple frontend HTML pages for submitting delivery requests and viewing logs  
- 📊 Optional integration with Metabase for analytics and dashboarding

---

## 🧰 Tech Stack

| Component          | Technology          |
|--------------------|---------------------|
| ML Model           | Python, scikit-learn|
| Backend API        | Python, Flask       |
| Database           | PostgreSQL          |
| Frontend           | HTML, JavaScript    |
| Environment Config | python-dotenv       |
| Analytics          | Metabase            |

---

## 🗃️ Folder Structure
```plaintext
delivery-eta-prediction/
├── model/               # Saved ML model files (e.g. delivery_eta_lr.pkl)
├── templates/           # Static files for frontend (HTML, CSS, JS)
├── mock_data.py         # Generating mock data
├── data/                # Saved mock data files
├── model.ipynb          # Training models
├── app.py               # Flask API and server
├── utils.py             # Utility functions (distance calculation, ETA prediction)
├── .env                 # Environment variables (DB credentials, etc.)
└── README.md            # Documentation (this file)
```

## 🚀 How It Works

### Build and train ML model
- Use mock delivery data with features: **distance (km)**, **hour of day**, and **weekday**  
- Train a **Linear Regression** model to predict ETA in minutes  
- Save the trained model with **joblib**

### Flask API Endpoints
- **`/predict_eta` (POST)**:  
  Accepts JSON with driver info and coordinates, returns predicted ETA and status message, saves log entry to the database  
- **`/eta_logs` (GET)**:  
  Returns all logged ETA predictions with timestamps  

### Frontend HTML pages
- ETA form for entering delivery info and receiving ETA predictions  
- ETA logs page to view historical prediction records  
- Optional dashboard page for visualization or embedding Metabase dashboards  

### Database (PostgreSQL)
- Stores delivery logs with **driver_id**, **order_id**, coordinates, ETA, status message, and timestamp  

---

## 📊 Sample Data Structure

| Column Name     | Description                             |
|-----------------|---------------------------------------|
| order_id        | Unique identifier for each order      |
| driver_id       | Delivery driver's ID                   |
| current_lat     | Latitude of current location           |
| current_lng     | Longitude of current location          |
| dropoff_lat     | Latitude of dropoff location            |
| dropoff_lng     | Longitude of dropoff location           |
| eta_minutes     | Predicted estimated time in minutes   |
| status_message  | ETA status ("Arrived", "En route", etc.) |
| created_at      | Timestamp of prediction/log entry      |

---

## ✅ Deliverables

- Mock data creation and model training (Linear Regression)  
- Utility functions for haversine distance calculation and ETA prediction  
- Flask API for prediction and data logging  
- Frontend HTML pages with input form and logs table  
- PostgreSQL database integration  
- Environment variables handling with `.env` file  
- Basic Metabase dashboards for delivery analytics (optional)  

---

## 📜 License

MIT License — Free to use, modify, and extend for learning or portfolio projects.

---

## 👩‍💻 Author

**Angela Loro**  
Developed during internship at LAMINA Studios  
GitHub: [github.com/llaight](https://github.com/llaight)
