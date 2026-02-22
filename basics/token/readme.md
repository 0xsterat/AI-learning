# Tokenizing with code

This code converts your sentence into the tokens that the GPT model uses internally. You are preparing it the same way the model does before generating output.

refer - https://platform.openai.com/tokenizer

## How Are Tokens Calculated? (Using OpenAI's Token Calculator)

```bash
pip install tiktoken
```
## 📦 Installation
** 1️⃣ Clone this repo**
```bash
git clone https://github.com/0xsterat/AI-learning.git
cd AI-learning
cd basics
cd token
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


## ▶️ Running the Application
```bash
python src/main.py
```

##📤 Sample Output
```bash
Tokens: [12194, 922, 1308, 382, 23747, 277, 2873, 326, 357, 1299, 48892]
12194 = Hi
922 =  my
1308 =  name
382 =  is
23747 =  Ath
277 = ar
2873 = va
326 =  and
357 =  I
1299 =  like
48892 =  Pizza
```

## 🛠 Customization
Change prompt inside src/main.py:
```bash
tokens = encoding.encode("Hi my name is YOUR_NAME and I like Pizza")
```

