import os


class NotesGenerator:
  
    PATH = "SAVE_PATH"
    IMAGE_DIR = os.listdir(PATH)

    def __init__(self, subject):
        self.SUBJECT = subject

    def generate_script(self):
        # internal variable: old_title, new_title, file_name, zero, i

        print(f"# Notes - {self.SUBJECT}\n\n[References down below👇](#ref)\n")

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

        print(f"\n<br>\n\n### <span id='ref'>References</span>\n")

        print("  - All lecture slides by [Andrew Brown](https://www.youtube.com/c/ExamProChannel) from [Exampro](https://www.youtube.com/c/ExamProChannel)")


if __name__ == "__main__":
    ng = NoteGenerator("subject")
    ng.generate_script()
