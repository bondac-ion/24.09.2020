n=7845
a=n%10 #unitatile numarului n
print(a,"ultima cifra a numarului n")
b=(n%100)//10 #zecile namarului n
print(b,"penultima cifra a numarului n")
c=(n%1000)//100 #sutimile numarului n
d=n//1000 #miimile numarului n
print(n//9,"catul impartirii la 9")
print(n%9,"restul impartirii la 9")
print(a+b+c+d,"suma cifrelor numarului n")
m=1000*a+100*b+10*c+d
print(m,"rasturnatul numarului")