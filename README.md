# Messanger Script

Program consists of 2 modules:
* message manager - send an recive messages
* user manager - create/delete/modify users

###User manager 
Options
```
-u --user [username]
-p --password [password]
-d --delete [user_id]
-l --list
-e --edit
-n --new-pass [new_password]
```
Add new user
```
-u [username] -p [password]
```
Delete user
```
-u [username] -p [password] -d [user_id]
```
Update password for user
```
-u [username] -p [password] -e -n [new_password]
```
Lists all users
```
-l
```
###Message manager 
Options
```
-u --user [username]
-p --password [password]
-l --list
-t --to [reciepient_id]
-s --send [text]
```
Send message
```
-u [username] -p [password] -t [reciepient_id] -s [text]
```

List messages for user
```
-u [username] -p [password] -l
```


###Used modules
* bcrypt
* mysql connector version 2.1.6