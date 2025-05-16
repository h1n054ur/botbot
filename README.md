# Twilio Manager CLI

A fully menu-driven, guided wrapper around Twilio services.

## Setup

### Requirements
- Python 3.10 or higher
- virtualenv

### Installation

1. Create and activate virtual environment:
```bash
# Create virtualenv
python -m venv venv

# Activate on Unix/MacOS
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
# Copy example env file
cp .env.example .env

# Edit .env with your Twilio credentials
nano .env
```

### Running the CLI
```bash
python main.py
```

## Development

### Running Tests
```bash
pytest
```

### Project Structure
```
app/
├── core/         # Business logic
├── gateways/     # External adapters
├── interfaces/   # CLI interface
├── models/       # Data models
├── services/     # Use case orchestration
└── use_cases/    # Flow orchestration
```
