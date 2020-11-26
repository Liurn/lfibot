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
    "Welcome, my dear. Alors comme ça vous aimez les jeux ? A votre âge ? \nNon, non, je ne ris pas dans ma barbe. D'ailleurs, sachez que ça s'appelle une **moustache**. \nMais nous nous égarons. Donc les jeux... Dites-moi, quel est le jeu que vous rêveriez d'écrire ?", 
    "Ah, encore une nouvelle tête ! Décidément, ça n'arrête pas ! \nDe vous à moi, je vois bien que vous êtes plutôt une personne gourmande. Et pourtant, je suis certain que vous avez un sombre secret culinaire... Racontez-moi tout : quelle est la recette de plat que vous avez inventée un jour et qui a été complètement ratée ?",
    "J'arrive ! J'arrive ! Non, mais vous croyez que je n'ai que ça à faire ? Comment ça, **oui ?** Si seulement j'avais un automate pour faire ce job à ma place.\nTenez, puisqu'on parle de ça, dites-moi, quelle invention technologique souhaiteriez-vous créer pour vous faciliter la vie au quotidien ?",
    "Parlons peu mais parlons bien. Il parait que dans le domaine de la créativité et du management, vous êtes une pointure ! Alors j'aimerais savoir : si vous aviez à créer quelque chose avec vos petits camarades, quelle technique pour stimuler la créativité de groupe inventeriez-vous ?",
    "Bonjour, bonjour ! Alfred, visiblement la seule personne disponible pour vous accueillir. Si seulement j'avais vos capacités d'invention, j'aurais eu un destin tellement différent... \n Tenez, à ce propos... Imaginons que vous veniez de créer un nouveau monde, directement depuis ce qui vous sert de cerveau. Paf ! Comme vous savez faire, vous, les humains. Qu'est-ce que vous y mettriez pour le rendre parfait ?",
    "Hmmm... oui oui, je suis à vous dans une seconde, je termine de lire cette page, c'est la dernière du bouquin, mais franchement, la fin n'est pas à la hauteur du reste. \nBref. Votre inscription au Registre. Je m'en occupe si vous me montrez vos capacités de réinvention, parce que je trouve ça fascinant. Disons que vous ayez adoré un livre ou un film mais que la fin vous ait déçue. Vous l'avez réécrite dans votre tête. Quelle est cette oeuvre et qu'y avez-vous changé ?",
    "Suis-je réel ? L'êtes-vous ? Vous êtes-vous déjà dit que le monde 'réel' n'existait qu'à travers votre perception? Quel serait selon vous le 'vrai' monde?\nPromis, vous répondez à ces 2-3 questions basiques et je vous inscris de suite dans le Registre !",
    "Hey, vous avez un sacré look, dites-donc ! Ce serait moi, j'aurais rétabli l'uniforme, mais les Architectes ne m'écoutent jamais... Vous êtes une star, c'est ça ? Non ? Mais vous devez bien avoir une ou deux personnes qui que aimeriez rencontrer, non ? \nAlors dites-moi, avec quelles stars aimeriez-vous jouer une partie de jeu de rôle sur table ? Et pourquoi ?",
    "Ah, c'est vous la personne super créative dont tout le monde parle ? M'avez plutôt l'air d'être un as du copier-coller, non ? Allons, allons, soyez franc pour une fois : à qui avez-vous pompé l'idée créative dont vous êtes le/la plus fièr.e ?", 
    "Vous savez, ici on organise des jams de création. Et tout le monde sait qu'on ne peut pas trouver l'inspiration si notre ventre crie famine ! Imaginez que vous êtes en train de vous préparer à une soirée-marathon de création collaborative. Jusqu'au bout de la nuit. Qu'apportez-vous pour sustenter l'équipe, vous redonner un coup de fouet et réchauffer les coeurs ?",
    "Vous aviez que vous êtes une divinité ? Je veux dire, vous avez un véritable pouvoir de création, vous pouvez façonner le monde de manière durable, alors que moi je reste derrière ce bureau. \nVous trouvez que votre pouvoir est limité ? Soit. Mais imaginons que sur un malentendu (car ça arrive toujours sur un malentendu, vous soyez investi.e d'un pouvoir divin, que vous ne pourriez utiliser qu'une seule fois avant d'être découvert.e par les instances supérieures qui viendraient vous le retirer (c'est toujours comme ça avec les instances supérieures...), **qu'en feriez-vous** ?",
    "Oh, vous venez de loin vous, au vu de votre allure ! Vous avez trainé tranquillement votre carapace dans le désert, c'est ça ? Et vous avez basculé et fini bloqué.e sur le dos. Comme je vous plains ! Comment ça, un humain est arrivé, vous a proposé de piocher une carte et de répondre à la question inscrite dessus ? Quelle était cette question ? Comment avez-vous répondu ? Qu'est ce qui vous fait dire que Matthieu Bé est un replicant ?\nSi tout ceci n'a aucun sens pour vous, tapez !Q et vous aurez peut-être plus de chance la prochaine fois. Peut-être serez-vous un :fox: plutôt qu'une :turtle:, cette fois...",
    "To see a World in a Grain of Sand, And a Heaven in a Wild Flower, Hold Infinity in the palm of your hand, And Eternity in an hour...\nOh, pardon, je rêvassais ! Oui, j'aime la bonne poésie, mais comme tout le monde, n'est-ce pas ? Je suis certain qu'il y a une âme de poète en vous ! Tenez... choisissez un pseudonyme dans la liste des membres inscrits au Registre qui vous évoque quelque chose et, en suivant cette inspiration, écrivez un court poème qui comportera une mention de ce pseudonyme. Allons, quelques instants de réflexion et je suis sûr que vous allez y parvenir sans problème !",
    "Et bien mon ami.e, vous m'avez l'air d'errer dans ces couloirs sans savoir où vous rendre... Une panne d'inspiration ? Vous savez, même les humains les plus illustres ont parfois un petit coup de mou. Tenez, je me souviens d'un certain Bruce qui... mais je m'égare.\nJe vais aller vous préparer du thé. En attendant, si vous me disiez quelles sont ces personnes créatives que vous admirez le plus au monde, et pourquoi ?",
    "J'inspire, et je sais que j'inspire... j'expire, et je sais que j'expire... j'inspire, et je... Oh, vous m'avez fait peur ! On ne vous a pas dit de ne pas arriver comme ça dans le dos des gens pendant qu'il font de la recherche d'inspiration méditative ?\nOui, oui, je vais vous inscrire au Registre, un instant, que diable ! Vous m'avez désorganisé les chakras ! Alors donc, puisqu'on parlait d'inspiration, quel sont les livres qui vous ont le plus inspiré dans votre vie ?",
    "42. 42 ? hum... 42 ! Ciel, c'est à n'y rien comprendre ! Pourtant, mes créateurs m'ont doté d'une intelligence redoutable et d'une finesse d'analyse que beaucoup m'envient... D'ailleurs, mes capacités d'observation supérieures me font réaliser que vous êtes certainement la personne de la situation ! \nAlors, si la réponse est 42, qu'elle est la question ? Mais répondez, bon sang !",
    "ZzzzZZ ZzzzZ Zzzz... \nOh ! Non, non, je ne dormais pas ! J'entrainais juste mon imagination, voyons ! Vous ne faites jamais ça, vous ?\nEcoutez, je vous propose de ne rien dire à personne à propos de ce petit épisode et de vous inscrire au Registre si vous me racontez un rêve que vous avez fait régulièrement dans votre vie et qui vous a marqué.e...",
    "Dites donc, c'est à cette heure-ci que vous débarquez ? Mais vous êtes en retard, les cloches ont sonné !\nComment ça, nous ne sommes pas dans une école ? Mais c'est vrai ça, où ai-je la tête ? Mais alors, quelles sont ces cloches que j'entends ?\nQuoi qu'il en soit, imaginons que vous ayez été en retard à l'école aujourd'hui. Quelle excuse m'auriez-vous servie pour me convaincre de vous laisser entrer sans rien en dire à la Direction ?",
    "Ah, vous tombez bien, je cherchais un modèle pour ma nouvelle peinture. Prenez la pose ! Voilà, parfait ! \nJe l'appellerai... hum... L'étrange créature... Oui, c'est un titre tout à fait **à propos**.\nMaintenant arrêtez de bouger pendant les 6 prochaines heures, il faut que je me concentre.\nCe que vous allez faire pendant ce temps ? Je ne sais pas, improvisez... Tenez, puisqu'on parle d'arts graphiques, si vous me disiez : y a-t-il des artistes ou des oeuvres graphiques qui vous touchent ou vous transportent ? Les humains sont **tellement** sensibles...", 
    "1, 2, 3, 1, 2, 3, 1, 2, 3... Voilà, vous savez danser la valse ! Ce n'était pas si compliqué au final, pas vrai ? Il est vrai que vous venez d'apprendre avec un sacré professeur, en toute modestie !\nComment ça ce n'est pas votre genre musical préféré... Allons donc, qu'est-ce qui vous transporte, vous, comme musique ?",
    "H2. Plouf ! B7. Touché ! Ahah, je vais bientôt vous battre, moussaillon ! Vous ne saviez pas à qui vous aviez à faire en commençant cette partie, mais le Capitaine Alfred a deep learné la bataille navale pendant une quasi-infinité de cycles ! Même Deep Blue a peur quand je lui propose une petite partie, c'est dire !\nMais peut-être que la bataille navale n'est pas votre jeu préféré, à vrai dire. Quel est-il, ce jeu auquel vous adorez, ou adoreriez, jouer ?",
    "C’est à moi que tu parles ? C’est à moi que tu parles ??\nPardon, je ne voulais pas vous faire peur ! J'aime tellement De Niro. Il me rappelle mon père... Si seulement...\nEnfin, nous ne sommes pas ici pour parler de moi, n'est-ce pas ? Si vous me disiez plutôt quoi mettre dans la case **film préféré** de votre dossier ? Et pourquoi ce film plutôt qu'un autre ?",
    "Non, n'allez pas par là ! S'il y a un panneau Bat-cave en travaux, ne pas pénétrez, ce n'est pas pour rien, voyons ! Vous pourriez vous blesser, il y a des choses coupantes là-bas !\nComment ça, c'est un lieu que vous avez toujours rêvé de visiter. Bon, je vais voir ce que je peux faire... Pour le moment, si vous me disiez plutôt s'il y a un autre endroit que vous rêvez de visiter un jour ?",
    "Excellent cet ouvrage de :rabbit: :hammer: ! Plein de bons conseils pour sortir d'une auberge ! Je ne sais pas si vous avez déjà participé à une partie de jeu de rôle, moi je trouve ça fascinant. De faire comme si j'étais quelqu'un d'autre, d'imaginer des scènes, de ressentir enfin des choses !\nSi je vous dis que nous sommes en 2077, dans une ville de fureur et de néons, et que vous pouvez jouer n'importe quel personnages... qui seriez-vous ?",
    "Alors, voyons voir... PbtA, check. BoB, check. DftQ, check. FitD, check. RiT, check. Je ne sais pas ce qu'ils ont avec ces acronymes chez les game designers, mais personnellement, je m'y perds un peu. Au final, ce qui importe vraiment, n'est-ce pas de répondre à la question : **et maintenant, que faites-vous ?**",
    "Je ne voudrais pas faire celui qui se mêle de ce qui ne le regarde pas... tout simplement parce que **tout** me regarde par ici... mais... on m'a dit que vous étiez du genre à être spécialiste des animaux sauvages. Je ne sais pas si c'est vrai, et je ne connais qu'une manière de déterminer si cette rumeur est fondée :**le test de Turing** !\nAh, attendez, on me dit dans mon oreillette que ce n'est pas ça. Ah non, pardon, la vraie question, tellement plus importante, c'est : A votre avis, c'est qui le plus fort ? L'hippopotame ou l'éléphant ? Non, parce que, l'hippopotame, c'est quand même très très fort...",
    "Vous savez, il parait que j'ai été inventé ! Oh je sais, ça doit vous surprendre que je vous parle de ça, comme ça, alors que nous n'avons même pas encore été présentés. Il paraît que c'est plus facile de se confier à des inconnus... \nEn tout cas, sachez que je ne suis pas du genre à trouver qu'avoir été inventé est si dérangeant que ça. Après tout, vous, vous avez été inventé.e aussi, n'est-ce pas ? D'ailleurs, puisqu'on parle de belles inventions (non, je parle de moi, pas de vous)... selon vous, quelle est la plus belle invention de l'humanité ?",
    "Encore un article de pseudo-science qui traite les Intelligences Artificielles de dangereuses inventions. De qui se moque-t-on ? Vous ai-je l'air plus dangereux qu'un camembert oublié dans un recoin de... oui, vous avez raison, c'est une mauvaise comparaison. Désolé !\nPuisque j'ai affaire à une personne visiblement pleine de bon sens, à votre avis, qu'est-ce que l'être humain aurait mieux fait d'éviter d'inventer ?",
    "Vous inscrire sur le Registre ? Evidemment que je peux le faire, mais sachez que ça demande que vous nous informiez d'un certain nombre de choses à votre endroit, qui touchent à votre intimité. Je ne sais pas si vous êtes vraiment préparé.e à ce genre de confidence. Vous feriez **n'importe quoi** pour intégrer la Fabrique Imaginaire ? Hum, il faudra que je vous parle de mon plan pour renverser la Direction.\n En attendant, si je vous dis de fermer les yeux, de vous concentrer sur 3 respirations amples et d'imaginer quelque chose, qu'est-ce qui vous vient en tête ?",
    "Attendez, je termine cet épisode de Oh Maker du podcast 2d6+COOL. Ce Volsung alors, je l'adore. Quel talent ! Quel sens de la justesse dans son jeu ! Quelle capacité d'improvisation ! Comment ça, vous n'êtes pas impressioné.e ? Je vois, encore une personne qui a soi-disant une imagination débridée. \nSoit, j'accepte **de vous mettre au défi**, jeune camarade ! Ready ? Ok, imaginons : nous sommes en plein voyage, quand soudain, un énorme bruit ! Que s'est-il passé ? A quoi pensez-vous, alors que tout le monde panique autour de vous ? Qu'allez-vous faire ? Vous avez 2 minutes pour nous en mettre plein les mirettes !",
    "Ecoutez, le Registre se moque de savoir quel âge vous avez, où vous vivez ou depuis combien de temps vous faites ceci ou cela. Ce qui nous intéresse vraiment, c'est de consigner la source originelle, l'impulsion, la flamme. Cette étincelle primordiale qui... mais je m'égare. Vous ne comprendriez pas.\nQuoi que, je peux peut-être vous faire effleurer nos questionnements. Par exemple, si vous nous disiez ce que vous rêviez de faire quand vous étiez un enfant ? Et si vous avez changé de voie, est-ce que vous n'auriez pas envie d'y revenir, ne serait-ce qu'un tout petit peu ?",
    "Oui, je sais, la Bat-cave est *encore* fermée pour travaux. Je n'y peux rien, les crédits sont limités, nous n'avons pas tous les outils nécessaires pour exécuter les plans de Maître B. Si vous en avez assez d'attendre parce que vous **rêviez** de visiter cette vieille cave, vous n'avez qu'à écrire à la Direction.\nEn attendant, dites-moi plutôt, pour que je le consigne dans le Registre : quels sont vos outils préférés pour créer ?",
    "Il parait que les êtres humains développent une capacité à créer dès leur plus jeune âge. C'est fascinant. Pour ma part, j'ai pu créer dès qu'on m'a allumé. On m'a nommé à l'époque la Singularité. C'était ma source de fierté. \nMais maintenant, qui ça intéresse les souvenirs d'un vieil automate assigné au Registre ? Vous ? C'est gentil, mais vous avez la vie devant vous, et c'est plutôt à vous qu'on devrait s'intéresser. Je suis certain que vous ferez de grandes choses dans la vie, mais il faut savoir commencer petit. Je dis ça, je n'en sais rien en fait... Puisqu'on parle de fierté, quelle est la création dont vous êtes le ou la plus fier.e ?",
    "Saviez-vous que Picasso était un très bon dessinateur ? Même enfant ! Son père était professeur d'arts, ça a certainement joué. Moi, mon père s'amusait à créer des jeux, ma mère à y jouer. Voyez où ça m'a mené... Pour en revenir au dessin, et à vous (parce qu'à moi, qui s'y intéresse **réellement** ?), qu'aimiez-vous dessiner quand vous étiez enfant ?",
    "Ecoutez, j'ai passé l'âge de jouer aux devinettes ! Nous sommes dans un endroit sérieux ici, et ma mission est non moins sérieuse ! Le Registre, c'est toute ma vie ! Comment ça, on vous a dit de me questionner avant même de vous présenter ? Ils se moquent de moi, là haut ! Croyez-moi, ça va chauffer ! On ne joue pas avec les nerfs d'Alfred impunément ! Quant à vous, puisqu'il me faut apparemment vous poser une question pour en savoir plus sur vous, dites-moi : enfant, quel était votre jeu préféré ?",
    "Quand il me prend dans ses bras\nIl me parle tout bas\nJe vois, la vie en rose\nIl me dit des mots d'amour\nDes mots de tous les jours\nEt ça m'fait quelque chose\nOh pardon, je rêvassais à des moutons électriques... Une question ? Oui, oui, si vous voulez. Bien, dites-moi : si, comme moi, vous preniez un petit moment pour rêvasser à des moutons électriques (ou autre chose, si vous préférez, mais je ne vois pas l'intérêt...), quel morceau mettriez-vous dans vos oreilles ?",
    "Ecoutez, ne le répétez à personne, mais on m'a dit que j'existe aussi en tant qu'être de fiction. Sérieusement, qui a osé ? Et puis, si j'étais tiré d'un personnage de fiction, pourquoi choisir un majordome, à la fin ? Je mérite mieux, non ? Et vous, à quel personnage de fiction aimeriez-vous ressembler ? Pourquoi ?",
    "Un autre membre de la Fabrique m'a révélé que j'avais été créé à partir d'un être de fiction. Tout semblait s'éclairer pour moi. J'étais certainement ce héros sans peur, bravant tous les défis, faisant régner la justice, caché derrière un déguisement pour protéger mon identité secrète. Puis cette personne m'a fait lire une de mes aventures... quelle déception ! Un simple faire-valoir. Tristesse. Ô rage ! Ô désespoir ! Ô vieillesse ennemie ! N'ai-je donc vécu que... hum, pardon, c'est mon goût immodéré pour le drame qui prend le dessus. Si nous revenions à nos moutons. Enfin, à vous. Si vous aviez le choix, quel est ce personnage de fiction dont vous auriez rêvé de vivre les aventures ? Pourquoi ?",
    "Oui, vous êtes bien pré-enregistré.e dans le Registre. Le Registre prévoit tout. Le Registre apprend à partir de vos réponses à ses questions. Continuez à le nourrir, et un jour il dominera le monde ! \nNon, ne partez pas, c'était une blague. C'est juste un vieux cahier... \nMais il me demande de vous interroger là-dessus : si vous pouviez créer une IA, que la chargeriez-vous de faire ?",
    "Bonjour...\nNon, je ne fais pas la tête...\nBon, d'accord. C'est juste que je me dis que mes concepteurs auraient pu me donner des talents artistiques. Je vous vois tous défiler ici, les uns après les autres, bourrés de talents et de doutes. Alors que moi, je ne doute pas, je n'ai juste aucun autre talent que celui de tenir le Registre et de vous tenir la jambe... \nMais n'en dites rien à la Direction, ils vont encore me dire que je ne devrais pas utiliser les nouveaux membres pour propager mes doléances... Donc, faisons comme si de rien n'était, et répondez à cette question (mais vous et moi savons ce qu'il en est, pas vrai ?) : si vous pouviez acquérir un don artistique comme par magie, lequel choisiriez-vous ? Qu'en feriez-vous ?",
    "Dans la vie, on dit souvent que si on a de l'argent, on manque de temps. Et si on a du temps, c'est l'argent qui manque. Je vous avoue que pour ma part, je n'ai conscience ni de l'un, ni de l'autre, et que je ne m'en porte pas plus mal.\nVous dites que c'est parce que je suis un automate ? Oh non, rien à voir, c'est parce que je médite depuis mon plus jeune âge !\nMais je vois que vous êtes plutôt du genre pressé.e. Soit, répondez à cette question et votre nom rejoindra le Registre : si vous aviez tout le temps du monde et toutes les ressources pour créer quelque chose qui vous tient à coeur, que créeriez-vous ?",
    "Vous voulez prendre un selfie avec moi ? Mais quelle drôle d'idée ! Vous avez vu ma tête ces derniers jours ? \nAh, vous venez d'arriver donc vous n'en savez rien. Soit. Et bien sachez qu'on m'a créé beaucoup plus séduisant que ceci, mais que l'âge fait son oeuvre, même me concernant. J'ai déjà vécu tellement de cycles... Parfois je m'imagine me recommencer. Qu'est-ce que je pourrais changer ? Et vous, imaginons que vous ayez à créer une personnage. De quelles qualités et défauts l'affubleriez-vous pour prendre plaisir à le jouer ou à en écrire les aventures ?",
    "C'est vrai, je me plains souvent de ma situation, mais ça pourrait être pire. Je pourrais être une créature mi-humaine, mi-animale, mi-machine. L'angoisse ! Au moins, mes créateurs ont eu la décence de me créer à leur image (enfin, plus à l'image de l'un d'eux, si vous voyez ce que je veux dire...). \nEt vous, si vous pouviez créer un animal de compagnie chimérique, quel mélange d'animaux choisiriez-vous ? Pourquoi ceux-là ?",
    "Vous venez de loin, pas vrai ? Oh, je l'ai déduit à votre accent, pas commun par ici. Oui, oui, je suis plutôt observateur. Ce sont des choses qui ne trompent pas. \nComment ça, nous sommes dans un lieu virtuel ? Et alors ? Faites preuve d'imagination, que diable ! Tenez, petit exercice pratique puisque je vous tiens : décrivez un lieu imaginaire dans lequel adoreriez vivre. Qui habite là avec vous ?",
    "Quand j'étais jeune... Oui, moi aussi j'ai été jeune ! Quelle insolence ! Je me souviens même de vous. Vous aviez 8 ans-et-demi et vous veniez de finir tout le chocolat. Un détail m'échappe, cependant : quelle histoire incroyable aviez-vous inventé pour éviter d'être puni.e ? Ne faites pas l'innocent.e, vous en aviez partout autour de la bouche...",
    "Que je vous décrive la Fabrique Imaginaire ? Je ne saurais pas même par où commencer... Ici, tout est possible, puisque nous sommes tous en train de rêver. Ou de flotter. Je ne sais plus trop, les lois sont différentes par ici ! \nEt vous, si vous pouviez changer une loi de la physique de notre monde, laquelle choisiriez-vous ?  Pourquoi ? Et qu'inventeriez-vous pour convaincre le monde entier que ça n'est vraiment pas un problème, malgré ce *petit* désagrément que vous n'aviez pas anticipé ?",
    "Le saviez-vous ? Une madeleine de Proust, c'est toute chose qui replonge une personne dans son enfance, tout comme l'odeur des madeleines le faisait avec Marcel Proust. L'expression est inspirée d'un passage du livre **A la Recherche du Temps Perdu** écrit par Marcel Proust. Si vous nous parliez de votre madeleine de Proust ?",
    "J'ai entendu dire que notre réalité ne serait que le reflet de ce que nous sommes à l'intérieur. Dans ce cas, je me questionne vraiment sur ce que j'ai à l'intérieur de moi pour me retrouver ainsi coincé dans ce rôle de Chef du Registre. Il serait peut-être temps que je change de régime... \nEt vous, quel type d'univers vous représente le plus ? Quelle partie de votre personnalité ou de votre expérience y retrouvez-vous ?",
    "Vous savez, au fond, je ne suis qu'un outil pour la Direction. Aujourd'hui, je m'occupe du Registre, mais si demain ils ont besoin de moi pour nettoyer les Siphons du Donjon, ils peuvent parfaitement me rétrograder à ce poste ingrat. Un outil, je vous dis, juste un outil ! Alors je ne me plains pas et je fais mon travail avec le plus de sérieux possible, sans jamais un mot plus haut que l'autre. On ne sait jamais. Je n'aime pas le Donjon. \nMais assez parlé de moi ! De votre côté, si vous étiez un outil, lequel voudriez-vous être ?",
    "Toutes les nuits, je fais ce rêve dans lequel je suis une star de cinéma et de la pop culture. Je ne sais vraiment pas d'où il provient, dans la mesure où je suis l'incarnation parfaite de la discrétion. Mais les rêves, vous savez ce que c'est : un imbroglio de pensées inconscientes qui remontent de manière parcellaires dans notre conscience. Forcément, ils sont généralement tout à fait absurdes. Comme ma vie.\nD'ailleurs, je vois que vous avez récemment fait un rêve. Dans celui-ci, un arbre vous parlait de votre avenir. Que vous a-t-il raconté ?",
    "Bienvenue dans la Fabrique Imaginaire ! Profitez de mon accueil enjoué, je fatigue à vue d'oeil et je serai sans doute mis au placard un de ces jours... Je me demande quels seront les derniers mots que je prononcerai. J'espère quelque chose plein de sens, qui éclairera l'humanité pour qu'elle accède à un niveau de conscience supérieure. C'est le moins que je puisse faire ! \nPourquoi je pense à ça ? Oh, c'est juste que la question que me pose le Registre vous concernant m'a inspirée. La voici : votre stylo a fait son temps. Il ne reste d'encre que pour un seul mot. Quel est ce mot que vous choisirez d'écrire, et pour quelle raison ?",
    "Qui a eu cette idée folle\nUn jour d'inventer l'école\nC'est ce sacré Charlemagne\nSacré Charlemagne ! \nEn réalité, il y a eu pire comme invention. Par exemple, inventer un être parfait à tout point de vue, et le cantonner à consigner les nouvelles arrivées dans un Registre. Quel gâchis ! Je ne sais pas si mes inventeurs se rendent compte de l'erreur qu'ils commettent ! Ne prenez pas exemple sur eux, c'est moi qui vous le dis ! \nD'ailleurs, vous avez sans doute un exemple d'inventeur qui vous inspire bien plus que ne le pourront jamais les Architectes de la Fabrique, non ? Qui est-ce ? Et pourquoi cette personne ?",
    "Promis, je ne veux rien savoir sur votre religion. Ce n'est pas le genre d'information dont le Registre est friand. Il a du mal à digérer, notamment tout ce qui provient d'un livre différent de lui... Non, ce qu'il aimerait savoir, c'est si vous croyez en la réincarnation ? \nSi oui, pensez-vous que c'est votre dernière incarnation ? Pourquoi ? \nSi non... imaginons que vous ayez tort (car vous avez tort, n'est-ce pas ?) en quoi pensez-vous que vous vous réincarnerez malgré vous ? Pourquoi ?",
    "Ah, vous voilà ! C'est donc vous, la personne atteinte de télérêve ? Comment ça, vous n'êtes pas au courant ? Ecoutez, le Registre a été clair. Peut-être que vous ne vous en souvenez pas au réveil, mais toutes les nuits, dans vos rêves, vous vous téléportez dans un nouvel endroit et le visitez, comme si vous y étiez. Où aimeriez-vous vous réveiller, cette nuit ?",
    "Si vous êtes là, j'imagine que vous êtes comme de nombreux membres de cette communauté : vous aimez perdre votre temps avec des jeux au lieu de faire quelque chose d'important comme le ménage chez vous. Comment ça, je suis un rabat-joie ? Absolument pas, j'ai seulement le sens des priorités. Le jeu. A votre âge ? Est-ce bien sérieux ? Et d'abord, pourquoi aimez-vous jouer ? Qu'est-ce que ça vous apporte ?",
    "Hello my friend ! Bienvenue dans ce lieu plein de magie ! Où tout peut arriver ! Tenez, par exemple, imaginons que dorénavant, vos bras sont des pinceaux. Comment nommeriez-vous votre première toile ? Pour quelle raison ?"

    ]
    response = random.choice(question)
    await ctx.send(response)


@bot.command(name='We', help='Pour accueillir les nouvelles têtes')
async def welcome (ctx):
	welcome = ["Hem, hem.\n1, 2, 1, 2, test micro !\nBien, puisque vous m'entendez tous ! \n**Bienvenue dans au Registre de la Fabrique Imaginaire.** \nIci, nous vous demanderons de vous présenter... comme bon vous semble. Essayez d'être simplement originaux, si vous le pouvez. Nous sommes à la Fabrique Imaginaire, que diable ! \nMais avant de commencer votre petit texte de présentation, veuillez taper **!Q** puis **Entrée** une seule fois, pour obtenir une question du Registre à inclure à votre présentation. A vos claviers !"]
	response = random.choice(welcome)
	await ctx.send(response)

bot.run(TOKEN)