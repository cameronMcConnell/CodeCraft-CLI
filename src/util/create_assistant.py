from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("CODECRAFT_CLI_OPENAI_API_KEY"),
    project=os.environ.get("CODECRAFT_CLI_PROJECT_ID"),
    organization=os.environ.get("CODECRAFT_CLI_ORGANIZATION_ID")
)

instructions = "You will only generate Python code using libraries like NumPy and Pandas \
for data processing prompts. Only answer questions relevant to the csv file you are \
supplied in the thread. If the prompt is not a data processing operation, return an \
empty string."

assistant = client.beta.assistants.create(
    name="codecraft_cli_assistant",
    instructions=instructions,
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo"
)

print(f"CODECRAFT_CLI_ASSISTANT_ID={assistant.id}")