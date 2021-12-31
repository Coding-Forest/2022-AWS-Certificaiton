import os
import re

class NoteGenerator:
    PATH = "SAVE_PATH"
    IMAGE_DIR = os.listdir(PATH)

    def __init__(self, subject):
        self.SUBJECT = subject

    def generate_script(self):
        # internal variable: old_title, new_title, file_name, zero, i

        print(f"# Notes - {self.SUBJECT}\n\n[References down below👇](#ref)\n")

        for i, image in enumerate(self.IMAGE_DIR):

            SUBJECT_url = str(self.SUBJECT)
            if (" " in SUBJECT_url):
                space = "%20"
                SUBJECT_url = re.sub(" ", space, SUBJECT_url)

                i += 1
                old_title = self.PATH + image
                zero = "0"

                if (i <= 9):
                    pass
                else:
                    zero = ""

                file_name = f"{SUBJECT_url}{zero}{i}.jpg"
                new_title = self.PATH + file_name

                # os.rename(old_title, new_title)

                print(
                    f'<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/1%20Cloud%20Practitioner/{SUBJECT_url}/{file_name}" width=900/>')

        print(f"\n<br>\n\n### <span id='ref'>References</span>\n")

        print(
            "  - All lecture slides by [Andrew Brown](https://www.youtube.com/c/ExamProChannel) from [Exampro](import os
import re

class NoteGenerator:
    PATH = "C:\\Users\\0woo0\\OneDrive\\문서\\카카오톡 받은 파일\\"
    IMAGE_DIR = os.listdir(PATH)

    def __init__(self, subject):
        self.SUBJECT = subject

    def generate_script(self):
        # internal variable: old_title, new_title, dir_name, file_name, zero, i

        print(f"# Notes - {self.SUBJECT}\n\n[References down below👇](#ref)\n")

        for i, image in enumerate(self.IMAGE_DIR):

            # Parse space into url percent
            dir_name = str(self.SUBJECT)
            if (" " in dir_name):
                space = "%20"
                dir_name = re.sub(" ", space, dir_name)

            # Rename file
            # Handle 0 for file_name
            i += 1
            zero = "0"
            if (i <= 9): pass
            else: zero = ""

            file_name = f"{self.SUBJECT}{zero}{i}.jpg"
            old_title = self.PATH + image
            new_title = self.PATH + file_name

            os.rename(old_title, new_title)

            print(f'<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/1%20Cloud%20Practitioner/{dir_name}/{file_name}" width=900/>')

        print(f"\n<br>\n\n### <span id='ref'>References</span>\n")

        print("  - All lecture slides by [Andrew Brown](https://www.youtube.com/c/ExamProChannel) from [Exampro](https://app.exampro.co/)")


if __name__ == "__main__":
    ng = NoteGenerator("Development Tools")
    ng.generate_script())")


if __name__ == "__main__":
    ng = NoteGenerator("subject")
    ng.generate_script()
