import { useMemo, useState } from "react";
import { analyzeHealthText, type NlpAnalysisResult } from "@/utils/nlpApi";

const SAMPLE_REPORT = `Public health teams reported a sudden rise in fever and cough cases in multiple districts. A few patients developed shortness of breath and required hospitalization. Officials advised mask use in crowded areas and recommended testing for suspected cases. International travel history was noted in some patients.`;

const SAMPLE_SYMPTOMS = `I have high fever, headache, body pain and joint pain for 3 days.`;

function Pill({ children }: { children: string }) {
  return (
    <span
      className="inline-flex items-center px-2 py-0.5 text-[10px] tracking-[0.08em] uppercase"
      style={{ border: "1px solid #1A2540", color: "#E8EDF5CC", background: "#0D1525" }}
    >
      {children}
    </span>
  );
}

function SectionTitle({ children }: { children: string }) {
  return (
    <div className="text-[10px] tracking-[0.15em] uppercase mb-2" style={{ color: "#E8EDF555" }}>
      {children}
    </div>
  );
}

export default function HealthTextPanel({
  onClose,
}: {
  onClose: () => void;
}) {
  const [reportText, setReportText] = useState(SAMPLE_REPORT);
  const [symptomText, setSymptomText] = useState(SAMPLE_SYMPTOMS);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string>("");
  const [result, setResult] = useState<NlpAnalysisResult | null>(null);

  const canAnalyze = useMemo(() => {
    const a = reportText.trim().length > 0;
    const b = symptomText.trim().length > 0;
    return a || b;
  }, [reportText, symptomText]);

  async function run() {
    setError("");
    setLoading(true);
    try {
      const data = await analyzeHealthText({
        report_text: reportText.trim() || undefined,
        symptom_text: symptomText.trim() || undefined,
      });
      setResult(data);
    } catch (e) {
      setResult(null);
      setError(e instanceof Error ? e.message : "Failed to analyze text.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div
      className="fixed top-0 right-0 bottom-0 z-50 overflow-y-auto slide-in-right"
      style={{
        width: 460,
        background: "rgba(5,10,20,0.96)",
        borderLeft: "1px solid #1A2540",
        backdropFilter: "blur(12px)",
      }}
    >
      <button
        onClick={onClose}
        className="absolute top-3 right-3 w-8 h-8 flex items-center justify-center text-sm transition-colors"
        style={{ color: "#E8EDF566", border: "1px solid #1A2540" }}
      >
        ✕
      </button>

      <div className="p-5 space-y-5">
        <div>
          <h2 className="text-lg font-bold" style={{ color: "#E8EDF5" }}>
            Analyze Health Text
          </h2>
          <div className="text-[11px] mt-1" style={{ color: "#E8EDF588" }}>
            Summarization • Keyword/Entity Extraction • Symptom Text Classification
          </div>
        </div>

        <div>
          <SectionTitle>Disease report / medical news text</SectionTitle>
          <textarea
            value={reportText}
            onChange={(e) => setReportText(e.target.value)}
            rows={6}
            className="w-full text-xs p-3 outline-none"
            style={{ background: "#0D1525", border: "1px solid #1A2540", color: "#E8EDF5CC" }}
            placeholder="Paste a disease report or outbreak description..."
          />
        </div>

        <div>
          <SectionTitle>Symptom description (natural language)</SectionTitle>
          <textarea
            value={symptomText}
            onChange={(e) => setSymptomText(e.target.value)}
            rows={3}
            className="w-full text-xs p-3 outline-none"
            style={{ background: "#0D1525", border: "1px solid #1A2540", color: "#E8EDF5CC" }}
            placeholder="Example: fever with cough and breathlessness..."
          />
        </div>

        <div className="flex items-center gap-2">
          <button
            disabled={!canAnalyze || loading}
            onClick={run}
            className="px-4 py-2 text-xs font-medium tracking-[0.12em] uppercase transition-all duration-200 disabled:opacity-50"
            style={{
              background: "rgba(0,255,209,0.08)",
              border: "1px solid #00FFD1",
              color: "#00FFD1",
            }}
          >
            {loading ? "Analyzing..." : "Run NLP Analysis"}
          </button>
          <div className="text-[10px]" style={{ color: "#E8EDF555" }}>
            Tip: run the Python NLP service for live results.
          </div>
        </div>

        {error && (
          <div className="p-3 text-xs" style={{ background: "#0D1525", border: "1px solid #1A2540", color: "#FF6B35" }}>
            {error}
          </div>
        )}

        {result && (
          <div className="space-y-4">
            <div>
              <SectionTitle>Generated summary</SectionTitle>
              <div className="p-3 text-xs leading-relaxed" style={{ background: "#0D1525", border: "1px solid #1A2540", color: "#E8EDF5CC" }}>
                {result.summary}
              </div>
            </div>

            <div>
              <SectionTitle>Predicted disease category</SectionTitle>
              <div className="flex flex-wrap gap-2">
                <Pill>{result.predicted_category}</Pill>
              </div>
            </div>

            <div>
              <SectionTitle>Extracted keywords</SectionTitle>
              <div className="flex flex-wrap gap-2">
                {result.keywords.length ? result.keywords.map((k) => <Pill key={k}>{k}</Pill>) : <Pill>none</Pill>}
              </div>
            </div>

            <div>
              <SectionTitle>Named entities</SectionTitle>
              <div className="space-y-2">
                {result.entities.length ? (
                  result.entities.slice(0, 18).map((ent, idx) => (
                    <div
                      key={`${ent.text}-${idx}`}
                      className="flex items-center justify-between gap-3 p-2"
                      style={{ background: "#0D1525", border: "1px solid #1A2540" }}
                    >
                      <div className="text-xs" style={{ color: "#E8EDF5CC" }}>
                        {ent.text}
                      </div>
                      <div className="text-[10px] tracking-[0.12em] uppercase" style={{ color: "#00FFD1" }}>
                        {ent.label}
                      </div>
                    </div>
                  ))
                ) : (
                  <div className="text-xs" style={{ color: "#E8EDF555" }}>
                    No entities detected.
                  </div>
                )}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

