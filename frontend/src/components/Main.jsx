import React from "react";
import MessageList from "./MessageList";
import ChatForm from "./ChatForm";

const Main = ({
  currentTitle,
  currentChat,
  scrollToLastItem,
  isResponseLoading,
  errorText,
  text,
  setText,
  submitHandler,
}) => {
  return (
    <section className="main">
      {!currentTitle && (
        <div className="empty-chat-container">
          <img
            src="images/helix-logo2.png"
            width={100}
            height={100}
            alt="HelixAI"
          />
          <h1>HelixAI Bot</h1>
          <h3>How can I help you today?</h3>
        </div>
      )}
      <MessageList
        currentChat={currentChat}
        scrollToLastItem={scrollToLastItem}
      />
      <ChatForm
        isResponseLoading={isResponseLoading}
        errorText={errorText}
        text={text}
        setText={setText}
        submitHandler={submitHandler}
      />
    </section>
  );
};

export default Main;
