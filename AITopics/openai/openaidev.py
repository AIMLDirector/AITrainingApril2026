from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()
# user_input = input("Enter your message: ")  
def devcode(user_input):
    response = client.responses.create(
        model="gpt-5-nano",
        input=user_input,
        
        
    )

    print(response.output_text)