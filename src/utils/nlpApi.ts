export type NlpEntity = {
  text: string;
  label: string;
};

export type NlpAnalysisResult = {
  summary: string;
  predicted_category: string;
  entities: NlpEntity[];
  keywords: string[];
};

export async function analyzeHealthText(input: {
  report_text?: string;
  symptom_text?: string;
}): Promise<NlpAnalysisResult> {
  const base = import.meta.env.VITE_NLP_API_BASE?.toString().trim() || "http://127.0.0.1:8000";
  const res = await fetch(`${base}/analyze`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(input),
  });

  if (!res.ok) {
    const msg = await res.text().catch(() => "");
    throw new Error(`NLP service error (${res.status}): ${msg || res.statusText}`);
  }

  return (await res.json()) as NlpAnalysisResult;
}

