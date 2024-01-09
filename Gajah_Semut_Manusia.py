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
            exit()

else:
    print('\nTerima kasih atas pertimbangannya. Bye!!')
