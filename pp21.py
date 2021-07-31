
a='020@'
b='030@'
c='040@'
d='050@'
e='060@'
f='070@'
g='080@'
h='090@'
i='010#'
j='011#'
k='012#'
l='013#'
m='014#'
n='015#'
o='016#'
p='017#'
q='018#'
r='019#'
s='020#'
t='021#'
u='022#'
v='023#'
w='024#'
x='025#'
z='026#'

clear=open('enc.txt','w')
clear.write('')
clear.close()

archive=open('enc.txt','a')
class pp21:
   def encrypt(message):
       primera=(message[:1])
       for xx in message:
           if xx==' ':
              archive.write(' ')
           if xx=='a':
              archive.write(str(a))
           if xx=='b':
              archive.write(str(b))
           if xx=='c':
              archive.write(str(c))
           if xx=='d':
              archive.write(str(d))
           if xx=='f':
              archive.write(str(f))
           if xx=='g':
              archive.write(str(g))
           if xx=='i':
              archive.write(str(i))
           if xx=='h':
              archive.write(str(h))
           if xx=='e':
              archive.write(str(e))
           if xx=='j':
              archive.write(str(j))
           if xx=='k':
              archive.write(str(k))
           if xx=='l':
              archive.write(str(l))
           if xx=='m':
              archive.write(str(m))
           if xx=='n':
              archive.write(str(n))
           if xx=='o':
              archive.write(str(o))
           if xx=='q':
              archive.write(str(q))
           if xx=='r':
              archive.write(str(r))
           if xx=='s':
              archive.write(str(s))
           if xx=='t':
              archive.write(str(t))
           if xx=='u':
              archive.write(str(u))
           if xx=='v':
              archive.write(str(v))
           if xx=='w':
              archive.write(str(w))
           if xx=='x':
              archive.write(str(x))
           if xx=='z':
              archive.write(str(z))
           if xx=='p':
              archive.write(str(p))
       archive.close()
       fin=open('enc.txt','r')
       co=fin.read()
       fin.close()
       print (co)
