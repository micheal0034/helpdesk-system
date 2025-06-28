// src/components/ChatInput.tsx
import { useCallback, useEffect, useRef } from "react";

interface Props {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLTextAreaElement>) => void;
  onSend: () => void;
  disabled: boolean;
}

export default function ChatInput({
  value,
  onChange,
  onSend,
  disabled
}: Props) {
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Auto-grow height based on content
  useEffect(() => {
    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = "auto";
      textarea.style.height = `${textarea.scrollHeight}px`;
    }
  }, [value]);

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        onSend();
      }
    },
    [onSend]
  );

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        onSend();
      }}
      className="sticky bottom-0 bg-white rounded-3xl px-4 py-3 flex gap-2"
    >
      <textarea
        ref={textareaRef}
        className="flex-1 rounded-xl p-3 resize-none overflow-hidden focus:outline-none"
        rows={1}
        placeholder="Type your question..."
        value={value}
        onChange={onChange}
        onKeyDown={handleKeyDown}
        disabled={disabled}
      />
      <button
        type="submit"
        className="bg-blue-600 text-white px-5 py-2 rounded-xl hover:bg-blue-700 disabled:opacity-50"
        disabled={disabled}
      >
        Send
      </button>
    </form>
  );
}
