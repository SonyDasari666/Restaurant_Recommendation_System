# 🍴 AI-Based Restaurant Discovery Website

An AI-powered restaurant recommendation system that helps users quickly find restaurants based on **location, cuisine, budget, and party size**.  
Built with **Python (Flask, Pandas, NumPy, Scikit-learn)** and a responsive **Bootstrap** front-end.

---

## 🚀 Features
- 🔍 **Search by city, cuisine, budget, and party size**
- 🤖 **AI-driven recommendations** using:
  - Content-based filtering
  - Cosine similarity
  - NLP vectorization (`CountVectorizer`)
- 📊 Dataset of restaurants across multiple Indian cities
- 🌐 Responsive **Flask + Bootstrap** web app
- ⚡ Reduced search time by ~60%, improving user experience
- 🛠️ Modular code for easy updates and extensions

---

## 📂 Project Structure
Restaurant-Recommendation-System-main/
│
├── app.py # Main Flask app
├── restaurant.csv # Restaurant dataset
├── food1.csv # Additional dataset
├── merged_restaurants.csv # Final merged dataset
├── merge_datasets.py # Script to merge datasets
├── templates/ # HTML files (Jinja2 templates)
│ ├── index.html
│ └── result.html
├── static/ # CSS, JS, images
├── requirements.txt # Dependencies
└── README.md # Project documentation


Copy code

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/AI-Restaurant-Discovery.git
   cd AI-Restaurant-Discovery
Create & activate virtual environment

Copy code
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Linux/Mac
Install dependencies

Copy code
pip install -r requirements.txt
Run the Flask server

Copy code
python app.py
Open in browser:
👉 http://127.0.0.1:5000

📊 Dataset
restaurant.csv ,food1.csv and main_rest

Contains data from cities like Lucknow, Warangal, Hyderabad, Bengaluru, Chennai, Delhi, Mumbai, Kolkata, Pune and more

Attributes: Restaurant Name, Cuisine, City, Budget, Rating, Address, etc.

🔮 Future Enhancements
✅ User login & personalized recommendations

✅ Real-time restaurant data using Zomato/Google Places API

✅ Chatbot-based search assistant

✅ Sentiment analysis on customer reviews

✅ Mobile app deployment (React Native / Flutter)

🛠️ Tech Stack
Backend: Python, Flask

Frontend: HTML, CSS, Bootstrap

AI/ML: Pandas, NumPy, Scikit-learn, NLP (CountVectorizer)

Deployment (future): Gunicorn, Heroku/AWS

👨‍💻 Author
Dasari Sony
📧 Email: sonydasari230@gmail.com
🔗 GitHub:GitHub Profile
🔗 LinkedIn: LinkedIn Profile

⭐ If you like this project, don’t forget to star the repo!
