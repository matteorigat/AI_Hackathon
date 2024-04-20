import os
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

os.environ["HF_TOKEN"] = "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"



tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b")

input_text = "what you know about universe"
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))