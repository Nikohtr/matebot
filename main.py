import discord
import os
from discord.ext import commands
import asyncio
from discord.utils import get
import random
import urllib.request
import json
from discord.ext.commands import has_permissions
from discord.ext.commands import has_role
from datetime import datetime, time
import ast
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord_webhook import DiscordWebhook
from datetime import timedelta 
import requests

client = commands.Bot(command_prefix='+')        
@client.event
async def on_ready():
    print("I'm in")
    print(client.user),
    client.loop.create_task(change_playing())
    client.loop.create_task(sub())
    
@client.command(pass_context=True)
async def role(ctx, user: discord.Member, *, roleadd):
#     if ctx.message.author != "263685060819943425":
#         pass
#     else:
#         await client.delete_message(ctx.message)
        role = discord.utils.get(user.server.roles, name=str(roleadd))
        await client.add_roles(user, role)







# requestParams = {
#     "method": "getQuote",
#     "key": "457653",
#     "format": "json",
#     "lang": "en"    
#     }
# url = "http://api.forismatic.com/api/1.0/"

# loop = True
# scopes = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# json_creds = os.getenv("KARMA")
# creds_dict = json.loads(json_creds)
# creds_dict["private_key"] = creds_dict["private_key"].replace("\\\\n", "\n")
# creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes)
# gs = gspread.authorize(creds)
# sheet = gs.open("karma").sheet1


# client = commands.Bot(command_prefix='+')        
# @client.event
# async def on_ready():
#     print("I'm in")
#     print(client.user),
#     client.loop.create_task(change_playing())
#     client.loop.create_task(sub())
    
# @client.command(pass_context=True)
# async def killswitch(ctx):
#     if ctx.message.author.id == "263685060819943425":
#         await client.say("Alright see you on the other side")
#         exit()
 
# async def register(user):
#     global sheet
#     try:
#         try:
#             cell = sheet.find(user)
#         except gspread.exceptions.APIError:
#             scopes = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#             json_creds = os.getenv("KARMA")
#             creds_dict = json.loads(json_creds)
#             creds_dict["private_key"] = creds_dict["private_key"].replace("\\\\n", "\n")
#             creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes)
#             gs = gspread.authorize(creds)
#             sheet = gs.open("karma").sheet1
#             cell = sheet.find(user)
#     except gspread.exceptions.CellNotFound:
#         reg = [user, 0]
#         sheet.insert_row(reg, 2)
        

# @client.event                
# async def update(user, num):
#     cell = sheet.find(user)
#     points = sheet.acell("B"+str(cell.row))
#     sheet.update_acell("B"+str(cell.row), int(points.value)+num)
    
    
# @client.command(pass_context=True, aliases=['as'])
# @commands.has_role('Owner')
# async def addscore(ctx, user: discord.Member, num: int):
#     if ctx.message.channel.type != discord.ChannelType.private:
#         user = user.id
#         await register(user)
#         await update(user, num)
#         await client.say("Done!")
        


# @client.command(pass_context=True, aliases=['ss'])
# @commands.has_role('Owner')
# async def subtractscore(ctx, user: discord.Member, num: int):
#     if ctx.message.channel.type != discord.ChannelType.private:
#         user = user.id
#         await register(user)
#         num = num-(2*num)
#         await update(user, num)
#         await client.say("Done!")

    
# @client.command(pass_context=True, aliases=['cs'])
# @commands.has_role('Owner')
# async def changescore(ctx, user: discord.Member, num: int):
#     if ctx.message.channel.type != discord.ChannelType.private:
#         user = user.id
#         await register(user)
#         cell = sheet.find(user)
#         sheet.update_acell("B"+str(cell.row), num)
#         await client.say("Done!")
    
# @client.command(pass_context=True)
# async def score(ctx, user: discord.Member = None):
#     if ctx.message.channel.type != discord.ChannelType.private:
#         if not user: user = ctx.message.author
#         await register(user.id)
#         cell = sheet.find(user.id)
#         points = sheet.acell("B"+str(cell.row))
#         await client.say("{0.mention} has a score of ".format(user)+ str(points.value))
                
    
# # @client.command(pass_context=True)
# # @commands.has_role('Owner')
# # async def rep(ctx, user: discord.Member):
# #     if ctx.message.channel.type != discord.ChannelType.private:


