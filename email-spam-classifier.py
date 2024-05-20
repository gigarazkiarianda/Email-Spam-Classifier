import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib
import tkinter as tk
from tkinter import messagebox


data = pd.read_csv('dataset/spam_dataset.csv')


X = data['email']
y = data['label']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


vectorizer = CountVectorizer()


X_train_count = vectorizer.fit_transform(X_train)
X_test_count = vectorizer.transform(X_test)


clf = MultinomialNB()
clf.fit(X_train_count, y_train)


y_predict = clf.predict(X_test_count)


accuracy = accuracy_score(y_test, y_predict)
print(f"Akurasi: {accuracy}")
print(classification_report(y_test, y_predict))


joblib.dump(clf, 'spam_classifier_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

def predict_email():
    email_text = email_entry.get()
    clf_loaded = joblib.load('spam_classifier_model.pkl')
    vectorizer_loaded = joblib.load('vectorizer.pkl')
    email_transformed = vectorizer_loaded.transform([email_text])
    prediction = clf_loaded.predict(email_transformed)
    result = 'Spam' if prediction[0] == 1 else 'Not Spam'
    messagebox.showinfo("Prediction Result", f"The email is classified as: {result}")


root = tk.Tk()
root.title("Email Spam Classifier")

tk.Label(root, text="Enter the email text:").pack(pady=10)
email_entry = tk.Entry(root, width=50)
email_entry.pack(pady=5)

predict_button = tk.Button(root, text="Predict", command=predict_email)
predict_button.pack(pady=20)

root.mainloop()
