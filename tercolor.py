import colorama as cl
from time import sleep as sl
con1=input("Press Enter to Continue...")
del con1
cl.init(autoreset=True)
print(cl.Fore.RED+'Red Text')
sl(1)
print(cl.Fore.GREEN+'Green Text')
sl(1)
print(cl.Style.DIM+'Dim Style Text')
sl(1)
print(cl.Style.BRIGHT+'Bright Text')
sl(1)
print(cl.Fore.WHITE+cl.Back.GREEN+'IMPORTANT CONSOLE')
