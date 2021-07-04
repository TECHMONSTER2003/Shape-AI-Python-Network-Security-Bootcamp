import hashlib
#print(hashlib.algorithms_available) #I have used md5,shake_128,sha3_512
str0=input("enter a string to hash : ")
str1=str0.encode() #I dont know why hashlib can accpet only encoded values but i read online that encoding is must
print("single MD5 hash of ",str0," is : ",hashlib.md5(str1))
print("single shake_128 hash of ",str0," is : ",hashlib.shake_128(str1))
print("single sha3_512 hash of ",str0," is : ",hashlib.sha3_512(str1))
#nerd alert!!!!!!!
print("lets go for iterations and salting😉")
samp_str='abcdefghijklmnopqrstuvwxyz' #making some string for salting usage
strx,hash,k='','',0
if len(str0)<=len(samp_str):
    for i in str0:
        strx=strx+i+samp_str[k]
        k=k+1
else:
    strx="a"+(str0)+'b'
print(strx,"salting performed")
str1=strx.encode()
hash=hashlib.md5(str1)
n=int(input("enter the number of iterations : "))
hashlist=[] #initialising an empty list to store hash values
for i in range(n-1): #as its already hashed one time, I have used n-1
    hashlist.append(hashlib.md5(str1))
print("Salting and ",n," iterations performed md5 hashing of ",str1," is",hashlist[n-2])
