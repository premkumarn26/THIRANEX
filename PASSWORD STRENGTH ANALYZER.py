PASSWORD STRENGTH ANALYZER :


SOURCE CODE :


import hashlib

password = input("Enter Password: ")

hashed = hashlib.sha256(password.encode()).hexdigest()

print(hashed)
import re

password = input("Enter password: ")

score = 0

if len(password) >= 8:
    score += 20

if re.search(r"[A-Z]", password):
    score += 20

if re.search(r"[a-z]", password):
    score += 20

if re.search(r"\d", password):
    score += 20

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 20

common = ["123456", "password", "admin", "qwerty"]

if password.lower() in common:
    score = 0

if score < 40:
    strength = "Weak"
elif score < 70:
    strength = "Medium"
elif score < 90:
    strength = "Strong"
else:
    strength = "Excellent"

print("\nStrength:", strength)
print("Score:", score)


OUTPUT:

Enter Password: Arun@123
7eebee3cf1824cae81ce0ec26827aeaa1d552dfe4a5e561dddd3118dda5aacbf
Enter password: Arun@123

Strength: Excellent
Score: 100
