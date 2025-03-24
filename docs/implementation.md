```md
# ⚙️ Technical Implementation

## Architecture Overview
The Solar AI Assistant is structured into:
- **Backend (FastAPI)**: Handles AI queries and API requests.
- **Frontend (Streamlit)**: User interface for interacting with AI.
- **Docker Support**: Enables easy deployment.

## Backend Details
- Built with **FastAPI**
- Queries OpenAI’s **GPT model** for real-time responses
- Uses `utils.py` for query processing

## Frontend Details
- Built with **Streamlit**
- Provides interactive UI with topic selection
- Communicates with backend via API requests

## API Endpoint
| Method | Endpoint | Parameters |
|--------|----------|------------|
| `GET` | `/ask` | `question`, `level` |

Example:
GET /ask?question=What is solar energy?&level=basic

css
Copy
Edit
Response:
```json
{"response": "Solar energy is harnessed from the sun and converted into electricity."}
```


