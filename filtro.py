


Archive = open('LemaFin','r')
Archive2 = open('3words','a')

lemas = []
for line in Archive:
    word = line.split()
    if len(word[0])== 3:
        lemas.append(word[0])
        Archive2.write(word[0]+'\n')
print(lemas)

Archive.close()
Archive2.close()