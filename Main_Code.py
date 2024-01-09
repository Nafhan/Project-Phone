def rps():
    import random

    tsp = 0
    tsc = 0

    print("Welcome to Rock, Paper, Scissor Game")

    choices = ["y", "n"]
    play = None

    while True:
        play = input('\nDo you wanna play? (y/n) ').lower()
        if play in choices:
            break
        else:
            print(f'Invalid {play} input. Please try again.')

    if play == "y":
        while True:
            choices = ["rock", "paper", "scissor"]
            computer = random.choice(choices)
            player = None

            while player not in choices:
                player = input("Rock, Paper, Scissor? ").lower()

            print("\nPlayer : " + player)
            print("Computer : " + computer)

            if player == computer:
                print("Tie")
                tsp += 0
                tsc += 0
            elif player == "rock":
                if computer == "scissor":
                    print("You Win!!")
                    tsp += 1
                elif computer == "paper":
                    print("You Lose!!")
                    tsc += 1
            elif player == "paper":
                if computer == "scissor":
                    print("You Lose!!")
                    tsc += 1
                elif computer == "rock":
                    print("You Win!!")
                    tsp += 1
            elif player == "scissor":
                if computer == "rock":
                    print("You Lose!!")
                    tsc += 1
                elif computer == "paper":
                    print("You Win!!")
                    tsp += 1

            play_again = ["y", "n"]
            play = None
            while True:
                play = input('\nDo you wanna play? (y/n) ').lower()
                if play in play_again:
                    break
                else:
                    print(f'Invalid {play} input. Please try again.')

            if play != "y":
                score_player = tsp
                score_computer = tsc
                if score_player > score_computer:
                    print("\nGREAT!! YOU WIN AGAINST A COMPUTER!!")
                else:
                    print("\nNICE TRY BUDDY, COMPUTER'S BETTER THAN YOU")

                print("Thank you for playing!! \n\nResults \nPlayer : " +
                      str(tsp) + "\nComputer : " + str(tsc))
                break
    else:
        print("\nThank You!!")
        aplikasi()

def tm():
    tasks = []

    def add_task(task):
        tasks.append(task)
        print(f'\nTask {task} has been added')

    def completed_task(task):
        if task in tasks:
            tasks.remove(task)
            print(f'\nTask {task} has been marked as completed')
        else:
            print(f"\nTask {task}'s not found. Please retry.")

    def show_task(task):
        saat_ini = None
        print(f'\nTasks : ')
        for task in tasks:
            print(f' - {task}')

    while True:
        print("\nHere's a few command to choose : \n1) Add Task \n2) Mark Completed Task \n3) Show Tasks \n4) Quit")
        choice = input("Please choose either of the command : ")

        if choice == "1":
            task = input("Enter the task : ")
            add_task(task)

        elif choice == "2":
            task = input("Enter the task to be marked as completed : ")
            completed_task(task)

        elif choice == "3":
            show_task(tasks)

        elif choice == "4":
            print("Goodbye!!")
            aplikasi()

        else:
            print("\nInvalid Command. Please choose a valid command.")

