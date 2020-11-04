class EmailUser:
 
 _email_list = [] # lista privata
 _max_number_of_emails = 10
 
 def __init__(self, username, full_name):
    self._username = username
    self._full_name = full_name

 def get_username(self):
    return self._username()
 
 def get_full_name(self):
     return self._full_name   

 def get_emails(self):  # metoda ca sa access lista 
     return self._email_list

 def _delete_old_emails(self):
     if len(self._email_list) > self._max_number_of_emails:
        self._email_list = self._email_list[1:]

 def add_email(self, subject, message):
    self._email_list.append({'subject': subject, 'message': message})
    self._delete_old_emails()


class PremiumEmailUser(EmailUser):
    def __init__(self, username, full_name): 
        self._username = username
        self._full_name = full_name

    def _delete_old_emails(self):
        return    

user1 = PremiumEmailUser("alexandru.luca@gmail.com", "Alexandru Luca")

print(user1.get_username)

#print(user1.get_full_name)
#user1.add_email("subj1", "hello")
#print(user1.get_emails()) 

i = 0 
while i < 12:
        user1.add_email('s' + str(i), 'm' + str(i))
        i += 1
        print(user1.get_emails)