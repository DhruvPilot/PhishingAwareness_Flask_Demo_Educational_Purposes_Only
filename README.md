# 🪝 Phishing Awareness Demo – Flask-Based (Educational Only)

**Short Description:**  
This project is a Flask-based educational demo that simulates a phishing login page to demonstrate how attackers capture credentials through social engineering techniques. It is designed solely for security awareness training and ethical demonstrations in controlled environments.

> ❗ **DISCLAIMER:**  
> This project is for **educational purposes only**. Do **not** use it in real-world phishing attacks or outside authorized lab settings. Misuse may be illegal and unethical.

---

## 📚 Project Overview

This demo creates a fake login page using Python and Flask to raise awareness of how easily phishing websites can be deployed. It is intended to teach:
- How phishing attacks are built
- What risks exist when users enter credentials on spoofed sites
- How to train users to recognize phishing attempts

---

## 🔍 Key Features

- Fake login page hosted via Flask
- Logs captured credentials to a file (for training only)
- Can be styled to mimic popular websites
- Emphasizes safe learning and ethical awareness

---

## 🚀 Getting Started

> ⚠️ Run only on **local machines** or isolated virtual environments.

### Prerequisites
- Python 3.x
- Flask (`pip install flask`)

### Usage
```bash
python Phishing_Flask.py
```
Visit `http://127.0.0.1:5000/` in your browser to see the phishing simulation.

---

## 🎯 Learning Objectives

- Understand phishing site construction and behavior
- See how attackers can capture credentials
- Learn common social engineering patterns
- Raise awareness through simulated training

---

## 🧯 Mitigation Advice

To defend against phishing:
- Verify URLs and SSL certificates
- Use a password manager (detects fake domains)
- Enable multi-factor authentication (MFA)
- Provide user awareness training regularly

---

## 👨‍💻 Author

**Dhruv Patel**  
[LinkedIn Profile](https://www.linkedin.com/in/dhruvpatel-infosec)


---

## 🌐 Hosting with Ngrok (Optional)

To simulate a phishing site with a public-facing URL for educational demos:

### Step 1: Download Ngrok
- Go to [https://ngrok.com](https://ngrok.com) and sign up
- Download and install Ngrok
- Authenticate with your Ngrok token:
```bash
ngrok config add-authtoken YOUR_TOKEN_HERE
```

### Step 2: Start your Flask server
In one terminal:
```bash
python Phishing_Flask.py
```

### Step 3: Expose your Flask app using Ngrok
In another terminal:
```bash
ngrok http 5000
```

Ngrok will give you a URL like:
```
https://abcd1234.ngrok.io
```

This URL can be accessed from anywhere (for demo/testing purposes only).

> ⚠️ **Note:** Do not distribute this URL publicly. Use in a lab or simulated phishing training environment only.

---