# @client.command(pass_context = True)
# @commands.has_role('Owner')
# async def esay(ctx, *, mg = None):
#       if ctx.message.channel.type != discord.ChannelType.private:
#           await client.delete_message(ctx.message)

#           if not mg: await client.say("Please specify a message to send")
#           else:
#             await client.send_message(ctx.message.channel, embed = discord.Embed(description = "["+mg+"](https://www.youtube.com/user/PewDiePie?sub_confirmation=1)", color = 0x2b44ff))

# @client.command()
# async def gap():
#     key = os.getenv("KEY")
#     data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="+key).read()
#     subspew = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
#     data1 = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key="+key).read()
#     subst = json.loads(data1)["items"][0]["statistics"]["subscriberCount"]
#     gapis=int(subspew)-int(subst)
#     await client.say("T-series is {:,d}".format(int(gapis))+" subs away from PewDiePie. PewDiePie has {:,d}".format(int(subspew))+" subscibers and T-series has {:,d}".format(int(subst))+" subscibers!")

# @client.command()
# async def dislikes():
#     key = os.getenv("KEY")
#     data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=YbJOTdZBX1g&key="+key).read()
#     dis = json.loads(data)["items"][0]['statistics']['dislikeCount']
#     data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=kffacxfA7G4&key="+key).read()
#     dis1 = json.loads(data)["items"][0]['statistics']['dislikeCount']
#     raz = int(dis)-int(dis1)
#     await client.say("Youtube Rewind 2018 has {:,d}".format(int(dis))+" dislikes. That's {:,d}".format(int(raz))+" above Justin Bieber's Baby")

# @client.command(pass_context = True)
# @commands.has_role('Owner')
# async def say(ctx, *, mg = None):
#       if ctx.message.channel.type != discord.ChannelType.private:
#           await client.delete_message(ctx.message)

#           if not mg: await client.say("Please specify a message to send")
#           else: await client.say(mg)
        
# @client.command(pass_context=True)
# @commands.has_role('Owner')
# async def joined_at(ctx, member: discord.Member = None):
#     if ctx.message.channel.type != discord.ChannelType.private:
#         if member is None:
#             member = ctx.message.author

#         await client.say('{0} joined at {0.joined_at}'.format(member))
        
        
# @client.command(pass_context=True, aliases = ["lb"])
# async def leaderboard(ctx):
#     all = sheet.get_all_records()
#     all.sort(key = lambda x: x["points"], reverse = True)
#     print(all)
#     em = discord.Embed(title="**Leaderboard**", color=0x00ff00)
#     for x in range(5):
#         em.add_field(name = str(x+1), value = "**<@"+str(all[x]["id"])+">: "+str(all[x]["points"])+"**", inline = False)
#         print("Added",x)
#     await client.send_message(ctx.message.channel, embed = em)
        
# @client.command(pass_context = True)
# @commands.has_role("Owner")
# async def ban(ctx, user: discord.Member = None):
#     if ctx.message.channel.type != discord.ChannelType.private:
#         if user == None: await client.say("Tell me who to ban")
#         else:
#             try:
#                 await client.ban(user, 7)
#                 await client.say("**Banned {0}**".format(user))
#             except discord.errors.NotFound:
#                 await client.say("I can't find that guy")

# @client.command(pass_context = True)
# @commands.has_role("Owner")
# async def unban(ctx, user = None):
#     if ctx.message.channel.type != discord.ChannelType.private:
#         if user == None: await client.say("Tell me who to unban")
#         else: 
#             try:
#                 user = await client.get_user_info(user)
#                 await client.unban(ctx.message.server, user)
#                 await client.say("**Unbanned {0}**".format(user))
#             except discord.errors.NotFound:
#                 await client.say("I can't find that guy")

        
# @client.command(pass_context = True)
# @commands.has_role("Owner")
# async def kick(ctx, user: discord.Member = None):
#     if ctx.message.channel.type != discord.ChannelType.private:
#         if user == None: await client.say("Tell me who to kick")
#         else:
#             try:
#                 await client.kick(user)
#                 await client.say("**Kicked {0}**".format(user))
#             except discord.errors.NotFound:
#                 await client.say("I can't find that guy")

