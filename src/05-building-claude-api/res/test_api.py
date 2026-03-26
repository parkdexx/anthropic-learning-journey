import os
import sys
import anthropic

sys.stdout.reconfigure(encoding="utf-8")

# Load API key from .env
with open(os.path.join(os.path.dirname(__file__), ".env")) as f:
    for line in f:
        line = line.strip()
        if line and "=" in line:
            key, val = line.split("=", 1)
            os.environ[key.strip()] = val.strip().strip('"')

client = anthropic.Anthropic()
model = "claude-opus-4-6"

message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "양자역학이란 무엇입니까? 한줄의 한글로 답해주세요"
        }
    ]
)

print(message.content[0].text)
