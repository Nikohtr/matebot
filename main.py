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

loop = True

client = commands.Bot(command_prefix='+')
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    client.loop.create_task(change_playing())
    client.loop.create_task(sub())
    
@client.command(pass_context = True)
@commands.has_role('Owner')
async def esay(ctx, *, mg = None):
      await client.delete_message(ctx.message)

      if not mg: await client.say("Please specify a message to send")
      else:
        await client.send_message(ctx.message.channel, embed = discord.Embed(description = "["+mg+"](https://www.youtube.com/user/PewDiePie?sub_confirmation=1)", color = 0x2b44ff))

@client.command()
async def gap():
    key = os.getenv("KEY")
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="+key).read()
    subspew = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    data1 = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key="+key).read()
    subst = json.loads(data1)["items"][0]["statistics"]["subscriberCount"]
    gapis=int(subspew)-int(subst)
    await client.say("T-series is {:,d}".format(int(gapis))+" subs away from PewDiePie. PewDiePie has {:,d}".format(int(subspew))+" subscibers and T-series has {:,d}".format(int(subst))+" subscibers!")

@client.command()
async def dislikes():
    key = os.getenv("KEY")
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=YbJOTdZBX1g&key="+key).read()
    dis = json.loads(data)["items"][0]['statistics']['dislikeCount']
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=kffacxfA7G4&key="+key).read()
    dis1 = json.loads(data)["items"][0]['statistics']['dislikeCount']
    raz = int(dis)-int(dis1)
    await client.say("Youtube Rewind 2018 has {:,d}".format(int(dis))+" dislikes. That's {:,d}".format(int(raz))+" above Justin Bieber's Baby")

@client.command(pass_context = True)
@commands.has_role('Owner')
async def say(ctx, *, mg = None):
      await client.delete_message(ctx.message)

      if not mg: await client.say("Please specify a message to send")
      else: await client.say(mg)
        
