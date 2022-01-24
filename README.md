# python-mnemonic
🐍 Mnemonic code for generating deterministic keys, BIP39

# New Verision in PySimpleGUI

![image](https://user-images.githubusercontent.com/88630056/150878588-1c12ab50-66fe-4b01-8d41-d91be15e9db2.png)


Installation
To install this library and its dependencies use:

pip install mnemonic

New Version 12or24 Word Choice.

![image](https://user-images.githubusercontent.com/88630056/150636896-1abda724-adb8-4251-bc34-b23ee084a772.png)

![image](https://user-images.githubusercontent.com/88630056/150636907-1cd2e5c8-a443-4978-93d9-8ac8095b010e.png)

Usage examples

Import library into python project via:

from mnemonic import Mnemonic
Initialize class instance, picking from available dictionaries:

english
chinese_simplified
chinese_traditional
french
italian
japanese
korean
spanish
mnemo = Mnemonic(language)
mnemo = Mnemonic("english")
Generate word list given the strength (128 - 256):

words = mnemo.generate(strength=256)
Given the word list and custom passphrase (empty in example), generate seed:

seed = mnemo.to_seed(words, passphrase="")
Given the word list, calculate original entropy:

entropy = mnemo.to_entropy(words)

![image](https://user-images.githubusercontent.com/88630056/149672848-3b3e6222-6527-42a1-8f95-2884181c2791.png)


```
Derivation Path :  m/44'/0'/0'/0/0  : Bitcoin Address :  15WfTLwKF6jba1DyHtDCwUXG6MVA32g9To
Privatekey WIF  :  Ky7y2YPfueYq3jn2r1KuKHQNkktSrN3J84BhidnzTGitvRgNr718
Derivation Path :  m/44'/0'/0'/0/1  : Bitcoin Address :  12PpkmUGk5DSmPinD2HxV3kWMMo1WyXCDk
Privatekey WIF  :  L1ts1KoPoyfb471tZQ22qg7V1L4CaFG2SPDePz7aViMJLJaXggZy
Derivation Path :  m/44'/0'/0'/0/2  : Bitcoin Address :  159dRmuC8P7vDDQniFnJihQKRGMvkfHwec
Privatekey WIF  :  L45Q32A4RTscLv36eZzE3N5ehibBbpJUQjAzC1yTBrLwUqiDJzKv
Derivation Path :  m/44'/0'/0'/0/3  : Bitcoin Address :  1HRXcHnoBFdM8KnyPfaSMJd2JQyXQVGCLM
Privatekey WIF  :  L4LbLYTLjLEgpp5ErZizUbcK6DEhKVkwc1nfN9dBK3brGXgRGUPM
Derivation Path :  m/44'/0'/0'/0/4  : Bitcoin Address :  1GPYzPGqD4GotpovY2S7WtvYHrzCpLxcsN
Privatekey WIF  :  L1aq6DLJkawVRqWrqApcQtmpDq46snGHgGKKeuCr2spqux7sggcM
Derivation Path :  m/44'/0'/0'/0/5  : Bitcoin Address :  1L8KpATECWk5K3uMc9nUkS3BTzsw6Gj5KF
Privatekey WIF  :  L4PYmumQnUbe1yqYXEa4xpRaa4Y4JF6wbnrYxHPq6P5eVVXwEXWU
Derivation Path :  m/44'/0'/0'/0/6  : Bitcoin Address :  1JJiXTqDjPooP5SNnALDm6iZT3Eu9T371M
Privatekey WIF  :  L1iSkBLvm8BFDeQrAPHnXZLWhpMFxx1ijbSgtu3B4AJa6v2FT84v
Derivation Path :  m/44'/0'/0'/0/7  : Bitcoin Address :  16ws6CYKV5Dyprw7V1NheZiDmofetHzbzT
Privatekey WIF  :  KxUbZ3KjUv9BND1s1B6GA48pcDXFasMCEnqK1UTVGpBvLhkekvMQ
Derivation Path :  m/44'/0'/0'/0/8  : Bitcoin Address :  16edyhibpGhH7Jyjp6dJLwBkzLAuMBjw1c
Privatekey WIF  :  Ky6x6vT8xVh5E9uZVy1S92AvTkh85THF74YCaHavwQrndkLLh1w6
Derivation Path :  m/44'/0'/0'/0/9  : Bitcoin Address :  1NwFWrr3XZ6gAKyiJxhR2yEgo5SJeVgwdT
Privatekey WIF  :  L2G6QmhTd4KK8ot4x24Po7fHEXztbDCA6HFakeSgVkvGzxUbM5gq
Derivation Path :  m/44'/0'/0'/0/10  : Bitcoin Address :  14mKm1SkxbiZKWiiACKVfdZBkZpXaTn6aB
Privatekey WIF  :  L191wtXBDT3LPE85kZ2k8NyjobPVbioHNuBD6r5NDwWYwP3nMWAR
Derivation Path :  m/44'/0'/0'/0/11  : Bitcoin Address :  16yc5kEd5Kq3MCrYEWYMi8sGeRKhwuBPxR
Privatekey WIF  :  L3bWukmGxG5H1PHWGBWWtZr58vGQ7xE9xtMX2RUnMwPQYHJwp69c
Derivation Path :  m/44'/0'/0'/0/12  : Bitcoin Address :  1LnPNzwGxFPdeGXzN6LV2ZkNhisjkDrzsa
Privatekey WIF  :  KwEkpqJeN4nP7PZXj8Bmzoaef8Z7aNPnq2pD61TsjNRUAUgXitrs
Derivation Path :  m/44'/0'/0'/0/13  : Bitcoin Address :  1NdDEUENqLsBCNjuZSoRWPV58hStxeu6sf
Privatekey WIF  :  L5WTyaeJKM6D7ZYztR82psJqApyjf2AhmD2ZdrCGmVpgNo9Gs311
Derivation Path :  m/44'/0'/0'/0/14  : Bitcoin Address :  1ksgToFMVwyG5bN54hDSsHHD6wPMWrfx6
Privatekey WIF  :  KzsheRoqHaYkodFvrW6NdqQmsamcjgv453NhkWDAfycv7Jfbbb1Y
Derivation Path :  m/44'/0'/0'/0/15  : Bitcoin Address :  16yR1M1KUUn5y9tcfdzsoJX7j1EDSpo3hM
Privatekey WIF  :  KwiJWucztrqva37viKRbN9xr1wCjZevaLSqeL4h7KHTgevHxrf6M
Derivation Path :  m/44'/0'/0'/0/16  : Bitcoin Address :  14QYRPcPjfq73i4GtbPMi2d7gUZQPrVsVh
Privatekey WIF  :  L1oZzvdPL27KaiED7e7xSJs6PTWe5unG5SnBrEk551w5wmgrYc3w
Derivation Path :  m/44'/0'/0'/0/17  : Bitcoin Address :  1CmW9rkyab6Naovom1uJ1S3ti4KFXighQs
Privatekey WIF  :  Kwm9QxAhzMH8b7ugzsREQpc8FymaFipeWEnVKpxh6u75HiKC8fXe
Derivation Path :  m/44'/0'/0'/0/18  : Bitcoin Address :  1CZyD5WswD4PxQVBP4aYzrtNhSoBPd9KT5
Privatekey WIF  :  KzNsKKXgyrehFf6tBmzM9Asfh3YjaPaHSRsSHusWQPpK93doscPr
Derivation Path :  m/44'/0'/0'/0/19  : Bitcoin Address :  1ASSUrBUzWi1zb1SbxpVHYatBZrGJucvDd
Privatekey WIF  :  L4Aoesz3p5NDyLesRmmhR9FkWqBPxh4hfk7NhLz9WTAt4xin5zkD
Derivation Path :  m/44'/0'/0'/0/20  : Bitcoin Address :  1FwdJwG9yEUsGKUQvxAbyGvTHBifd21rYL
Privatekey WIF  :  KxnntMAnuZoCxuB8qREnbzoXefBrEZy8YjSsqTEHPmTS795FZtJ1
Derivation Path :  m/44'/0'/0'/0/21  : Bitcoin Address :  1HHNXuCjf5gwDjUcgZVGjrAZPqSWNxCidT
Privatekey WIF  :  KwhaUUrhjc717WG6yJkQFwwM52jcg8pCGnHcbnCb9wwksBY1mA6k
Derivation Path :  m/44'/0'/0'/0/22  : Bitcoin Address :  1FA3afzNUkczHij6mZFoJnMB32eHrkHDUv
Privatekey WIF  :  KyjCCP6ze2m6CHHJjhVzf5McshgyVp83Uo9FKJYhom4hGXRUzG4g
Derivation Path :  m/44'/0'/0'/0/23  : Bitcoin Address :  1bUYC6xW4NfbS8npWzCgLuYzMgfXAr2DT
Privatekey WIF  :  L2paSeFFzrqYaqpFjfWiCZ2qjxMvAHSWHX1z4c9Mdp1vHYycVvrD
Derivation Path :  m/44'/0'/0'/0/24  : Bitcoin Address :  15Dq3MbKh2t61eLGeVr9q2G8p4YxZfieDr
Privatekey WIF  :  KzdQwWmy1S2WzhwB3HpUsH4qxzkS5sAwBkKJh2rEDLG5nWwGoxhw
Derivation Path :  m/44'/0'/0'/0/25  : Bitcoin Address :  1LVtJvwQu1YnGgeFQujtAAHjrJ8EHGmBUB
Privatekey WIF  :  L1eoANg4aUTw7W6EbF6mZGz1Ms43VgQ8x97kU53TbtVFKJj5hA2N
Derivation Path :  m/44'/0'/0'/0/26  : Bitcoin Address :  14oUo5wgUNvpjN9QSYo2Y9P3M4uPGuDS6S
Privatekey WIF  :  L4LJq5meSK8ciunRCzSwFyk9hGafk1Uvh759PzWhmTns2tjA2jcZ
Derivation Path :  m/44'/0'/0'/0/27  : Bitcoin Address :  1FBchHCoCS7yJA8Rdrr3K6X8uSLphWs4rx
Privatekey WIF  :  Kx69gLmMWmyANe98SGZRz9WNz1MLRu97dqRmD5e9xftLJcRC4orY
Derivation Path :  m/44'/0'/0'/0/28  : Bitcoin Address :  1L2GDdbhow81JjfYm3Y9jiMEecb58prSVj
Privatekey WIF  :  L5LebHYazbAt6yotNjzapj5g4Mm4eUwb9eg8ZEuqJEgC5wDZ5jFZ
Derivation Path :  m/44'/0'/0'/0/29  : Bitcoin Address :  1Pntu6sXkgQNJc2ni48nPLqiiw4wXFh1Zq
Privatekey WIF  :  L1Xa2c2ZYQwvAF73XDDV5hUfAfPTK5MB7R3JuXm2mecF8BrmmdY1
Derivation Path :  m/44'/0'/0'/0/30  : Bitcoin Address :  12FohCdVT4TSqQASt1Q3K6vg7QZ5Mk8MPi
Privatekey WIF  :  L3RQ5bkQKbHwsnqTaGBNNv7VjV3WAJSp55jvENEBhD6chHWJe8bx
Derivation Path :  m/44'/0'/0'/0/31  : Bitcoin Address :  1G9SkucG5kFk8JeGELAspRxjaKDajk3qTu
Privatekey WIF  :  L3xx4hkPymcdMdvvYwAY51Kh9yopDVkEndBo7Z6TkbqKyhGNaHgw
Derivation Path :  m/44'/0'/0'/0/32  : Bitcoin Address :  19YERz1KFV8iBZwG1fWmCyXkjRD3GwVa5c
Privatekey WIF  :  Kxt3SBEBcBt9cRgNvAXasdLNFbssUPBjuqFYhNdggiGBtzPDcKC1
Derivation Path :  m/44'/0'/0'/0/33  : Bitcoin Address :  1PcwXB8hoAKkfRp678ygLKbH8VFF7vwCtB
Privatekey WIF  :  L5C5vAzbC6vAAuCC7jZ6qshzDuE8d7hKctTGjjCghJdZ18y72uTW
Derivation Path :  m/44'/0'/0'/0/34  : Bitcoin Address :  1DAr6Gp4e3odVqpy2iiGKTj761drFRb5K
Privatekey WIF  :  Kzx1KZR7tD6BAnmwXU5QfWp5dAAdxdWhH2qsZ794da5roDcJHETG
Derivation Path :  m/44'/0'/0'/0/35  : Bitcoin Address :  1K9a7wtvR3Hste2PihZ2EDDGUR38xeG1yW
Privatekey WIF  :  L5cFFgbszdQWmsj6Xt8VgFu8bup5Q5YPBZGoWX1v7qqYPwraP4Gn
Derivation Path :  m/44'/0'/0'/0/36  : Bitcoin Address :  1y8Hyg82zKutSuXo1MtPMZKS9gPif9Ehp
Privatekey WIF  :  KxuazYstdEMqDaKHUh2CMev4L3VBznjr7TPWiJ546vWWb2FcXBDK
Derivation Path :  m/44'/0'/0'/0/37  : Bitcoin Address :  16KqnPGS1FVVpHwXxQwBMY4pEjR4s4s2zK
Privatekey WIF  :  KzPMh7wCtfR2XQd5ooi6NDwJarkKUVF3GYp8DdTbBmWQ4zw3F8Xf
Derivation Path :  m/44'/0'/0'/0/38  : Bitcoin Address :  16kQALQ5Viw2fF5Bcjmr5h2x1ETozaB6FB
Privatekey WIF  :  L3MBWi5tEW9RJQTVdATqoi3pd2dj2L6JUKattKxXo45eQhUtePzh
Derivation Path :  m/44'/0'/0'/0/39  : Bitcoin Address :  16XSS1KTfgWHm6XuQWKSCi9yYLbQucnDD2
Privatekey WIF  :  KyHLyWaFLpaLCk7XKu6sEQG2UpeoajKUvNedhL6wrXB5i2MfSKT3
Derivation Path :  m/44'/0'/0'/0/40  : Bitcoin Address :  1EQwCC9NbH4zjzsqLjU1msLCDStX1RY18c
Privatekey WIF  :  L5SoEx7QqYamy2dSTDxjbn1LydLY55Ab8pbGDV54v3RKr5R29DG6
Derivation Path :  m/44'/0'/0'/0/41  : Bitcoin Address :  13bpF4eMygK8hN6AdjKoaauZ8w6sRqNd22
Privatekey WIF  :  KzapLVBvJQo5tog2CRT6DYEtGAhrMyjU9TYwyuqENVnau28TYYPj
Derivation Path :  m/44'/0'/0'/0/42  : Bitcoin Address :  1MdtvUzTk3bRGkvZVJ33VG42fSSDat46Wv
Privatekey WIF  :  L26pHhwRDUmNrLz4wK9odVTUSkNAxufrwhHXdVejRQu6uyrry786
Derivation Path :  m/44'/0'/0'/0/43  : Bitcoin Address :  19iwCDCPQueBaKSEBWndZLyZ2Cz4ZxqfR6
Privatekey WIF  :  L19QV6mncYVKZkzabcdjkQKgPz3iGihC23x79ZB6oFQE6rFhGZ97
Derivation Path :  m/44'/0'/0'/0/44  : Bitcoin Address :  16f5Ch31xS8JacTtY4D8wUTvmPjQBZ5R21
Privatekey WIF  :  Kypcep8o4d8AAhPny9df2zTUCT8MrS9uhSiuY3xzXCx4YdnPFzFC
Derivation Path :  m/44'/0'/0'/0/45  : Bitcoin Address :  1EYAgXmczzDqsHCiLGBbDzvkDdcNTXQks
Privatekey WIF  :  L34AxWYn3RTF5ibU8PLjfzMg5xLGeSuTWcnWHjChTg1G7hmnjdUP
Derivation Path :  m/44'/0'/0'/0/46  : Bitcoin Address :  1AQwc2oDVT84Toj3JnFGeTJM36JcGMPJ6H
Privatekey WIF  :  L2Dmpra756P4mC1K3se6gcAqnXUgvSkQazivU9XpRsQE7uoDNLWc
Derivation Path :  m/44'/0'/0'/0/47  : Bitcoin Address :  1Jarxikvh9NeYqNUv4DAGfwXJE6C87VUEs
Privatekey WIF  :  L2r4TTJb8tsWDwCmKGqTzGzTERYMe5Cp7cXY5SQSVM827Kpw2oVP
Derivation Path :  m/44'/0'/0'/0/48  : Bitcoin Address :  1GUAjFfGcwgfaJBRDkJ4R4JYXQTEsi7Rp6
Privatekey WIF  :  L2rdJsz6N6QQNXc9AuYtiY76nfJmNvZkgozSjKKUWwmKK4wnWepF
Derivation Path :  m/44'/0'/0'/0/49  : Bitcoin Address :  1Ce4G5JxN62FaSdmFojTDFqfm2EpwNVMxP
Privatekey WIF  :  KwnxXSPADyy2Aq6ekhKMDYQFdmM2fggBcW1gMURc4mQtetuVM7mg
Derivation Path :  m/44'/0'/0'/0/50  : Bitcoin Address :  14qvVimW873XaB7kfdpcbFmntcPwNdcT4R
Privatekey WIF  :  L1p6BaQ8kEnfD56rUnMZLmcDCRaGDBgWLKRwazrPxXmT3sA7xHQ9
Derivation Path :  m/44'/0'/0'/0/51  : Bitcoin Address :  14ESqFvsnHBs5HrmLbiAJDwqbG6pF78dE7
Privatekey WIF  :  KzLEugncDPEZTgU1k5H1GDwoibtppyYhRnDe8CFfHtQ9Cuc1BGYw
Derivation Path :  m/44'/0'/0'/0/52  : Bitcoin Address :  1M1deyhimHWCrktf9G1fEoa4XNZsUxr5Hd
Privatekey WIF  :  Kx3C3VwJSMta5PBh4Hckc628XhD1Gu3D5NeBHU6YfKq51LjCfT4U
Derivation Path :  m/44'/0'/0'/0/53  : Bitcoin Address :  12MaXGC5yaQ28WCypYVG6VkNtj9BdGVL6p
Privatekey WIF  :  L4YxHT5hG9A8fUpv8SrXLnwJL3f42mk2JTSHZ7buGCTxXBtJko2F
Derivation Path :  m/44'/0'/0'/0/54  : Bitcoin Address :  18wNciZjJH1bYVxJETTLbEPo1EpYhno7rL
Privatekey WIF  :  L1LbTSGL4AviHCZbyzB3Fi2SiYYSFwtYpM8Z2ND6Pu3w8kMEgZpN
Derivation Path :  m/44'/0'/0'/0/55  : Bitcoin Address :  1MsaBNtcvQGQaKv5nBqMuTZBcwYsH3Fmpx
Privatekey WIF  :  L4paoZNJPAhrp6y4c1iZg7oWobtavE5gcLQB4dBUstwr5r4hBzAr
Derivation Path :  m/44'/0'/0'/0/56  : Bitcoin Address :  164PwMgr6PDC1kcCrp1PUTJrMDL4xgqxwY
Privatekey WIF  :  KxMyJ5Zsbst9xXyS1u6ELPZ74JSZZAwKmn6p89aB5Xmu8Xfs2ANf
Derivation Path :  m/44'/0'/0'/0/57  : Bitcoin Address :  14J23bxeijT7nD6fBbT2kNGrLVBGvc6xJv
Privatekey WIF  :  L4EdCfxgZPmy43S6DyP1ThaPiopHt34q7oNddLsdgpDDgwiG3epQ
Derivation Path :  m/44'/0'/0'/0/58  : Bitcoin Address :  1HUpVBWYawJknkk73qx4r4SReVQ2YKHPdJ
Privatekey WIF  :  L34nQsGt8s78C9kC9vNCuK6JuYJeg3Rz1ibmUcQ5T2cJiH53ZxZH
Derivation Path :  m/44'/0'/0'/0/59  : Bitcoin Address :  1CTzRTkXLMcAXWFGLeXMeMPbcikBjX2HcP
Privatekey WIF  :  L1SVTBnPob3Exis9QPiqKdU3nq7EmC6Wi3T8ChKQs6ttF3qkh1Ek
Derivation Path :  m/44'/0'/0'/0/60  : Bitcoin Address :  1JPQ5v2yBRAem8ttviDQLyk9betmoCRJr9
Privatekey WIF  :  KznE6H2FUE9yA8sfEVXj1YnTupMrH1mim1rmBUGbjJE13jK8V3yX
Derivation Path :  m/44'/0'/0'/0/61  : Bitcoin Address :  1L6D2z3hABSZedAGA9QENpKCe2SRiyJCvg
Privatekey WIF  :  L3r9sjZnGa9Ca36Xx1W3tXMweXFAEtLWiGyQb2YBbSXVjwoN93Xc
Derivation Path :  m/44'/0'/0'/0/62  : Bitcoin Address :  1NLwnjWuBGRmRKZVXr48Lr8Sh5QKovCTPK
Privatekey WIF  :  L2FjKFofibD7fT1Dx1LT28dS4MyGxhgV1VPW4HhDUivpUv1Fg81K
Derivation Path :  m/44'/0'/0'/0/63  : Bitcoin Address :  1Mb5kC7J5ysxu8ZAPhswM6NjC2sW6LHNTv
Privatekey WIF  :  KwoFnpWWme4631SuQxiXnC4iFMy7JUx2cx8ZcT2Nfw2FcKT7LgCu
Derivation Path :  m/44'/0'/0'/0/64  : Bitcoin Address :  1Q8Zi6qsA9ytxJkYv5LEJpwFtjrN9bhXP2
Privatekey WIF  :  L1P7xrP3pxU4odurYSkbGYfy2tPvKBFTAGfyi6ck1CyTu3ztntPe
Derivation Path :  m/44'/0'/0'/0/65  : Bitcoin Address :  1KJoYPJXuA2iyZ2wW4PEo1BdiU98tAarbp
Privatekey WIF  :  KweGZ7KU4U8CarQvbB4RBgKbsd3mHWkAzRU3vHjhZ8EnquNjeZ26
Derivation Path :  m/44'/0'/0'/0/66  : Bitcoin Address :  1G35mf1M2KeVJAgpH5AVVb4odbiqpQGBNC
Privatekey WIF  :  L4ka7ZR9pTd2xAizC8q1FSuQsmgYCYV6YuYyffwKXFuL1muRvpxn
Derivation Path :  m/44'/0'/0'/0/67  : Bitcoin Address :  13CkdfRfoVnL7DtnN4nVt7J38zvKtmCiAn
Privatekey WIF  :  L535EUDXZRVksRiFaiti9UhpW4th1rJYPCKNkzMj6j8XiP49o6eS
Derivation Path :  m/44'/0'/0'/0/68  : Bitcoin Address :  183znJcTTdS89tYTc1HnUAAZdfMEDBpq7U
Privatekey WIF  :  KxkhzvsFfXt7aeFE2EjhmGatUL4T1j7ckNzVHyBU2zD6cgi5dvEu
Derivation Path :  m/44'/0'/0'/0/69  : Bitcoin Address :  1ANydA3XYXfBzmEpyk5FfUeCZcUwsuhkM8
Privatekey WIF  :  L26eqVrkA3KYrTanFNxfRxLY2x5cnMSgorFrsPubNVWAdrjHYAK7
Derivation Path :  m/44'/0'/0'/0/70  : Bitcoin Address :  1JkVeg6o69r4zpqpHShN4yCAbuMFdEYk3c
Privatekey WIF  :  KwWA1C5sGUArffKmrZoXuSTfZXGkFnTkFy1ETTJjdBTtZZmDys7D
Derivation Path :  m/44'/0'/0'/0/71  : Bitcoin Address :  1QDUvmyXEfBdeARLdX2P4Tp6RANPiryzHJ
Privatekey WIF  :  L1Q7BgiALZJnek9cmcZhjN2MAswhc9UJxifF1oKqzZzZ8n3dn1rX
Derivation Path :  m/44'/0'/0'/0/72  : Bitcoin Address :  1EDVFYNeBtqv8f3x7VbPJG8CJwaLRHbXg4
Privatekey WIF  :  L3zN9dTfnVUByA4a5E1HziBBJfV49bvsTgtSD64H3a2KUyF41TSB
Derivation Path :  m/44'/0'/0'/0/73  : Bitcoin Address :  1MguGetaKNQgtYYgNcFGapGFfqTe2Keqsm
Privatekey WIF  :  KyFqyZmXmXXpFBU8RyHJv5VJvEtQmLC2TXVgJRG1YXVhxZ4F43X4
Derivation Path :  m/44'/0'/0'/0/74  : Bitcoin Address :  1CZCt4MKQJsR7zMkCvDiN4z6CCt22KsXr1
Privatekey WIF  :  KwPa83jukaf7HiGUP8EdAaEyRjQcBEAs2zr2hAUKSSTkGJmXBAVM
Derivation Path :  m/44'/0'/0'/0/75  : Bitcoin Address :  13wox2NdsKhqzjW1Tw2KKGpfiGg2a7o1Lj
Privatekey WIF  :  L27xsiDdPZ2ry9igVFxepJhjosJ6sLExnoZ8gEYuC4zCv1GDmcmD
Derivation Path :  m/44'/0'/0'/0/76  : Bitcoin Address :  1ML9wGCZrj65Y7h7EWFgS8MqPwRrdRmiuJ
Privatekey WIF  :  L5MHmgN8msd66NWKnkJGjSddQvh9SBMyRBdw9fZ3hpgWnymiX7UD
Derivation Path :  m/44'/0'/0'/0/77  : Bitcoin Address :  12na4aAUopniGCkDtQHvTyUJbWrNEopcHy
```
