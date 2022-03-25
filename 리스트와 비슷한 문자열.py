aa=[10,20,30,40,50]
print (aa[0])
print (aa[1:3])
print (aa[3:])


ss="파이썬만세"
print (ss[0])
print (ss[1:3])
print (ss[3:])



ss='파이썬'+'만세'

print(ss)

ss='파이썬'*3

print(ss)

ss='파이썬abcd'
print (len(ss))

ss='파이썬짱!'

sslen=len(ss)
for i in range(0,sslen):
    print(ss[i]+'$', end='')
