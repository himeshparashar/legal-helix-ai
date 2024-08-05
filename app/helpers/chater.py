import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from app.helpers.retrival import retrieverfn
from langchain.chains import create_history_aware_retriever
from langchain_core.chat_history import BaseChatMessageHistory
import dotenv

dotenv.load_dotenv()



AI71_BASE_URL = "https://api.ai71.ai/v1/"
AI71_API_KEY = os.environ.get("AI_KEY")

print(os.environ.get("QDRANT_KEY"))
print(os.environ.get("AI_KEY"))

print(AI71_API_KEY)
print("yoyoyoyoyoyo")
# os.environ["LANGCHAIN_TRACING_V2"] = "true"

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

async def get_chat_response(input_message: str,userid:str):
    try:
        retriever = await retrieverfn()

        llm = ChatOpenAI(
            model="tiiuae/falcon-180B-chat",
            api_key=AI71_API_KEY,
            base_url=AI71_BASE_URL,
            streaming=True,
        )

        contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, "
    "just reformulate it if needed and otherwise return it as is."
)

        contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
        )

        history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
        )

        system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "{context}"
        )
        qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
        )

        question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)


        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

        conversational_rag_chain = RunnableWithMessageHistory(
            rag_chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )


        response = conversational_rag_chain.invoke(
        {"input": input_message},
        config={
            "configurable": {"session_id": userid}
        },  
        )["answer"]

        return response
    except Exception as e:
        return str(e)