import openai
import requests

class GPTJudge:
    def __init__(self, api_key=None, endpoint=None):
        self.api_key = api_key
        self.endpoint = endpoint

    def evaluate(self, prompt):
        if self.endpoint:
            # AWS endpoint for GPT-4 judging (expects score in response)
            response = requests.post(self.endpoint, json={"prompt": prompt})
            return response.json().get("score", 0)
        else:
            openai.api_key = self.api_key
            completion = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return completion.choices[0].message["content"]
