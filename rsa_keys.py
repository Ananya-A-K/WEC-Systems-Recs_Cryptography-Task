import math
def rsa_keys(n,e):
    print(f"n={n}")
    print(f"e={e}")
    factors=[] #other than 1,itself and integral square root if it exists
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            if i!=1 and i*i!=n:
                factors.append(i)
                factors.append(n//i)
                break
    print(f"p={factors[0]}")
    print(f"q={factors[1]}")
    phi_n=(factors[0]-1)*(factors[1]-1)
    print(f"phi_n={phi_n}")
    d=pow(e,-1,phi_n)
    print(f"d={d}")
    return factors[0],factors[1],d

n=421649
e=17
p,q,d=rsa_keys(n,e)
c="Web.Club"
C=""
for char in c:
    C+=(str(ord(char)))
ciphertext=int(C)
print("Web.Club to ascii: ",ciphertext)
plaintext=pow(ciphertext, d, n)
decrypted_message=str(plaintext)
print("Decrypted message:", decrypted_message)
txt=pow(ciphertext,e,n)
txt2=str(txt)
print("Encrypted w/ rsa:",txt2)