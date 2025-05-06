from typing import Dict, List
from fastapi import APIRouter, HTTPException
from src.schemas.chat import ChatIn, ChatOut
from src.services.rag_service import RAG
from src.services.chatbot_service import Bot
from dotenv import load_dotenv
import re
import os

router = APIRouter(prefix="/chat", tags=["Chat"])

load_dotenv()

@router.post("/ask", response_model=ChatOut)
def ask_chat(chat_in: ChatIn) -> ChatOut:
    """
    Ask the chat service a question.
    """

    query: str = chat_in.query
    messages: List[Dict[str, str]] = chat_in.messages

    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    if not messages:
        raise HTTPException(status_code=400, detail="Messages cannot be empty.")
    
    chatbot = Bot(
        api_key=os.getenv("GROQ_API_KEY"),
        model=os.getenv("MODEL"),
        language=os.getenv("LANGUAGE")
    )

    chatbot.message_history = messages
    answer: str = chatbot.chat(query)
    answer = re.sub(r"<think>(.*?)</think>", "", answer, flags=re.DOTALL).strip()

    chat_out = ChatOut(
        query=query,
        messages=messages,
        answer=answer,
    )

    return chat_out

@router.post("/ask-rag", response_model=ChatOut)
def ask_chat_rag(chat_in: ChatIn) -> ChatOut:
    """
    Ask the chat service a question using RAG.
    """

    rag = RAG(
        data_path="docs/RAG_info/",
        chroma_path="chroma_db/"
    )

    query: str = rag.augment_query(chat_in.query)
    chat_in.query = query

    chat_out_response: ChatOut = ask_chat(chat_in)

    return chat_out_response
