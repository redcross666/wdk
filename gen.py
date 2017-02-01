# -*- coding: utf-8 -*-

import sys
from Crypto.Hash import MD5, SHA256

for arg in sys.argv[1:]:
    Crypt5 = MD5.new()
    Crypt256 = SHA256.new()
    file = open(arg,'rb')
    text = file.read()
    Crypt5.update(text)
    Crypt256.update(text)
    print ("Uzyty plik            : ",arg)
    print ("Funkcja skrotu MD5    : ",Crypt5.hexdigest())
    print ("Funkcja skrotu SHA256 : ",Crypt256.hexdigest())

    file.close()
