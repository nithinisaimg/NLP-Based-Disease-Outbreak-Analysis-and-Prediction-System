# NLP-Based Disease Outbreak Analysis and Prediction System

## Abstract
This mini‑project presents an **intelligent disease monitoring system** that combines **big data analytics on structured disease statistics** (cases, active, recovered, deaths, country-wise spread) with **Natural Language Processing (NLP) on unstructured health text** (disease reports, outbreak descriptions, and symptom narratives). The platform provides a country‑level visualization dashboard and disease spread forecasting using the **SIR epidemiological model**, while also enabling **text summarization**, **symptom text classification**, and **keyword/entity extraction** from health-related text. By integrating numerical forecasting and text intelligence in a single interface, the system supports faster understanding of outbreaks and improved situational awareness for early public health decisions.

## Aim
To develop an integrated disease surveillance platform that performs **(1) outbreak analytics and SIR‑based forecasting using structured disease data** and **(2) NLP‑based intelligence from unstructured health text** to support early warning and decision-making.

## Objectives
- **Structured analytics**: Collect and visualize country‑wise disease statistics and trends on a dashboard.
- **Epidemiological forecasting**: Predict infection trends using the **SIR model** for short‑term (e.g., 30‑day) outlook.
- **Text summarization**: Generate a short, readable summary of pasted disease reports/medical news.
- **Symptom text classification**: Accept symptoms in natural language and predict a **possible disease category**.
- **Entity/keyword extraction**: Extract important entities such as **disease names, symptoms, countries, transmission type, and severity**.
- **Unified platform**: Integrate NLP outputs into the same UI with the existing analytics so the system looks like a complete intelligent monitoring solution.

## Methodology (Updated)
### 1) Data Sources and Inputs
- **Structured input**: Country‑level disease statistics (cases, active, recovered, deaths, population).
- **Unstructured input**: User‑pasted **disease report text** / **medical bulletin** and **symptom descriptions**.

### 2) System Workflow
1. Fetch structured disease statistics and update the dashboard.
2. Run SIR model to generate short‑term spread forecast.
3. User opens **Analyze Health Text** and pastes report/symptoms.
4. NLP module performs preprocessing and generates:
   - summary
   - predicted disease category
   - keywords/entities
5. UI shows results next to existing disease analytics to support combined monitoring.

### 3) Technology Stack (Updated)
- **Frontend**: Existing React dashboard (unchanged).
- **Structured analytics**: Existing disease data utilities + charts (unchanged).
- **Prediction**: Existing **SIR model** module (unchanged).
- **NLP processing (new)**:
  - **Python** for NLP services and processing
  - **NLTK / spaCy** for preprocessing and information extraction
  - **Hugging Face Transformers** summarization pipeline (optional; with fallback summarization)

## Implementation (Updated – NLP + Big Data)
### A) Structured Data Analytics + Forecasting (Existing)
- Fetch and display country-wise statistics.
- Generate time trend charts for disease spread.
- Run **SIR model** to estimate infected/recovered curves and risk level.

### B) NLP Module (New)
The NLP module processes unstructured text and follows these steps:

1. **Text preprocessing**
   - lowercasing, whitespace cleaning
   - punctuation cleaning (basic)

2. **Tokenization**
   - split text into word tokens

3. **Stopword removal**
   - remove common words (the, is, and, etc.) to reduce noise

4. **Stemming / Lemmatization**
   - basic normalization (rule-based / pipeline-based where available)

5. **Feature extraction**
   - keyword frequency and important term selection

6. **Summarization**
   - Transformer summarization pipeline (if available), else a simple frequency-based extractive summary

7. **Classification**
   - symptom text classification into a disease category (lightweight pipeline approach using symptom/disease keywords; can be extended to ML later)

8. **Keyword / Entity extraction**
   - Identify disease/symptom/country/transmission/severity terms (spaCy NER if available, else rule-based)

## Results (Sample Outputs)
### 1) Input report → Generated summary
- **Input**: “Public health teams reported a sudden rise in fever and cough cases…”
- **Summary (sample)**: “A rise in fever and cough cases was reported across districts, with some hospitalizations. Officials advised testing and preventive measures in crowded areas.”

### 2) Input symptom text → Predicted disease category
- **Input**: “I have high fever, headache, body pain and joint pain for 3 days.”
- **Predicted label (sample)**: “Dengue”

### 3) Extracted keywords/entities
- **Keywords (sample)**: fever, cough, hospitalization, testing, respiratory
- **Entities (sample)**:
  - DISEASE: COVID‑19 / Influenza
  - SYMPTOM: fever, cough, shortness of breath
  - COUNTRY: India
  - TRANSMISSION: airborne/droplet
  - SEVERITY: hospitalized

### 4) Existing spread analytics (dashboard)
- Country‑level charts showing confirmed/active/recovered/deaths.
- 30‑day SIR trend and risk forecast (existing module).

## Conclusion (Updated)
The project has been enhanced from a disease analytics dashboard into an **intelligent disease surveillance system**. It now supports:
- **Numerical disease spread forecasting** using an epidemiological **SIR prediction model**, and
- **Text-based disease intelligence** using NLP techniques such as summarization, symptom classification, and entity/keyword extraction.
This combined approach provides a more complete view of outbreaks by connecting “what the numbers show” with “what reports and symptoms describe.”

## Future Scope (Updated)
- **Multilingual medical text analysis** (Hindi/Tamil/Spanish, etc.)
- **AI healthcare chatbot** for symptom guidance and FAQs
- **Live health bulletin mining** from PDFs/news feeds
- **Social media outbreak monitoring** (Twitter/Reddit signals)
- **Real-time disease news summarization** and alert generation

