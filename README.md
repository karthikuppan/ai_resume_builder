# AI Resume Builder

A modern, AI-powered resume builder that leverages multiple specialized AI agents to customize your resume for a given job.

## Features

- **Multi-Agent Analysis**: Utilizes four specialized AI agents:
  - Job Researcher: Analyzes given job posting
  - Personal Profiler: Profile the resume
  - Resume Strategist: Strategize resume preparation and create a custom version of resume for the job
  - Interview Preparer: Prepare interview questions

## Tech Stack

- Python
- CrewAI for agent orchestration
- Advanced AI LLM Models

## Prerequisites


- Python 3.10+
- uv (Python package and project manager)
- CrewAI

## Installation

1. **Set up Python environment**
   Install uv 
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh # On Windows powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install 'crewai[tools]'
   ```

2. **Clone the repository**
   ```bash
   git clone https://github.com/karthikuppan/ai_resume_builder.git
   cd ai_resume_builder
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   MODEL=gpt-4o-mini
   OPENAI_API_KEY=your_openai-api_key_here
   SERPER_API_KEY=your_serper-api_key_here

   # Add other necessary environment variables
   ```

## 🚀 Running the Application

1. **Run**
   ```bash
   # From the project root directory
   crewai install
   crewai run
   ```

## 📁 Project Structure

```
ai_resume_builder/
├── src/
│   ├── resume_builder/         # AI agent implementations
│       ├── config/             # Agent and task configuraton in YAML format
│           ├── agents.yaml     # AI agents definition and their roles
│           ├── tasks.yaml.     # Agent tasks and workflows
│       ├── tools/              # Directory for custom agent tools
│       └── crew.py             # Crew orchestration and coordination
|       └── main.py             # Project entry point and execution flow
|       └── __init__.py.        # Packaging
|   ├── knowledge/
│   └── tests/                  # Python tests
└── pyproject.toml              # Project dependencies
└── .env                        # API keys and environment variables
```

## 🔧 Configuration

The application can be configured through various environment variables:

- `MODEL`: LLM Model name
- `OPENAI_API_KEY`: Your OpenAI API key
- `SERPER_API_KEY`: Your Serper API key
- Add other relevant configuration options

## 🧪 Testing

- **Run Tests**
  ```bash
  cd resume_builder
  pytest
  ```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the agent orchestration framework
- [Deeplearning AI](http://deeplearning.ai/) for training
- [OpenAI](https://openai.com/) for the AI models

