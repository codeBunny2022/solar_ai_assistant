from fastapi import FastAPI, Query
from utils import query_llm

app = FastAPI()

@app.get("/ask")
def ask_solar(
    question: str = Query(..., title="User Question"),
    level: str = Query("intermediate", title="Explanation Level", enum=["basic", "intermediate", "advanced"])
):
    """
    API endpoint to answer user questions about solar energy with AI-generated responses.
    """
    prompt = f"Answer this question about solar energy: {question}. Provide a {level} level explanation."

    try:
        response = query_llm(prompt)  # AI-generated answer
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
