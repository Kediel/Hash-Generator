import hashlib 

file = open("pass.txt", "w")

hashGen = hashlib.sha1()
hashGen.update("NSAproof")

hash = hashGen.hexdigest()

file.write(hash)

file.close()