def gsm():
    import random

    SP = 0
    SR = 0

    print('Selamat datang di Game Gajah, Semut, Manusia!!')

    pilihan_main = ['y', 'n']
    main_ga = []

    while True:
        main_ga = input('\nApakah kamu ingin bermain? (y/n) ').lower()
        if main_ga in pilihan_main:
            break
        else:
            print(f'Invalid {main_ga} input. Coba isi kembali.')

    if main_ga == 'y':
        while True:
            choices = ['gajah', 'semut', 'manusia']
            choice_robot = random.choice(choices)
            choice_pemain = []

            while True:
                choice_pemain = input('\nGajah / Semut / Manusia : ').lower()
                if choice_pemain in choices:
                    break
                else:
                    print(f'Invalid {choice_pemain} input. Coba isi kembali.')

            print(f'\nKamu: {choice_pemain} \nRobot: {choice_robot}')

            if choice_pemain == choice_robot:
                print('Wow Seri!!')
                SP += 1
                SR += 1

            elif choice_pemain == 'gajah':
                if choice_robot == 'manusia':
                    print('Kamu MENANG.')
                    SP += 1
                elif choice_robot == 'semut':
                    print('Kamu KALAH HAHAHA.')
                    SR += 1

            elif choice_pemain == 'semut':
                if choice_robot == 'gajah':
                    print('Kamu MENANG.')
                    SP += 1
                elif choice_robot == 'manusia':
                    print('Kamu KALAH HAHAHA.')
                    SR += 1

            if choice_pemain == 'manusia':
                if choice_robot == 'semut':
                    print('Kamu MENANG.')
                    SP += 1
                elif choice_robot == 'gajah':
                    print('Kamu KALAH HAHAHA.')
                    SR += 1

            choice_play_again = ['y', 'n']
            play_again = []

            while True:
                play_again = input('\nApakah anda ingin bermain kembali? (y/n) ').lower()
                if play_again in choice_play_again:
                    break
                else:
                    print(f'Invalid {play_again} input. Coba isi kembali.')

            if play_again != 'y':
                print(f'\nTerima kasih telah bermain.'
                      f'\n\nHASIL AKHIR'
                      f'\nKamu: {SP}'
                      f'\nRobot: {SR}')
                if SP > SR:
                    print('Kamu berhasil MENANG melawan Robot.')
                elif SP < SR:
                    print('Robot berhasil MENGALAHKAN Kamu, Manusia.')
                elif SP == SR:
                    print('Robot berhasil IMBANG melawan Kamu, Manusia.')
                aplikasi()

    else:
        print('\nTerima kasih atas pertimbangannya. Bye!!')
        aplikasi()

def guessing():
    import random

    print("Welcome to the Guessing Number Game!!")

    secret_number = random.randint(1, 100)

    choices = ["y", "n"]
    play = None

    attempts = 0

    while play not in choices:
        play = input("Do you wanna play (y/n)? ").lower()

    if play == "y":
        while True:
            numbers_choices = [str(i) for i in range(1, 100 + 1)]
            guess = None

            while guess not in numbers_choices:
                guess = input("Enter your guess (between 1 and 100): ")
                attempts += 1

            if int(guess) == secret_number:
                print("\nCongratulations!! Your guess is correct!!")
                print(f'Total attempts: {attempts}')
            elif int(guess) >= secret_number:
                print("Too high!! Try again.")
                continue
            elif int(guess) <= secret_number:
                print("Too low!! Try again.")
                continue

            play_again = ["y", "n"]
            play = None
            while play not in play_again:
                play = input("\nDo you wanna play again (y/n)? ").lower()
            if play == "n":
                print("Thank you for playing, have a nive day!!")
                aplikasi()
    else:
        print("Thank you!!")
        aplikasi()

def aplikasi():
    pemilihan_sistem = ['1', '2', '3', '4', '5']
    pemilihan = []
    while True:
        pemilihan = input('\nBerikut adalah beberapa fitur yang dapat dipilih :'
                        '\n1) Task Manager'
                        '\n2) Guessing Number Game'
                        '\n3) Rock, Paper, Scissor Game'
                        '\n4) Game Gajah, Semut, Manusia '
                        '\n5) Shut Down'
                        '\n\nPilihan Anda: ')
        if pemilihan in pemilihan_sistem:
            break
        else:
            print(f'Invalid {pemilihan} input. Please try again.')

    if pemilihan == '1':
        tm()

    elif pemilihan == '2':
        gsm()

    elif pemilihan == '3':
        rps()

    elif pemilihan == '4':
        gsm()

    elif pemilihan == '5':
        print('Terima kasih telah membuka HP NAFHAN')
        exit()

def main_screen():
    print("SELAMAT DATANG DI HP NAFHAN")

    hidup_mati = ['lanjutkan', 'shutdown']
    pilihan_hidup = None

    while True:
        pilihan_hidup = input('lanjutkan / shutdown : ').lower()
        if pilihan_hidup in hidup_mati:
            break
        else:
            print(f'Invalid {pilihan_hidup} input. Please try again.')
    if pilihan_hidup == 'lanjutkan':
        aplikasi()
    elif pilihan_hidup == 'shutdown':
        print('Terima kasih telah membuka HP NAFHAN')
        exit()

main_screen()
