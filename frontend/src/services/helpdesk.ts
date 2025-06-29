// src/services/helpdesk.ts
import axios from "axios";

const API_BASE = "https://helpdesk-system.railway.internal/api/v1"; // Update if your backend is elsewhere

export interface HelpRequest {
  text: string;
}

export interface ClassificationResult {
  label: string;
  confidence: number;
  escalate: boolean;
}

export interface RetrievalResult {
  id: string;
  text: string;
  distance: number;
}

export interface HelpResponse {
  classification: ClassificationResult;
  snippets: RetrievalResult[];
  answer: string;
}

export const classifyRequest = async (data: HelpRequest) => {
  const res = await axios.post<ClassificationResult>(
    `${API_BASE}/classify`,
    data
  );
  return res.data;
};

export const retrieveSnippets = async (data: HelpRequest) => {
  const res = await axios.post<RetrievalResult[]>(
    `${API_BASE}/retrieve`,
    data
  );
  return res.data;
};

export const helpdeskRequest = async (data: HelpRequest) => {
  const res = await axios.post<HelpResponse>(
    `${API_BASE}/helpdesk`,
    data
  );
  return res.data;
};
