import discord
import asyncio
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


client = discord.Client()
removeTagMSG = "You can do that by typing -cheer [TEAM] in the channel"


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
	if message.content.startswith('=test'):
		if(discord.utils.get(message.author.roles, name="Discord Mod")):
			await client.send_message(message.channel, 'Beep Beep Lettuce')
			await client.add_reaction(message, "\U0001F430")

	if message.content.startswith('=reactions'):
		if(discord.utils.get(message.author.roles, name="Discord Mod")):
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('=help'):
		msg = ('Currently avaible roles:'
			   '\nTSM, IMT, C9'
			   '\nG2, MSF, FNC'
			   '\nEDG, RNG, WE'
			   '\nLZ, SKT, SSG'
			   '\nFW, AHQ'
			   '\nGAM, FB')
		msg2 = 'Dont expect something special. This bot only exist for Worlds 2017'
		msg3 = ('Use +cheer [Team] to get your favorite team role'
				'\n'
				'\nUse -cheer [Team] to remove your favorite team role'
				'\n'
				'\nYou can have only 1 favorite team role. So remove them first if you want to switch teams')
		await client.send_message(message.author, msg)
		await client.send_message(message.author, msg2)
		await client.send_message(message.author, msg3)
		await client.add_reaction(message, "\u2753")

	if message.content.startswith('+cheer TSM'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[TSM]"
		role = discord.utils.get(message.server.roles, name="TSM")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer TSM'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="TSM")
		if(discord.utils.get(member.roles, name="TSM")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer IMT'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[IMT]"
		role = discord.utils.get(message.server.roles, name="IMT")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer IMT'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="IMT")
		if(discord.utils.get(member.roles, name="IMT")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer C9'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[C9]"
		role = discord.utils.get(message.server.roles, name="C9")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer C9'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="C9")
		if(discord.utils.get(member.roles, name="C9")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer G2'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[G2]"
		role = discord.utils.get(message.server.roles, name="G2")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer G2'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="G2")
		if(discord.utils.get(member.roles, name="G2")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer MSF'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[MSF]"
		role = discord.utils.get(message.server.roles, name="MSF")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer MSF'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="MSF")
		if(discord.utils.get(member.roles, name="MSF")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer FNC'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[FNC]"
		role = discord.utils.get(message.server.roles, name="FNC")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer FNC'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="FNC")
		if(discord.utils.get(member.roles, name="FNC")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer EDG'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[EDG]"
		role = discord.utils.get(message.server.roles, name="EDG")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer EDG'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="EDG")
		if(discord.utils.get(member.roles, name="EDG")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer RNG'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[RNG]"
		role = discord.utils.get(message.server.roles, name="RNG")
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer RNG'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="RNG")
		if(discord.utils.get(member.roles, name="RNG")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer WE'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[WE]"
		role = discord.utils.get(message.server.roles, name="WE")
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer WE'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="WE")
		if(discord.utils.get(member.roles, name="WE")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer LZ'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[LZ]"
		role = discord.utils.get(message.server.roles, name="LZ")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer LZ'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="LZ")
		if(discord.utils.get(member.roles, name="LZ")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer SKT'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[SKT]"
		role = discord.utils.get(message.server.roles, name="SKT")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer SKT'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="SKT")
		if(discord.utils.get(member.roles, name="SKT")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer SSG'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[SSG]"
		role = discord.utils.get(message.server.roles, name="SSG")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer SSG'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="SSG")
		if(discord.utils.get(member.roles, name="SSG")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer FW'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[FW]"
		role = discord.utils.get(message.server.roles, name="FW")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer FW'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="FW")
		if(discord.utils.get(member.roles, name="FW")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer AHQ'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[AHQ]"
		role = discord.utils.get(message.server.roles, name="AHQ")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer AHQ'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="AHQ")
		if(discord.utils.get(member.roles, name="AHQ")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer GAM'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[GAM]"
		role = discord.utils.get(message.server.roles, name="GAM")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.send_message(member, removeTagMSG)
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer GAM'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="GAM")
		if(discord.utils.get(member.roles, name="GAM")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('+cheer FB'):
		member = message.author
		memberName = message.author.display_name
		nameTag = "[FB]"
		role = discord.utils.get(message.server.roles, name="FB")
		roleCounter = None
		if(discord.utils.get(member.roles, name="TSM") or discord.utils.get(member.roles, name="IMT") or discord.utils.get(member.roles, name="C9") or discord.utils.get(member.roles, name="G2") or discord.utils.get(member.roles, name="MSF") or discord.utils.get(member.roles, name="FNC") or discord.utils.get(member.roles, name="EDG") or discord.utils.get(member.roles, name="RNG") or discord.utils.get(member.roles, name ="WE") or discord.utils.get(member.roles, name="LZ") or discord.utils.get(member.roles, name="SKT") or discord.utils.get(member.roles, name="SSG") or discord.utils.get(member.roles, name="FW") or discord.utils.get(member.roles, name="AHQ") or discord.utils.get(member.roles, name="GAM") or discord.utils.get(member.roles, name="FB")):
			roleCounter = 1
		if(roleCounter == 1):
			await client.send_message(message.author, 'Please delete your existing role first')
			await client.send_message(member, removeTagMSG)
			await client.add_reaction(message, "\U0001F1FD")
			await client.add_reaction(message, "\u2709")
		else:
			await client.add_roles(member, role)
			await client.change_nickname(member, nameTag + memberName)
			await client.add_reaction(message, "\u2611")

	if message.content.startswith('-cheer FB'):
		member = message.author
		role = discord.utils.get(message.server.roles, name="FB")
		if(discord.utils.get(member.roles, name="FB")):
			await client.remove_roles(member, role)
			await client.change_nickname(member, None)
			await client.add_reaction(message, "\u2611")

client.run('MzYzNDY5MDkxNjc3NDA1MTg2.DLFHtg.9UGE9s0u79ZhaUUclnYzZ_6DWYM')