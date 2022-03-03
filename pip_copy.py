f = open('/home/alaskaris/Downloads/piplist.txt','r')
# print(f.read())


piplist=[]

for line in f:
    piplist.append(line)

# print(piplist)    


f.close()
f = open('/home/alaskaris/Downloads/piplist_new.txt','w')

finallist = []
for line in piplist:
    pip2 = str(line[:])
    a = pip2.replace(' ','')
    b = a.replace('\n','')
    c = 'pip install ' + b + '\n'
    print(c)
    f.write(str(c))

f.close()