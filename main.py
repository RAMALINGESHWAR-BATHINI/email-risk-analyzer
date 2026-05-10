import re

email = input("Paste Email Content:\n")

risk_keywords = [
    "urgent",
    "bank",
    "password",
    "otp",
    "verify",
    "click here",
    "limited time"
]

risk_score = 0

for word in risk_keywords:
    if word.lower() in email.lower():
        risk_score += 1

links = re.findall(r'https?://\S+', email)

if links:
    risk_score += 1

print("\nAnalysis Result")

if risk_score >= 3:
    print("Risk Level: Suspicious")
else:
    print("Risk Level: Safe")

if links:
    print("Detected Links:")
    for link in links:
        print(link)