@client.command(pass_context=True)
async def joined_at(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author

    await client.say('{0} joined at {0.joined_at}'.format(member))
        
@client.command(pass_context = True)
@commands.has_role("Owner")
async def ban(ctx, user: discord.Member = None):
    if user == None: await client.say("Tell me who to ban")
    else: 
        await client.ban(user, 7)
        await client.say("**Banned {0}**".format(user))
        
@client.command(pass_context = True)
@commands.has_role("Owner")
async def unban(ctx, user = None):
    if user == None: await client.say("Tell me who to unban")
    else: 
        try:
            user = await client.get_user_info(user)
            await client.unban(ctx.message.server, user)
            await client.say("**Unbanned {0}**".format(user))
        except discord.errors.NotFound:
            await client.say("I can't find that guy")
        
        
@client.command(pass_context = True)
@commands.has_role("Owner")
async def kick(ctx, user: discord.Member = None):
    if user == None: await client.say("Tell me who to kick")
    else: 
        await client.kick(user)
        await client.say("**Kicked {0}**".format(user))
        
        
@client.command(pass_context = True)
@commands.has_role("Owner")
async def clear(ctx, *, number = None):
    if not number or not number.isdigit(): await client.send_message(ctx.message.channel, "Tell me how many messages to delete")
    else:
        try:
            mgs = []
            number = int(number)+1
            if number>100:
                times = number//100
                for i in range(times):
                    async for x in client.logs_from(ctx.message.channel, limit = 100):
                        mgs.append(x)
                    await client.delete_messages(mgs)
                    mgs.clear()
                async for x in client.logs_from(ctx.message.channel, limit = number-(times*100)):
                    mgs.append(x)
                await client.delete_messages(mgs)
            else:
                async for x in client.logs_from(ctx.message.channel, limit = number):
                    mgs.append(x)
                await client.delete_messages(mgs)
            mgs.clear
        except discord.errors.HTTPException:
            await client.say("There was an error! Messages are most likely older than 14 days")
                
            

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return True
    else:
        return False
lp = True


@client.command(pass_context = True)
@commands.has_role('Owner')
async def color(ctx):
    global lp
    lp = True
    role = get(ctx.message.server.roles, id="517751310989131796")
    await client.send_message(ctx.message.channel, "**Started rainbow colored roles!**")
    while lp:
      r = lambda: random.randint(0,255)
      color = ('%02X%02X%02X' % (r(),r(),r()))
      await client.edit_role( ctx.message.server, role, color = discord.Colour(value = int(color, 16)))
      await asyncio.sleep(2)

def is_time_between(begin_time, end_time, check_time=None):
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:
        return check_time >= begin_time or check_time <= end_time
        
            
@client.event
async def sub():
    while True:
        key = os.getenv("KEY")
        data1 = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key="+key).read()
        subst = json.loads(data1)["items"][0]["statistics"]["subscriberCount"]
        data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="+key).read()
        subspew = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        subsnow = int(subspew)//100000
        async for message in client.logs_from(client.get_channel("532571319196188712"), limit=1):
                if message.author == client.user:
                    subsbefore = int(message.content)
        if is_time_between(time(19,0,0), time(19,0,1)):
            data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key="+key).read()
            subspew = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
            async for message in client.logs_from(client.get_channel("529692628518830091"), limit=1):
                if message.author == client.user:
                    su = message.content
            await client.send_message(client.get_channel("529692628518830091"), subspew)
            await client.send_message(client.get_channel("528874952342896640"), "@everyone PewDiePie got {:,d} subscribers today".format(int(subspew)-int(su)))
            async for message in client.logs_from(client.get_channel("530336392455258142"), limit=1):
                if message.author == client.user:
                    loser = message.content
                    loser = loser.split(",")
                    print(loser)
            for item in loser:
                try:
                    print(item)
                    await client.send_message(await client.get_user_info(item) , "Just a friendly reminder that no one likes you and you are a disappointment for your parents")
                except discord.Forbidden:
                    print(item+" blocked me")
                    await client.send_message(client.get_channel("517780380049473563") , "<@"+item+"> You think blocking me can save you. Pathetic. Just a friendly reminder that no one likes you and you are a disappointment for your parents")
        elif is_time_between(time(15,0,0), time(15,0,1)):
            await client.send_message(await client.get_user_info('418380611233775626') , "Hey Berk I am just here to remind you that you are worth nothing and no one likes you becuase you are a noob. No one has ever liked you and no one will. You will die alone in some miserable house!")
        elif subsnow>subsbefore:
            print(subspew)
            await client.send_message(client.get_channel("532571319196188712"), subsnow)
            await client.send_message(client.get_channel("528874952342896640"), "@everyone PewDiePie just hit {:,d}".format(subsnow*100000))
        elif int(subst)>int(subspew):
            await client.send_message(client.get_channel("528874952342896640"), "@everyone If you are reading this then it's too late. The worst thing has happened. PewDiePie our lord and savior has been passed and yes I am crying I am not gonna lie. It was a good fight solders. All of you have earned my respect. He is still number one in our hearts. He was passed at {:,d}".format(int(subspew))+" and the time was "+str(datetime.time)+" \nSAD by xxxtentacion ")
        await asyncio.sleep(1)

@client.command(pass_context = True)
@commands.has_role('Owner')
async def stopcolor(ctx):
    global lp
    lp = False
    await client.send_message(ctx.message.channel, "**Stoped rainbow colored roles!**")
      
@client.command(pass_context = True)
@commands.has_role('Owner')
async def word(ctx, *, word=None):
      global loop
      await client.send_message(ctx.message.channel, "Saying "+word+" 100,000 times")
      await client.delete_message(ctx.message)
      times = 2000//(len(word)+2)
      to100 = 100000//times
      count = 0
      if not word: await client.say("Please specify a word to say 100,000 times")
      else: 
        while count<=to100:
          loop = False
          await client.change_presence(game=discord.Game(name='SAYING '+word+" 100,000 TIMES."))
          await client.send_message(client.get_channel('518709484634243082'), ("\n"+word)*times)
          count+=1
        await client.send_message(client.get_channel('518709484634243082'), "I said "+word+" 100,000 times") 
        if count>=to100:
          loop=True
          await change_playing() 

@client.event
async def on_member_remove(member):
    await client.send_message(client.get_channel('517765643114643457'),member.display_name+" wasn't a real mate so he left. HAHA WHAT A NOOB!!!")

@client.event
async def change_playing():
    global loop
    while loop:
      await client.change_presence(game=discord.Game(name='SUBSCRIBING TO PEWDIEPIE'))
      await asyncio.sleep(10)
      await client.change_presence(game=discord.Game(name='UNSUBSCRIBING FROM T-SERIES'))
      await asyncio.sleep(10)
  
@client.event
async def on_message_edit(old, new):
    await on_message(new)

@client.event
async def on_message(message):
    m = message.content
    m = m.lower()
    await client.process_commands(message)
    if message.author != client.user:
      if (message.content.startswith("+") or message.content.startswith("?")) and message.author.id == "263685060819943425":
        pass
      elif message.content=="+gap" or message.content=="+dislikes" or message.content == "+joined_at":
        pass
      elif isEnglish(message.content):
        await client.delete_message(message)
        await client.send_message(message.channel, "That's not very nice you know. I only understand English")
      elif message.channel.type == discord.ChannelType.private:
        await client.send_message(message.channel, "Nah I don't like speaking in DMs")
      else:    
        if "mate" in m or "m8" in m or ":mate:" in m or message.attachments:
          if message.channel.id != '517780380049473563':
            mesg = "Thank you mate, very cool!!!"
            await client.send_message(message.channel, mesg)
          elif message.author.id == "263685060819943425":
            await client.send_message(message.channel, "You are cool mate don't worrry")
          
          else:
              num = random.randint(1,3)
              if num == 1:
                msg1="YOU CAN'T SAY THAT YOU LITTLE RAT!!!"
              elif num == 2:
                msg1="DON'T EVEN THINK ABOUT IT!!!"  
              elif num == 3:
                msg1="NO, NO AND NO!!!"
              await client.send_message(message.channel, msg1)
              await asyncio.sleep(0.5)
              await client.delete_message(message)    
        else:
          if message.channel.id != '517780380049473563':  
            mesg = "WTF {0.author.mention}???".format(message)
            await client.send_message(message.channel, mesg)
            if message.channel.id != "518086090436116491":
              await client.send_message(client.get_channel('517765643114643457'), "{0.author.mention}".format(message))
              role = get(message.server.roles, id='517774248010579969')
              await client.add_roles(message.author, role)
              await asyncio.sleep(0.5)
              await client.delete_message(message)
              role1 = get(message.server.roles, id='517751378802638904')
              await client.remove_roles(message.author, role1)
              if message.author.id != "263685060819943425":
                await client.change_nickname(message.author, message.author.display_name.replace("MATE", "LOSER"))
              else: 
                pass
              async for mesg in client.logs_from(client.get_channel("530336392455258142"), limit=1):
                if mesg.author == client.user:
                    losers = mesg.content
                    losers = losers+","+message.author.id
                    await client.send_message(client.get_channel("530336392455258142"), losers)
          elif message.author.id == "263685060819943425":
            await client.send_message(message.channel, "You are cool mate don't worry")
          else:
            await client.send_message(message.channel, "YOU ARE A DISAPPOINTMENT FOR EVERYONE!!!")    


token = os.getenv("DISCORD_BOT_SECRET")
client.run(token)
