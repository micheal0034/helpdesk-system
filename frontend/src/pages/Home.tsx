// src/pages/Home.tsx
import { useState } from "react";
import ChatLayout from "../components/ChatLayout";
import ChatWindow from "../components/ChatWindow";
import ChatInput from "../components/ChatInput";
import { useHelpdesk } from "../hooks/useHelpdesk";
import type { HelpResponse } from "../services/helpdesk";

export default function Home() {
  const [messages, setMessages] = useState<
    { user: string; bot?: HelpResponse }[]
  >([]);
  const [text, setText] = useState("");
  const { mutate: askHelpdesk, isPending } = useHelpdesk();
  const handleSubmit = () => {
    if (!text.trim()) return;

    const currentUserText = text;
    setMessages((prev) => [...prev, { user: currentUserText }]);
    setText("");

    askHelpdesk(
      { text: currentUserText },
      {
        onSuccess: (response) => {
          setMessages((prev) => {
            const updated = [...prev];
            updated[updated.length - 1].bot = response;
            return updated;
          });
        }
      }
    );
  };

  return (
    <>
    <ChatLayout
      input={
        <ChatInput
          value={text}
          onChange={(e) => setText(e.target.value)}
          onSend={handleSubmit}
          disabled={isPending}
        />
      }
    >
      <ChatWindow messages={messages} loading={isPending} />
    </ChatLayout>
    </>
  );
}
