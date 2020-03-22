# 📟 CryptoGraphy Tool 

***Hello everyone, today I present two new tools in the encryption / hashing category. These tools are used to encode a message, a password with different methods.***

<img src="https://github.com/pyr3q/PythonProject/blob/master/CryptoAPP/IMG/image1.png" width="200"> <img src="https://github.com/pyr3q/PythonProject/blob/master/CryptoAPP/IMG/image2.png" width="300">

# How To Install ?

<img src="https://i0.wp.com/www.jflinch.com/wp-content/uploads/2014/12/question-person-1.jpg" width="300">

```root@gnu:~# apt-get install git && git clone https://github.com/pyr3q/PythonProject/CryptoAPP | chmod +x install.sh && ./install.sh | python program.py```

# 🔑 Encoding By MD5 Method

***What is MD5?***

***I will try to explain what the MD5 is simply through this README***
***MD5, for Message Digest 5, is a cryptographic hash function that allows you to obtain the digital fingerprint of a file (we often speak of a message). It was invented by Ronald Rivest in 1991.***

***MD5 (Message Digest 5) is a cryptographic hash function that calculates, from a digital file, its digital fingerprint (in this case a sequence of 128 bits or 32 characters in hexadecimal notation) with a very high probability that two different files give two different fingerprints.
MD5 uses 64 constant 32-bit word values <img src="https://github.com/pyr3q/PythonProject/blob/master/CryptoAPP/IMG/image5.png" width="200"> , denoted image these numbers represent sines of integers. The following values are expressed in hexadecimal (base 16) notation.
They can be obtained with the formula*** ```floor (abs (sin (i + 1)) × 2 ^ 32)```

<img src="https://github.com/pyr3q/PythonProject/blob/master/CryptoAPP/IMG/image4.png" width="700">

***The main algorithm works with a state on 128 bits. It is itself divided into 4 words of 32 bits (in computer science, we use the term "word" to designate a value of 32 bits or "word" in English): A, B, C and D. They are initialized at start with constants. The algorithm then uses the blocks coming from the message to be hashed, these blocks will modify the internal state. The operations on a block are broken down into four rounds (steps), themselves subdivided into 16 similar operations based on a non-linear function F which varies according to the round, an addition and a rotation to the left. The four non-linear functions available are:***

<img src="https://github.com/pyr3q/PythonProject/blob/master/CryptoAPP/IMG/image6.png" width="300">

**🔎 PseudoCode**

***MD5 can be written in this form in pseudo-code:***
```//Note : All variables are 32-bit

//Define r as follows:
var entier[64] r, k
r[ 0..15] := {7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22}
r[16..31] := {5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20}
r[32..47] := {4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23}
r[48..63] := {6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21}

//MD5 uses integer sines for its constants:
for i from 0 to 63 do
    k[i] := floor(abs(sin(i + 1)) × 2^32)
end for

// Preparation of variables:
var entier h0 := 0x67452301
var entier h1 := 0xEFCDAB89
var entier h2 := 0x98BADCFE
var entier h3 := 0x10325476

// Preparation of the message (padding):
add bit "1" to the message
add the bit "0" until the message size in bits is equal to 448 (mod 512)
add the size of the initial message (before padding) coded in 64-bit little-endian to the message

// Split into 512-bit blocks:
for each 512 bit block of the message
subdivide into 16 32-bit words into little-endian w[i], 0 ≤ i ≤ 15

// initialize hash values:
    var entier a := h0
    var entier b := h1
    var entier c := h2
    var entier d := h3

    //Principal while :
      for i from 0 to 63 do
       if 0 ≤ i ≤ 15 do
              f := (b et c) ou ((non b) et d)
              g := i
        else if si 16 ≤ i ≤ 31 do
              f := (d et b) ou ((non d) et c)
              g := (5×i + 1) mod 16
        else if 32 ≤ i ≤ 47 do
              f := b xor c xor d
              g := (3×i + 5) mod 16
        else if 48 ≤ i ≤ 63 do
            f := c xor (b or (not d))
            g := (7×i) mod 16
        end if
        var entier temp := d
        d := c
        c := b
        b := leftrotate((a + f + k[i] + w[g]), r[i]) + b
        a := temp
    end for

// add the result to the previous block:
    h0 := h0 + a
    h1 := h1 + b 
    h2 := h2 + c
    h3 := h3 + d
end for

var entier footprint := h0 concatenate h1 concatenate h2 concatenate h3 //(in little-endian)
```


# 🔑 Encoding By SHA-256 [ SHA-2 ] Method

***SHA-2 (Secure Hash Algorithm) is a family of hash functions which were designed by the <a href="https://nsa.gov/">National Security Agency of the United States (NSA)</a>, on the model of the functions SHA-1 and SHA-0, themselves strongly inspired from the MD4 function of Ron Rivest (who also gave MD5). As described by the National Institute of Standards and Technology (NIST), it includes the functions, SHA-256 and SHA-512 whose algorithms are similar but operate on different word sizes (32 bits for SHA-256 and 64 bits for SHA-512), SHA-224 and SHA-384 which are essentially versions of the previous ones whose output is truncated, and more recently SHA-512/256 and SHA-512/224 which are truncated versions of SHA-512. The last suffix indicates the number of hashed bits.***

<img src="https://upload.wikimedia.org/wikipedia/commons/7/7d/SHA-2.svg" width="400">

***Like all the hash functions, the SHA-2 functions take as input an arbitrarily sized message, with a (all theoretical) bound for it, and produce a result (called "hash", hash, condensate or even imprint ...) fixed size. The size of the hash is indicated by the suffix: 224 bits for SHA-224, 256 bits for SHA-256, 384 bits for SHA-384 and 512 bits for SHA-512.
The SHA-2 algorithms are very similar, there are essentially two different functions, SHA-256 and SHA-512, the others being variants of either. The SHA-256 and SHA-512 functions have the same structure but differ in the size of the words and blocks used.***

# 📚 Function
***This section describes the functions used when calculating hash values. SHA-256 uses 6 logic functions working on 32-bit words denoted x, y, z. The result of each of these functions is a new 32-bit word as output.***

<img src="https://github.com/pyr3q/PythonProject/blob/master/CryptoAPP/IMG/image7.png" width="400">
 
