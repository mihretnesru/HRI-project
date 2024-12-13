import openai
import os
import json

# Load the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the environment.")

# Initialize OpenAI client
client = openai.Client(api_key=api_key)
# Load the question from a JSON file
def load_question_from_json(json_file):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
            question = data.get("question", "").strip()
            if not question:
                raise ValueError("The 'question' field in the JSON file is empty or missing.")
            return question
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{json_file}' not found.")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file '{json_file}'.")

# Path to the JSON file containing the input question
json_file_path = "input_to_llm.json"

# Load the question
question = load_question_from_json(json_file_path)

# Generate a chat completion with OpenAI
completion =  client.chat.completions.create(
    model="gpt-4o-mini",  # Change model to "gpt-4" if needed
    messages=[
        {"role": "system", "content": "You are assisting a user with high technical literacy. Employ complex terminology and indirect reasoning if desired, but remain concise. Provide detailed insight within 50 tokens per response. The user can handle sophisticated concepts without confusion."},
        {"role": "user", "content": question}
    ],
    temperature=0.5
)

# Get the assistant's response
assistant_response = completion.choices[0].message.content

# Print the assistant's response
print("Assistant Response:", assistant_response)


# Save the assistant's response to output_from_llm.json
output_file_path = "output_from_llm.json"
with open(output_file_path, "w") as file:
    json.dump({"response": assistant_response}, file, indent=4)



