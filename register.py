from mock_database import add_user
from rich.prompt import Prompt
from rich_module import console
from typing import Dict

def register() -> Dict[str, str]:
    console.print('[yellow]REGISTER[/]')
    
    username: str = ''
    while not username:
        temp_username = Prompt.ask('Enter your username')
        
        if len(temp_username) < 5:
            console.print('[red]Username must be at least 5 characters[/]')
        else:
            username = temp_username

    password: str = ''
    while not password:
        temp_password: str = Prompt.ask('Enter your password', password=True)

        if len(temp_password) < 8:
            console.print('[red]Password must be at least 8 characters[/]')
        else:
            recheck_password: str = Prompt.ask('Retype your password', password=True)

            if recheck_password != temp_password:
                console.print('[red]Password doesn\'t match[/]')
            else:
                password: str = temp_password
    
    account: Dict[str, str] = {
        'username': username,
        'password': password
    }

    add_user(account)
    console.print('[green]Successfully created new account[/]')

    return account
