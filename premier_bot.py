# importation du fonctionement correct du programme
import itertools
import random
import discord
import asyncio
from discord.ext import commands
r = True
# définition du prefix du bot et de sa description
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', description= "Le bot Hyperxko est un Bot multi-tâches français", help_command=None, intents=intents)
# créé un event qui fais que quand le bot est en ligne faire un print de "Ready !" dans la console
# le nom "on_ready" pour la fonction est obligatoire
@bot.event
async def on_ready():
    print("Ready !")
@bot.command()
async def help(ctx):
    embed = discord.Embed(title = "**Liste des commandes**", description = "flemme de la faire pour l'instant", url="https://www.youtube.com/channel/UC63cDEWkTlQ1PhqenmF0WGQ")
    # met une photo à l'embed
    embed.set_thumbnail(url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Femoji.gg%2Fassets%2Femoji%2F5061_the_rules.png&f=1&nofb=1")
    embed.add_field(name = "Listes des commandes du bot hyperxko",value=None, inline=True)
    # envoie le message de l'embed
    await ctx.send(embed = embed)
# créé une commande : serverInfo

@bot.command()
async def serverInfo(ctx):
    # récuperer ctx.guild dans une commande server
    server = ctx.guild
    # compter le nombre de channels textuel
    number_of_text_channel = len(server.text_channels)
    # compter le nombre de channels vocal
    number_of_voice_channel = len(server.voice_channels)
    # récuperer la description du serveur (none si il n'y en a pas)
    server_description = server.description
    # compte le nombre de membres qu'à le serveur
    number_member = server.member_count
    # récupere le nom du serveur
    server_name = server.name
    # créé le message avec toutes les infos
    message = f"Le serveur **{server_name}** contient {number_member} *membres*, il a {number_of_text_channel} channels textuel, et  {number_of_voice_channel} channels vocaux et sa description est : {server_description}"
    # envoyer le message
    await ctx.send(message)

@bot.command()
# définir le nom de la commande : say et mettre les paramètres
async def say(ctx, number, * texte):
    # l'afficher en texte dans la console
    print('  '.join(texte))
    # supprimer le message de la commande
    await ctx.message.delete() 
    # faire une boucle for du nombre de fois que l'utilisateur veut envoyer le msg
    for i in range (int(number)):
        # envoie le msg selon le nombre qu'à mit l'utilisateur
        msg_say = await ctx.send(' '.join(texte))
@bot.command()
# définir le nom de la commande : chinese et mettre les paramètres
async def chinese(ctx, * texte):
    # mettre tous les characères
    chinese_char = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
    # définir une liste
    chinese_text =  []
    # créé une boucle for qui va prendre le paramètre texte que l'utilisateur aura mit
    for word in texte:
        # créé une autre boucle for qui va parcourir les characères
        for char in word:
            # vérifie si dans les charactère il a des lettres de l'alphabet
            if char.isalpha():
                # utilise la table ascii pour transformer les charatère normeaux en chinois
                index = ord(char) - ord("a")
                # créé une variable transformed
                transformed = chinese_char[index]
                # ajoute dans chinese_text le contenant de la variable transformed
                chinese_text.append(transformed)
                # sinon si il n'y a pas de charactères dans if char alors :
            else:
                # ajouter à chinese_text le contenu de char
                chinese_text.append(char)
                # ajouter un espace a chinese_text
        chinese_text.append(" ")
        # envoyer le message final 
    await ctx.send("".join(chinese_text))
@bot.command()
# définir le nom de la commande : kick et mettre les paramètres
async def kick(ctx, user : discord.User, * reason):
    # met en texte et non en liste le paramètre reason
    reason = " ".join(reason)
    # kick l'utilisateur mentionner
    await ctx.guild.kick(user, reason = reason)
    # envoie un message de confirmation du kick
    await ctx.send(f"{user}, a été kick pour la raison suivante :  {reason}")
@bot.command()
@commands.has_permissions(manage_messages = True)
# définir le nom de la commande : clear et mettre les paramètres
async def clear(ctx, nombre : int):
    # regarde l'historique des messages envoyé et ajoute 1 a cause du !clear
    messages_history = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages_history:
        # supprime le nombre de messages demandé par l'utilisateur
        await message.delete()
@bot.command()
@commands.has_permissions(ban_members = True)
# définir le nom de la commande : unban et mettre les paramètres
async def unban(ctx, user):
    # séparé le discriminatoire du pseudo
    userName, userId = user.split("#")
    # parcour une liste des gens banni
    banned_user = await ctx.guild.bans()
    # créé une boucle for dans banned_user
    for i in banned_user:
        # vérifie si l'utilisateur est banni
        if i.user.name == userName and i.user.discriminator == userId:
            # unban l'utilisateur
            await ctx.guild.unban(i.user)
            # envoie un msg de confirmation du unban
            await ctx.send(f"L'utilisateur {user} a bien unban !")
            return
            # si l'utilisateur n'est pas trouvé envoyer un message d'erreur
    await ctx.send(f"désolé mais l'utilisateur {user} n'est pas banni !")
@bot.command()
@commands.has_permissions(ban_members = True)
# définir le nom de la commande : ban et mettre les paramètres
async def ban(ctx, user : discord.User, *, reason):
    # mettre a espace a la raison
    reason = " ".join(reason)
    # ban l'utilisateur mentionné
    await ctx.guild.ban(user, reason = reason)
    # créé le titre et la description de l'embed
    embed = discord.Embed(title = "**Banissement**", description = "Un modérateur à banni un membre", url="https://www.youtube.com/channel/UC63cDEWkTlQ1PhqenmF0WGQ")
    # met une photo à l'embed
    embed.set_thumbnail(url = "https://emoji.discord.st/emojis/f8a71635-4645-4522-a655-cbe998556907.png?filename=chika_ban.png")
    embed.add_field(name = "Le membre",value = user.name + "à été banni", inline=True)
    embed.add_field(name = "Raison : ", value = reason, inline=True)
    # envoie le message de l'embed
    await ctx.send(embed = embed)
@bot.command()
# commande brut-force.
async def CrgfrGTGEFDGFrgDSG3674TJYU6YGDZFEffrgttefdi6515667(ctx):
    for combi in range (0, 10000):
        n = "0123456789"
        combinaisons = ["".join(i) for i in itertools.permutations(n, 4)]
        combinaisonChoisie = random.choice(combinaisons)
        subit_messag_brut_force = await ctx.send(combinaisonChoisie)
    print("la commande c'est fini !")
@bot.command()
async def dm(ctx, member: discord.Member,*, content):
    print("un message privé a été  envoyé voici le contenu :", content)
    channel = await member.create_dm()
    await channel.send(content)

@bot.command()
async def cuisiner(ctx):
	await ctx.send("Envoyez le plat que vous voulez cuisiner")

	def checkMessage(message):
		return message.author == ctx.message.author and ctx.message.channel == message.channel

	try:
		recette = await bot.wait_for("message", timeout = 12, check = checkMessage)
	except:
		await ctx.send("Commande annulé timeout dépasser.")
		return
	message = await ctx.send(f"La préparation de {recette.content} va commencer. Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
	await message.add_reaction("✅")
	await message.add_reaction("❌")


	def checkEmoji(reaction, user):
		return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")

	try:
		reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = checkEmoji)
		if reaction.emoji == "✅":
			await ctx.send("La recette a démarré.")
		else:
			await ctx.send("La recette a bien été annulé.")
	except:
		await ctx.send("La recette a bien été annulé.")
def IsOwner(ctx):
    return ctx.message.author.id == 683707116996788254
@bot.command()
@commands.check(IsOwner)
async def private(ctx):
    await ctx.send("Cette commande peut être éffectuer seulement par le propriétaire du bot !")

async def CreateMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted", permissions = discord.Permissions(send_messages = False, speak = False), reason = "création du rôle Muted")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak= False)
        return mutedRole
async def GetMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    return await CreateMutedRole(ctx)       
@bot.command()
@commands.has_permissions(ban_members = True)
async def mute(ctx, member : discord.Member, * , reason = "Aucune raison assigner"):
    mutedRole = await GetMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} à été mute !")
