## 2021 Project 2

![](logo.png)

Ερωτήσεις:

1. Πού βρίσκεται ο Γιώργος;
1. Ποιος έκλεψε τα αρχεία του "Plan X";
1. Πού βρίσκονται τα αρχεία του "Plan X";
1. Ποια είναι τα results του "Plan Y";
1. Ποιο είναι το code του "Plan Z";




#### Παρατηρήσεις

- Οι ίδιες ομάδες με την εργασία 1
- Εγγραφή στο github: https://classroom.github.com/g/jlkOQHdH 
- Μόλις ολοκληρώσετε κάθε βήμα στέλνετε claim στο ys13@chatzi.org
- Για τα βήματα 3-5 απαιτείται να γράψετε ένα πρόγραμμα που να αυτοματοποιεί την εύρεση της λύσης.
  Μπορείτε να χρησιμοποιήσετε ό,τι γλώσσα προγραμματισμού θέλετε, αλλά θα πρέπει να μπορώ να το τρέξω
  σε Ubuntu 20.04 χρησιμοποιώντας software που είναι διαθέσιμο στο Ubuntu. Θα πρέπει επίσης
  να φτιάξετε ένα script `run.sh` που εκτελεί το πρόγραμμα με ό,τι παραμέτρους χρειάζονται.
- Επίσης γράφετε report στο README.md με τα βήματα που ακολουθήσατε, και το κάνετε commit μαζί με οποιοδήποτε κώδικα χρησιμοποιήσατε
- Βαθμολογία
    - Η δυσκολία στα βήματα αυξάνεται απότομα.
    - Για ό,τι δεν ολοκληρώσετε περιγράψτε (και υλοποιήστε στο πρόγραμμα) την πρόοδό σας και πώς θα μπορούσατε να συνεχίσετε.
    - Με τα πρώτα 2 βήματα παίρνετε 5 στο μάθημα (αν έχετε πάει καλά στην εργασία 1)
    - Με τα 3-5 φτάνετε μέχρι το 10 (δεν υπάρχει γραπτή εξέταση)
    - Για τους μεταπτυχιακούς τα 3-5 είναι προαιρετικά. ΔΕΝ αντικαθιστούν το project
     (αλλά μπορούν να λειτουργήσουν προσθετικά στο βαθμό της εργασίας 1)
    - Για τα βήματα 3-5 μπορεί να γίνει προφορική εξέταση
- Timeline
    - Την πρώτη εβδομάδα δεν υπάρχουν hints
    - 11/6: αρχίζουν τα hints για τα βήματα 1,2
    - 16/6: deadline για τα βήματα 1,2
    - Για τα βήματα 3-5 δίνονται hints μόνο σε όσους ζητήσουν (με μικρό penalty)
    - 11/7: deadline για τα βήματα 3-5
- Η ταχύτητα των λύσεων (και ο αριθμός hints που έχουν δοθεί) μετράει στο βαθμό
(ειδικά για τα βήματα 1,2)

- __Οχι spoilers__
- __Οχι DoS__ (ή μαζικά requests, δε χρειάζεται
κάτι τέτοιο)


# CTF Report

## Step 1

### First things first
While visiting and browsing the code of the instructor-given .onion link, we skimmed the blog-article about onion site security, hence we discovered that the site-creator allowed us to view the `/server-info` page. There we discovered the existence of a second site. At the same time we noticed that the cookie in the site, when changed, printed some interesting messages in the user id section. We also discovered that the cookie was generated by the following algorithm:
```
Let 'L' be the message you want to display in user id field. 
1) Y = "SHA256(L)"
2) X = "L:Y"
3) COOKIE = BASE64(X)
```
so we constructed a small python script to generate cookies that would print our desired input.

### The bypass

Visiting the second site we bumped into a user validation page. Since we failed to login with simple credentials, we checked the respective `/server-info` page and also we tried to access the `/robots.txt` page, where we found something quite interesting: `.phps` files where allowed, but why? So we checked if there was a `access.phps` page. So now we just had to find the `$desired` variable, being *1337* and now we had to find the password. After a little googling we found out that the `strcmp()` function was quite vulnerable even if the condition check was *strict*. We could pass an array as `$password` and bypass the login section. We tried something like this: `?user=0001337&password[]=0`.

