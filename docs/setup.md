This document explains how to install and set up the Solar AI Assistant.

## 1️⃣ Prerequisites

* Python 3.8+
* `pip` installed
* OpenAI API Key (from [OpenAI](https://platform.openai.com/account/api-keys))

## 2️⃣ Install Dependencies

Run:

```bash
pip install -r requirements.txt
3️⃣ Configure API Key
Create a .env file in the root directory:

ini
Copy
Edit
OPENAI_API_KEY=your-api-key
4️⃣ Start the Backend
bash
Copy
Edit
uvicorn main:app --reload
5️⃣ Start the Frontend
bash
Copy
Edit
streamlit run frontend/app.py

Now visit http://localhost:8501 to use the app.
```


