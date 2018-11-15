#=========================================================#
# [+] Script : ZlibDecoder                                #
# [+] Auteur : oOScuByOo                                  #
# [+] Site : xxxxxxxxxxxxxxxxxxx                          #
# [+] Twitter : xxxxxxxx                                  #
#=========================================================#

import zlib # Importe la librairie zlib
import binascii # Importe la librairie BinAscii

Str = 'Hello world' # Chaine de caractere a traiter
StrEncoded = 'eJwL8LTIMgtJMvKLNEj1SwQAH0wERQ=='

compressed_str = zlib.compress(Str, 2) # Compresse la chaine avec Zlib
decompressed_str = zlib.decompress(compressed_str) # Decompresse la chaine avec Zlib
decompressed_strencoded = zlib.decompress(StrEncoded) # Decompresse la chaine avec Zlib

print('Chaine compresser : ' + binascii.hexlify(compressed_str)) # Affiche la chaine Str compresser
print('Chaine decompresser : ' + decompressed_str) # Affiche la chaine decompressed_str decompresser
print('Chaine decompresser : ' + decompressed_strencoded) # Affiche la chaine StrEncoded decompresser
