# Install required libraries (uncomment if not already installed)
# %pip install flask transformers accelerate torch bitsandbytes

from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from flask import Flask, request, jsonify
import torch

# Initialize Flask app
app = Flask(__name__)

# Load the model and tokenizer
model_name = "defog/sqlcoder-7b-2"
device = "mps" if torch.backends.mps.is_available() else "cpu"  # Use MPS if available, otherwise CPU
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create a text-generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if device == "mps" else -1)

# Define the Flask route for SQL generation
@app.route("/generate", methods=["POST"])
def generate_sql():
    data = request.json
    question = data["question"]

    # Define the prompt for the model
    prompt = f"""
    You are a SQL expert. Use the following schema:

    Table: employees
    Columns: id, name, department, salary, date_joined

    ### Convert the following question into a SQL query:
    {question}

    SQL:
    """
    # Generate the SQL query
    output = generator(prompt, max_new_tokens=150, do_sample=False)[0]["generated_text"]
    sql_query = output.split("SQL:")[-1].strip()

    # Return the generated SQL query as JSON
    return jsonify({"sql": sql_query})

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)