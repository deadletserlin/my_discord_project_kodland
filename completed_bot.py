import discord
from bot_logic import gen_pass

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('$pasw'):
        await message.channel.send("password kamu " + gen_pass(10))
    elif message.content.startswith('!deleteme'):
        await message.channel.send('Goodbye in 3 seconds...', delete_after=3.0)
    else:
        await message.channel.send(message.content)

@client.event 
async def on_message_delete(self, message):
        msg = f'{message.author} has deleted the message: {message.content}'
        await message.channel.send(msg)

client.run("MTExMDU1Nzk4MDM4NDA0NzE5NA.GFcYB9.9Tf-FPaP9D9JGh9ypqCnlymZP1V-ydlkTzPmNs")
