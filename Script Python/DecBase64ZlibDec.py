#=========================================================#
# [+] Script : Decoder Base64 / Decompresse Zlib          #
# [+] Auteur : oOScuByOo                                  #
# [+] Site : xxxxxxxxxxxxxxxxxxx                          #
# [+] Twitter : xxxxxxxx                                  #
#=========================================================#

import base64 # Importe la librairie Base64
import zlib # Importe la librairie zlib
import binascii # Importe la librairie BinAscii

Str1 = "eJwL8LTIMgtJMvKLNEj1SwQAH0wERQ=="; # Definit la premiere Chaine
Str1 = base64.b64decode(Str1) # Decode la premiere Chaine

print "Decoded String: " + Str1 # Affiche le resultat de la premiere Chaine

Str2 = Str1 # La valeur de la chaine vaut le resultat de Str1

decompressed_str = zlib.decompress(Str2) # Decompresse la chaine avec Zlib

print('Chaine decompresser : ' + decompressed_str) # Affiche la chaine decompressed_str decompresser
