#Było to pisane na Windzie 10 i paczka Random nie działa bez zmiany \Lib\site-packages\Crypto\Random\OSRNG\nt.py
#import winrandom na from . import winrandom albo ja tak miałem tylko
from Crypto.PublicKey import RSA
from Crypto import Random

print ("Podczas pierwszego uruchomienia rozsadnie jest wygenerowac klucz")
if(input("Czy chcesz wtgenerować klucz? nie -> 0 tak -> 1 \n")=='1'):
    
    randomgen = Random.new().read
    key = RSA.generate(2048, randomgen)

    private_handler = open("privkey.pem", 'ab',)
    private_handler.write(key.exportKey(format='PEM'))
    private_handler.close()

    public_handler = open("pubkey.pem", 'ab')
    public_handler.write(key.publickey().exportKey(format='PEM'))
    public_handler.close()


print ("Dodawanie pliku do klucza publicznego\n")
if(input("Chcesz zaszyfrować plik? nie -> 0 tak -> 1 \n")=='1'):
    
    public_handler = open('pubkey.pem', 'rb')
    file_name = input("\nPodaj nazwę pliku do zaszyfrowania\n")
    file_to_encrypt = open(file_name,'rb')
    file_encrypted = open('szyfr.txt','wb')
    public_key = RSA.importKey(public_handler.read())
    
    msg = file_to_encrypt.read()
    cipher = public_key.encrypt(msg, 32)
    file_encrypted.write(cipher[0])

    file_to_encrypt.close()
    file_encrypted.close()
    public_handler.close()


print ("Przerzuć swoj private key do privkey.pem")
if(input("Chcesz odszyfrowac plik? nie -> 0 tak -> 1 : \n")=='1'):
    
    private_handler = open('privkey.pem', 'rb')
    file_name = input("\nPodaj nazwę pliku do odszyfrowania\n")
    file_to_decrypt = open(file_name, 'rb')
    file_decrypted = open('tekst.txt', 'wb')
    private_key = RSA.importKey(private_handler.read())
    
    cipher = file_to_decrypt.read()
    msg = private_key.decrypt(cipher)
    file_decrypted.write(msg)

    file_to_decrypt.close()
    file_decrypted.close()
    private_handler.close()
