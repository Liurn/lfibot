import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('welcomeBotToken')
#c'est le token du bot
GUILD = 'La Fabrique Imaginaire'
#c'est le serveur sur lequel on se trouve (le mien)

bot = commands.Bot(command_prefix='!')

@bot.command(name='Q', help='Pour en savoir plus sur ta joueuse')
async def question(ctx):
    question = ["Bienvenue parmi nous ! Si vous pouviez juste ne pas oublier d'essuyer vos pieds en entrant la prochaine fois, ce serait **parfait**. Je n'ai pas que ça à faire de nettoyer derrière vous ! Oh, ce n'est pas une question... vous avez raison ! Hé bien qu'attendez-vous, tapez à nouveau **!Q** pour que je vous en pose une nouvelle. \nOn ne va pas y passer la journée !",
    "Quel est le jeu que tu rêves d'écrire ? Et puis santé au passage ! :beers:", 
    "Quelle est la recette de plat que tu as inventé un jour et qui a été complètement foireuse ?",
    "Quelle invention technologique souhaiterais-tu créer pour te faciliter la vie quotidienne ?",
    "quelle technique de créativité de groupe privilégierais-tu ?",
    "Félicitation ! Tu viens de créer un nouveau monde. Dis nous pourquoi celui-ci est parfait !",
    " Tu as adoré ce livre/film mais la fin t'as déçue, tu l'as réécrite dans ta tête, de quoi ça parle et qu'as tu changé ?",
    "T'es-tu déjà dit que le monde 'réel' n'existait qu'à travers ta perception? Quel serait selon toi le 'vrai' monde?",
    "avec quelles stars tu aimerais jouer au jeu de rôle sur table ?",
    "A qui as tu pompé l'idée de jeu dont tu es le/la plus fièr.e ?", 
    "Tu te prépares à une soirée-marathon création de personnage de 8h non-stop. Qu'est ce que tu apportes à manger / à boire pour tenir le coup?",
    "Sur un malentendu tu es investi d'un pouvoir divin, tu ne peux l'utiliser qu'une seule fois avant d'être découvert par les instances supérieures qui viendront te le retirer, qu'est ce que tu fais ?",
    "Tu traines tranquillement ta carapace dans le désert quand tout à coup tu bascules et finis bloquée sur le dos. Un humain arrive, te dis de piocher une carte et de répondre à la question inscrite dessus. Qu'est ce qui te fait dire que @/Matthieu Bé (il / he) est un replicant ?",
    "Choisis un pseudonyme dans la liste des membres qui t'évoque quelque chose et, en suivant cette inspiration, écris un court poème qui comportera une mention de ce pseudonyme."

    ]
    response = random.choice(question)
    await ctx.send(response)


bot.run(TOKEN)