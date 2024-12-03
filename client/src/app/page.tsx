"use client";
import {  useSearchParams } from "next/navigation";
import { useState, useEffect } from "react";
import { getHistory, sendMessage } from "@/utils/api";
import { History } from "@/utils/types";

export default function Home() {
  const query = useSearchParams();
  const session = query.get("session");
  const [currentText, setText] = useState("")
  const [chats, setChats] = useState<History[]>([]);

  const handleSend = () => {
    sendMessage(session || "default", currentText).then((success) => {
      if (success) {
        getHistory(session || "default").then((data) => {
          setChats(data);
        })
      }
    })
    setText("")
  }

  useEffect(() => {
    getHistory(session || "default").then((data) => {
      setChats(data);
    })
    console.log(chats)
  }, [])

  useEffect(() => {}, [chats])
  
  return (
    <div className="grid place-items-center p-0 lg:p-32 h-full">
      <div className="w-full h-full">
        <div className="bg-white shadow-md rounded-lg p-4 h-full">
          <div className="h-96 overflow-y-scroll mb-4">
            {chats.map((chat: History, index: number) => {
              return (
                <div className="grid w-full p-2 gap-2" key={index}>
                  <div className="chat chat-start">
                    <div className="chat-bubble bg-gray-200 text-black shadow-2xl">
                      <p className="text-sm">{chat.query}</p>
                    </div>
                  </div>
                  <div className="chat chat-end">
                    <div className="chat-bubble bg-blue-200 text-black shadow-2xl">
                      <p className="text-sm">{chat.output}</p>
                    </div>
                  </div>
                </div>
              )
            })}
          </div>
          <div className="flex">
            <input
              type="text"
              className="flex-grow p-2 border rounded-l-lg"
              value={currentText}
              onChange={(e) => setText(e.target.value)}
              placeholder="Type your message..."
            />
            <button
              className="bg-blue-500 text-white p-2 rounded-r-lg"
              onClick={handleSend}
            >
              Send
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
