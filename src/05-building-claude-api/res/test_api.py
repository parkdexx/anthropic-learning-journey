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
def chat(messages, system=None, temperature=0.5):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
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

# print("채팅을 시작합니다. 종료하려면 Ctrl+C를 누르세요.\n")

# try:
#     isFirst = True
#     system = None
#     temperature = 0.5
#     isStreaming = True

#     while True:

#         if isFirst:
#             isFirst = False

#             # 시스템 프롬프트를 선택적으로 입력 받음
#             system = input("시스템 프롬프트 입력(없으면 Enter): ")
#             if system == "":
#                 system = None

#             # 온도 입력 받기
#             temperature = input("온도 입력(없으면 0.5): ")
#             if temperature == "":
#                 temperature = 0.5
#             else:
#                 temperature = float(temperature)

#             # 스트리밍 응답 사용 여부 입력 받기
#             isStreaming = input("스트리밍 응답 사용(y/n, 기본값: y): ").lower()
#             if isStreaming == "":
#                 isStreaming = True
#             else:
#                 isStreaming = isStreaming == "y"



#         user_input = input("사용자 질문 : ")
#         add_user_message(messages, user_input)


#         if(isStreaming):
#             # 스트리밍 응답 받기
#             with client.messages.stream(
#                 model= model,
#                 max_tokens=1000,
#                 messages= messages
#             )  as stream :
#                 for text in stream.text_stream:
#                     print("AI 답변 : ", end="")
#                     print(text, end="")
#                     print("\n")
#                 #final_message = stream.get_final_message() #메시지 완성본
#         else:
#             # 일반 응답 받기
#             #answer = chat(messages, system)
#             answer = chat(messages, system)
#             add_assistant_message(messages, answer)
#             print(f"AI 답변 : {answer}\n")


# except KeyboardInterrupt:
#     print("\n\n채팅을 종료합니다.")



## VER4. 커맨드만 출력 모드 (prefill + stop_sequences 활용)
# 핵심 기법:
#   - assistant 메시지를 "```\n" 으로 prefill → Claude가 코드블록 안에서 응답 시작
#   - stop_sequences=["```"] → 닫는 펜스 직전에 자동 중단
#   - 결과: 펜스 사이의 순수 커맨드만 추출됨

COMMANDS_ONLY_SYSTEM = """You are a command generator. Respond with ONLY the raw commands, one per line.
No explanations. No markdown. No backticks. No code blocks. No numbering. No descriptions.
Just the bare commands."""

print("커맨드 전용 모드입니다. 종료하려면 Ctrl+C를 누르세요.\n")

try:
    while True:
        user_input = input("요청 : ")

        # assistant prefill로 코드블록 시작을 강제
        response = client.messages.create(
            model=model,
            max_tokens=1000,
            temperature=0.0,
            system=COMMANDS_ONLY_SYSTEM,
            stop_sequences=["```"],
            messages=[
                {"role": "user",      "content": user_input},
                {"role": "assistant", "content": "```"},   # prefill
            ]
        )

        commands = response.content[0].text.strip()
        print(f"\n{commands}\n")

except KeyboardInterrupt:
    print("\n\n종료합니다.")



