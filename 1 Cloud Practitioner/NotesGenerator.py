import os


class NoteGenerator():
  
  PATH = "SAVE_PATH"
  IMAGE_DIR = os.listdir(PATH)
  
  
  def __init__(self, subject):
    self.SUBJECT = subject
  

  def generate_script(self):
    # internal variable: old_title, new_title, file_name, zero, i
    
    for i, image in enumerate(self.IMAGE_DIR):
        i += 1
        old_title = self.PATH + image
        zero = "0"

        if (i <= 9): pass
        else: zero = ""

        file_name = f"{self.SUBJECT}{zero}{i}.jpg"
        new_title = self.PATH + file_name

        # os.rename(old_title, new_title)

        print(f'<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/1%20Cloud%20Practitioner/{self.SUBJECT}/{file_name}" width=900/>')

        
if __name__ == "__main__":
  ng = NoteGenerator("subject")
  ng.generate_script()

  
    
""" ======== EXAMPLE =========

if __name__ == "__main__":
    ng = NoteGenerator("Database")
    ng.generate_script()
 
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/1%20Cloud%20Practitioner/Database/Database01.jpg" width=900/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/1%20Cloud%20Practitioner/Database/Database02.jpg" width=900/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/1%20Cloud%20Practitioner/Database/Database03.jpg" width=900/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/1%20Cloud%20Practitioner/Database/Database04.jpg" width=900/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/1%20Cloud%20Practitioner/Database/Database05.jpg" width=900/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/1%20Cloud%20Practitioner/Database/Database06.jpg" width=900/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/1%20Cloud%20Practitioner/Database/Database07.jpg" width=900/>

"""
