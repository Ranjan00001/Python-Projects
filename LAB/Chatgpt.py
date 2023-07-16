import openai
openai.api_key = "YOUR_API_KEY"
prompt = "Hello, can you tell me a joke?"
response = openai.Completion.create(engine="davinci", prompt=prompt,
    max_tokens=60, n=1, stop=None, temperature=0.7)
message = response.choices[0].text.strip()
print(message)
