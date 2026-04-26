from __future__ import annotations

from typing import Any, Dict, List, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .nlp_engine import analyze_text


class AnalyzeRequest(BaseModel):
    report_text: Optional[str] = Field(default=None, description="Disease report / outbreak text")
    symptom_text: Optional[str] = Field(default=None, description="User symptom description")


class Entity(BaseModel):
    text: str
    label: str


class AnalyzeResponse(BaseModel):
    summary: str
    predicted_category: str
    entities: List[Entity]
    keywords: List[str]
    debug: Dict[str, Any] = Field(default_factory=dict)


app = FastAPI(title="NLP Disease Intelligence Service", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest) -> AnalyzeResponse:
    report_text = (req.report_text or "").strip()
    symptom_text = (req.symptom_text or "").strip()
    payload = analyze_text(report_text=report_text, symptom_text=symptom_text)
    return AnalyzeResponse(**payload)

