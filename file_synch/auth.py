import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")
url = os.getenv("url")
print(token)
print(url)
