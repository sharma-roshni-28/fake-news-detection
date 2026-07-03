import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load datasets
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Add labels
fake["label"] = "Fake"
true["label"] = "Real"

# Combine datasets
data = pd.concat([fake, true])

# Use news text
X = data["text"]
y = data["label"]

# Convert text into vectors
vectorizer = TfidfVectorizer(stop_words='english')

X_vector = vectorizer.fit_transform(X)

# Train model
X_train, X_test, y_train, y_test = train_test_split(
    X_vector, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

# Streamlit UI
st.title("📰 Fake News Detection System")

news = st.text_area("Enter News Here")

if st.button("Check News"):

    if news.strip() == "":
        st.warning("Please enter news")
    else:
        news_vector = vectorizer.transform([news])

        prediction = model.predict(news_vector)

        if prediction[0] == "Fake":
            st.error("⚠ Fake News Detected")
        else:
            st.success("✅ Real News")