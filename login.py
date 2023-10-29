from mock_database import get_user
from rich.prompt import Prompt
from rich_module import console
from typing import Dict

def login(account: Dict[str, str]) -> Dict:

    if not account:
        console.print('[yellow]LOGIN[/]')
        username = Prompt.ask('Enter your username')
        password = Prompt.ask('Enter your password', password=True)

        account: Dict[str, str] = {
            'username': username,
            'password': password
        }

    user_info = get_user(account['username'])

    if not user_info or password != user_info['password']:
        console.print('[red]Invalid credentials![/]')
        return {}
    
    console.print(f'[green]Welcome, {user_info["username"]}[/]')
    return user_info


