from rich.prompt import Prompt, Confirm
from rich_module import console
from register import register
from login import login
from typing import Dict

def main() -> None:
    console.print("""WELCOME TO CRAFTSMEN RESERVATION SYSTEM""")

    haveAccount: bool = Confirm.ask("Do you have an account?")
    current_user: Dict[str, str] = {}
    if haveAccount:
        current_user = login()
    else:
        account_info = register()
        current_user = login(account_info)
    
    
    
    

if __name__ == '__main__':
    main()