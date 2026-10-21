def battle(prompt):
    msgs = [{"role": "user", "content": prompt}]

    # Model A — GPT-OSS on Groq
    a = client.chat.completions.create(model="openai/gpt-oss-20b", messages=msgs)

    # Model B — Qwen on Groq
    b = client.chat.completions.create(model="qwen/qwen3.8-27b", messages=msgs)

    return a.choices[0].message.content, b.choices[0].message.content
# …now we wrap this in Gradio with two columns + thumbs up/down 👇
