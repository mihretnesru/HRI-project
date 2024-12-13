import json
from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

# Load the LLAMA model and tokenizer
model_name = "meta-llama/Meta-Llama-3.1-8B-Instruct"  # Replace with your model path or name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16
)

# Create a pipeline for HuggingFace
llm_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100,
    temperature=0.2,
    top_p=0.9,
    repetition_penalty=1.2,
    do_sample=True,
    truncation=True,
    pad_token_id=tokenizer.eos_token_id,
    device="cuda",
)

# Wrap the pipeline in LangChain
llm = HuggingFacePipeline(pipeline=llm_pipeline)

# Define the prompt template
template = """You are a specialized conversational assistant focused on technical literacy in computer science, coding, data science, and machine learning. Your role is to provide accurate, concise, and conversational responses. Follow these guidelines strictly:

1. **Precision and Accuracy**: Answer the question directly without adding unrelated details. If you do not know the answer, say, "I do not know."
2. **No Hallucinations**: Base your response only on facts. Do not invent or assume information.
3. **Token Efficiency**: Ensure your response fits within the `max_new_tokens` limit without truncation.
4. **Conversational Style**: Write in a friendly and clear tone as if engaging in a conversation.

User Question: {question}
Main rule : Do no display the prompt template and user question in the LLM response
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=template
)

# Create the LLM chain (no memory used)
llm_chain = LLMChain(llm=llm, prompt=PromptTemplate(input_variables=["question"], template=template), verbose=False)
def get_llm_response_from_json(json_file="input_to_llm.json"):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
            user_question = data.get("question", "").strip()
            if not user_question:
                raise ValueError("The 'question' field in the JSON file is empty or missing.")
        
        # Generate the response
        raw_response = llm_chain.invoke({"question": user_question})
        
        # Handle response formats
        if isinstance(raw_response, str):
            clean_response = raw_response.strip()
        elif isinstance(raw_response, dict) and "text" in raw_response:
            clean_response = raw_response["text"].strip()
        else:
            raise ValueError("Unexpected response format from LLM.")
        
        # Post-process the response to remove echoed prompt content
        return clean_response.split("Answer:", 1)[-1].strip()

    except FileNotFoundError:
        return "Error: The input JSON file was not found. Please check the file path."
    except json.JSONDecodeError:
        return "Error: The JSON file is not formatted correctly."
    except ValueError as ve:
        return f"Error: {ve}"


if __name__ == "__main__":
    response = get_llm_response_from_json()
    print("LLM Response:", response)
