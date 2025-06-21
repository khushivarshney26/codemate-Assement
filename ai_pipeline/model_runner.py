from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

MODEL_NAME = "google/flan-t5-base"

# ✅ Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# ✅ Create pipeline and assign to `generator`
generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=-1)

# ✅ Function to run model
def run_model(prompt):
    instruction = f"""
You are a planner AI that converts user instructions into a sequence of function calls.

### Available functions:
1. get_invoices(month)
2. summarize_invoices(invoices)
3. send_email(to, content)

### Example input:
Retrieve all invoices for March, summarize the total amount, and send the summary to my email.

### Example output:
get_invoices(month="March")
summarize_invoices(invoices)
send_email(to="user@example.com", content=summary)

### Now convert this request:
{prompt}
"""
    output = generator(instruction.strip(), max_new_tokens=256, do_sample=False)
    return output[0]["generated_text"]
