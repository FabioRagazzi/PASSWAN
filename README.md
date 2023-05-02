# PASSWAN
 A Passward Manager Python Application

## Installation 
* Download Python 3 and add it to PATH
* Place the files "swan.py" and "Swan.ico" in the folder C:\Users\\***my_user_name*** 

## Run
* Press **Windows** + **R**
* Type **cmd**
* Press **Enter**
* Type:
> python swan.py
* Press **Enter**

## Use
* Add your account information at the top of the file "swan.py", following the example given in "swan.py"  
* The order in which the accounts appear in the file "swan.py" will be the same displayed in the application  
* The field "password_id" is the unique password identifier, ranging from "000" to "999"  
* The field "version" is useful for changing the password, it can be any character  
* The field "character_list" can be set to **NUM**, **BASIC**, **PAYPAL**, **FULL** in order to specify different 
character sets for the final password (you can create your personal combination of characters, give it a custom name, 
add it to **CHAR** dictionary and use it)  
* When you select an account in the GUI the corresponding password will be automatically copied to your clipboard
(you can then press **Ctrl** + **V** to paste it)

## Working Principle
To generate an account password, first of all a string of 16 characters is created as:  

| m   | y   | P   | a   | s   | s   | w   | o   | r   | d   | !   | !   | version (1) | password_id (3) |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-------------|-----------------|

Each character is then converted to a byte using the ASCII table, this generates a sequence of 128-bit (**plain_text**) 

The user will insert a master password in the GUI top row (ideally 16 characters long). If the password inserted has
less than 16 characters, zeros will be added at the end until reaching a length of exactly 16. If the password inserted
has more than 16 characters, only the first 16 will be considered. The exactly 16 characters long master password will be 
converted in a 128-bit sequence (**key**) using the ASCII table.  

The **key** is used to encrypt the **plain_text** according to 
[AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard). 
This will produce a 128-bit sequence (**cipher_text**). This sequence will be converted in a text password of exactly
16 characters, using only the characters allowed in the set specified.  

The advantage of using this system is that you can always retrive all your password as long as you remember:
* The master password
* The "password_id" and "version" for each account
* The set of characters used for each account

The latter two points can be achieved by performing a backup of the dictionaries **ACCOUNTS** and **CHAR** 
in the file "swan.py". You could store them in plain sight on the internet, as long as your master password is secure
and remains secret.

## Notes
* All your passwords will be determined by the single master password you choose. It may be a good idea to choose a 
good master password (ideally 16 characters long). Watch [this video](https://www.youtube.com/watch?v=3NjQ9b3pgIg&t=0s)
to get some inspiration
