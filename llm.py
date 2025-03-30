# Import necessary libraries
import os
from together import Together
from dotenv import load_dotenv

def generate_response(prompt):
    # Set your API key as an environment variable (replace with your key)
    os.environ["TOGETHER_API_KEY"] = "3045ace567b59cd96ed78310bee29038b11611cfce527e0da8ed9c7ae4da67e1"  

    # Initialize the client with the API key
    client = Together(api_key=os.environ["TOGETHER_API_KEY"])

    # Make a request to the model
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>", "<|eom_id|>"],
        stream=True
    )

    # Initialize a variable to accumulate the content
    result = ""

    # Process and accumulate the results
    for token in response:
        if hasattr(token, 'choices'):
            result += token.choices[0].delta.content

    # Return the accumulated result
    return result





