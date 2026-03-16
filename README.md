# AI Terminal Chatbot

An intelligent terminal chatbot that translates natural language into system commands with rule-based execution, smart dependency management, and safe command execution.

## Features

- 🤖 **AI Translation**: Convert English to system commands using LLM (OpenAI, Anthropic, Ollama)
- 🔍 **Smart Matching**: Fuzzy match commands against a predefined JSON database
- 🔗 **Dependency Resolution**: Automatically checks and installs prerequisites
- ✅ **Safe Execution**: Shows commands and requires user confirmation before running
- 🌍 **Cross-Platform**: Supports Windows, macOS, and Linux
- 📊 **Logging**: Complete audit trail of all executed commands
- 🛡️ **Security**: Whitelist-only execution, no arbitrary code eval

## Installation

```bash
# Clone the repository
git clone https://github.com/ShubhamP08/ai-terminal-chatbot.git
cd ai-terminal-chatbot

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

## Quick Start

```bash
python src/main.py
```

## Project Structure

```
ai-terminal-chatbot/
├── src/
│   ├── main.py              # Main CLI interface
│   ├── llm_translator.py    # LLM integration
│   ├── command_matcher.py   # Fuzzy matching engine
│   ├── rule_engine.py       # Dependency validation
│   ├── command_executor.py  # Safe execution
│   ├── logger.py            # Logging system
│   └── utils.py             # Helper functions
├── config/
│   └── commands.json        # Command database
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

## Configuration

Edit `.env` with your LLM provider:

```env
# OpenAI
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here

# Or Anthropic
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=your_key_here

# Or Local Ollama
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
```

## License

MIT License
