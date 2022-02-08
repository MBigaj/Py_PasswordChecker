# Py_PasswordChecker
Script that checks if a given password has been hacked (safe)

Using SHA Hashing we first cipher the password and then get information on it from haveibeenpwned.com websites API.
(I tried keeping it safe by sending only the last 5 letters of the hashed password out to the web, this way we are sure it is secure)
Then we go ahead and count the occurences of our password in the database which determines whether or not our password has ever been leaked...
