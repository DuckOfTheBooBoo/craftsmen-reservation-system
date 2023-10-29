from rich.prompt import Prompt, Confirm
from rich_module import console
from register import register

def main() -> None:
    console.print("""WELCOME TO CRAFTSMEN RESERVATION SYSTEM""")

    haveAccount: bool = Confirm.ask("Do you have an account?")

    if haveAccount:
        pass
    else:
        register()

if __name__ == '__main__':
    main()