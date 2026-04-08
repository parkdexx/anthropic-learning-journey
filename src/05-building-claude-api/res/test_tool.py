import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
from anthropic import Anthropic
from anthropic.types import Message, ToolParam

# 같은 디렉터리의 .env 파일에서 ANTHROPIC_API_KEY 등 환경변수를 로드
load_dotenv(dotenv_path=".env")

client = Anthropic()
model = "claude-haiku-4-5"


# ── Helper functions ──────────────────────────────────────────────────────────

def add_user_message(messages, message):
    """
    대화 히스토리 리스트에 사용자(user) 역할의 메시지를 추가한다.

    Args:
        messages (list): 대화 히스토리를 담는 딕셔너리 리스트.
        message (Message | str | list): 추가할 메시지.
            - Anthropic Message 객체이면 .content 속성을 사용한다.
            - 문자열 또는 content 블록 리스트이면 그대로 사용한다.
    """
    user_message = {
        "role": "user",
        "content": message.content if isinstance(message, Message) else message,
    }
    messages.append(user_message)


def add_assistant_message(messages, message):
    """
    대화 히스토리 리스트에 어시스턴트(assistant) 역할의 메시지를 추가한다.

    Args:
        messages (list): 대화 히스토리를 담는 딕셔너리 리스트.
        message (Message | str | list): 추가할 메시지.
            - Anthropic Message 객체이면 .content 속성을 사용한다.
            - 문자열 또는 content 블록 리스트이면 그대로 사용한다.
    """
    assistant_message = {
        "role": "assistant",
        "content": message.content if isinstance(message, Message) else message,
    }
    messages.append(assistant_message)


def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools=None):
    """
    Claude API를 호출하여 대화 응답을 반환한다.
    tools와 system 프롬프트가 있을 경우 요청에 포함한다.

    Args:
        messages (list): 대화 히스토리 딕셔너리 리스트 (role + content 쌍).
        system (str | None): 시스템 프롬프트 문자열. None이면 포함하지 않는다.
        temperature (float): 응답의 무작위성 조절값 (0.0 ~ 1.0). 기본값 1.0.
        stop_sequences (list): Claude가 응답을 중단할 문자열 목록. 기본값 빈 리스트.
        tools (list | None): Claude에게 제공할 도구 스키마 리스트. None이면 포함하지 않는다.

    Returns:
        Message: Anthropic API가 반환한 응답 Message 객체.
    """
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
        "stop_sequences": stop_sequences,
    }
    if tools:
        params["tools"] = tools
    if system:
        params["system"] = system
    # client.messages.create()를 호출하여 Claude API에 요청 전송
    return client.messages.create(**params)


def text_from_message(message):
    """
    Anthropic Message 객체의 content 블록 중 텍스트 블록만 추출하여
    줄바꿈으로 이어 붙인 문자열을 반환한다.
    tool_use 블록 등 텍스트가 아닌 블록은 무시된다.

    Args:
        message (Message): Anthropic API가 반환한 응답 Message 객체.

    Returns:
        str: 텍스트 블록들을 줄바꿈(\\n)으로 연결한 문자열.
    """
    return "\n".join([block.text for block in message.content if block.type == "text"])


# ── Tool functions ────────────────────────────────────────────────────────────

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    """
    현재 날짜와 시간을 지정한 포맷 문자열로 변환하여 반환한다.
    Claude가 tool_use 블록으로 호출하는 실제 도구 함수이다.

    Args:
        date_format (str): Python strftime 포맷 코드 문자열.
            예) '%Y-%m-%d' → '2025-04-08', '%H:%M' → '14:32'.
            기본값은 '%Y-%m-%d %H:%M:%S'.

    Returns:
        str: 현재 날짜/시간을 date_format으로 포맷한 문자열.

    Raises:
        ValueError: date_format이 빈 문자열인 경우.
    """
    if not date_format:
        raise ValueError("date_format cannot be empty")
    # datetime.now()로 현재 시각을 가져온 뒤 strftime()으로 포맷 적용
    return datetime.now().strftime(date_format)


