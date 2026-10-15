# Student Placement Prediction System

A full-stack ML application for predicting whether a student is likely to get placed based on academic performance, technical skills, communication, internships, projects, and other placement-related indicators.

This project combines a machine learning training pipeline, interpretable analytics, a Streamlit dashboard, and a FastAPI backend into a single placement intelligence platform for universities, training centers, and career services teams.

## Overview

The system helps users:

- Evaluate a single student's placement readiness
- Upload and process batch student data
- Train and compare multiple machine learning models
- View explainability charts for model decisions
- Track prediction records and reports in SQLite
- Ask an AI-powered placement assistant for career guidance

## Key Features

- Multiple ML models and benchmarking for placement prediction
- Automatic model selection using evaluation metrics such as accuracy, precision, recall, and F1-score
- SHAP-based feature importance and interpretability output
- Interactive dashboard with analytics and plotted summaries
- CSV upload and bulk prediction workflows
- FastAPI backend with OpenAPI docs
- SQLite storage for datasets, training history, and predictions
- AI-powered placement chatbot for student guidance
- Role-based access in the Streamlit portal

## Tech Stack

| Area | Tools |
|---|---|
| Programming language | Python 3.12+
| ML & analytics | scikit-learn, XGBoost, LightGBM, CatBoost, SHAP, pandas, NumPy |
| Visualization | Streamlit, Plotly, Matplotlib, Seaborn |
| Web API | FastAPI, Uvicorn, Pydantic |
| Database | SQLite, SQLAlchemy |
| Testing | Pytest |
| Deployment | Docker, Docker Compose |
| AI integration | Groq SDK |

## Project Structure

```text
Student-Placement-Prediction-System/
├── api/
│   └── main.py                  # FastAPI backend and routes
├── data/
│   └── raw/                    # Raw and generated datasets
├── database/
│   └── placement.db            # SQLite database
├── docs/
│   ├── architecture_diagrams.md
│   ├── developer_guide.md
│   ├── installation_guide.md
│   ├── project_report.md
│   └── user_manual.md
├── logs/
│   └── placement_system.log     # Runtime logs
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
│   ├── auth.py
│   ├── authorization.py
│   ├── chatbot.py
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
│   └── utils.py
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
- Optional: Docker and Docker Compose

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Student-Placement-Prediction-System.git
cd Student-Placement-Prediction-System
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

The project uses environment variables such as `GROQ_API_KEY` for the AI assistant. If needed, create a local `.env` file or export variables in your shell before running the app.

Example:

```bash
export GROQ_API_KEY="your_api_key_here"
export GROQ_MODEL="openai/gpt-oss-20b"
```

### 5. Generate data and train the model

```bash
python src/generate_data.py
python src/train.py
```

This creates the sample dataset, initializes model artifacts, and prepares the training pipeline.

## Run the Application

### Start the API backend

```bash
uvicorn api.main:app --reload --port 8000
```

Open the API docs in a browser:

- http://localhost:8000/docs
- http://localhost:8000/redoc

### Start the Streamlit frontend

In a separate terminal:

```bash
streamlit run streamlit/app.py
```

Open the dashboard at:

- http://localhost:8501

## API Endpoints

The FastAPI backend exposes the following major routes:

- `GET /` — health check
- `POST /predict` — predict placement for a single student
- `POST /predict/batch` — predict placement for multiple records
- `POST /upload` — upload a CSV or dataset for processing
- `POST /train` — trigger model training
- `GET /models` — list available model artifacts
- `GET /reports/{filename}` — access generated reports
- `POST /chat` — chat with the AI placement assistant

## Docker Deployment

The project includes Docker support for running both the API and frontend together.

```bash
docker-compose up --build
```

Access points:

- Frontend: http://localhost:8501
- API docs: http://localhost:8000/docs

## Testing

Run the project tests with:

```bash
pytest tests/ -v
```

## Output Artifacts

The application creates and stores important assets in these folders:

- `models/` — trained model and preprocessing objects
- `reports/` — metrics, confusion outputs, and SHAP plots
- `database/` — SQLite database files
- `logs/` — application runtime logs
- `data/raw/` — generated and uploaded dataset files

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Notes

This project is intended for educational and real-world placement analytics use cases, combining modern machine learning workflows with a user-friendly dashboard and API-based system design.
