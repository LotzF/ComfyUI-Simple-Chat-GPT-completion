import time
from openai import OpenAI

amountOfRetries = 3
sleepDuration = 5

def openAIPostRequest(apiKey, model, backstory, prompt) -> str:
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
            completionResponse = completion.choices[0].message.content
            return completionResponse
        except:
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
        text = openAIPostRequest(apiKey, model, agentBackstory, prompt)
        return (text,)


# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ChatGPTCompletion": ChatGptCompletion,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ChatGPTCompletion": "ChatGPTCompletion",
}