def add_duration_to_datetime(
    datetime_str, duration=0, unit="days", input_format="%Y-%m-%d"
):
    """
    주어진 날짜 문자열에 지정한 기간을 더하거나 빼서 새 날짜를 반환한다.
    월(month) 단위는 월별 일수와 윤년을 고려하여 계산한다.

    Args:
        datetime_str (str): 기준 날짜/시간 문자열. input_format에 맞는 형식이어야 한다.
        duration (int | float): 더할 기간의 양. 음수이면 과거 날짜를 계산한다. 기본값 0.
        unit (str): 기간 단위. 'seconds' | 'minutes' | 'hours' | 'days' |
                    'weeks' | 'months' | 'years' 중 하나. 기본값 'days'.
        input_format (str): datetime_str을 파싱할 strptime 포맷 코드. 기본값 '%Y-%m-%d'.

    Returns:
        str: 계산된 날짜를 'Weekday, Month DD, YYYY HH:MM:SS AM/PM' 형식으로 반환.
            예) 'Thursday, April 03, 2025 10:30:00 AM'.

    Raises:
        ValueError: unit이 지원하지 않는 값인 경우.
    """
    # datetime.strptime()으로 문자열을 datetime 객체로 변환
    date = datetime.strptime(datetime_str, input_format)

    if unit == "seconds":
        # timedelta()로 초 단위 기간을 더함
        new_date = date + timedelta(seconds=duration)
    elif unit == "minutes":
        # timedelta()로 분 단위 기간을 더함
        new_date = date + timedelta(minutes=duration)
    elif unit == "hours":
        # timedelta()로 시간 단위 기간을 더함
        new_date = date + timedelta(hours=duration)
    elif unit == "days":
        # timedelta()로 일 단위 기간을 더함
        new_date = date + timedelta(days=duration)
    elif unit == "weeks":
        # timedelta()로 주 단위 기간을 더함
        new_date = date + timedelta(weeks=duration)
    elif unit == "months":
        month = date.month + duration
        year = date.year + month // 12
        month = month % 12
        if month == 0:
            month = 12
            year -= 1
        # 해당 월의 최대 일수를 초과하지 않도록 day 값을 보정
        day = min(
            date.day,
            [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28,
             31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1],
        )
        # date.replace()로 연/월/일을 교체한 새 datetime 객체 생성
        new_date = date.replace(year=year, month=month, day=day)
    elif unit == "years":
        # date.replace()로 연도만 교체
        new_date = date.replace(year=date.year + duration)
    else:
        raise ValueError(f"Unsupported time unit: {unit}")

    return new_date.strftime("%A, %B %d, %Y %I:%M:%S %p")


def set_reminder(content, timestamp):
    """
    지정한 시각에 표시할 알림 내용을 콘솔에 출력한다.
    (실제 알림 시스템 연동 대신 출력으로 동작을 시뮬레이션한다.)

    Args:
        content (str): 알림에 표시할 메시지 내용.
        timestamp (str): 알림이 발생할 날짜/시간 (ISO 8601 형식 권장).
    """
    print(f"----\nSetting the following reminder for {timestamp}:\n{content}\n----")


# ── Tool schemas ──────────────────────────────────────────────────────────────

# Claude API에 전달할 get_current_datetime 도구의 JSON 스키마 정의
get_current_datetime_schema = ToolParam(
    {
        "name": "get_current_datetime",
        "description": (
            "Returns the current date and time formatted according to the specified "
            "format string. Use this tool when you need to know the current date and "
            "time. The default format returns the date and time in ISO-like format "
            "(YYYY-MM-DD HH:MM:SS)."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "date_format": {
                    "type": "string",
                    "description": (
                        "A string specifying the format of the returned datetime using "
                        "Python's strftime format codes. Defaults to '%Y-%m-%d %H:%M:%S'."
                    ),
                    "default": "%Y-%m-%d %H:%M:%S",
                }
            },
            "required": [],
        },
    }
)

# Claude API에 전달할 add_duration_to_datetime 도구의 JSON 스키마 정의
add_duration_to_datetime_schema = {
    "name": "add_duration_to_datetime",
    "description": (
        "Adds a specified duration to a datetime string and returns the resulting "
        "datetime. Handles seconds, minutes, hours, days, weeks, months, and years."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "datetime_str": {
                "type": "string",
                "description": "The input datetime string formatted according to input_format.",
            },
            "duration": {
                "type": "number",
                "description": "Amount of time to add (can be negative for past dates). Defaults to 0.",
            },
            "unit": {
                "type": "string",
                "description": "One of: 'seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'years'. Defaults to 'days'.",
            },
            "input_format": {
                "type": "string",
                "description": "strptime format string for parsing datetime_str. Defaults to '%Y-%m-%d'.",
            },
        },
        "required": ["datetime_str"],
    },
}

# Claude API에 전달할 set_reminder 도구의 JSON 스키마 정의
set_reminder_schema = {
    "name": "set_reminder",
    "description": (
        "Creates a timed reminder that will notify the user at the specified time "
        "with the provided content."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "content": {
                "type": "string",
                "description": "The message text to display in the reminder notification.",
            },
            "timestamp": {
                "type": "string",
                "description": "ISO 8601 timestamp (YYYY-MM-DDTHH:MM:SS) when the reminder fires.",
            },
        },
        "required": ["content", "timestamp"],
    },
}

