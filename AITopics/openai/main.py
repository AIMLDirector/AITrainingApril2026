from openaidev import devcode
from openaiprod import prodcode
import os
# APP_ENV1 = os.getenv("APP_ENV")

# def main():
#     user_input = str(input("Enter your message: ")) 

#     if APP_ENV1 == "development":
#         print("Development Environment Response:")
#         devcode(user_input)
#     elif APP_ENV1 == "production":
#         print("\nProduction Environment Response:")
#         prodcode(user_input)
#     else:
#         print("Invalid environment. Please set ENV to 'development' or 'production'.")
env_var = os.getenv("APP_ENV")

load_dotenv(f".env.{env_var}")


main()