### Blogging

After loggin in, we browsed the blog a little and found out a quite-obscurely hidden post-page named `/post3.html` under `/blogposts7589109238/` that actualy gave us the user-id we had to use at *YS13 fixers* site. Using our script and changing the cookie via the `document.cookie` attribute in the JS console, we found about George Komninos' secret back-up, that contained the encrypted files of firefox and signal logs, so we knew that should do it, but we did not find the decryption key... yet.

### Ethereum Transactions

Reading the note George left, we got interested in the meaning of the last line `ropsten <hex number>`. We tried to transform it to ascii, in case we got anything secret-like and that failed. Then we googled about `ropsten`. Firstly, we found it was a transaction wallet, but (little did we knew) we thought this was a long shot. The next thing we came accross was a Sweden bus station in Stockholm... well we revisited the first idea. We found out that we could embed the hex into a transaction-record link and there we actually found that the hex line in the note resembled an *Ethereum Transaction Hash*, that has taken place 13 days earlier (what a coincidence!?) and has the ammount of 0.01 Ethereum ($0.00 USD). This record had an inputData line `bigtent` in hex encoding. We kept that in mind and continued...

### Decrypting Logs 

Having `bigtent` as our latest discovery, we assumed that it is the `<secret string>` part of the key's SHA256 input. Thus, we only needed to find the `<current date in RFC3339 format>` field. Having ran out of clues, we tried to brute-force the date (after all, it was very unlikely that George would showcase a future date for his example `SHA256("2020-05-18 cement")`, so we thought that the *actual* date was somewhere in 2020 or 2021 - a total of around 700 dates to try). We used `/step1/decrypt_gpg.sh` and our favorite scripting language (bash for life) for the cracking.

After successfully decrypting the logs, we read the `signal.log` and assumed that we should look for a specific commit, for which we knew its hash. But, in which repo?

The answer was revealed to us after dumping around 500MB of "[en.wikipedia.org/wiki/The_Conversation](https://en.wikipedia.org/wiki/The_Conversation)" lines in the `firefox.log`, with the divine command `$ cat firefox.log | grep -v 'The_Conversation[^H]'`. It was none other than the tor-project fork by the infamous dev *asd-d6*: https://github.com/asn-d6/tor .

### Git commits and RSA hackz

The [commit](https://github.com/asn-d6/tor/commit/4ec3bbea5172e13552d47ff95e02230e6dc99692) we were instructed to look for contained the following cryptic message:
```
/**
 * Hey Maria... So I went to the Rivest club again yesterday and met a guy who
 * sold me tickets that will take me out of this crazy city. I hope that in a
 * few days we will be together again. Find me at:
 *
 *     http://aqwlvm4ms72zriryeunpo3uk7myqjvatba4ikl3wy6etdrrblbezlfqd.onion/x||y||x||y.txt
 *
 *          where || means concatenation
 *
 ******
 *
 * N = 127670779
 * e = 7
 *
 * E(x) = 122880244
 * E(y) = 27613890
 */

```

Just by observing **N** and **e** the RSA crypto algorithm came to mind.
Having a famous [quote](https://en.wikiquote.org/wiki/Ken_Thompson) as our guide, we tried a very advanced and underground technique to crack RSA, brute-force. We noticed that N is a pretty small integer (< 32bits) thus we used the `find_rsa_pq.py` script to learn the `p` and `q` used in the generation of the keys. Knowing `p` and `q`, we used https://www.wolframalpha.com/ for a couple of modulo operations and eventually got `x = 306` and `y = 3735`.

The `/30637353063735.txt` file we found stated:

```
Hey M,

I just started my ascent to the Gilman's Point on the Kilimanjaro.

I will set my camp there and wait for you. Please bring some clean water because
the people in the village were trying to poison me so I didn't get any.

see you~~
```

Thus disclosing George's location (**Gilman's Point on the Kilimanjaro**).

PS. We noticed the eerie resemblance between George and the famous Kurt Gödel, in the fear of getting poisoned - hopefully George won't end up like his counterpart (guess we'll find out next year).

## Step 2

