import os
import re

class ImageScriptGenerator:
    PATH = "IMAGE_DIR_PATH"
    IMAGE_DIR = os.listdir(PATH)

    def __init__(self, subject):
        self.SUBJECT = subject

    def generate_script(self, dir_name, width):

        directory = re.sub(" ", "%20", dir_name)
        directory = re.sub("tree", "blob", directory)

        for i, image in enumerate(self.IMAGE_DIR):
            #old_title = self.PATH + image
            #new_title = self.PATH + file_name
            #os.rename(old_title, new_title)
            file_name = re.sub(" ", "%20", image)

            print(f'<img src="{directory}/{file_name}" width={width}/>')


if __name__ == "__main__":
    isgen = ImageScriptGenerator("Database")
    isgen.generate_script("https://github.com/Coding-Forest/2022-AWS-Certificaiton/tree/main/0%20AWS%20Training/VCP", 750)