#run le bot


@bot.command(pass_context=True)
async def ticket(ctx):
    guild = ctx.guild
    embed = discord.Embed(
        title = 'Ticket system',
        description = 'Réagis 📩 pour créé un ticket.'
    )

    embed.set_footer(text="ticket system")

    msg = await ctx.send(embed=embed)
    await msg.add_reaction("📩")

    def check(reaction, user):
        return str(reaction) == '📩' and ctx.author == user

    await bot.wait_for("reaction_add", check=check)
    await guild.create_text_channel(name=f'ticket - {ctx.message.author.name}')

ban_list = []
day_list = []
server_list = []

#This is a background process
async def countdown(ctx):
    await bot.wait_until_ready()
    while not bot.is_closed:
        await asyncio.sleep(1)
        day_list[:] = [x - 1 for x in day_list]
        for day in day_list:
            if day <= 0:
                try:
                    await ctx.unban(server_list[day_list.index(day)], ban_list[day_list.index(day)])
                except:
                    print('Error! User already unbanned!')
                del ban_list[day_list.index(day)]
                del server_list[day_list.index(day)]
                del day_list[day_list.index(day)]
               
#Command starts here
@bot.command(pass_context = True)
@commands.has_permissions(ban_members = True)
async def tempban(ctx,member:discord.Member, days = 1):
        await ctx.guild.ban(member, delete_message_days=0)
        await ctx.send('Membre banni pour **' + str(days) + ' jour(s)**')
        ban_list.append(member)
        day_list.append(days * 24 * 60 * 60)
bot.run("")