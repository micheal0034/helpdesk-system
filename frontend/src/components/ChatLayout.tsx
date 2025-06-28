export default function ChatLayout({
  children,
  input
}: {
  children: React.ReactNode;
  input: React.ReactNode;
}) {
  return (
    <div className="flex flex-col h-screen bg-gray-100">
      <header className="sticky top-0 text-center py-4 text-xl font-semibold bg-white shadow z-10">
        🧠 Intelligent Help Desk
      </header>

      {/* Chat Scrollable Area */}
      <div className="flex-1 overflow-y-auto p-4 flex justify-center">
        <div className="w-full max-w-3xl">{children}</div>
      </div>

      {/* Input Fixed to Bottom */}
      <div className="bg-gray-100 p-4 flex justify-center">
        <div className="w-full max-w-3xl">{input}</div>
      </div>
    </div>
  );
}
