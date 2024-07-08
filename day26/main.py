import random       
list_names = ['Alex','Jalex','Calex','Talex']

randomscores = {Key:random.randint(1,100) for Key in list_names }
print(randomscores)

passedscores = {key:value for key,value in randomscores.items() if value > 50}
print(passedscores)