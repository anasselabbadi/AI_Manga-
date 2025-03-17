from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Charger DeepSeek depuis Hugging Face
MODEL_NAME = "deepseek-ai/deepseek-llm-7b-chat"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float16, device_map="auto")

def chat_with_user(user_input):
    try:
        input_ids = tokenizer(user_input, return_tensors="pt").input_ids.to("cuda" if torch.cuda.is_available() else "cpu")

        output = model.generate(input_ids, max_length=200)
        response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
        
        return response
    except Exception as e:
        return f"Erreur lors de la génération de la réponse : {str(e)}"
