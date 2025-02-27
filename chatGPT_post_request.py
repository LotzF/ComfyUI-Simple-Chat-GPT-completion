import time
from openai import OpenAI, AzureOpenAI

amountOfRetries = 3
sleepDuration = 5

def openai_post_request(apiKey, model, backstory, prompt) -> str:
    client = OpenAI(api_key=apiKey, )
    i = 0
    while i < amountOfRetries:
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": backstory, },
                    {"role": "user", "content": prompt, },
                ],
            )
            completion_response = completion.choices[0].message.content
            return completion_response
        except Exception as e:
            print(f"Chat completion failed. Trying again in {sleepDuration} seconds!")
            i += 1
            if i < amountOfRetries:
                time.sleep(sleepDuration)
            else:
                assert False, f"Failed to get response. Tried {i} times."

def azure_openai_completion(apiKey, endpoint_url, api_version, model, backstory, prompt) -> str:
    client = AzureOpenAI(api_key=apiKey, azure_endpoint=endpoint_url, api_version=api_version)
    i = 0
    while i < amountOfRetries:
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": backstory, },
                    {"role": "user", "content": prompt, },
                ],
            )
            completion_response = completion.choices[0].message.content
            return completion_response
        except Exception as e:
            print(f"Chat completion failed. Trying again in {sleepDuration} seconds!")
            i += 1
            if i < amountOfRetries:
                time.sleep(sleepDuration)
            else:
                assert False, f"Failed to get response. Tried {i} times."

class ChatGptCompletion:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "apiKey": ("STRING", {"default": "put your api key here"}),
                "prompt": ("STRING", {"multiline": True}),
                "model": ("STRING", {"default": "gpt-3.5-turbo"}),
                "agentBackstory": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    OUTPUT_NODE = True
    CATEGORY = "g_nodes"
    EXECUTE = 'process'

    @staticmethod
    def process(apiKey, prompt, model, agentBackstory) -> str:
        text = openai_post_request(apiKey, model, agentBackstory, prompt)
        return (text,)

class AzureChatGptCompletion:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "endpoint_url": ("STRING", {"default": "put your endpoint URL here"}),
                "api_version": ("STRING", {"default": "2024-08-01-preview"}),
                "api_key": ("STRING", {"default": "put your api key here"}),
                "prompt": ("STRING", {"multiline": True}),
                "model": ("STRING", {"default": "gpt-4o"}),
                "agent_backstory": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    OUTPUT_NODE = True
    CATEGORY = "g_nodes"
    EXECUTE = 'process'

    @staticmethod
    def process(api_key, endpoint_url, api_version, prompt, model, agent_backstory) -> str:
        text = azure_openai_completion(api_key, endpoint_url, api_version, model, agent_backstory, prompt)
        return (text,)


# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ChatGPTCompletion": ChatGptCompletion,
    "AzureChatGptCompletion": AzureChatGptCompletion,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ChatGPTCompletion": "ChatGPTCompletion",
    "AzureChatGptCompletion": "AzureChatGPTCompletion",
}