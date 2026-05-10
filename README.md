# NLP-Based Disease Outbreak Analysis and Prediction System

This project combines:
- **Structured disease analytics + dashboards** (country-wise stats, charts)
- **SIR model forecasting** (existing prediction module)
- **NLP health text intelligence** (new: summarization, symptom classification, entity/keyword extraction)

## Run the dashboard
```bash
npm install
npm run dev
```

## Run the NLP module (Python)
```bash
python -m pip install -r nlp_service/requirements.txt
python -m uvicorn nlp_service.main:app --host 127.0.0.1 --port 8000 --reload
```

Then in the UI, click **Analyze Health Text** (top-right) and run the analysis.

## Notes
- If the `transformers` model download is slow, the NLP service automatically falls back to a simple summarizer.
- If the spaCy model is not installed, entity extraction falls back to a lightweight rule-based approach.

## Report
See `PROJECT_REPORT.md` for updated title, abstract, aim, objectives, methodology, implementation, results, conclusion, and future scope.
