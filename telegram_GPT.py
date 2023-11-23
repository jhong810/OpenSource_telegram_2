import telegram
import asyncio

from openai import OpenAI
client = OpenAI(api_key = '')

token =""
bot = telegram.Bot(token = token)
chat_id = ""

def chatGPT():
  '''completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
  )'''
  return "GPT Echo 결과값"

result = chatGPT()

asyncio.run(bot.sendMessage(chat_id=chat_id,text=result))