import sys
import argparse
import binascii
from Crypto.Hash import MD5, SHA256
from binascii import hexlify, unhexlify


def md5hash(args):
    hashh = MD5.new()
    hashh.update(args.encode("utf-8"))
    return hashh.hexdigest()

def sha256hash(args):
    hashh = SHA256.new()
    hashh.update(args.encode("utf-8"))
    return hashh.hexdigest()

files = []
files = sys.argv[1:]
option = '1'
while(option!='0'):
    option = input("1. Wygeneruj hash uzywajac MD5 \n2. Wygeneruj hash uzywajac SHA256 \n0. Wyjdz z programu\n \nWybor:")
    if(option=='1'):
        for arg in files:
            file = open("%s"%arg)
            x = file.read()
            print ("Tekst z pliku: %s"%x)
            print ("Hash z pliku: %s"%md5hash(x))
        
    elif(option=='2'):
        for arg in files:
            file = open("%s"%arg)
            argument = file.read()
            print ("Tekst z pliku: %s"%x)
            print ("Hash z pliku: %s"%sha256hash(x))
            
    elif(option=='0'):
        sys.exit("\nBYE BYE!!!")
        
    else:
        print ("\nNie umiesz czytac!!! (.)(.)")
