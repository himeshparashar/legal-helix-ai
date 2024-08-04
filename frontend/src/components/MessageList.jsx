import React from "react";
import { BiSolidUserCircle } from "react-icons/bi";

const MessageList = ({ currentChat, scrollToLastItem }) => {
  return (
    <div className="main-header">
      <ul>
        {currentChat?.map((chatMsg, idx) => {
          const isUser = chatMsg.role === "user";
          return (
            <li key={idx} ref={scrollToLastItem}>
              {isUser ? (
                <div>
                  <BiSolidUserCircle size={28.8} />
                </div>
              ) : (
                <img src="images/helix-logo.jpg" alt="HelixAI" /> 
              )}
              {isUser ? (
                <div>
                  <p className="role-title">You</p>
                  <p>{chatMsg.content}</p>
                </div>
              ) : (
                <div>
                  <p className="role-title">HelixAI</p>
                  <p>{chatMsg.content}</p>
                </div>
              )}
            </li>
          );
        })}
      </ul>
    </div>
  );
};

export default MessageList;
