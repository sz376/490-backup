import React, { useState } from "react";
import "./styles.css";

const initialMessages = [];
export default function App() {
  const [messages, setMessage] = useState(initialMessages);
  const [msg, setMsg] = useState("");

  function handleChange(event) {
    setMsg(event.target.value);
  }

  function handleAdd() {
    const newMessage = messages.concat({ msg });
    setMessage(newMessage);
    setMsg("");
  }

  return (
    <div>
      <div>
        <input type="text" value={msg} onChange={handleChange} />
        <button type="button" onClick={handleAdd}>
          chat
        </button>
      </div>

      <ul>
        {messages.map((item) => (
          <li key={item.id}>{item.msg}</li>
        ))}
      </ul>
    </div>
  );
}
