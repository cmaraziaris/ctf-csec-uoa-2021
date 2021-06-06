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
While visiting and browsing the code of the instructor-given .onion link, we skimmed the blog-article about onion site security, hence we discovered that the site-creator allowed us to view the `server-info` page. There we discovered the existence of a second site. At the same time one of us noticed that the cookie in the site, when changed, printed some interesting messages in the user id section. We also discovered that the cookie was generated by the following algorithm
```
Let 'L' be the message you want to display in user id field. 
1) Y = "SHA256(L)"
2) X = "L:Y"
3) COOKIE = BASE64(X)
```
so we constructed a small python script to generate cookies fast, based on our input.
### The bypass
Visiting the second site we bumped into a user validation page. Since we failed to login with simple credentials, we checked the respective `server-info` page and also we tried to access the `robots.txt` page, where we found something quite interesting: .phps files where allowed, but why? So we checked if there was a `access.phps` page. So now we just had to find the `$desired` variable, being *1337* and now we had to find the password. After a little googling we found out that the `strcmp()` function was quite vulnerable even if the condition check was *strict*. We could pass an array as `$password` and bypass the login section. We tried something like this: `?user=0001337&password[]=0`.

### Blogging
After loggin in, we browsed the blog a little and found out a quite-obscurely hidden post-page named `post3.html` that actualy gave us the user-id we had to use at *YS13 fixers* site. Using our script we found about George Komninos' secret back-up, that contained the encrypted files of firefox and signal logs, so we knew that should do it, but we did not find the decryption key... yet.

### Ethereum Transactions
Reading the note that George has left we got interested in the meaning of the last line `ropsten <hex number>`. We tried to transform it to ascii, in case we got anything secret-like and that failed. Then we googled about `ropsten`. Firstly, we found it was a transaction wallet, but (little did we knew) we thought this was a long shot. The next thing we came accross was a Sweden bus station in Stockholm... well we revisited the first idea. We found out that we could embed the hex into a transaction-record link and there we actually found that the hex line in the note resembled an *Ethereum Transaction Hash*, that has taken place 13 days earlier (what a coincidence!?) and has the ammount of 0.01 Ethereum ($0.00 USD). This record had an inputData line `bigtent` in hex encoding. We kept that in mind and continued...

### Decrypting Logs 

### Git commits and RSA hackz


## Step 2

## Step 3

## Step 4

## Step 5
