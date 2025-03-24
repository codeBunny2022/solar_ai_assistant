```md
# ☀️ Solar AI Assistant

The **Solar AI Assistant** is an AI-powered tool that provides real-time answers about solar energy. It supports **predefined topics** and **custom queries** with different explanation levels.

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/codeBunny2022/solar_ai_assistant.git
cd solar_ai_assistant
```

### 2️⃣ Create a Virtual Environment (Optional)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key

Create a `.env` file in the root directory and add:

```
OPENAI_API_KEY=your-api-key
```


---

## 🚀 Running the Project

### 1️⃣ Start the Backend (FastAPI)

```bash
uvicorn main:app --reload
```

* API will run at: `http://127.0.0.1:8000`

### 2️⃣ Start the Frontend (Streamlit)

```bash
streamlit run frontend/app.py
```

* Open `http://localhost:8501` in your browser.


---

## 🔬 Testing the API

### 📌 Test the API using `curl`

```bash
curl -X GET "http://127.0.0.1:8000/ask?question=What is solar energy?&level=basic"
```

Example Response:

```json
{"response": "Solar energy is power from the sun converted into electricity."}
```

### 📌 Test API using Postman


1. Open Postman
2. Create a **GET** request to:

   ```
   http://127.0.0.1:8000/ask?question=What is solar energy?&level=basic
   ```
3. Click **Send** and check the response.


---

## 🚢 Running with Docker (Optional)

### 1️⃣ Build the Docker Image

```bash
docker build -t solar-ai-assistant ./deployment
```

### 2️⃣ Run the Container

```bash
docker run -p 8000:8000 -p 8501:8501 solar-ai-assistant
```


---

## 🛠 Troubleshooting

| Issue | Solution |
|----|----|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `Invalid API Key` | Check `.env` file and verify your API key |
| `Frontend Not Loading` | Ensure FastAPI backend is running |


---

## 📜 License

MIT License


---

```

This **minimalist README** provides **setup, running, testing, and troubleshooting** without unnecessary clutter. Let me know if you need modifications! 🚀
```


