import tiktoken

encoding = tiktoken.encoding_for_model("gpt-5-nano")

tokens = encoding.encode("Hi my name is Atharva and I like Pizza")

print(f"Tokens:" , tokens)

for token_id in tokens:
    token_text = encoding.decode([token_id])
    print(f"{token_id} = {token_text}")