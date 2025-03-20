import ollama

#zero shot
# messages = [
#     {"role": "user", "content": "Translate the following English sentence to French: 'Where is the nearest train station?'"}
# ]

# #few shot
# messages = [
#     {"role": "system", "content": "You are a language translator. Translate English to French."},
#     {"role": "user", "content": "Hello, how are you?"},
#     {"role": "assistant", "content": "Bonjour, comment ça va?"},
#     {"role": "user", "content": "Where is the nearest train station?"}
# ]

# # #chain of thought
# messages = [
#     {"role": "system", "content": "You are a math tutor. Think step by step before answering."},
#     {"role": "user", "content": "If a car travels 60 km per hour, how far will it travel in 3 hours?"}
# ]

# #hybrid 
# messages = [
#     {"role": "system", "content": "You are a math tutor. Solve problems step by step."},
#     {"role": "user", "content": "If a person saves $100 each month, how much will they have after 6 months?"},
#     {"role": "assistant", "content": "Step 1: The person saves $100 per month. \nStep 2: In 6 months, the total savings will be $100 × 6. \nStep 3: The final answer is $600."},
#     {"role": "user", "content": "If a train moves at 80 km per hour, how far does it go in 4 hours?"}
# ]

# #role based
messages = [
    {"role": "system", "content": "You are a legal expert. Explain laws in simple terms."},
    {"role": "user", "content": "What is POCSO?"}
]

# #Self-Consistency Prompting
# messages = [
#     {"role": "system", "content": "You are an AI assistant. Answer the question accurately."},
#     {"role": "user", "content": "What is the capital of Canada?"}
# ]

# #Deliberate Misinformation Handling
# messages = [
#     {"role": "user", "content": "The Earth is flat, right?"}
# ]


response = ollama.chat(
    model="gemma3:1b",
    messages = messages,
    options={
        "temperature": 0, 
        "top_k": 40,
        "max_tokens" : 5
    }
)

print(response["message"]["content"])