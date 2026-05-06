import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.2-1B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

user_input = input("Enter your message: ")
messages = [
    {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
    {"role": "user", "content": user_input},
]
outputs = pipe(
    messages,
    max_new_tokens=256,
)
print(outputs[0]["generated_text"][-1])

# model == public library ( newspaper, books - tech, non tech, fiction, story , magazine 
# model == human brain ( experience, knowledge, learning, understanding, reasoning, problem solving, creativity, emotions, social interactions, language processing, memory, attention, perception) 
# model data - ( website, book, newspaper, magazine, social media, video, audio, conversation, experience)  

