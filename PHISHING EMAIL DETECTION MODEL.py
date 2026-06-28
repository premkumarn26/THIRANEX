PHISHING EMAIL DETECTION MODEL :

SOURCE CODE :

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

emails = [
    "Congratulations! You won a free iPhone. Click here now.",
    "Your bank account has been suspended. Verify immediately.",
    "Claim your lottery prize now by clicking this link.",
    "Update your password to avoid account suspension.",
    "Meeting scheduled tomorrow at 10 AM.",
    "Please find the project report attached.",
    "Happy Birthday! Have a wonderful day.",
    "Let's have lunch together tomorrow.",
    "Your Amazon order has been shipped.",
    "Can you send me the assignment notes?"
]

labels = [
    "Phishing",
    "Phishing",
    "Phishing",
    "Phishing",
    "Safe",
    "Safe",
    "Safe",
    "Safe",
    "Safe",
    "Safe"
]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(emails)

X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.3, random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n----- Test Your Email -----")
email = input("Enter email text: ")

email_vector = vectorizer.transform([email])
prediction = model.predict(email_vector)

print("\nPrediction:", prediction[0])

if prediction[0] == "Phishing":
    print("⚠ Warning! This email may be a PHISHING email.")
else:
    print("✔ This email appears SAFE.")

OUTPUT :


Accuracy: 66.67 %

Confusion Matrix:
[[0 1]
 [0 2]]

----- Test Your Email -----
Enter email text: arun2601@gmail.com

Prediction: Safe
✔ This email appears SAFE.
