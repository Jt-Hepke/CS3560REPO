import os
from google import genai
from google.genai import types

# Initialize Gemini client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

############################################################
# FUNCTION DECLARATIONS (TOOLS)
############################################################

set_light_values_declaration = {
    "name": "set_light_values",
    "description": "Set brightness and color temperature of a light",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "integer",
                "description": "Light brightness from 0 to 100"
            },
            "color_temp": {
                "type": "string",
                "enum": ["daylight", "cool", "warm"],
                "description": "Color temperature of the light"
            }
        },
        "required": ["brightness", "color_temp"]
    }
}

schedule_meeting_declaration = {
    "name": "schedule_meeting",
    "description": "Schedule a meeting",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "date": {"type": "string"},
            "time": {"type": "string"}
        },
        "required": ["title", "date", "time"]
    }
}

add_task_declaration = {
    "name": "add_task",
    "description": "Add a task to the to-do list",
    "parameters": {
        "type": "object",
        "properties": {
            "task": {"type": "string"},
            "priority": {"type": "string"}
        },
        "required": ["task"]
    }
}

get_weather_declaration = {
    "name": "get_weather",
    "description": "Get the weather for a city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string"}
        },
        "required": ["city"]
    }
}

send_email_declaration = {
    "name": "send_email",
    "description": "Send an email",
    "parameters": {
        "type": "object",
        "properties": {
            "recipient": {"type": "string"},
            "subject": {"type": "string"},
            "message": {"type": "string"}
        },
        "required": ["recipient", "subject", "message"]
    }
}


def set_light_values(brightness, color_temp):
    return {
        "brightness": brightness,
        "colorTemperature": color_temp
    }

def schedule_meeting(title, date, time):
    return {
        "status": "Meeting Scheduled",
        "title": title,
        "date": date,
        "time": time
    }

def add_task(task, priority="normal"):
    return {
        "status": "Task Added",
        "task": task,
        "priority": priority
    }

def get_weather(city):
    return {
        "city": city,
        "temperature": "72F",
        "condition": "Sunny"
    }

def send_email(recipient, subject, message):
    return {
        "status": "Email Sent",
        "recipient": recipient,
        "subject": subject
    }


tools = types.Tool(
    function_declarations=[
        set_light_values_declaration,
        schedule_meeting_declaration,
        add_task_declaration,
        get_weather_declaration,
        send_email_declaration
    ]
)

config = types.GenerateContentConfig(tools=[tools])


contents = [
    types.Content(
        role="user",
        parts=[types.Part(text="Schedule a meeting called AI Project tomorrow at 3pm")]
    )
]

response = client.models.generate_content(
    model="gemini-3.0-flash",
    contents=contents,
    config=config
)

tool_call = response.candidates[0].content.parts[0].function_call
print("Function Call:", tool_call)

result = None

if tool_call.name == "set_light_values":
    result = set_light_values(**tool_call.args)

elif tool_call.name == "schedule_meeting":
    result = schedule_meeting(**tool_call.args)

elif tool_call.name == "add_task":
    result = add_task(**tool_call.args)

elif tool_call.name == "get_weather":
    result = get_weather(**tool_call.args)

elif tool_call.name == "send_email":
    result = send_email(**tool_call.args)

print("Function result:", result)

function_response_part = types.Part.from_function_response(
    name=tool_call.name,
    response={"result": result}
)

contents.append(response.candidates[0].content)
contents.append(types.Content(role="user", parts=[function_response_part]))

final_response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=contents,
    config=config
)

print("\nAssistant Response:")
print(final_response.text)

def analyze_image():

    with open("test.jpg", "rb") as f:
        image_bytes = f.read()

    image_contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/jpeg",
                ),
                types.Part(text="What objects do you see in this image?")
            ],
        )
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=image_contents,
    )

    print("\nImage Analysis:")
    print(response.text)

def generate_image():

    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents="Generate a minimal productivity wallpaper with a motivational quote"
    )

    print("\nImage generated successfully")

analyze_image()
generate_image()