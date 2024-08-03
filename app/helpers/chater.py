from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory

AI71_BASE_URL = "https://api.ai71.ai/v1/"
AI71_API_KEY = "<your AI71 API key>"

chat = ChatOpenAI(
    model="tiiuae/falcon-180B-chat",
    api_key=AI71_API_KEY,
    base_url=AI71_BASE_URL,
    streaming=True,
)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)


chain = prompt | chat

demo_ephemeral_chat_history_for_chain = ChatMessageHistory()

chain_with_message_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: demo_ephemeral_chat_history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history",
)