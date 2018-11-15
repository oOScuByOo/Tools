#=========================================================#
# [+] Script : Encoder / Decoder Base64                   #
# [+] Auteur : oOScuByOo                                  #
# [+] Site : xxxxxxxxxxxxxxxxxxx                          #
# [+] Twitter : xxxxxxxx                                  #
#=========================================================#

import base64 # Importe la librairie Base64

Str1 = "V1RKZ0NabDBFcVdNcko5QlZzN0RDWDVzUQ=="; # Definit la premiere Chaine
Str1 = base64.b64decode(Str1) # Decode la premiere Chaine

Str2 = "WTJgCZl0EqWMrJ9BVs7DCX5sQ"; # Definit la deuxieme Chaine
Str2 = base64.b64encode(Str2) # Encode la deuxieme Chaine

print "Decoded String: " + Str1 # Affiche le resultat de la premiere Chaine
print "Encoded String: " + Str2 # Affiche le resultat de la deuxieme Chaine