# @client.command(pass_context = True)
# @commands.has_role("Owner")
# async def clear(ctx, *, number = None):
#     if ctx.message.channel.type != discord.ChannelType.private:
#         if not number or not number.isdigit(): await client.send_message(ctx.message.channel, "Tell me how many messages to delete")
#         else:
#             try:
#                 mgs = []
#                 number = int(number)+1
#                 if number>100:
#                     times = number//100
#                     for i in range(times):
#                         async for x in client.logs_from(ctx.message.channel, limit = 100):
#                             mgs.append(x)
#                         await client.delete_messages(mgs)
#                         mgs.clear()
#                     async for x in client.logs_from(ctx.message.channel, limit = number-(times*100)):
#                         mgs.append(x)
#                     await client.delete_messages(mgs)
#                 else:
#                     async for x in client.logs_from(ctx.message.channel, limit = number):
#                         mgs.append(x)
#                     await client.delete_messages(mgs)
#                 mgs.clear
#                 await client.send_message(client.get_channel("517753229258391567"), embed = discord.Embed(description ="Bulk delete by **"+str(ctx.message.author)+"** in **"+str(ctx.message.channel)+"**. **"+str(number)+"** messages were deleted", color = 0x2b44ff))
#             except discord.errors.HTTPException:
#                 await client.say("There was an error! Messages are most likely older than 14 days")
                
            
# @client.command(pass_context = True)
# async def clear(ctx, user: discord.Member = None, role):
#     if user == None: await client.delete_message(ctx.message)
#         else:
            




# async def isEnglish(s):
#     try:
#         s.encode(encoding='utf-8').decode('ascii')
#     except UnicodeDecodeError:
#         return True
#     else:
#         return False
# lp = True


# @client.command(pass_context = True)
# @commands.has_role('Owner')
# async def color(ctx):
#     if ctx.message.channel.type != discord.ChannelType.private:
#         global lp
#         lp = True
#         role = get(ctx.message.server.roles, id="517751310989131796")
#         await client.send_message(ctx.message.channel, "**Started rainbow colored roles!**")
#         while lp:
#           r = lambda: random.randint(0,255)
#           color = ('%02X%02X%02X' % (r(),r(),r()))
#           await client.edit_role( ctx.message.server, role, color = discord.Colour(value = int(color, 16)))
#           await asyncio.sleep(2)

# async def is_time_between(begin_time, end_time, check_time=None):
#     check_time = check_time or datetime.utcnow().time()
#     if begin_time < end_time:
#         return check_time >= begin_time and check_time <= end_time
#     else:
#         return check_time >= begin_time or check_time <= end_time
    
    
# def secondsToText(secs):
#     days = secs//86400
#     hours = (secs - days*86400)//3600
#     minutes = (secs - days*86400 - hours*3600)//60
#     seconds = secs - days*86400 - hours*3600 - minutes*60
#     result = ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
#     ("{0} hour{1}, ".format(hours, "s" if hours!=1 else "") if hours else "") + \
#     ("{0} minute{1}, ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
#     ("{0} second{1}, ".format(seconds, "s" if seconds!=1 else "") if seconds else "")
#     return result
        
