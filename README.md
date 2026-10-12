# Student Placement Prediction System

A full-stack machine learning project that predicts whether a student is likely to get placed based on academic performance, technical skills, soft skills, internships, projects, and other placement-related indicators. The project combines a training pipeline, interpretability tools, a Streamlit dashboard, and a REST API into a single end-to-end placement analytics platform.

## Overview

This system helps universities, training centers, and placement teams evaluate student readiness for campus hiring. It supports:

- Individual student prediction
- Batch CSV prediction
- Dataset upload and validation
- Multiple model benchmarking
- Model explainability with SHAP
- Storage of predictions and training history in SQLite
- An AI-powered placement assistant for guidance and career Q&A

## Key Features

- Multi-model benchmarking across common classifiers and boosting algorithms
- Best-model selection using evaluation metrics such as F1-score, precision, recall, and accuracy
- SHAP-based feature importance to explain model decisions
- Interactive dashboard with Plotly visualizations and summary analytics
- Resume parsing support to prefill candidate data from text
- CSV upload and bulk prediction export
- FastAPI backend with Swagger docs
- SQLite reporting and audit logs for predictions and model runs
- Streamlit-based frontend with a polished placement portal UI

## Tech Stack

| Area | Technologies |
|---|---|
| Language | Python 3.12+ |
| ML & Data Science | scikit-learn, XGBoost, LightGBM, CatBoost, SHAP, pandas, NumPy |
| Visualization | Streamlit, Plotly, Matplotlib, Seaborn |
| API | FastAPI, Uvicorn, Pydantic |
| Database | SQLite, SQLAlchemy |
| Testing | Pytest |
| Deployment | Docker, Docker Compose |
| AI Assistant | Groq / Python SDK integration |

## Project Structure

```text
Student-Placement-Prediction-System/
├── api/
│   └── main.py                # FastAPI application and endpoints
├── data/
│   └── raw/                   # Raw and generated datasets
├── database/
│   └── placement.db           # SQLite database
├── docs/
│   ├── architecture_diagrams.md
│   ├── developer_guide.md
│   ├── installation_guide.md
│   ├── project_report.md
│   └── user_manual.md
├── logs/
│   └── placement_system.log   # Application logs
├── models/
│   ├── placement_model.pkl
│   └── preprocessor.pkl
├── reports/
│   ├── classification_report.txt
│   ├── diagnostics_report.md
│   ├── metrics.json
│   ├── shap_force.html
│   ├── shap_summary.png
│   └── shap_waterfall.png
├── src/
│   ├── config.py
│   ├── database.py
│   ├── diagnose.py
│   ├── evaluate.py
│   ├── explain.py
│   ├── feature_engineering.py
│   ├── generate_data.py
│   ├── kaggle_adapter.py
│   ├── predict.py
│   ├── pregenerate_reports.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── utils.py
│   └── chatbot.py
├── streamlit/
│   ├── app.py
│   ├── api_client.py
│   ├── _pages/
│   └── css/style.css
├── tests/
│   ├── test_api.py
│   ├── test_predict.py
│   └── test_preprocessing.py
├── .devcontainer/
├── .env
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── docker-compose.yml
├── requirements.txt
└── .git
```

## Prerequisites

- Python 3.12+
- pip
- Git
- Optional: Docker and Docker Compose for containerized setup

## Getting Started

### 1) Clone the Repository

```bash
git clone https://github.com/<your-username>/Student-Placement-Prediction-System.git
cd Student-Placement-Prediction-System
```

### 2) Create a Virtual Environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3) Install Dependencies

```bash
pip install -r requirements.txt
```

### 4) Initialize Data and Model Assets

```bash
python src/generate_data.py
python src/train.py
```

These steps create the sample dataset, initialize the SQLite database, and train the placement prediction model.

### 5) Run the Backend API

In one terminal:

```bash
uvicorn api.main:app --reload --port 8000
```

The API documentation is available at:

- http://localhost:8000/docs
- http://localhost:8000/redoc

### 6) Launch the Streamlit App

In a second terminal:

```bash
streamlit run streamlit/app.py
```

Then open:

- http://localhost:8501

## API Endpoints

The project exposes several endpoints through FastAPI:

- `GET /` – Health/root endpoint
- `POST /predict` – Predict placement for a single student
- `POST /predict/batch` – Predict placement for multiple students from a CSV or payload
- `POST /upload` – Upload a dataset for analysis or processing
- `POST /train` – Trigger model training
- `GET /models` – List trained model information
- `GET /reports/{filename}` – Access generated report files
- `POST /chat` – Chat-based student guidance endpoint using the AI assistant

## Running with Docker

```bash
docker-compose up --build
```

Then access:

- Streamlit UI: http://localhost:8501
- API docs: http://localhost:8000/docs

## Testing

Run the test suite with:

```bash
pytest tests/ -v
```

## Usage Notes

- Model files and preprocessing objects are saved under the `models/` directory.
- Report artifacts such as confusion matrices, SHAP charts, and metrics are generated in `reports/`.
- The application logs runtime events in `logs/placement_system.log`.
- A trained model can be reused for fast prediction without retraining.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is designed for educational and placement analytics use cases, combining modern machine learning and web application practices in a practical student outcome prediction workflow.
