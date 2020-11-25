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
    "Welcome, my dear. Alors comme ça vous aimez les jeux ? A votre âge ? \nNon, non, je ne ris pas dans ma barbe. D'ailleurs, sachez que ça s'appelle une moustache. \nMais nous nous égarons. Donc les jeux... Dites-moi, quel est le jeu que vous rêveriez d'écrire ?", 
    "Ah, encore une nouvelle tête ! Décidément, ça n'arrête pas ! \nDe vous à moi, je vois bien que vous êtes plutôt une personne gourmande. Et pourtant, je suis certain que vous avez un sombre secret culinaire... Racontez-moi tout : quelle est la recette de plat que vous avez inventée un jour et qui a été complètement ratée ?",
    "J'arrive ! J'arrive ! Non, mais vous croyez que je n'ai que ça à faire ? Comment ça, **oui ?** Si seulement j'avais un automate pour faire ce job à ma place.\nTiens, puisqu'on parle de ça, dites-moi, quelle invention technologique souhaiteriez-vous créer pour vous faciliter la vie au quotidien ?",
    "Parlons peu mais parlons bien. Il parait que dans le domaine de la créativité et du management, vous êtes une pointure ! Alors j'aimerais savoir : si vous aviez à créer quelque chose avec vos petits camarades, quelle technique pour stimuler la créativité de groupe inventeriez-vous ?",
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


@bot.command(name='W', help='Pour accueillir les nouvelles têtes')
async def welcome (ctx):
    welcome = ["Ceci est un message d'accueil de test, bande de chenapans !"]
    await ctx.send(response)

bot.run(TOKEN)