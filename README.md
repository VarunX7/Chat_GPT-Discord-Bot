# Chat_GPT-Discord-Bot (V_Gpt)  

This is a discord bot that uses openAi's **GPT-3.5 turbo** LLM model to generate human like speech to interact with users.    
Here I have provided a chat.txt file to add some context and persona to the bot.    
The text from 'chat.txt' file is used as a chat history by the bot and it uses it to generate appropriate response.   
The dialogues in the chat.txt file were generated using ChatGPT with the promp - *assume that a ragnar lothbrok and robin hood both exist in the same time and are very close friends and also allies in war against the cruel and tyrannical lannisters.They both have led their armies to many battles together and now its time for the final battle. Now generate 20 dialogues in which they  are discussing strategy for the upcoming battle of casterly rock which is the home of the lannisters and also has the fort that has never ever been captured before.*   
The bot will give the first user the persona of Robin Hood and other users the personas of people associated with Robin Hood and Ragnar Lothbrok.
The 'chat.txt' can be easily edited to change the above scenario or personas.

## Getting started...

Clone and extract this repository.
Install the discord package using `pip install discord` and the openAi package using `pip install --upgrade openai`.   
You will need to obtain the following environment information-   
  1. APP_ID; PUBLIC_KEY   # go to -> https://discord.com/developers/docs/getting-started (you might need to login to discord first) -> create app -> name your bot and create -> General Information(left sidebar) ->copy the APPLICATION ID and PUBLIC KEY
  2. TOKEN  # After obtaining the above keys go to-> Bot(left sidebar) -> Reset token -> copy the new token 
  3. OPENAI  #from https://openai.com/
You will also need to host the bot for it to work.    

