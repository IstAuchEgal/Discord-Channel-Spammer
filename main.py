import requests
from time import sleep

spam_amount = 5 # How often you want the message to be sent

def send_messages(channelid):
  payload = {
    'content': Test # The message you want to be sent
  }

  headers = {
    'authorization': '*' # Your Discord authorization key goes here
  }
  requests.post(f'https://discord.com/api/v9/channels/{channelid}/messages', data=payload, headers=headers) 


x = 1 

while(x <= spam_amount):
  send_messages('*') # Your channel ID goes here
  x += 1
  sleep(0.25) # The time between each message, if this is to low discord wont accept every message
  print(x - 1) # This is to print how often the message has been sent

if(x >= spam_amount): # This prints a message when the script has finished
  print("Finished.")
