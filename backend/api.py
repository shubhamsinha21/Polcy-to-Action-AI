from fastapi import FastAPI
from pydantic import BaseModel

from app.rule_engine import check_eligibility
from app.ranking_engine import rank_schemes
from app.chat_engine import run_policy_chat
from app.vector_store import search_schemes

app = FastAPI(title="Policy-to-Action AI API")


class UserProfile(BaseModel):

    occupation: str
    state: str
    income: int
    land_owned: bool


class ChatRequest(BaseModel):

    message: str


@app.get("/")
def root():

    return {"message": "Policy-to-Action AI API running"}


@app.post("/check-schemes")
def check_schemes(user: UserProfile):

    schemes = check_eligibility(user.dict())

    ranked = rank_schemes(user.dict(), schemes)

    return {"schemes": ranked}


@app.post("/policy-chat")
def policy_chat(req: ChatRequest):

    response = run_policy_chat(req.message)

    return {"response": response}


@app.get("/search-schemes")
def search(query: str):

    results = search_schemes(query)

    return {"results": results}