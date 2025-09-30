from openai import OpenAI 

cliente = OpenAI(api_key="")

resposta = cliente.chat.completions.create(
    model='gpt-4o-mini', 
    messages=[
        {"role": "system", "content": "Você é um assistente que responde em português"},
        {"role": "user", "content": "Qual a diferença entre JavaScript e Java ?"}
    ]
)
print(resposta.choices[0].message.content)