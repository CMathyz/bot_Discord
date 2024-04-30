import discord
from discord.ext import commands
import random


bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user.name} le bot est pret a l'emploi")

@bot.event   
async def on_message(message:discord.Message):
    if message.author.bot:
        return
    #on envoie une réaction si bonsoir est tapé dans le chat
    if "bonsoir" == message.content:
        await message.add_reaction("👌")

    #on bannie l'utilisateur si il utilise le mot ratio
    if "ratio" == message.content:
        await message.guild.ban(message.author, reason=f"Vous avez était bannis du serveur car vous avez prononcé le mot interdit: ratio")    
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    # fonction utilisé pour acceuillir comme il se doit l'utilisateur
    channel = member.guild.system_channel
    if channel:
        await channel.send(f"Bienvenue dans l'antre du monstre {member.mention} Grrrrr \nhttps://giphy.com/gifs/happy-dance-music-MGneiRkJcWphh4WubH")

@bot.command()
async def welcome(ctx):
    #quand on recois $welcome on envoie le message d'acceuil
    await ctx.send("Bienvenue dans l'antre du monstre Grrrrr \nhttps://giphy.com/gifs/happy-dance-music-MGneiRkJcWphh4WubH")

@bot.command()
async def ping(ctx):
    #quand on recois $ping on renvoie pong
    await ctx.send("pong :ping_pong:")

@bot.command()
async def blague(ctx):
    #quand on recois $blague on renvoie une blague aléatoire
    liste_blague= ["Que dit une noisette quand elle tombe dans l’eau ? \n Je me noix.","Comment est-ce que les abeilles communiquent entre elles ?\n Par -miel.","Quel est l’arbre préféré du chômeur ? \n Le bouleau.","Qu’est-ce qu’une frite enceinte ? \n Une patate sautée.","Que dit une mère à son fils geek quand le dîner est servi ? \n Alt Tab !","Quelle est la différence entre les bières et les chasseurs ?\nLes bières, on arrive à en faire des sans alcool.","Quel est le point commun entre un gynécologue myope et un chien en bonne santé ?\nIls ont tous les deux le nez mouillé.","Quelle est la partie de la voiture la plus dangereuse ?\nLa conductrice.","Pour un chasseur, qu’elle est la différence entre son chien et sa femme ?\nLe prix du collier.","Pourquoi les Ch’tis aiment les fins de vacances au camping ?\nParce que c’est le moment où ils peuvent démonter leur tente.","Qu’est-ce qui est pire qu’un bébé dans une poubelle ?\nUn bébé dans deux poubelles.","Pourquoi est-ce que les écologistes aiment les lépreux ?\nParce qu’ils sont biodégradables.","Les bonnes mamans te laissent lécher le batteur…\nLes meilleures mamans l’éteignent d’abord.","Quelle partie du légume ne passe pas dans le mixer ?\nLa chaise roulante.","Qu’est-ce qui est mieux que gagner une médaille d’or aux Jeux Paralympiques ?\nMarcher."]
    i = random.randint(0, len(liste_blague))
    await ctx.send(liste_blague[i])

@bot.command()
async def membre(ctx):
    #quand on recois $membre on renvoie touts les membres  du server avec leurs roles
    membres = ctx.guild.members
    listMembre = []
    for membre in membres:
        roles = [role.name for role in membre.roles]
        listMembre.append(f"{membre.display_name}  -  {' / '.join(roles)}")

    await ctx.send(f"Liste des membres :\n {' | '.join(listMembre)}")

@bot.command()
async def touché(ctx):
    #quand on recois $touché on renvoie coulé
    await ctx.send("coulé !")

@bot.command()
async def command(ctx):
    # commande permettant d'afficher toutes les commandes disponible
    embed = discord.Embed(title="Bot Commands", description="Liste des commandes du bot.", color=0x3B2077)
    embed.add_field(name="$membre", value="Liste les membres du serveur, rôle, nom.", inline=False)
    embed.add_field(name="$blague", value="Donne une blague aléatoire.", inline=False)
    embed.add_field(name="$welcome", value="Dit bienvenue", inline=False)
    embed.add_field(name="$ping", value="Répond pong", inline=False)
    embed.add_field(name="$touché", value="coulé ", inline=False)
    embed.add_field(name="bonsoir", value="répond avec une réaction sous le message", inline=False)
    embed.add_field(name="ratio", value="ban du serveur ", inline=False)
    await ctx.send(embed=embed)


if __name__ == "__main__":
    bot.run("replace TOKEN")