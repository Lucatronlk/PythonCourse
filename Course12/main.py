
# list_users = ['lucatronlk', 'lucatronlk', 'lucatronlk']
# list_websites = ['amazon', 'netflix', 'spotify']
# list_passwords = ['parola1', 'parola2', 'parola3']
# dict = {'amazon': {'user': 'lucatronlk', 'password': 'parola1'},
#         'netflix': {'user': 'lucatronlk', 'password': 'parola2'},
#         'spotify': {'user': 'lucatrnlk', 'password': 'parola3'}
#         }


class Credentials:
    #we need to give
  def __init__(self, user, password):
     #save the variables to the object
     self.user = user
     self.password = password

#extend credentials
class EmptyCredentials(Credentials):
    def __init__(self):
        #call the parent credentials constructors
        super().__init__('', None)

dict = {
        'amazon': Credentials('lucatronlk', 'parola1'),
        'netflix': Credentials('lucatronlk', 'parola2'),
        'spotify': Credentials('lucatronlk', 'parola3'),
            }


def get_user_and_pass(websiste_name):
    # i = 0
    # for website in list_websites:
    #     # parcurgem_website
    #     if websiste_name == website:
    #         return list_users[i], list_passwords[i]
    #     i += 1



 try:
        return dict[websiste_name]
      # user = dict[websiste_name]['user']
      # password = dict[websiste_name]['password']
      # return user, password
    #if an exeption of type KeyError executes code in exept
 except KeyError:
        return EmptyCredentials()


 #
 # for website in list_websites:
 #    print(get_user_and_pass(website))

if __name__ == '__main__':
    new = Credentials('value1', 'value2')
    print(new.__dict__)