import React from "react";
import { BiSend } from "react-icons/bi";

const ChatForm = ({
  isResponseLoading,
  errorText,
  text,
  setText,
  submitHandler,
}) => {
  return (
    <div className="main-bottom">
      {errorText && <p className="errorText">{errorText}</p>}
      {errorText && <p id="errorTextHint">*Error.</p>}
      <form className="form-container" onSubmit={submitHandler}>
        <input
          type="text"
          placeholder="Send a message."
          spellCheck="false"
          value={isResponseLoading ? "Processing..." : text}
          onChange={(e) => setText(e.target.value)}
          readOnly={isResponseLoading}
        />
        {!isResponseLoading && (
          <button type="submit">
            <BiSend size={20} />
          </button>
        )}
      </form>
      <p>Your Trusted Guide to Consumer Rights and Legal Assistance.</p>
    </div>
  );
};

export default ChatForm;