# Claude API에 전달할 batch_tool 도구의 JSON 스키마 정의 (여러 도구를 동시에 호출)
batch_tool_schema = {
    "name": "batch_tool",
    "description": "Invoke multiple other tool calls simultaneously.",
    "input_schema": {
        "type": "object",
        "properties": {
            "invocations": {
                "type": "array",
                "description": "The tool calls to invoke.",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Tool name."},
                        "arguments": {
                            "type": "string",
                            "description": "Tool arguments as a JSON string.",
                        },
                    },
                    "required": ["name", "arguments"],
                },
            }
        },
        "required": ["invocations"],
    },
}


# ── Tool execution ────────────────────────────────────────────────────────────

def run_tool(tool_name, tool_input):
    """
    Claude가 요청한 단일 도구를 이름으로 찾아 실행하고 결과를 반환한다.

    Args:
        tool_name (str): 실행할 도구의 이름. 등록된 도구 이름과 일치해야 한다.
        tool_input (dict): 도구에 전달할 인자 딕셔너리.

    Returns:
        str | any: 해당 도구 함수의 반환값.

    Raises:
        ValueError: tool_name이 등록되지 않은 도구 이름인 경우.
    """
    if tool_name == "get_current_datetime":
        # get_current_datetime()을 호출하여 현재 날짜/시간 반환
        return get_current_datetime(**tool_input)
    raise ValueError(f"Unknown tool: {tool_name}")


def run_tools(message):
    """
    Claude 응답 메시지에 포함된 모든 tool_use 블록을 순서대로 실행하고,
    각 실행 결과를 tool_result 형식의 딕셔너리 리스트로 반환한다.
    실행 중 예외가 발생하면 is_error=True로 표시하여 오류 내용을 반환한다.

    Args:
        message (Message): Anthropic API가 반환한 응답 Message 객체.
            content 안에 tool_use 블록이 하나 이상 포함되어 있어야 한다.

    Returns:
        list[dict]: 각 도구 실행 결과를 담은 tool_result 딕셔너리 리스트.
            각 딕셔너리는 type, tool_use_id, content, is_error 키를 포함한다.
    """
    # message.content에서 tool_use 블록만 추출
    tool_requests = [block for block in message.content if block.type == "tool_use"]
    tool_result_blocks = []

    for tool_request in tool_requests:
        try:
            # run_tool()을 호출하여 요청된 도구를 실행
            tool_output = run_tool(tool_request.name, tool_request.input)
            tool_result_block = {
                "type": "tool_result",
                "tool_use_id": tool_request.id,
                # json.dumps()로 결과값을 JSON 문자열로 직렬화
                "content": json.dumps(tool_output),
                "is_error": False,
            }
        except Exception as e:
            tool_result_block = {
                "type": "tool_result",
                "tool_use_id": tool_request.id,
                "content": f"Error: {e}",
                "is_error": True,
            }
        tool_result_blocks.append(tool_result_block)

    return tool_result_blocks


# ── Agentic conversation loop ─────────────────────────────────────────────────

def run_conversation(messages):
    """
    Claude가 도구 호출을 멈출 때까지 대화를 반복 진행하는 에이전틱 루프이다.
    Claude가 tool_use를 반환하면 도구를 실행하고 결과를 대화에 추가한다.
    stop_reason이 'tool_use'가 아니면 루프를 종료한다.

    Args:
        messages (list): 초기 대화 히스토리 딕셔너리 리스트.
            최소한 user 역할의 메시지가 하나 이상 포함되어 있어야 한다.

    Returns:
        list: 도구 실행 결과와 Claude 응답이 모두 추가된 최종 대화 히스토리 리스트.
    """
    while True:
        # chat()을 호출하여 Claude API에 현재 대화와 도구 스키마를 전송
        response = chat(messages, tools=[get_current_datetime_schema])
        # add_assistant_message()로 Claude 응답을 대화 히스토리에 추가
        add_assistant_message(messages, response)

        # text_from_message()로 응답의 텍스트 블록만 추출하여 출력
        text = text_from_message(response)
        if text:
            print(text)

        # stop_reason이 tool_use가 아니면 대화 종료
        if response.stop_reason != "tool_use":
            break

        # run_tools()로 tool_use 블록의 도구들을 실행하고 결과 수집
        tool_results = run_tools(response)
        # add_user_message()로 도구 실행 결과를 대화 히스토리에 추가
        add_user_message(messages, tool_results)

    return messages


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    messages = []
    # add_user_message()로 초기 사용자 질문을 대화 히스토리에 추가
    add_user_message(
        messages,
        "What is the current time in HH:MM format? Also, what is the current time in SS format?",
    )
    # run_conversation()으로 에이전틱 대화 루프 시작
    run_conversation(messages)
