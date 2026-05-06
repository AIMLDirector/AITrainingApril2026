from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

def prodcode(user_input):
    response = client.responses.create(
        model="gpt-5.5",
        input=user_input,
       
        
    )

    print(response.output_text)