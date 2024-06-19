from openai import OpenAI
from yaml_reader import YamlReader

config = YamlReader("../../config.yaml").get_yaml_object()

client = OpenAI(
    api_key=config["CODECRAFT_CLI_OPENAI_API_KEY"],
    project=config["CODECRAFT_CLI_PROJECT_ID"],
    organization=config["CODECRAFT_CLI_ORGANIZATION_ID"],
)

instructions = "You will only generate Python code using libraries like NumPy and Pandas \
for data processing prompts."

assistant = client.beta.assistants.create(
    name="codecraft_cli_assistant",
    instructions=instructions,
    model=config["CODECRAFT_CLI_ASSISTANT_MODEL"]
)

print(f"CODECRAFT_CLI_ASSISTANT_ID={assistant.id}")