# @client.event
# async def sub():
#     while True:
#         key = os.getenv("KEY")
#         data1 = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key="+key).read()
#         subst = json.loads(data1)["items"][0]["statistics"]["subscriberCount"]
#         data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="+key).read()
#         subspew = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
#         gap = int(subspew)-int(subst)
#         async for message in client.logs_from(client.get_channel("556818522056163339"), limit=1):
#             if message.author == client.user:
#                 su = message
#         msg = su
#         su = su.content
#         subsnow = int(subspew)//100000
#         async for message in client.logs_from(client.get_channel("532571319196188712"), limit=1):
#                 if message.author == client.user:
#                     subsbefore = int(message.content)
#         if subsnow>subsbefore:
#             print(subspew)
#             await client.send_message(client.get_channel("532571319196188712"), subsnow)
#             await client.send_message(client.get_channel("528874952342896640"), "@everyone PewDiePie just hit {:,d}".format(subsnow*100000))
#         elif gap<0 and su == "False":
#             await client.send_message(client.get_channel("528874952342896640"), "@everyone Damn very sad gamer moment. He was passed at {:,d}".format(int(subspew))+", the gap is {:,d}".format(gap)+" right now and the time is "+str(datetime.now()+timedelta(hours=2))+" \nSAD by xxxtentacion ")
#             await client.send_message(client.get_channel("556818522056163339"), "True")
#         elif su == "True" and gap>0:
#             now = datetime.now()
#             dif = (datetime.now()-msg.timestamp).total_seconds()
#             await client.send_message(client.get_channel("528874952342896640"), "@everyone We are back on top boys! He was passed for "+secondsToText(dif))
#             await client.send_message(client.get_channel("556818522056163339"), "False")
#         await asyncio.sleep(20)
        
        
# @client.command(pass_context= True)
# async def pewdie9(ctx):
#     if ctx.message.author.bot:
#         key = os.getenv("KEY")
#         data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="+key).read()
#         subspew = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
#         async for message in client.logs_from(client.get_channel("529692628518830091"), limit=1):
#             if message.author == client.user:
#                 su = message.content
#         await client.send_message(client.get_channel("529692628518830091"), subspew)
#         await client.send_message(client.get_channel("528874952342896640"), "@everyone PewDiePie got {:,d} subscribers today".format(int(subspew)-int(su)))
#         async for message in client.logs_from(client.get_channel("530336392455258142"), limit=1):
#             if message.author == client.user:
#                 loser = message.content
#                 loser = loser.split(",")
#                 print(loser)
#         for item in loser:
#             requestToApi = requests.post(url, params=requestParams)
#             jsonq = requestToApi.json()
#             finishedQuote = jsonq['quoteText'] + " -" + jsonq['quoteAuthor']
#             try:
#                 print(item)
#                 await client.send_message(await client.get_user_info(item) , "Hope you enjoyed living today. Be grateful for what you have because you don't know when you might lose it. Here is an inspirational quote to keep you going:\n"+finishedQuote)
#             except discord.Forbidden:
#                 hurl = os.getenv("hook_url")
#                 hook = DiscordWebhook(url= hurl, content = "<@"+item+"> Hope you enjoyed living today. Be grateful for what you have because you don't know when you might lose it. Here is an inspirational quote to keep you going:\n"+finishedQuote)
#                 hook.execute()
                
# @client.command(pass_context = True)
# @commands.has_role('Owner')
# async def stopcolor(ctx):
#     if ctx.message.channel.type != discord.ChannelType.private:
#         global lp
#         lp = False
#         await client.send_message(ctx.message.channel, "**Stoped rainbow colored roles!**")
        
# @client.command(pass_context = True)
# async def keepalive(ctx):
#     if ctx.message.channel.type != discord.ChannelType.private and ctx.message.author.bot:
#         await client.say("I ain't sleeping boi!")
        
# @client.command()
# @commands.has_role("Owner")
# async def dm(*, text):
#     async for message in client.logs_from(client.get_channel("530336392455258142"), limit=1):
#             if message.author == client.user:
#                 loser = message.content
#                 loser = loser.split(",")
#                 print(loser)
#     for item in loser:
#         await client.send_message(await client.get_user_info(item) , text)

# @client.command()
# @commands.has_role("Owner")
# async def testq():
#     requestToApi = requests.post(url, params=requestParams)
#     json = requestToApi.json() 
#     finishedQuote = json['quoteText'] + " -" + json['quoteAuthor']
#     await client.send_message(await client.get_user_info("263685060819943425") , "Hope you enjoyed living today. Be grateful for what you have because you don't know when you might lose it. Here is an inspirational quote to keep you going:\n"+finishedQuote)
                                      
      
# @client.command(pass_context = True)
# @commands.has_role('Owner')
# async def word(ctx, *, word=None):
#       if ctx.message.channel.type != discord.ChannelType.private and ctx.message.author.id == "263685060819943425":
#           global loop
#           await client.send_message(ctx.message.channel, "Saying "+word+" 100,000 times")
#           await client.delete_message(ctx.message)
#           times = 2000//(len(word)+2)
#           to100 = 100000//times
#           count = 0
#           if not word: await client.say("Please specify a word to say 100,000 times")
#           else: 
#             while count<=to100:
#               loop = False
#               await client.change_presence(game=discord.Game(name='SAYING '+word+" 100,000 TIMES."))
#               await client.send_message(client.get_channel('518709484634243082'), ("\n"+word)*times)
#               count+=1
#             await client.send_message(client.get_channel('518709484634243082'), "I said "+word+" 100,000 times") 
#             if count>=to100:
#               loop=True
#               await change_playing() 

