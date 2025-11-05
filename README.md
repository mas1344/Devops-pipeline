# Devops-pipeline
project about devops and pipeline

# Setup Instructions - Crypto Price App


## Prerequisites
- [ ] Python 3.12 or higher installed
- [ ] Git installed (to clone the repository)


## Setup Steps


### 1. Install uv (Ultra-fast Python Package Manager)
```bash
# Install uv
pip install uv
```


### 2. Clone and Navigate
```bash
git clone <repository-url>
cd Devops-pipeline
```


### 3. Install All Dependencies (Workspace Setup)
```bash
# Install all workspace dependencies automatically
uv sync 
uv sync —-extra dev
```


### 4. Environment Configuration
- [ ] Create a `.env` file in the project root (needed for API keys)
- [ ] Add any required environment variables


### 5. Run the Application
```bash
streamlit run src/webapp/app.py
```
### 6. Access the App
- [ ] Open your web browser
- [ ] The crypto price dashboard should be running!


## To Stop the App
- Press `Ctrl+C` in the terminal


## Development Workflow
### Running Tests
```bash
# Run tests with uv
uv run pytest
```
