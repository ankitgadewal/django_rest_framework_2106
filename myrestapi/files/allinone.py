print(".............Welcome to the all in one website checking tool.............\n \n \n Please select an option \n")
print(" 1) Ip to domain \n 2) Domain to ip \n 3) Subdomain finder \n 4) Website opening time \n 5) Ports open in a website \n 6) Whois scan a website \n 7) Get headers of website \n 8) Get source code of website\n 9) Website made in platforms \n 10) Admin panel finder \n")

import requests
def iptodomain():
    pass

def domaintoip():
    pass

def findsubdomain():
    pass

def openingtime():
    pass

def openports():
    pass

def whoisscan():
    pass

def getheaders():
    print(requests.head('https://secrets4you.ml').headers)

def getsource():
    x = requests.get('https://w3schools.com')
    print(x.headers)

def madein():
    pass

def findadmin():
    pass

user_input = int(input("Please Select an option : "))
if user_input == 1:
    print("1")
    iptodomain()
if user_input == 2:
    domaintoip()
elif user_input == 3:
    findsubdomain()
elif user_input == 4:
    openingtime()
elif user_input == 5:
    openports()
elif user_input == 6:
    whoisscan()
elif user_input == 7:
    getheaders()
elif user_input == 8:
    getsource()
elif user_input == 9:
    madein()
elif user_input == 10:
    findadmin()