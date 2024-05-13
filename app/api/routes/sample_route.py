from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.api.utils import templates
from pydantic import BaseModel
from app.utils.utils import ollama_client
import ollama

router = APIRouter()


class ChatMessage(BaseModel):
    role: str = 'user'
    content: str


@router.get('/', response_class=HTMLResponse)
def get_sample_page(request: Request):
    return templates.TemplateResponse('chat.html',
                                      context={'request': request})


@router.post('/chat')
def post_chat(chat_messages: list[ChatMessage]):
    messages = []
    for chat_message in chat_messages:
        messages.append(
            {
                'role': chat_message.role,
                'content': chat_message.content,
            }
        )

    response = ollama_client.chat(model='llama3', messages=messages)
    return {'response': response['message']['content']}
