import random 


'''
Listas
diccionarios
tuplas

lt = [2,4,5,87,5, True]
print(type(lt))
print(lt)


dc = {'Nombre':'Alfredo', 'inscrito':True, 'calificacion':7}
print(type(dc))
print(dc)

tp = (2,45,True)
print(type(tp))
print(tp)


lt2 = []
for x in range(10):
    lt2.append(random.randint(0,8))

print(lt2)

dt2 = dict()

for x in range(10):
    num = random.randint(0,100)
    if not num in dt2:
        dt2[str(num)] = num

print(dt2)

'''

tp2 = tuple()
t = 10 
c = 0
while(c < t):
    tp2 +=(c,)
    c += 1

print(type(tp2))
print(tp2)