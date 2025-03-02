# sh-ai

> A macOS terminal utility that converts natural language into shell commands.

## Description

`sh-ai` is a simple command-line utility that leverages the power of large language models to translate your natural language requests into executable bash/zsh commands. Instead of remembering complex command syntax, simply describe what you want to do, and `sh-ai` will generate the appropriate command.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sh-ai.git
   cd sh-ai
   ```

2. Install the required Python dependencies:
   ```bash
   pip3 install groq
   ```

3. Make the script executable and move it to your PATH:
   ```bash
   chmod +x ai
   sudo mv ai /usr/local/bin/
   ```

4. Set your API key:
   Edit `script.py` and replace `"YOUR_API_KEY"` with your actual Groq API key

## Usage

Simply prefix your natural language request with `ai`:

```bash
ai list all files in current directory
# Generated command:
ls -la
```

```bash
ai find all pdf files modified in the last 7 days
# Generated command:
find . -name "*.pdf" -type f -mtime -7
```

## Examples

- `ai create a new directory called projects`
- `ai count all lines in text files recursively`
- `ai zip all jpg files in the current folder`
- `ai show system memory usage`
- `ai find largest files in current directory`
