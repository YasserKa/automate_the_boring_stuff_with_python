import random
import smtplib


def assignChore(email, chore):
    bodyTemplate = "You have to do the " + chore
    smtpObj.sendmail(myEmail, email, 'Subject:Chores!\n' + bodyTemplate)


people = ['yasser.kaddouralearn@gmail.com',
          'yasser.kaddoura19@gmail.com']
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
myEmail = 'yasser.kaddoura.19@gmail.com'

# this chore is now taken, so remove it
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(myEmail, 'my secret password')


for person in people:
    randomChore = random.choice(chores)
    chores.remove(randomChore)
    assignChore(person, randomChore)

smtpObj.quit()
print('Done!')
