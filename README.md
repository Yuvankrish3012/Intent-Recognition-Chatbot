# Chatbot-using-NLP-Rule-Based-ML-Hybrid-
This project demonstrates a hybrid chatbot that combines rule-based logic and machine learning for intent classification using NLP techniques. It identifies user queries into intents like greetings, weather, jokes, and more.

---

## 📁 Dataset

We used a custom JSON dataset containing intents and their corresponding example patterns and responses:

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Is anyone there?", "Hey", "Hola"],
      "responses": ["Hello!", "Hi, how can I help you?", "Greetings!"]
    },
    ...
  ]
}
✅ Download the dataset from this project repo under intents.json

📊 Features
Intent classification using TF-IDF and Logistic Regression

Rule-based fallback responses

Trained model and vectorizer saved using pickle

Streamlit UI for testing chatbot in real time

✅ Model Performance
Accuracy: 1.00

Precision: 1.00

Recall: 1.00

F1 Score: 1.00

📋 Classification Report:

Intent	Precision	Recall	F1-score	Support
covid_info	1.00	1.00	1.00	8
greeting	1.00	1.00	1.00	8
joke	1.00	1.00	1.00	8
restaurant_recommendation	1.00	1.00	1.00	8
weather	1.00	1.00	1.00	8

✅ Confusion Matrix Visualization:
<!-- Replace with your image path -->

🧠 Technologies Used
Python

NLTK (for tokenization and lemmatization)

Scikit-learn (TF-IDF & Logistic Regression)

Streamlit (UI)

Pickle (model saving)

💡 Streamlit Chatbot UI
You can launch the Streamlit chatbot with:

bash
Copy
Edit
streamlit run "intent_chatbot_app.py"
![image](https://github.com/user-attachments/assets/b0aa7e68-0039-41b2-bb82-185d663bfbc3)

📁 File Structure
pgsql
Copy
Edit
├── intent_chatbot_app.py
├── train_intent_model.ipynb
├── intents.json
├── intent_model.pkl
├── intent_vectorizer.pkl
├── intent_label_encoder.pkl
├── images/
│   ├── confusion_matrix_chatbot.png
│   └── chatbot_ui.png
└── README.md
🚀 How to Run
Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/chatbot-nlp-ml.git
cd chatbot-nlp-ml
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run chatbot UI:

bash
Copy
Edit
streamlit run intent_chatbot_app.py
🔮 Future Improvements
Add support for more intents and fallback detection

Integrate with external APIs (e.g., weather, restaurant search)

Use transformer models like BERT for better classification

Improve context memory for multi-turn conversations

📽️ Demo
🎥 Insert a screen recording or GIF of your chatbot in action here.

📌 Author
Yuvan Krishnan
📬 Feel free to connect: LinkedIn

