// src/components/UserMessage.tsx
export default function UserMessage({ text }: { text: string }) {
  return (
    <div className="text-right">
      <div className="inline-block bg-blue-100 text-blue-900 p-3 rounded-2xl max-w-md mb-6">
        {text}
      </div>
    </div>
  );
}
