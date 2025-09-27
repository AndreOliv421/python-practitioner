from openai import OpenAI 

cliente = OpenAI(api_key="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")

resposta = cliente.chat.completions.create(
    model='gpt-4o-mini', 
    messages=[
        {"role": "system", "content": "Você é um assistente que responde em português"},
        {"role": "user", "content": "Qual a diferença entre JavaScript e Java ?"}
    ]
)
print(resposta.choices[0].message.content)