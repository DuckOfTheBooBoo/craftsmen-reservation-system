from rich.prompt import Prompt, Confirm

def main() -> None:
    console.print("""WELCOME TO CRAFTSMEN RESERVATION SYSTEM""")

    haveAccount: bool = Confirm.ask("Do you have an account?")

    if haveAccount:
        pass
    else:
        pass

if __name__ == '__main__':
    main()