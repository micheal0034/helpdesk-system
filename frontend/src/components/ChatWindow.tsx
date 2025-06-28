// src/components/ChatWindow.tsx
import { useEffect, useRef } from "react";
import UserMessage from "./UserMessage";
import BotMessage from "./BotMessage";
import Loader from "./Loader";
import type { HelpResponse } from "../services/helpdesk";

interface Props {
  messages: { user: string; bot?: HelpResponse }[];
  loading: boolean;
}

export default function ChatWindow({ messages, loading }: Props) {
  const bottomRef = useRef<HTMLDivElement | null>(null);
  
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]); // or `data` if using React Query

  return (
    <div className="max-w-3xl mx-auto space-y-6">
      {messages.map((msg, idx) => (
        <div key={idx}>
          <UserMessage text={msg.user} />
          {msg.bot ? <BotMessage data={msg.bot} /> : loading && <Loader />}
        </div>
      ))}
      <div ref={bottomRef} />
    </div>
  );
}
