from Course7_email import EmailUser

user1 = EmailUser("alexandru.luca@gmail.com", "Luca Alexandru")
print(user1.get_username())
print(user1.get_emails())

i = 3
while i < 6:
  user1.add_email('s' + str(i), 'm ' + str(i))
  i += 1
  print(user1.get_emails())