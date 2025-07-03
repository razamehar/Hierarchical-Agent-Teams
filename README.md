# Hierarchical AI Agent Team

A modular, multi-agent AI system built using [LangGraph](https://github.com/langchain-ai/langgraph), [LangChain](https://www.langchain.com/), and OpenAI's GPT model. The system uses a **hierarchical architecture** with supervisors managing specialized agents to perform complex tasks through collaboration.

---

## Project Structure
```text
├── main.py
├── agents/
│ ├── math_agent.py
│ ├── doc_saving_agent.py
│ ├── research_agent.py
│ ├── summary_agent.py
├── teams/
│ ├── mid_supervisor.py
│ ├── supervisor.py
├── tools/
│ ├── doc_saver.py
│ ├── math_tools.py
│ ├── research_tools.py
│ ├── summarize_tool.py
├── utils/
│ ├── model_loader.py
├── schema/
│ ├── schema.py
├── config/
│ ├── config.py
├── requirements.txt
└── README.md
```

---

## How It Works

### `main.py`
Interactive console interface. Type a query and watch the agent hierarchy handle it. Type `exit` or `quit` to stop.

```python
Query: How has Tesla stock performed in the last year?
```

## Top-Level Supervisor
Coordinates the entire agent ecosystem:
- Delegates research and calculations to research_team
- Summarizes results via summary_agent
- Saves outputs using doc_saving_agent

## Mid-Level Supervisor: research_team
Manages:
- research_agent: performs web-based information retrieval
- math_agent: handles all arithmetic using separate tools

## 🧩 Agents and Responsibilities

| Agent              | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| `math_agent`       | Performs addition, subtraction, multiplication, and division. |
| `doc_saving_agent` | Saves results in `.pdf` or `.docx` format.                    |
| `research_agent`   | Searches online using Tavily (general + finance).             |
| `summary_agent`    | Summarizes large chunks of text using GPT.                    |


## Tools

### Math Tools
- add_tool
- subtract_tool
- multiply_tool
- divide_tool

### Research Tools
- finance_research_tool
- general_research_tool
- 
### Document Tools
- save_doc_tool: Save text in .pdf, .doc, or .docx format

### Summarizer
- get_summary: Generates a 300-word summary

## Requirements
Install dependencies using:
```bash
pip install -r requirements.txt
```

```nginx
langchain
langchain-community
langchain-openai
langchain_core
langgraph
langchain-tavily
python-dotenv
pydantic
wikipedia
fpdf
python-docx
openai
```

## Environment Variables
Create a .env file and add your API keys:
```ini
OPENAI_API_KEY=your-key-here
TAVILY_API_KEY=your-key-here
```

## Run the Project
```bash
python main.py
```

## Built With
- LangGraph
- LangChain
- OpenAI
- Tavily
- FPDF
- python-docx

## Contact
For any questions or clarifications, please contact Raza Mehar at [raza.mehar@gmail.com](mailto:raza.mehar@gmail.com).