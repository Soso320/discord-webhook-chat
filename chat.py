import requests
import json
from os import system, name

# Clears the console
# Change "cls" to "clear" if you're on linux! (better fix soon)
def clear():
    system('cls')

url = input("Enter your webhook url:\n>")
name = input("Enter your webhook username [Enter for default]:\n>")
avatar = input("Enter your webhook avatar URL [Enter for default]:\n>")

clear()
print(f"Parameters saved.\nWebhook url: {url}\nWebhook Username: {name}\nWebhook Avatar URL: {avatar}")
input("Press Enter to continue...")
clear()


# Sends the webhook
def webhook(message):
    data = {}
    data["content"] = message
    data["username"] = name
    data["avatar_url"] = avatar
    result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Info: Payload delivered successfully, code {result.status_code}.")

# Checks if the webhook is valid
def check(webhook):
    print("Checking webhook, Please wait...")
    headers = {'User-agent': 'Mozilla/5.0 (Linux; soso-bot; webhook-verify)'}
    r = requests.get(webhook, headers=headers)
    if r.status_code in {200}:
        return True
    if r.status_code in {10015}:
        return False

# Check some more stuff
if url == "":
    print("Warn: Blank URL!\nExiting...")
    quit()
if "https://discordapp.com/api/webhooks/" in url:
    if check(url):
        print("Info: Webhook URL is valid!")
    else:
        print("Warn: Webhook Url invalid!\nExiting...")
        quit()
else:
    print("Warn: Not a webhook URL!\nExiting...")
    quit()


# Repeatedly asks for a message
print("You may now start sending messages!")
while True:
    content = input(">")
    webhook(content)
    print(f"[{name}] {content}")
