import os
import io
import os, sys, stat
import os.path


def file():
    f = open("Password_File.txt","w")
    with open("Password_File.txt","w", encoding= 'utf-8') as f:
        f.write(info())
    f.close()

def file1():
    f = open("Password_File.txt","a+")
    with open("Password_File.txt","a+", encoding= 'utf-8') as f:
        f.write(info())
    f.close()

def read():
    f = open("Password_File.txt","r")
    with open("Password_File.txt","r", encoding= 'utf-8') as f:
        f.read()
    f.close()

def info():
    password = ''
    passConfirmation=''
    username = ''
    email = ''
    site = ''
    PassCheck = 0
    MailCheck = 0
    Finish = False
    while(PassCheck == 0):
        password += input("Enter your password: \n")
        passConfirmation += input("confirm your password \n")
        if password != passConfirmation:
            print("Not the Same Password")
        else:
            username += input("Enter your username, Press Enter is None: \n")
            while(MailCheck ==0):
                email += input("Enter your e-mail: \n")
                if not '@' in email:
                    print("Email Not exact")
                else:
                    site += input("Enter the website: \n")
                    MailCheck +=1
        PassCheck +=1
    if site != "":
        print("Information Add Successfully")
    return("""--------- \n
    Password: """+ password +""" \n
    Username: """ + username + """\n
    Email: """ + email+"""\n
    Website: """ + site + '\n')



def Password():
    boucle =0
    activity = input("""If you want to Add a new Password, press 1 \nIf you want to know a password, press 2\nIf you want to exit, press 3\n""")
    choice = int(activity)
    while choice != 3:
        if choice == 1:
            if os.path.isfile("Password_File.txt"):
                while boucle <1:
                    file1()
                    boucle +=1
            else:
                while boucle < 1:
                    file()
                    boucle +=1
            choice = 3
            return "Thank you for using this tool"
        elif choice == 2:
            while boucle <1:
                read()
                boucle +=1
    return("Have a nice day !")

print(Password())

