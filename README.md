# Cryptography task Wec Recs-

The 'Cryptography Question.zip' file has two files: welcome.txt and stage-1.zip
On extracting stage1.zip, two files are found stage-2.zip and Info.txt, which are password protected. Checking welcome.txt for hints to the password.

welcome.txt
Let me tell you about Julius Caesar. He started using Caesar cipher, one of the simplest and most widely known encryption 
techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed 
number of positions down the alphabet.
The password is
YZH(878GBC 8BFC87 8C7999 F8AFB ADA8GG 8GGCC7 A7F9EG 8BFDAB)
But, is it though?

## Stage 1
The welcome.txt file hints at caeser cipher being used to encrypt the password. Another observation is that numbers are 
present too. The traditional caeser cipher has only letters. So considering three cases:
1)Remove the numbers and decrypt the rest. Maybe the numbers are used as salt on the password..
2)Keep the numbers as they are and decrypt teh rest. Maybe the numbers are used later or somthin.. 
  (Collecting the numbers together we get: 878 887 87999 8 8 87 97 8, just a bunch of 7s,8s and 9s, could't find anything useful from this)
3)Include numbers in the character set.

### Trying... 
case1: The shift number ranges from 1 to 25(26 shift is back to the same number). First brute is tried,
- 1-> XYG(FAB AEB B EZEA ZCZFF FFBB ZEDF AECZA)
- 2-> WXF(EZA ZDA A DYDZ YBYEE EEAA YDCE ZDBYZ)
- 3-> VWE(DYZ YCZ Z CXCY XAXDD DDZZ XCBD YCAXY)
- 4-> UVD(CXY XBY Y BWBX WZWCC CCYY WBAC XBZWX)
- 5-> TUC(BWX WAX X AVAW VYVBB BBXX VAZB WAYVW)
- 6-> STB(AVW VZW W ZUZV UXUAA AAWW UZYA VZXUV)
- 7-> RSA(ZUV UYV V YTYU TWTZZ ZZVV TYXZ UYWTU) 
Interesting! Hints at the password being of the format RSA(..somethign..) 
But nope, this isn't the password! Let's try just including numbers
case2: Simply add the numbers to the respective position in the previously obtained password
RSA(878ZUV 8UYV87 8V7999 Y8TYU TWT8ZZ 8ZZVV7 T7Y9XZ 8UYWTU)
But nope!
case3: 
With char set ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:
===>>> RSA(101945 148510 150222 81384 363199 199550 308279 148634)
Unlocked🥳

# Stage 2
Next, stage-2.zip is extracted. 2 files are obtained, 'Final soln_protected.pdf' and encrypt.c, which are password protected.

Info.txt
This is stage 2.
Info on encrypter's public key:
n = 421649
e = 17

Remember if you are stuck somewhere "Web.Club" will help you.

We are given info on encrypter's public key, n and e, and teh previous password hints at RSA algorithm being used. 
In RSA, the following is the computation involved to get the private key,d and public key,e.
Two large primes p and q are taken. 
n=p*q
Euler totient of n, phi(n)=(p-1)*(q-1) , since p and q are primes we get that formula for euler totient of n.
(Euler totient of n, is the number of numbers lesser than n which are relatively prime to n, ie., 
if a and n are relatively prime, gcd(a,n)=1.
A number e is choosen such that gcd(phi(n),e)=1.
A number d is found such that d == e^(-1) mod phi(n) or de == 1 mod phi(n)
Private key: {n,d}
Public key: {n,e}

To encrypt message, M: Cipher text, C == M^(e) mod phi(n)
To decrypt cipher text, C: Message, M == C^(d) mod phi(n)

In the Info.txt we are given the encrypter's public key info: 
==> n=421649 and e=17
421649 has only two factors other than 1 and itself: 557 and 757
421649=1*421649=557*757=p*q
==> p=557, q=757
    phi(n)=(p-1)*(q-1)=556*756
==> phi(n)=420336
    gcd(phi(n),e)=gcd(420336,17)=1 Yupp!
    d*17 == 1 mod phi(n)
==> d=74177
Decrypting number by number keeping the password of the form RSA(..something..),
RSA(9135 5700 6382 9648 7286 4198 1686 3054)
