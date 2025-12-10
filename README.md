# Adaptive-_Learning


# 📚 Math Adaptive Learning Prototype  
AI-Powered Personalized Practice System for Kids (Ages 5–10)

---

## 🚀 Overview

This project is a **simple adaptive learning prototype** designed to help children practice basic math (addition & subtraction).  
The system dynamically adjusts the difficulty level based on the learner’s performance.

The goal is to demonstrate how **adaptive learning + rule-based intelligence** can keep learners in the *optimal challenge zone*—not too easy, not too hard.

---

## 🎯 Features

### ✅ **Three Difficulty Levels**
- **Easy** → numbers 1–10  
- **Medium** → numbers 10–50  
- **Hard** → numbers 50–100  

### ✅ **Adaptive Engine**
Automatically changes difficulty using:
- **+1 Level** → after 2 consecutive correct answers  
- **−1 Level** → after 2 consecutive wrong answers  
- Level always remains within **1 to 3**

### ✅ **Performance Tracking**
The system records:
- Correct / Incorrect answers  
- Time taken per question  
- Accuracy summary  
- Average response time  

### ✅ **Session Summary**
At the end of each session:
- Accuracy (%)  
- Average time per question  
- Recommended next difficulty level  

---

## 📁 Project Structure

math-adaptive-prototype/
│── README.md
│── requirements.txt
└── src/
├── main.py
├── puzzle_generator.py
├── tracker.py
└── adaptive_engine.py


---

## ⚙️ How the Adaptive Logic Works

### 🔍 Rule-Based Mechanism
The core logic is simple but effective:
if 2 correct in a row → increase difficulty (max: 3)
if 2 wrong in a row → decrease difficulty (min: 1)
else → keep difficulty same



This ensures the user always stays at the right level for learning.

---

## 🧠 Code Components

### **1. puzzle_generator.py**
Generates math questions based on difficulty level.

### **2. tracker.py**
Tracks correctness, response time, and computes summary metrics.

### **3. adaptive_engine.py**
Implements the adaptive difficulty rules.

### **4. main.py**
Controls the session flow:
- Display question  
- Take user input  
- Pass metrics to tracker  
- Update difficulty  
- Show end summary  

---

## ▶️ Running the Project

### **Step 1: Install Python 3.8+**

Verify:

### **Step 2: Run the App**
cd math-adaptive-prototype/src
python main.py


---

## 📊 Output Example

At session end:

===== SESSION SUMMARY =====
Student: nikitha
Accuracy: 75.00%
Avg Time: 3.12 sec
Next Recommended Level: 2


---

## 🔮 Future Enhancements

- Addition of **multiplication**, **division**, and **word problems**
- Conversion to **Streamlit web app**
- Use of ML models:
  - Logistic Regression  
  - Decision Tree  
  - Reinforcement Learning  
- Long-term student modeling  
- Error classification and personalized hints  

---

## 📝 Author

Created as part of the **Adaptive Learning Assignment**.  
Designed to be clean, modular, and easy to extend.

---

## ⭐ If you want, I can also generate:
- A **complete GitHub-ready README with badges**
- A **zip file with full code structure**
- A **Streamlit UI version**
- Fancy **flowcharts and architecture diagrams**

Just tell me! 😊
"""

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

readme_path
