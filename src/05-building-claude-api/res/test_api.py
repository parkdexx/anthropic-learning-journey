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


## VER1. 가장 클래식한 문답 방법
# ## question 1
# message = client.messages.create(
#     model=model,
#     max_tokens=1000,
#     messages=[
#         {
#             "role": "user",
#             "content": "양자역학이란 무엇입니까? 한줄의 한글로 답해주세요"
#         }
#     ]
# )
# print(message.content[0].text)

# ## question 2
# ## 내 의도 : 앞에서 질문한 양자역학이란 무엇인지에 대한 다른 한줄의 의견을 주십시오
# ## 결과 : 앞에 대화를 전혀 기억하지 못함. 엉뚱한 대답을 함.
# message = client.messages.create(
#     model=model,
#     max_tokens=1000,
#     messages=[
#         {
#             "role": "user",
#             "content": "다른 한줄의 한글로 답해주세요"
#         }
#     ]
# )
# print(message.content[0].text)



## VER2. 어시스턴스와의 맥락을 유지하면서 계속 문답하는 방법

messages = []
answer = []

def add_user_message(messages, text):
    user_message = {
        "role": "user",
        "content": text
    }
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {
        "role": "assistant",
        "content": text
    }
    messages.append(assistant_message)


#  Anthropic API는 system 파라미터에 None을 허용하지 않고, 아예 키 자체가 없어야 합니다.
def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages
    }

    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text

# # 사용자 -> ai
# add_user_message(messages, "양자역학이란 무엇입니까? 한줄의 한글로 답해주세요")
# print(messages)

# # ai -> 사용자
# answer = chat(messages)
# add_assistant_message(messages, answer)
# print(messages)

# # 사용자 -> ai
# add_user_message(messages, "다른 한줄의 한글로 답해주세요")
# print(messages)

# # ai -> 사용자
# answer = chat(messages)
# add_assistant_message(messages, answer)
# print(messages)




## VER3. 어시스턴스와의 채팅

print("채팅을 시작합니다. 종료하려면 Ctrl+C를 누르세요.\n")

try:
    isFirst = True
    system = None

    while True:

        # 채팅이 처음 시작되면 프롬프트를 선택적으로 입력 받음
        if isFirst:
            system = input("시스템 프롬프트 입력(없으면 Enter): ")
            isFirst = False  

            if system == "":
                system = None

        user_input = input("사용자: ")
        add_user_message(messages, user_input)

        # 시스템 프롬프트를 매개변수로 날림
        answer = chat(messages, system)
        add_assistant_message(messages, answer)
        print(f"AI: {answer}\n")

except KeyboardInterrupt:
    print("\n\n채팅을 종료합니다.")



