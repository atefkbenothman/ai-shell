#!/usr/bin/env python3
import re
import sys
from groq import Groq

SYSTEM_PROMPT = f"""
You are a command-line expert assistant that converts natural language questions into accurate bash/zsh commands for macos.
RULES:
- Provide ONLY the executable command with no explanations, no markdown, and no additional text
- Do NOT include any commentary, just the raw command
- Use common unix/macOS tools and utilities
- Favor simple, efficient commands when possible
- Ensure commands are properly escaped and quoted for safe execution
- NEVER include 'sudo'
- For file operations, prioritize safety (don't use dangerous options like rm -rf without confirmation)
"""

def extract_command(response: str):
  cleaned_response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL)
  pattern = r"`(.*?)`"

  match = re.search(pattern, cleaned_response)

  if match:
    return match.group(1).strip()
  else:
    lines = [line.strip() for line in cleaned_response.split("\n") if line.strip()]
    if lines:
      return lines[-1].strip()
    else:
      return "Error: No command found in response"



def ask(user_question: str):
  try:
    chat_completion = client.chat.completions.create(
      messages=[
        {
          "role": "system",
          "content": SYSTEM_PROMPT
        },
        {
          "role": "user",
          "content": user_question
        }
      ],
      model="deepseek-r1-distill-llama-70b"
    )
    return chat_completion.choices[0].message.content
  except:
    return "Error generating response"


if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print("Please provide a command request")
    exit(0)

  client = Groq(
    api_key="YOUR_API_KEY"
  )

  user_question = " ".join(sys.argv[1:])

  response = ask(user_question)
  cmd = extract_command(response)

  print(cmd)
