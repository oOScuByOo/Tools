#=========================================================#
# [+] Script : AntiCandyBot v2.0                          #
# [+] Auteur : oOScuByOo                                  #
# [+] Site : xxxxxxxxxxxxxxxxxxx                          #
# [+] Twitter : xxxxxxxx                                  #
#=========================================================#

#-----------librairie-------------#

import socket # Ajout librairie Socket
import time # Ajout librairie Time
import os # Ajout librairie OS
import base64 # Ajout librairie Base64

#-----------Fonctions-------------#

def JouerAuPingPong(): # Fonction permettant de passer le Test de PING
    while 1:
        BOT.send(str('PONG ' + data.split(':')[1] + '\r\n').encode())
        print('PONG envoyer \n')
        break

def Salut(): # Fonction Salut Juste pour le fun
  BOT.send("PRIVMSG "+ CHANNEL +" :Salut !\n")

def AvoirLePass(): # Fonction pour avoir le mot de passe
    BOT.send("PRIVMSG "+TARGET+" :!ep2\r\n") # MP Candy pour commencer le challenge
    while 1:
        POUBELLE=BOT.recv(7000)
        print(POUBELLE)
        if POUBELLE.find(":")>-1: # Verifie le MP pour etre sur d'avoir la chaine encodee
            POUBELLE=POUBELLE[(POUBELLE[1:].find(":"))+2:] # Decoupe le message pour le verifier
            POUBELLE=POUBELLE[:POUBELLE.find(".")]         # Doit ressembler a quelque chose comme "V1RKZ0NabDBFcVdNcko5QlZzN0RDWDVzUQ=="
            print(POUBELLE)
            REPONSE=str(POUBELLE[(POUBELLE.find(":"))+1:])
            print "Chaine encodee : " + REPONSE
            REPONSE=base64.b64decode(REPONSE); # Decode en Base64
            print "Chaine decodee : " + REPONSE
            BOT.send("PRIVMSG "+TARGET+" :!ep2 -rep "+REPONSE+"\r\n") # Envoie la reponse a Candy
            print(BOT.recv(7000)) # Obtenir la reponse de Candy et donc le MDP
            BOT.send("QUIT :By3 By3 !") # Ferme la connection a Candy
            break

#-----------Variables-------------#

HOST = 'irc.root-me.org' # Variable Host du serveur IRC
PORT = 6667 # Variable Port du serveur IRC
NICK = 'AntiCandyB0t' # Variable Pseudo du Bot
USERNAME = 'V2' # Variable 2 de l'username du Bot
REALNAME = 'par oOScuByOo' # Variable 3 de l'username du Bot
CHANNEL = '#root-me_challenge' # Variable Channel (Salon) sur lequel on veut aller sur le serveur
TARGET = 'Candy' # Variable Target (Cible) avec laquelle on veut interragir en l'occurence Candy
BOT = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Definir la variable Bot pour appeler le Socket
NICK_CR = ('NICK ' + NICK + '\r\n').encode() # Variable(Fonction) servant a cree notre Nickname
USERNAME_CR = ('USER '+ NICK +' '+ USERNAME +' '+ REALNAME +'\r\n').encode() # Variable(Fonction) servant a cree notre Username
CHAN_CR = ('JOIN ' + CHANNEL + '\r\n').encode() # Variable(Fonction) Permettant de se connecter au bon Channel

#-----------Initialise la connection-------------#

print("[!] SOC cree | ", BOT)
remote_ip = socket.gethostbyname(HOST) # Initialisation de notre Socket
print("[!] IP du serveur : ", remote_ip)
BOT.connect((HOST, PORT)) # Connection au serveur
print("[!] Connecter sur : ", HOST, PORT)

#-----------Definit le Nickname et Username-------------#

print("[+] Envoie NickName")
BOT.send(NICK_CR) # Initialisation de notre Nickname
print("[+] Envoie UserName")
BOT.send(USERNAME_CR) # Initialisation de notre Username

#-----------Fonction a appeler une fois connecter-------------#

while 1: # Boucle permettant de garder la connection le temps que l'on en a besoin

    data = BOT.recv(4096).decode('utf-8') # Permet de transformer les donnees recu en caracteres lisibles
    print(data)

    print("[+] Rejoint ",CHANNEL)
    BOT.send(CHAN_CR) # Connection au Channel que l'on desire

    if data.find('ACB!') != -1: # Appel de la fonction AvoirLePass si le Bot recoit sur l'entree standard ACB!
        AvoirLePass()

    if data.find('PING') != -1: # Appel de la fonction JouerAuPingPong si le Bot recoit sur l'entree standard PING
        JouerAuPingPong()

    if data.find('Salut') != -1: # Appel de la fonction Salut si le Bot recoit sur l'entree standard Salut
        Salut()

    if data.find('ACBSleep') != -1: # Ferme le bot (A revoir fait le job mais parceque casse la chaine x') )
        print("[+] Au Dodo !")

BOT.close()
