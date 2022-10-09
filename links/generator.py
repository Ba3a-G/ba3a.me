import template as t
import os
import subprocess

def commit(message) -> None:
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push"])

def generateCLI() -> None:
    title = str(input("Title: "))
    link = str(input("Link: "))
    document = t.template(title, link)
    try:
        os.mkdir("links/" + title)
    except FileExistsError:
        print("Link already exists. Overwriting...")
    with open("links/" + title + "/index.html", "w") as f:
        f.write(document)
    commit("Added " + title)

if __name__ == "__main__":
    generateCLI()