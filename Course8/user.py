class User:

  #constructor of class, receivs it`s username
  
 def __init__(self, username):
    self.username = username
    self.file_path = 'user_' + self.username # generate the file path here

 def save(self):
    try: 
        # try to open a file, succes if it already exists
     file = open(self.file_path)
     file.close()
     print('User already exist')
    except:
       # if the file does not exist and we can`t open it we create it
      file = open(file_path, 'w')
      file.close   