// src/hooks/useHelpdesk.ts
import { useMutation } from "@tanstack/react-query";
import { helpdeskRequest } from "../services/helpdesk";
import type {
    HelpRequest,
    HelpResponse
  } from "../services/helpdesk";

export function useHelpdesk() {
  return useMutation<HelpResponse, Error, HelpRequest>({
    mutationFn: helpdeskRequest
  });
}
