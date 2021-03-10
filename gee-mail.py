import smtplib
import getpass
import time

print("\n################## gee-mail sender ###################")
time.sleep(1.5)
print("\nRemeber to activate 'less secure app' access on gmail, \nor this script will not work")

def final():
    ending = input()
    if ending == "n" or ending == "N":
        print("\n##############################")
        print("\nBye bye!")
        time.sleep(1)
        print("\nSee you next time!")
        time.sleep(1)
        print("\n     Uriel-SG")
        print("\n##############################")
        input()
        exit()
    if ending == "y" or ending == "Y":
        email_sending()

def email_sending():
    mail_object = str(input("\nObject: "))
    complete_object = "Subject: " + mail_object + "\n"
    mail_content = str(input("\nContent: "))
    message = complete_object + mail_content

    email = smtplib.SMTP("smtp.gmail.com", 587)  #server and port

    email.ehlo  #connect to server

    email.starttls()  #crypted tunnel

    mail_user = str(input("\nYour username (works also without domain): "))

    user_pass = getpass.getpass()

    email.login(str(mail_user), str(user_pass))

    mailsender = str(mail_user + "@" + "gmail.com")
    mailreceiver = input("\nReceiver: ")

    email.sendmail(mailsender, mailreceiver, message)

    email.quit()

    print("\nDo you want to send another e-mail? (y/n)")

    final()

email_sending()
final()



