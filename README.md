# Cryptography task Wec Recs-

The 'Cryptography Question.zip' file has two files: welcome.txt and stage-1.zip<br>
On extracting stage1.zip, two files are found stage-2.zip and Info.txt, which are password protected. <br>
Checking welcome.txt for hints to the password.<br>

<details>
  <summary>welcome.txt<br></summary>
  Let me tell you about Julius Caesar. He started using Caesar cipher, one of the simplest and most widely known encryption <br>
  techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed <br>
  number of positions down the alphabet.<br>
  The password is<br>
  YZH(878GBC 8BFC87 8C7999 F8AFB ADA8GG 8GGCC7 A7F9EG 8BFDAB)<br>
  But, is it though?<br>
</details>


## Stage 1
The welcome.txt file hints at caeser cipher being used to encrypt the password. Another observation is that numbers are <br>
present too. The traditional caeser cipher has only letters. So considering three cases:<br>
1) Remove the numbers and decrypt the rest. Maybe the numbers are used as salt on the password..<br>
2) Keep the numbers as they are and decrypt teh rest. Maybe the numbers are used later or somthin..<br>
  (Collecting the numbers together we get: 878 887 87999 8 8 87 97 8, just a bunch of 7s,8s and 9s, could't find anything useful from this)<br>
3) Include numbers in the character set.<br>

### Trying... 
case1: The shift number ranges from 1 to 25(26 shift is back to the same number). First brute force is tried,<br>
- 1-> XYG(FAB AEB B EZEA ZCZFF FFBB ZEDF AECZA)
- 2-> WXF(EZA ZDA A DYDZ YBYEE EEAA YDCE ZDBYZ)
- 3-> VWE(DYZ YCZ Z CXCY XAXDD DDZZ XCBD YCAXY)
- 4-> UVD(CXY XBY Y BWBX WZWCC CCYY WBAC XBZWX)
- 5-> TUC(BWX WAX X AVAW VYVBB BBXX VAZB WAYVW)
- 6-> STB(AVW VZW W ZUZV UXUAA AAWW UZYA VZXUV)
- 7-> RSA(ZUV UYV V YTYU TWTZZ ZZVV TYXZ UYWTU) <br>
Interesting! Hints at the password being of the format RSA(..somethign..) <br>
But nope, this isn't the password! Let's try just including numbers<br>

case2: Simply add the numbers to the respective position in the previously obtained password<br>
RSA(878ZUV 8UYV87 8V7999 Y8TYU TWT8ZZ 8ZZVV7 T7Y9XZ 8UYWTU)<br>
But nope!<br>
case3: <br>
With char set ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:<br>
===>>> RSA(101945 148510 150222 81384 363199 199550 308279 148634)<br>
Unlocked🥳<br>

## Stage 2
Next, stage-2.zip is extracted. 2 files are obtained, 'Final soln_protected.pdf' and encrypt.c, which are password protected.<br>

<details>
  <summary>Info.txt<br></summary>
  This is stage 2.<br>
  Info on encrypter's public key:<br>
  n = 421649<br>
  e = 17<br>
<br>
Remember if you are stuck somewhere "Web.Club" will help you.<br>
</details>

<br>
We are given info on encrypter's public key, n and e, and teh previous password hints at RSA algorithm being used. <br>
In RSA, the following is the computation involved to get the private key,d and public key,e.<br>
Two large primes p and q are taken. <br>
n=p*q<br>
Euler totient of n, phi(n)=(p-1)*(q-1) , since p and q are primes we get that formula for euler totient of n.<br>
(Euler totient of n, is the number of numbers lesser than n which are relatively prime to n, ie., <br>
if a and n are relatively prime, gcd(a,n)=1.<br>
A number e is choosen such that gcd(phi(n),e)=1.<br>
A number d is found such that d ≡ e^(-1) mod phi(n) or d * e ≡ 1 mod phi(n)<br>
Private key: {n,d}<br>
Public key: {n,e}<br>

To encrypt message, M: Cipher text, C ≡ M^(e) mod phi(n)<br>
To decrypt cipher text, C: Message, M ≡ C^(d) mod phi(n)<br>

In the Info.txt we are given the encrypter's public key info: <br>
--> n=421649 and e=17<br>
421649 has only two factors other than 1 and itself: 557 and 757<br>
421649=1 * 421649=557 * 757=p * q<br>
--> p=557, q=757<br>
    phi(n)=(p-1) * (q-1)=556 * 756<br>
--> phi(n)=420336<br>
    gcd(phi(n),e)=gcd(420336,17)=1 Yupp!<br>
    d * 17 ≡ 1 mod phi(n)<br>
--> d=74177<br>
Decrypting number by number keeping the password of the form RSA(..something..),<br>
RSA(9135 5700 6382 9648 7286 4198 1686 3054) But, that's not teh password :( <br>

Converting 'Web.Club' to ascii => 8710198466710811798 
On decrypting, rsa: 
33578
