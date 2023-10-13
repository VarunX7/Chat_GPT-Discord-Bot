import discord
import os
import openai

token = os.environ['TOKEN']
app_id = os.environ['APP_ID']
public_key = os.environ['PUBLIC_KEY']
openai_key = os.environ['OPENAI']

openai.api_key = openai_key

with open("chat.txt", "r") as f:
  chat = f.read()


class MyClient(discord.Client):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    global chat
    chat += f"{message.author}: {message.content}"
    # print(f'Message from {message.author}: {message.content}')
    channel = message.channel
    if self.user != message.author:
      # print(chat)
      if message.content.startswith('$v') or self.user in message.mentions:
        channel = message.channel
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                messages=[{
                                                    "role":
                                                    "user",
                                                    "content":
                                                    f"{chat}\nV_gpt: "
                                                }],
                                                temperature=1,
                                                max_tokens=256,
                                                top_p=1,
                                                frequency_penalty=0,
                                                presence_penalty=0)
        messageToSend = response.choices[0].message.content
        await message.channel.send(messageToSend)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
