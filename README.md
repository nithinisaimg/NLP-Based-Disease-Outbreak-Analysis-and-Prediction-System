# 🌍 NLP-Based Disease Outbreak Analysis & Prediction System

> **An intelligent disease surveillance platform that combines Natural Language Processing (NLP), epidemiological forecasting, and interactive data visualization to analyze and predict disease outbreaks worldwide.**

![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-38BDF8?style=for-the-badge&logo=tailwind-css)
![NLP](https://img.shields.io/badge/NLP-Powered-success?style=for-the-badge)

---

# 📖 Overview

The **NLP-Based Disease Outbreak Analysis & Prediction System** is an intelligent health analytics platform that integrates structured disease statistics with Natural Language Processing (NLP) to monitor, analyze, and forecast disease outbreaks.

The application enables users to visualize global disease trends, analyze outbreak reports, summarize health-related text, classify diseases from symptom descriptions, and predict future infection patterns using the **SIR epidemiological model**.

Designed as an educational and practical public health solution, the project demonstrates how AI and data analytics can support disease surveillance and informed decision-making.

---

# ✨ Features

## 🌍 Global Disease Dashboard

- Interactive world visualization
- Country-wise disease statistics
- Active, recovered, and death counts
- Disease trend monitoring

---

## 📈 Outbreak Forecasting

Predict future disease spread using the **SIR (Susceptible–Infected–Recovered)** epidemiological model.

Features include:

- Infection forecasting
- Recovery prediction
- Trend visualization
- Short-term outbreak analysis

---

## 🧠 Natural Language Processing

Analyze health-related text using built-in NLP capabilities.

### Supported Features

- 📄 Text Summarization
- 🦠 Symptom Classification
- 🔍 Keyword Extraction
- 🏥 Disease Identification
- 🌎 Country Recognition
- 📌 Entity Extraction

---

## 📊 Interactive Analytics

- Disease comparison charts
- Historical outbreak trends
- Visual dashboards
- Country-level statistics

---

## 🔍 Smart Search

Search diseases, countries, and outbreak information instantly.

---

## 📱 Responsive Interface

Optimized for:

- Desktop
- Tablet
- Mobile

---

# 🧠 NLP Pipeline

The platform processes health-related text through the following pipeline:

```text
User Input
      │
      ▼
Text Preprocessing
      │
      ▼
Tokenization
      │
      ▼
Keyword & Entity Extraction
      │
      ▼
Disease Classification
      │
      ▼
Text Summarization
      │
      ▼
Prediction & Insights
```

---

# 📈 Forecasting Pipeline

```text
Historical Disease Data
          │
          ▼
Data Cleaning
          │
          ▼
SIR Model
          │
          ▼
Future Infection Prediction
          │
          ▼
Visualization Dashboard
```

---

# 🛠 Tech Stack

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- shadcn/ui

## Backend

- Python
- FastAPI

## NLP

- Text Summarization
- Symptom Classification
- Entity Recognition
- Keyword Extraction

## Epidemiological Modeling

- SIR (Susceptible–Infected–Recovered) Model

## Visualization

- Interactive Charts
- Globe View
- Country Statistics
- Disease Trend Graphs

---

# 📂 Project Structure

```text
.
├── src/
│   ├── components/
│   │   └── epiglobe/
│   │       ├── GlobeView.tsx
│   │       ├── DiseaseChart.tsx
│   │       ├── DiseaseSelector.tsx
│   │       ├── HistoricalDiseases.tsx
│   │       ├── SearchBar.tsx
│   │       ├── StatsBar.tsx
│   │       ├── SidePanel.tsx
│   │       └── HealthTextPanel.tsx
│   │
│   ├── routes/
│   └── lib/
│
├── nlp_service/
│   ├── main.py
│   ├── nlp_engine.py
│   └── requirements.txt
│
├── PROJECT_REPORT.md
└── package.json
```

---

# 🚀 Installation

## Clone the Repository

```bash
git clone https://github.com/nithinisaimg/NLP-Based-Disease-Outbreak-Analysis-and-Prediction-System.git
```

Navigate into the project

```bash
cd NLP-Based-Disease-Outbreak-Analysis-and-Prediction-System
```

Install frontend dependencies

```bash
npm install
```

Install backend dependencies

```bash
cd nlp_service
pip install -r requirements.txt
```

Start the FastAPI server

```bash
uvicorn main:app --reload
```

Run the frontend

```bash
npm run dev
```

Open your browser

```
http://localhost:5173
```

---

# 🎯 Key Features

- 🌍 Global Disease Visualization
- 📊 Country-wise Statistics
- 📈 SIR Forecasting
- 🧠 NLP-based Health Text Analysis
- 📄 Text Summarization
- 🦠 Disease Classification
- 🔍 Entity Extraction
- 📱 Responsive Dashboard

---

# 📚 Learning Outcomes

This project demonstrates practical knowledge of:

- Natural Language Processing (NLP)
- Epidemiological Modeling
- SIR Mathematical Model
- Data Visualization
- FastAPI Development
- React & TypeScript
- Healthcare Analytics
- AI for Public Health

---

# 🔮 Future Enhancements

- Real-time WHO/CDC data integration
- Machine Learning forecasting models
- LSTM-based outbreak prediction
- Interactive heat maps
- Multi-language report analysis
- AI-powered chatbot for health queries
- Hospital resource prediction
- Vaccination trend analysis
- User authentication
- Cloud deployment

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature/NewFeature
```

3. Commit your changes

```bash
git commit -m "Added New Feature"
```

4. Push your branch

```bash
git push origin feature/NewFeature
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Nithin P Gowda**

📧 Email: nithinpgowda0099@gmail.com

🌐 Portfolio: https://adios-amigo.vercel.app/

💼 LinkedIn: https://linkedin.com/in/nithinisaimg

🐙 GitHub: https://github.com/nithinisaimg

---

# 💡 Project Vision

> **Empowering public health through AI-driven disease surveillance and intelligent outbreak prediction.**

By combining **Natural Language Processing**, **epidemiological forecasting**, and **interactive analytics**, this project demonstrates how modern AI techniques can transform disease monitoring, support informed decision-making, and improve situational awareness during public health emergencies.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support encourages future development and helps others discover the project.
