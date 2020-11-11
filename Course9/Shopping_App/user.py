import os

class User:

  #constructor of class, receivs it`s username
  
 def __init__(self, username):
    self.username = username
    #self.file_path = 'user_' + self.username


 def save(self):
    file_path = 'user_' + self.username
    try: 
        # try to open a file, succes if it already exists
     file = open(file_path)
     file.close()
     return 'User already exist'
    except:
       # if the file does not exist and we can`t open it we create it
      file = open(file_path, 'w')
      file.close 

 def remove(self):
    file_path = 'user_' + self.username
    try:
       os.remove(file_path)  #try to remove the file with name user_
       print('Removed user')
       return True
    except:
       print('User does not exist')
       return False


 def rename(self, new_username):
    success = self.remove() #delte the curent file
    if not success:
       return
    self.username = new_username
    self.file_path = 'user_' + self.username #change the file path variable
    self.save() #save the new file


