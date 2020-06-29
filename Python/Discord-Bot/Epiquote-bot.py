import discord
import random

class Bot(discord.Client):

    def __init__ (self):
        super().__init__()


    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-----------')

    async def on_message(self,message):
        rnd =random.randint(1,51)
        if(message.author == self.user):
            return
        if(message.content.startswith("!epiquote")and rnd ==1):
            await message.channel.send("Chewie (Veille des partiels): \n On adore procrastiner. On a jamais autant avancé ses mangas et ses séries que la veille des partiels.")
        if(message.content.startswith("!epiquote")and rnd == 2):
            await message.channel.send(" M. Joël Courtois (Jury de passage en Ing2): \n Mais tu comptes travailler ou devenir fonctionnaire ?")
        if(message.content.startswith("!epiquote")and rnd ==3):
            await message.channel.send("Nathalie Bouquet (En parlant du partiel d'algo): \nCeux qui ont utilisé le pouvoir débranchant du retourne, mais qui on fait ça proprement, bon, j'ai dit Allez ça va.Par contre les autres, ils ont morflé leur race. Et il y en avait beaucoup.")
        if(message.content.startswith("!epiquote")and rnd ==4):
            await message.channel.send(" haltode (En réunion Prologin, à propos d'engager des ING1 pour du travail manuel) : \n Les ing1 sont putes à ENAC.")
        if(message.content.startswith("!epiquote")and rnd ==5):
            await message.channel.send("Christophe Boullay : \n T étais pas né que j étais déjà root ici !")
        if(message.content.startswith("!epiquote")and rnd ==6):
            await message.channel.send("Check Presence (Cours de Construction des Compilateurs) \n Etienne Renault : Vous savez quelle est la plus grande arnaque du siècle ? \n Check Presence : EPITA")
        if(message.content.startswith("!epiquote")and rnd ==7):
            await message.channel.send("Alizée (Des élèves arrivent en cours avec des Mr. Freeze) : \nLe premier qui suce trop fort il finit dehors.")
        if(message.content.startswith("!epiquote")and rnd ==8):
            await message.channel.send("Nonoctis : \n J'avais jamais remarqué que les initiales d'interdit bancaire, ça faisait BDE.")
        if(message.content.startswith("!epiquote")and rnd ==9):
            await message.channel.send("Christophe Boullay : \n De toutes facons, si vous avez pas d'idée pour le nom du groupe, vous pouvez toujours additionner les deux premières lettres de chaque nom, ça vous donnera forcément un truc du genre wasabi ou tout autre truc à consonance asiatique.")
        if(message.content.startswith("!epiquote")and rnd ==10):
            await message.channel.send("M. GORON (En corrigeant un exercice sur les suites): \n Un suite qui fait 1, 2, 4, 8, ça vous rappelle rien ? Et oui, c'est vos notes de QCM.")
        if(message.content.startswith("!epiquote")and rnd ==11):
            await message.channel.send("Anne-Sophie Dujardin (Pendant un cours sur les additions et soustractions en binaire): \n Au prochain type qui passe dans le couloir, je dis 1+1 vous me répondez tous 10.")
        if(message.content.startswith("!epiquote")and rnd ==12):
            await message.channel.send("Max Testemale (En parlant d'une de ses quotes sur Epiquote.): \n Non mais moi j'en ai une petite, elle me va très bien !")
        if(message.content.startswith("!epiquote")and rnd ==13):
            await message.channel.send("Yona (Parle des nombreux fails des yakas): \n <Yona> Les yakas ils ont tellement échoué qu'ils devraient monter le prochain bureau Test..")
        if(message.content.startswith("!epiquote")and rnd ==14):
            await message.channel.send("seure-_a et escoba_c (Lors du débat entre les différents BDE candidats, serialk, membre de la liste Test. , commence la présentation en testant le micro.): \n <serialk> Test. Test. Test. \n <seure-_a> C'est ça leur campagne de pub ? \n<escoba_c> C'est comme les Pokemons. C'est comme ça qu'ils s'appellent entre eux et qu'ils communiquent.")
        if(message.content.startswith("!epiquote")and rnd ==15):
            await message.channel.send("Chef ACU 2017: \n Le WEI c’était bien. Le WEI c'est fini.")
        if(message.content.startswith("!epiquote")and rnd ==16):
            await message.channel.send("yahia_i (Cours d'algo avec Gollum) : \n Gollum : OK donc ça c'était pour l'arbre parfait, maintenant qui peut me dire ce qu'est un arbre complet ? \n yahia_i : Salade tomate oignon ? \n Gollum : tu sors.")
        if(message.content.startswith("!epiquote")and rnd ==17):
            await message.channel.send("Hibiscus (En parlant de sa queue de cheval): \n <Hibiscus> En Angleterre ils arrêtaient pas de tirer dessus en boîte. \n <Bruce> Tirer sur ? \n <Hibiscus> Ma queue")
        if(message.content.startswith("!epiquote")and rnd ==18):
            await message.channel.send("Alouest (Quelques jours après la présentation de Tiger Backend): \n Faire le backend de tigrou c'est un peu de la zoophilie non ?")
        if(message.content.startswith("!epiquote")and rnd ==19):
            await message.channel.send("colin_l : \n Les seules relations que tu connais à EPITA ce sont les relations entreprises")
        if(message.content.startswith("!epiquote")and rnd ==20):
            await message.channel.send("Hatrix: \n <Hatrix> Moi j'aime bien les moustiques. Pour une fois qu'on me suce... ")
        if(message.content.startswith("!epiquote")and rnd ==21):
            await message.channel.send("Christophe Boullay (Répondant à un élève qui l'interpelle): \n Elève > Hé monsieur ! \n Krisboul > J'en ai rien à foutre.")
        if(message.content.startswith("!epiquote")and rnd ==22):
            await message.channel.send("Paul Hervot (Discussion avec Paul Hervot au sujet du nouveau professeur de physique) : \n <Paul> On a une piste pour trouver un nouveau prof de physique. \n<Élève> Et elle est bonne ? \n <Paul> Mais c'est un homme. \n <Élève> Non, la piste...")
        if(message.content.startswith("!epiquote")and rnd ==23):
            await message.channel.send("Un epitech lors du CIA (Le CIA discute sur le fait que madame Cavatorta n'aime pas que le prépas participe à la vie associative): \n C'est qui cette gonzesse qui embête tout le monde ?")
        if(message.content.startswith("!epiquote")and rnd ==24):
            await message.channel.send("Bashar (Bashar essaie de tracer une droite en analyse convexe) : \n C'est pas pour rien que j'ai pas fait les beaux arts, au moins je suis pas devenu dictateur.")
        if(message.content.startswith("!epiquote")and rnd ==25):
            await message.channel.send("Le Parrain (Propose d'imprimer une photo au stand Éphémère): \n Si tu veux je te l'imprime en 10x15. C'est en centimètre hein, 10 comme Fabien et 15 comme moi")
        if(message.content.startswith("!epiquote")and rnd ==26):
            await message.channel.send("M. David Bouchet (Pendant un TD d'archi.) : \n Le prof :Tu dois être Maître de la Conversion.\n Romain Lofaso : Que la force du bit soit avec toi !")
        if(message.content.startswith("!epiquote")and rnd ==27):
            await message.channel.send("halfr : \n 17:25 <Dettorer> vous revenez quand ? \n 17:26 <seirl> bah tard \n 17:27 <halfr> c'est toi le bah tard")
        if(message.content.startswith("!epiquote")and rnd ==28):
            await message.channel.send("Anonyme (Planification d'une sortie pour les étudiants) : \n Etudiant #1 : Pour vous, quel est le parc d'attraction qui plairait le plus aux étudiants ? Disneyland ? Parc Astérix ? \n Etudiant #2 : l'étage des Epitech")
        if(message.content.startswith("!epiquote")and rnd ==29):
            await message.channel.send("Enulp (En réunion GConfs): \n <sunbro> : Pourquoi t'as un polo Epitech ? \n <Enulp> : Bah c'est Halloween !")
        if(message.content.startswith("!epiquote")and rnd ==30):
            await message.channel.send("Martin Van Laere (Transition lors d'un TD Caml): \n Bon ! On se reprend nos fonctions en Caml ? Ça va être <fun> ! \n Personne n'a compris ! Bon tant pis...")
        if(message.content.startswith("!epiquote")and rnd ==31):
            await message.channel.send("Douze (Discussion suite aux fuites d'informations chez Epitech) : \n Issun : Est-ce que tu fais confiance à pegasus pour la sécu ? \n Satan : La meilleure protection de Pegasus c'est son uptime claqué \n Douze : Protection par la lenteur")
        if(message.content.startswith("!epiquote")and rnd ==32):
            await message.channel.send("Professeur anonyme (a écrit au Velleda sur un écran de rétroprojecteur) : \n *tente de trouver une solution pour camoufler son erreur* \n <prof> Vous pensez que l'alcool est une solution ?")
        if(message.content.startswith("!epiquote")and rnd ==33):
            await message.channel.send("Le Bleu : \n La limite entre le primate et l'homme, le panneau Kremlin-Bicetre. \n Les ASMs et les ACDC ils vont au zoo une a deux fois par semaine.")
        if(message.content.startswith("!epiquote")and rnd ==34):
            await message.channel.send("N_sys (En parlant de la moyenne de 0.2 en SIN 1) : \n N_sys: Il y a eu des gens qui ont eu sin(1) en SIN 1")
        if(message.content.startswith("!epiquote")and rnd ==35):
            await message.channel.send("ducast_j: \n J'espère que tu baise pas comme tu code.")
        if(message.content.startswith("!epiquote")and rnd ==36):
            await message.channel.send("turfu (en cours de Linux embarqué, le prof remarque le t-shirt de cigix): \n <Ficheux> Tiens, j'ai le même t-shirt que vous ! \n <cigix> MOI AUSSI, J'AI LE MÊME T-SHIRT QUE MOI")
        if(message.content.startswith("!epiquote")and rnd ==37):
            await message.channel.send("Un élève : \n Tu vois le grand mec barbu là... Comment il s'appelle déjà ? Ah oui, Courtois.")
        if(message.content.startswith("!epiquote")and rnd ==38):
            await message.channel.send(" Floom (En rush projet LSE) : \n Floom: Si ça marche, je vais me coucher. Si ça marche pas, je vais me coucher")
        if(message.content.startswith("!epiquote")and rnd ==39):
            await message.channel.send("Mme Tremoulet : \n Il n'y a pas que votre vie dans la vie, il y a les espaces vectoriels aussi.")
        if(message.content.startswith("!epiquote")and rnd ==40):
            await message.channel.send("tavuck_a (Prevoie une nuit blanche pour 42sh) : \n Kimicol: Bon, je retourne coder \n Douze: Reste avec moi pour la nuit !")
        if(message.content.startswith("!epiquote")and rnd ==41):
            await message.channel.send("bakablue : \n On était à la tour Eiffel, on se faisait chier donc on est allées au LSE parce qu'il y avait de l'alcool.")
        if(message.content.startswith("!epiquote")and rnd ==42):
            await message.channel.send("Matthieu cornet (Presentation de la majeure SIGL, Matthieu pose une question au professeur) : \n Le professeur: Ta tete me dit quelque chose, t'aurais pas un grand frere? \n cornet_m: Non mais j'ai eu vos deux filles!")
        if(message.content.startswith("!epiquote")and rnd ==43):
            await message.channel.send("M. Goron (En parlant des partiels de S3) :\n Vos partiels c'est un peu comme mes cadeaux de Noël, c'est toujours décevant.")
        if(message.content.startswith("!epiquote")and rnd ==44):
            await message.channel.send("PolyB ($env) : \n Le Parrain : Il s'appelle comment l'explorateur de fichier sous manjaro i3 ?PolyB : ls")
        if(message.content.startswith("!epiquote")and rnd ==45):
            await message.channel.send("manden_p (Arrive devant Gollum avec une Sup'Biotech): \n Je vous échange Chloé contre 5 points au partiel.")
        if(message.content.startswith("!epiquote")and rnd ==46):
            await message.channel.send("Michel Sasson (En cours de MINN): \n Il faut être gentil avec elle, elle a un gosse à Epitech.")
        if(message.content.startswith("!epiquote")and rnd ==47):
            await message.channel.send("M. Fabrice Bardeche (Lors du discours d'ouverture d'ING1.) : \n Lors de la piscine, vous n'allez pas beaucoup dormir donc vous allez être fatigués.")
        if(message.content.startswith("!epiquote")and rnd ==48):
            await message.channel.send("Marie Moins : \n Les Yakas finalement sont des schtroumpfs malades")
        if(message.content.startswith("!epiquote")and rnd ==49):
            await message.channel.send("Vermeille : \n <Bruce> J'adore les crêpes \n <Bruce> j'ai bizarrement pensé à des cumshots en balançant la pate sur la poële \n <Vermeille> Toi aussi ?")
        if(message.content.startswith("!epiquote")and rnd ==50):
            await message.channel.send("WrongPasswd (Cours d'architecture) : \n <WrongPasswd> 50 nuances de code Gray.")
        if(message.content.startswith("!epiquote")and rnd ==51):
            await message.channel.send("Chewie (Chewie illustre, durant une conf' sur la POO...) : \n Chewie : Tout ici dans cet pièce est objet. Les tables sont des objets, les chaises sont des objets... Vous êtes des objets ! \n Un élève : Les femmes sont des objet? \n Chewie : Oui ! Les femmes sont des objets ! ")
        if(message.content.startswith("!rocco")):
            await message.channel.send("Floom (Parlant de l'achat d'un clavier ergonomique) : \n Ouais quand j'ai compris que j'allais bouffer plus de lignes de code par semaine que Rocco n'a bouffé de chattes dans sa vie, je me suis dis que c'était urgent")
        if(message.content.startswith("!chewie")):
            await message.channel.send("Chewie (Cours de NET2) : \n Votre clé privée c'est comme votre bite. C'est bien d'en avoir une, c'est bien d'en être fier, mais on la montre pas à tout le monde.")
        if(message.content.startswith("!alex")):
            await message.channel.send("Shepard : \n J'ai un Mac mais je me respecte, j'ai viré MacOs et j'ai mis Arch.")
        if(message.content.startswith("!risson")):
            await message.channel.send("risson ((42sh)) : \n <risson> Vous trouvez pas que sigaction ça ressemble un peu à sidaction ?")
        if(message.content.startswith("!cavatutu")):
            await message.channel.send("Mme Cavatorta (Réunion pour IonisX) : \n ohayon_e : Mais madame, pourquoi vous lockez les MiMos alors ? \n Mme Cavatorta : Pourquoi le ciel il est bleu aussi hein ?")
        if(message.content.startswith("!sale")):
            await message.channel.send("fouche_r (En archi, alors qu'A.S Dujardin parle d'une mémoire à 13 fils d'adresse): \n Il faut qu'elle soit profonde pour qu'il y ait 13 bits dedans !")
        if(message.content.startswith("!under")):
            await message.channel.send("Christian Dujardin (Conference avec les ing1, à Joël Courtois) : \n Dans l'under, il y a des néons et des pigeons. Les pigeons ils volent et les néons ils tombent.")
        if(message.content.startswith("!putes")):
            await message.channel.send("Warren Seine (Justificatif d'absence à un cours (notez que ceci lui a valu un conseil de discipline et un Mais tu es un fou ! de M. Christian Dujardin)) : \n J'étais aux putes et il y avait du monde.")










if __name__ == "__main__":
    bot = Bot()
    bot.run("NzEyNjY3NTIwNjcwMTA1NzAw.XsZCdg.ZJcq4N8abLYOBBpxSk7DI3abmxk")
