# ComfyUI simple ChatGPT completion

A simple node to request ChatGPT completions.

Do not share your workflows including the API key!
I'll take no responsibility for your leaked keys.

## How to install
Download or clone repo.

Extract/Clone to ../ComfyUI/custom_nodes

run within ./ComfyUI-Simple-Chat-GPT-completion

```
pip install -r requirements.txt
```

## OpenAI API key location

Create and use an API-key from

https://platform.openai.com/api-keys

## Select OpenAI model

Select a completion model from 

https://platform.openai.com/docs/models/overview

## Usage

Node can be found via search

ChatGPTCompletion

or right click add nodes

g_nodes/ChatGPTCompletion

### Node Values

apiKey: *Your API key*

prompt: *Your prompt*

model: *OpenAI completion model*

agentBackstory: *backstory of gpt agent* (optional)


