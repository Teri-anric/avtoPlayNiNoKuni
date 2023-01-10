from time import sleep
import login


def main():
    login.start_game()
    sleep(60)
    login.login()


if __name__ == "__main__":
    main()