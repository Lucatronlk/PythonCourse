from email import EmailUser


class PremiumEmailUser(EmailUser):
    def __init__(self, username, full_name):
        self._username = username
        self._full_name = full_name

    def _delete_old_emails(self):
        return


user1 = PremiumEmailUser("alexandru.luca@gmail.com", "Alexandru Luca")

print(user1.get_username())

# print(user1.get_full_name)
# user1.add_email("subj1", "hello")
# print(user1.get_emails())

i = 0
while i < 12:
    user1.add_email('s' + str(i), 'm' + str(i))
    i += 1
    print(user1.get_emails())
