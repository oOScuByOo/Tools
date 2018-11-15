#=========================================================#
# [+] Script : ZlibEncoder                                #
# [+] Auteur : oOScuByOo                                  #
# [+] Site : xxxxxxxxxxxxxxxxxxx                          #
# [+] Twitter : xxxxxxxx                                  #
#=========================================================#

import zlib # Importe la librairie Zlib
import binascii # Importe la librairie BinAscii

Str = 'Hello world' # Chaine de caractere a traiter

compressed_str = zlib.compress(Str, 2) # Compresse la chaine avec Zlib

print('Chaine de base : ' +  Str) # Affiche la chaine de base
print('Chaine compresser : ' + binascii.hexlify(compressed_str)) # Affiche la chaine compresser
