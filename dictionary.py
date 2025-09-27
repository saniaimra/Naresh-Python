# Take a username and password from the user and store it in a dictionary
# After storing some user and password manually check if the username exists 
# If username present print user exists

user_pwd = {'smoothoperator@gmail.com':[30,'Carlos','sainz55'],'ferrariboy@gmail.com':[28,'Charles','leclerc16'],'saniaimra86@gmail.com':[21,'Sania','imra1408']}
user_name = input("Enter username: ")
if user_pwd.get(user_name) == None:
    print ("User does not exist")

else:
    print("User exists type in the pwd")

    pwd = input("Enter password: ")
    if pwd == user_pwd[user_name][2]:
        print("Correct password!!!")
        print('user_name:',user_name,
              'password:',pwd)
    else:
        print("Incorrect password")




