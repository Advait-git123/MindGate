# utils/llm.py
from llama_cpp import Llama

# Initialize once
llm = Llama(
    model_path="model_llm/TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf",
    n_threads=6,             # Or more depending on your CPU
    n_ctx=2048,
    f16_kv=True,             # Optional: set to False if you face issues
    temperature=0.7,
    top_p=0.95,
)

def call_local_llm(prompt: str) -> str:
    output = llm(prompt, max_tokens=300, stop=["<|user|>", "<|system|>"])
    return output["choices"][0]["text"].strip()
