from rich.console import Console
from rich.theme import Theme
from rich.markdown import Markdown
from rich.prompt import Prompt

from week1.method1 import method1
from week1.method2 import method2
from week1.method3 import method3
from week2.RGB import rgbToBgr
from week3.resize import resize




custom_theme = Theme({"success":"bold green", "error":"bold red","warning":"bold yellow",})
console = Console(theme=custom_theme)

#Main menu markdown
markdown = """

# Image Processing

First week exercise : 1 \n
Second week exercise : 2\n
Third week exercise : 3\n
Fourth week exercise : 4\n

"""

# 1st week exercise markdown
markdown2 = """

# First week exercises

Method 1 : 1 \n
Method 2 : 2 \n
Method 3 : 3 \n
"""

# 2nd week exercise markdown
markdown3 = """

# Second week exercise

Convert BGR and RGB  : 1 \n
\n
"""

# 3rd week exercise markdown
markdown4 = """

# Second week exercise

Resize an image  : 1 \n
\n
"""
def main():
    md = Markdown(markdown)
    console.print(md)
    #weekSelection = input("Haftayı seç aga: ")
    Prompt.illegal_choice_message = "Wrong choice!"
    weekSelection = Prompt.ask("Choose the week",choices=["1", "2", "3"])
    switch(weekSelection)


#Week switch
def switch(choise):
    if choise == "1":
        md2 = Markdown(markdown2)
        console.print(md2)
        Prompt.illegal_choice_message = "Wrong exercise choice!"
        workSelection = Prompt.ask("Choose the exercise",choices=["1", "2", "3"])
        switch2(workSelection) 
    elif choise == "2":
        md3 = Markdown(markdown3)
        console.print(md3)
        Prompt.illegal_choice_message = "Wrong exercise choice!"
        workSelection = Prompt.ask("Choose the exercise",choices=["1"])
        switch3(workSelection) 
    elif choise == "3":
        md4 = Markdown(markdown4)
        console.print(md4)
        Prompt.illegal_choice_message = "Wrong exercise choice!"
        workSelection = Prompt.ask("Choose the exercise",choices=["1"])
        switch4(workSelection)
    else:
        console.print("There is nothing here!",style="error")

#first week exercise switch
def switch2(choise):
    if choise == "1":
        method1()
    elif choise == "2":
        method2()
    elif choise == "3":
        method3()
    else:
        console.print("There is nothing here!",style="error")

#second week exercise switch
def switch3(choise):
    if choise == "1":
        rgbToBgr()
    # elif choise == "2":
    #     method2()
    # elif choise == "3":
    #     method3()
    else:
        console.print("There is nothing here!",style="error")

#third week exercise switch
def switch4(choise):
    if choise == "1":
        resize()
    # elif choise == "2":
    #     method2()
    # elif choise == "3":
    #     method3()
    else:
        console.print("There is nothing here!",style="error")

main()