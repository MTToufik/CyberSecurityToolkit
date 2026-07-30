from database import create_tables
from login import LoginWindow
#from register import RegisterWindow

def main():
    create_tables()
    LoginWindow()
   #RegisterWindow()
    
    


if __name__ == "__main__":
    main()