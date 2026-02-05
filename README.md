# 🏠 Bangalore House Price Predictor

An end-to-end **Machine Learning web application** that predicts house prices in Bangalore based on user inputs such as location, total square feet, number of bedrooms (BHK), and bathrooms.

## 🔗 Live Demo

🚀 Try the application here:  
👉 https://kunalx30-bangalore-house-price-predictor.vercel.app/

This project demonstrates the complete **Data Science lifecycle** — data cleaning, feature engineering, model training, and deployment.

---

## 🚀 Features

- 📊 Cleaned and preprocessed Bangalore housing dataset
- 🧠 Machine Learning model using **Ridge Regression**
- 🌐 Interactive **Flask web application**
- 🏡 Simple and user-friendly UI
- ⚡ Real-time house price prediction

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** NumPy, Pandas, Scikit-learn  
- **Web Framework:** Flask  
- **Frontend:** HTML, CSS  
- **Model Serialization:** Pickle  
- **Deployment:** Vercel

---

## 📂 Project Structure

```
Banglore_house_Price_Predictor/
│
├── main.py # Flask application
├── RidgeModel.pkl # Trained ML model
├── Cleaned_data.csv # Cleaned dataset
├── requirements.txt # Project dependencies
├── .gitignore
│
├── templates/
│ └── index.html # Frontend UI
```


---

## ⚙️ How It Works

1. User enters property details (location, total sqft, BHK, bathrooms)
2. Input data is preprocessed
3. Ridge Regression model predicts the house price
4. Predicted price is displayed instantly

---

## ▶️ Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Kunalx30/bangalore_house_price_-predictor.git
cd bangalore_house_price_-predictor
```

### 2️⃣ Create virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate
```
### 3️⃣ Install dependencies
``` bash
pip install -r requirements.txt
```
### 4️⃣ Run the application
``` bash
python main.py
```
### Open your browser and visit:
``` bash
http://127.0.0.1:5000
```

### 📈 Machine Learning Model
- Algorithm: Ridge Regression
- Reason for selection:
- Handles multicollinearity
- Reduces overfitting
- Performs well on linear regression problems


### 🔮 Future Improvements
- Add advanced models (Random Forest, XGBoost)
- Improve UI using Bootstrap
- Add data visualizations
- Deploy backend on cloud services


## 👤 Author
### Kunal Chandelkar
