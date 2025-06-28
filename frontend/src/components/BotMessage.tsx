// src/components/BotMessage.tsx
import type { HelpResponse } from "../services/helpdesk";

export default function BotMessage({ data }: { data: HelpResponse }) {
  return (
    <div className="text-left space-y-2">
      <div className="inline-block text-gray-900 px-4 rounded-2xl ">
        <p className="whitespace-pre-wrap">{data.answer}</p>
      </div>
      <div className="flex justify-baseline items-center gap-3 px-4 mb-4">
        <p className="text-xs text-green-900 bg-green-300 rounded-3xl px-2 py-1 border border-green-500">
          <strong>Category:</strong> {data.classification.label}
        </p>
        <p className="text-xs text-fuchsia-900 bg-fuchsia-300 rounded-3xl px-2 py-1 border border-fuchsia-500">
          <strong>Confidence:</strong>{" "}
          {(data.classification.confidence * 100).toFixed(1)}%
        </p>
        {data.classification.escalate && (
          <p className="text-xs text-red-900 bg-red-300 rounded-3xl px-2 py-1 border border-red-500">
            Escalation Recommended
          </p>
        )}
      </div>
      {/* <div className="text-sm text-gray-500 pl-4">
        {data.snippets.length > 0 && (
          <>
            <p className="font-semibold">Context:</p>
            <ul className="list-disc list-inside">
              {data.snippets.map((snip, idx) => (
                <li key={idx}>{snip.text}</li>
              ))}
            </ul>
          </>
        )}
      </div> */}
    </div>
  );
}
