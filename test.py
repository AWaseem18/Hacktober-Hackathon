
import ollama

MODEL = "gemma4:e4b"  # must match the name shown by `ollama list`
print("start")
try:
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": "Write a 5-sentence Halloween story. Use exactly 6 blanks in the form {noun}, {verb}, {adjective}. Output only the story, no intro"}],
        options={"num_gpu": 0},
    )
    print("It works! Model said:")
    print(response["message"]["content"])
except Exception as e:
    print("Something went wrong:", e)

print("end")
