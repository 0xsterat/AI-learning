# 🚀 Gemini Python Starter Project

A simple Python project demonstrating how to use Google’s Gemini API with environment variables for secure API key management.

This project generates a short bio using the gemini-2.5-flash model.

## 🧩 Features

- **Uses Google Gemini Generative AI API**

- **Secure API key handling using .env**

- **Virtual environment support**

- **Beginner-friendly setup**


## 📁 Project Structure
```text
API_testing/
│
├── .env
├── requirements.txt
├── src/
│   └── main.py
└── README.md
```

##⚙️ Prerequisites

- **Python 3.9+

- **pip (comes with Python)

- **VS Code or any code editor

- **Check Python version:**
```bash
python --version**
```
## 📦 Installation
** 1️⃣ Clone this repo**
```bash
git clone https://github.com/0xsterat/AI-learning.git
cd AI-learning
cd basics
cd API_testing
```

** 2️⃣ Create Virtual Environment**
```bash
python3 -m venv venv
```
Activate it:

Mac/Linux
```bash
source venv/bin/activate
```

Windows
```bash
venv\Scripts\activate
```

** 3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables
Create a file named .env in project root:
```text
GEMINI_API_KEY=your_api_key_here
```
No space, no quotes

** Note: Never commit this file to GitHub.**

## ▶️ Running the Application
```bash
python src/main.py
```

##📤 Sample Output
```bash
Here are a few options, choose the one that best fits the context (e.g., LinkedIn, personal website, intro):

**Option 1 (Concise & Direct):**

> Atharva is a passionate DevOps Engineer who loves to build systems. He thrives on creating robust, scalable infrastructure and automating workflows to deliver seamless and efficient solutions.

**Option 2 (Highlighting Impact):**

> Driven by a genuine love for building systems, Atharva is a dedicated DevOps Engineer. He specializes in bridging the gap between development and operations, leveraging automation to craft resilient and high-performing environments.

**Option 3 (A Bit More Personal):**

> For Atharva, the ultimate satisfaction comes from building systems. As a DevOps Engineer, he channelizes this passion into designing, automating, and optimizing infrastructure, ensuring everything runs smoothly from code to production.
```

## 🛠 Customization
Change prompt inside src/main.py:
```bash
contents="Your about section"
```