# @client.event
# async def on_member_remove(member):
#     await client.send_message(client.get_channel('517765643114643457'),member.display_name+" wasn't a real mate so he left. HAHA WHAT A NOOB!!!")

    
# @client.event
# async def on_member_join(member):
#     if not member.bot:
#         await client.send_message(client.get_channel("517753134357938176"), "Hey {0.mention} what's your name?".format(member))
#         name = await client.wait_for_message(author = member)
#         role1 = get(name.server.roles, id='517751378802638904')
#         name = name.content
#         await client.send_message(client.get_channel("517753134357938176"), "Thanks MATE "+name.upper()) 
#         await client.add_roles(member, role1)
#         await client.change_nickname(member, "MATE "+name.upper())
    
# @client.event
# async def on_message_delete(message):
#         await client.send_message(client.get_channel("517753229258391567"), embed = discord.Embed(description ="Message sent by **"+str(message.author)+"** was deleted in **"+str(message.channel)+"**\n\n**"+message.content+"**", color = 0x2b44ff))
    

# @client.event
# async def change_playing():
#     global loop
#     while loop:
#       await client.change_presence(game=discord.Game(name='SUBSCRIBING TO PEWDIEPIE'))
#       await asyncio.sleep(10)
#       await client.change_presence(game=discord.Game(name='UNSUBSCRIBING FROM T-SERIES'))
#       await asyncio.sleep(10)
  
# # @client.event
# # async def on_message_edit(old, new):
# #     if new.author!=client.user:
# #         await on_message(new)
# #         await client.send_message(client.get_channel("517753229258391567"), embed = discord.Embed(description ="Message sent by **"+str(new.author)+"** in **"+str(new.channel)+"** was edited\n\nOld \n**"+str(old.content)+"**\n\nNew \n**"+str(new.content)+"**", color = 0x2b44ff))

# # async def should_mod(channelid):
# #     async for msg in client.logs_from(client.get_channel("538382600981446656"), limit=1):
# #         if msg.author == client.user:
# #             mod = eval(msg.content)
# #     return mod[channelid]
# # q = False
# # isitdone = False
# # @client.event
# # async def on_channel_create(channel):
# #     if channel.type != discord.ChannelType.private:
# #         async for msg in client.logs_from(client.get_channel("538382600981446656"), limit=1):
# #             if msg.author == client.user:
# #                 mod = eval(msg.content)
# #         global q
# #         global isitdone
# #         q = True
# #         await client.send_message(channel, "Should I mod this?")
# #         ans = await client.wait_for_message(author = await client.get_user_info("263685060819943425"))
# #         ans = ans.content
# #         ans = ans.lower()
# #         print(ans)
# #         if ans == "y" or ans == "yes":
# #             mod[channel.id] = True
# #             await client.send_message(client.get_channel("538382600981446656"), mod)
# #             await client.send_message(channel, "Ok I am gonna mod")
# #             while not isitdone:
# #                 q=True
# #             q = False
# #         elif ans == "n" or ans == 'no':
# #             mod[channel.id] = False
# #             await client.send_message(client.get_channel("538382600981446656"), mod)
# #             await client.send_message(channel, "Ok I am not gonna mod")
# #             while not isitdone:
# #                 q=True
# #             q = False
# #         else:
# #             await on_channel_create(channel)
    
    
# # @client.event
# # async def on_channel_delete(channel):
# #     if channel.type != discord.ChannelType.private:
# #         if message.channel.type != discord.ChannelType.private:
# #             async for msg in client.logs_from(client.get_channel("538382600981446656"), limit=1):
# #                 if msg.author == client.user:
# #                     mod = eval(msg.content)
# #             mod.pop(channel.id)
# #             await client.send_message(client.get_channel("538382600981446656"), mod)


# # @client.command(pass_context = True)
# # @commands.has_role("Owner")
# # async def mod(ctx, channel: discord.Channel = None):
# #     if ctx.message.channel.type != discord.ChannelType.private:
# #         async for msg in client.logs_from(client.get_channel("538382600981446656"), limit=1):
# #                 if msg.author == client.user:
# #                     mod = eval(msg.content)
# #         if not channel: channel = ctx.message.channel
# #         mod[channel.id] = True
# #         await client.say("Done")
# #         await client.send_message(client.get_channel("538382600981446656"), mod)


