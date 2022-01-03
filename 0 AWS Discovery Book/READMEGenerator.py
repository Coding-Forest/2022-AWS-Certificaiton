import re


class READMEGenerator:

    def __init__(self, CHAPTER):
        self.chapter = CHAPTER
        self.topics = []

    def add_topics(self, topic):
        if (type(topic) == str):
            self.topics.append(topic)
        elif (type(topic) == list):
            self.topics.extend(topic)
        else:
            print("Please enter your topic in str or [list].")

    def generate_script(self):

        print(f"# {self.chapter}  \n")

        for i in range(1, len(self.topics)+1):
            print(f"[{i}. {self.topics[i-1]}](#{i})  ")

        print("\n<br>  \n")
        print(f"## ⚙ Key Components & Key Concepts  \n")

        for i in range(1, len(self.topics)+1):
            print(f'**<span id="{i}">{i}. {self.topics[i-1]}**</span>  \n')
            print("  -   \n")
            print("<br>  \n")

        print("## 🙌⌨ Hands-on Practice   \n")
        print("  -   \n")
        print("<br>  \n")
        print("### References}  \n")
        print("  - Yeonghwan Gwon(2021) AWS Discovery Book")


if __name__ == "__main__":
    rmgen = READMEGenerator("Network")
    #rmgen.add_topics("")
    rmgen.add_topics(["VPN", 'VPC', 'VPC components', 'VPC services'])
    rmgen.generate_script()
