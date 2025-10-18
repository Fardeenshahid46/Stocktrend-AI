🧠 Stocktrend-AI

Stocktrend-AI is an intelligent machine learning–powered web app that predicts stock price trends (up or down) using historical data.
Built with Python, Streamlit, and scikit-learn, it allows users to visualize, analyze, and forecast stock movement with ease.

🚀 Features

✅ Fetches live stock market data using yfinance
✅ Trains a machine learning model to predict future stock trends
✅ Interactive UI built with Streamlit
✅ Visualizes stock price trends and prediction results
✅ Exports trained model (model.pkl) for reuse

🏗️ Project Structure
Stocktrend-AI/
│
├── app.py                 # Main Streamlit app
├── requirements.txt       # Python dependencies
├── src/
│   ├── train_model.py     # Script to train and save model.pkl
│   └── model.pkl          # Trained ML model
│
├── Data/
│   └── AAPL.csv           # Example stock dataset (Apple)
│
└── README.md              # Project documentation

⚙️ Installation

1️⃣ Clone the repository:

git clone https://github.com/Fardeenshahid46/Stocktrend-AI.git
cd Stocktrend-AI


2️⃣ Create a virtual environment:

python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate   # On Mac/Linux


3️⃣ Install dependencies:

pip install -r requirements.txt


4️⃣ Run the Streamlit app:

streamlit run app.py

🧮 Model Training

If you want to train a new model:

python src/train_model.py


This will generate a new model.pkl inside the src/ folder.

🌐 Deployment

The project is deployed using Streamlit Cloud.

🔗 Live App: Click Here to Open

🧰 Tech Stack

Streamlit

Pandas / NumPy

scikit-learn

yfinance

📊 Real-time stock charts

🤖 AI-predicted stock trend: Up or Down