# # @client.command(pass_context = True)
# # @commands.has_role("Owner")
# # async def nomod(ctx, channel: discord.Channel = None):
# #     if ctx.message.channel.type != discord.ChannelType.private:
# #         async for msg in client.logs_from(client.get_channel("538382600981446656"), limit=1):
# #                 if msg.author == client.user:
# #                     mod = eval(msg.content)
# #         if not channel: channel = ctx.message.channel
# #         mod[channel.id] = False
# #         await client.say("Done")
# #         await client.send_message(client.get_channel("538382600981446656"), mod)

    
    
# # @client.command(pass_context = True)
# # @commands.has_role("Owner")
# # async def ismod(ctx, channel: discord.Channel = None):
# #     if ctx.message.channel.type != discord.ChannelType.private:
# #         async for msg in client.logs_from(client.get_channel("538382600981446656"), limit=1):
# #                 if msg.author == client.user:
# #                     mod = eval(msg.content)
# #         if not channel: channel = ctx.message.channel
# #         if mod[channel.id]:
# #             await client.say("Yes I moderate this channel")
# #         else:
# #             await client.say("No I don't moderate this channel")

    
        

# # @client.event
# # async def on_message(message):
# #     m = message.content
# #     m = m.lower()
# #     await client.process_commands(message)
# #     global q
# #     global isitdone
# #     isitdone = False
# #     urole = [y.name.lower() for y in message.author.roles]
# #     if message.author != client.user:
# #       if message.channel.type == discord.ChannelType.private:
# #         await client.send_message(message.channel, "Nah I don't like speaking in DMs")  
# #       elif message.content.startswith("+") and "owner" in urole:
# #         pass
# #       elif message.content=="+gap" or message.content=="+dislikes" or message.content == "+score" or message.content == "+leaderboard" or message.content == "+lb":
# #         pass
# #       elif await isEnglish(message.content):
# #         await client.delete_message(message)
# #         await client.send_message(message.channel, "That's not very nice you know. I only understand English")
      
# #       elif not await should_mod(message.channel.id):
# #         pass
# #       elif q:
# #             pass
# #       else:    
# #         if "mate" in m or "m8" in m or ":mate:" in m or message.attachments:
# #           if message.channel.id != '517780380049473563':
# #             mesg = "Thank you mate, very cool!!!"
# #             await client.send_message(message.channel, mesg)
# #           elif "mate" in urole:
# #             await client.send_message(message.channel, "You are cool mate don't worry")
          
# #           else:
# #               num = random.randint(1,3)
# #               if num == 1:
# #                 msg1="YOU CAN'T SAY THAT YOU LITTLE RAT!!!"
# #               elif num == 2:
# #                 msg1="DON'T EVEN THINK ABOUT IT!!!"  
# #               elif num == 3:
# #                 msg1="NO, NO AND NO!!!"
# #               await client.send_message(message.channel, msg1)
# #               await asyncio.sleep(0.5)
# #               await client.delete_message(message)    
# #         else:
# #           if message.channel.id != '517780380049473563':  
# #             mesg = "WTF {0.author.mention}???".format(message)
# #             await client.send_message(message.channel, mesg)
# #             if message.channel.id != "518086090436116491":
# #               await client.send_message(client.get_channel('517765643114643457'), "{0.author.mention}".format(message))
# #               role = get(message.server.roles, id='517774248010579969')
# #               await client.add_roles(message.author, role)
# #               await asyncio.sleep(0.5)
# #               await client.delete_message(message)
# #               role1 = get(message.server.roles, id='517751378802638904')
# #               await client.remove_roles(message.author, role1)
# #               if message.author.id != "263685060819943425":
# #                 await client.change_nickname(message.author, message.author.display_name.replace("MATE", "LOSER"))
# #               else: 
# #                 pass
# #               async for mesg in client.logs_from(client.get_channel("530336392455258142"), limit=1):
# #                 if mesg.author == client.user:
# #                     losers = mesg.content
# #                     losers = losers+","+message.author.id
# #                     await client.send_message(client.get_channel("530336392455258142"), losers)
# #           elif "mate" in urole:
# #             await client.send_message(message.channel, "You are cool mate don't worry")
# #           else:
# #             await client.send_message(message.channel, "YOU ARE A DISAPPOINTMENT FOR EVERYONE!!!")
#     isitdone = True


token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)
