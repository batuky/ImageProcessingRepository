from rich.console import Console
from rich.theme import Theme
from rich.markdown import Markdown
from rich.prompt import Prompt

from week1.method1 import method1
from week1.method2 import method2
from week1.method3 import method3




custom_theme = Theme({"success":"bold green", "error":"bold red","warning":"bold yellow",})
console = Console(theme=custom_theme)

markdown = """

# Image Processing

Birinci hafta ödevi için : 1 \n
İkinci hafta ödevi için : 2\n
Üçüncü hafta ödevi için : 3\n
Dördüncü hafta ödevi için : 4\n

"""
markdown2 = """

# Birinci hafta ödevi

Method 1 : 1 \n
Method 2 : 2 \n
Method 3 : 3 \n
"""
def main():
    md = Markdown(markdown)
    console.print(md)
    #weekSelection = input("Haftayı seç aga: ")
    Prompt.illegal_choice_message = "Yanlış seçtiniz beyfendi"
    weekSelection = Prompt.ask("Haftayı seç aga",choices=["1", "2", "3"])
    switch(weekSelection)


def switch(choise):
    if choise == "1":
        md2 = Markdown(markdown2)
        console.print(md2)
        Prompt.illegal_choice_message = "Ödevi yanlış seçtin"

        workSelection = Prompt.ask("Ödevi seç aga",choices=["1", "2", "3"])
        switch2(workSelection) 
    else:
        console.print("Burada bir şey yok",style="error")

def switch2(choise):
    if choise == "1":
        method1()
    elif choise == "2":
        method2()
    elif choise == "3":
        method3()
    else:
        console.print("Böyle bir ödev yok",style="error")



main()