Getting access to the blog file, allowed us to get the link for an onion server that required username and password (we did not yet acquired). According to the relative post the server src code was in a github repo, chatziko/pico, so we cloned it and installed it in our machines. The moment we compiled the code we noticed a warning (unsual for chatziko coding standards) with a `-Wformat-security` flag, so we investigate it a little further. The first thing we bumped into was [Format String Software Attack](https://owasp.org/www-community/attacks/Format_string_attack) by OWASP so we knew we did good. A couple minutes later we tried the described attack and we passed the following username `%x %x %x %x %x %x %s` and got the username `admin` and the password md5 hash `e5614e27f3c21283ad532a1d23b9e29d` that we cracked by putting it in famous online md5 crackers and got  the password `bob's your uncle`.

After a successful log-in, we were greeted by a not-so-friendly message:
```
Hacked by 5l0ppy 8uff00n5 
```
Thus we figured that **5l0ppy 8uff00n5** stole the "Plan X" server files.

## Step 3

## Step 4

For step 4 we used the script of the previous step and adjusted the final payload, so that we can read any file we want, by just passing the file-path, as an cmd-argument.
To exploit the script we followed 2 different approaches. Both of them was based on the fact that stack was non-executable.

The first approach used the `send_file()` function from the server-app source code. This was a work-around for the ASLR mitigation that messed up system's offset, but it was not perfect still. By executing the send file we could not get an `HTTP OK` response so the output was never returned. This could be easily solved by just calling the `serve_ultimate()` before we overwrite the stack to call the `send_file()` routine. The payload was the same as in step 3 but with some extra small steps. Specifically we made sure that after `serve_ultimate()` the program would return into `send_file()` and we could set the argument in the stack, by just adding its address in the next 4 bytes and the actual argument in the last bytes of the payload. We found out how to do this and why it should work in [one of the buffer overflow slides' references](https://css.csail.mit.edu/6.858/2014/readings/return-to-libc.pdf). 

The stack after loading our payload was something like the following:
```
          |                     |                     |          |                         |                    |     |
top stack | payload from step 3 | return to send_file | fake eip | send_file_argument_addr | send_file argument | ... | bottom of the stack
          |                     |                     |          |                         |                    |     |
```
The second approach was to try executing libc code, specifically the `system()` routine in to execute shell code and pass a `cat` command. At first we could not find a fixed address in the programm since ASLR, messed all the offsets we acquired from __gcc__, run in __linux02__ machine. After a couple of tries we found a common fixed address between gcc-run and normal run of the server, we calculated the offset from the known stack address and found the libc return address we needed. At this point, we could execute arbitary code and get the terminal-output in the http response. FULL POWUH <3 <3  

Again the stack would look like that:
```
          |                     |                     |          |                      |                 |     |
top stack | payload from step 3 | return to system    | fake eip | system_argument_addr | system argument | ... | bottom of the stack
          |                     |                     |          |                      |                 |     |
```

So after all that we displayed the containing of z.log and got

```
Computing, approximate answer: 41.998427123123
```

## Step 5

For the fifth and last step we had to solve 2 problems, first of which was to find the next move in this particular chess sequence
```
1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Ng5 Ngf6 6.Bd3 e6 7.N1f3 h6 8.Nxe6 Qe7 9.0-0 fxe6 10.Bg6+ Kd8 11.Bf4 b5 12.a4 Bb7 13.Re1 Nd5 14.Bg3 Kc8 15.axb5 cxb5 16.Qd3 Bc6 17.Bf5 exf5 18.Rxe7 Bxe7
```

which was `19. c4`

The second task was to find the machine IP. To do that we used the second version of step 4, using system and pass the following cmd-command as an argument:

```bash
dig +short myip.opendns.com @resolver1.opendns.com
```

We got the IP: `54.159.81.179`, hence the final answer is 
```
c4-54.159.81.179
```


## Final Thoughts

We wrapped up all the code for steps 3,4,5 in the relative directory and created a script, that contains all the hardcoded offsets of the programs stack. The program also executes the proper socat command to enable the communication with the onion server. The script that answers the last 3 steps can be run with 

```
./run.sh
```

__Remember to open-up tor browser__ before running the script. 
