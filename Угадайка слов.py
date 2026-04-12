from random import choice
word_list = ["яблоко", "река", "гора", "лес", "океан", "ветер", "молния", 
    "гром", "звезда", "луна", "солнце", "облако", "трава", "цветок", 
    "дерево", "птица", "рыба", "кот", "собака", "дом", "город", 
    "машина", "книга", "ручка", "стол", "стул", "дверь", "окно", 
    "зеркало", "ковёр", "лампа", "часы", "телефон", "компьютер", 
    "учитель", "ученик", "друг", "семья", "счастье", "радость", 
    "грусть", "мечта", "путь", "тайна", "чудо", "огонь", "вода", 
    "воздух", "земля", "небо"]

def get_word():
    return choice(word_list)

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    print('Давайте играть в угадайку слов!')
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    while not guessed and tries > 0 :
       print(display_hangman(tries))
       print(' '.join(word_completion))
       print()

       char = input('Введите букву: ').lower()

       if len(char) != 1:
            print('Введите одну букву!\n')
            continue
       
       if char not in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
            print('Введите русскую букву!\n')
            continue
        
       if char in guessed_letters:
            print(f'Вы уже называли букву "{char}". Попробуйте другую.\n')
            continue
        
       guessed_letters.append(char)

       if char in word:
         print(f'Да, буква "{char}" есть в слове!')

         for i in range(len(word)):
             if word[i] == char:
               word_completion = word_completion[0:i] + char + word_completion[i+1:]

         if '_' not in word_completion:
            print(f'\nПоздравляем! Вы угадали слово "{word}"!')
            print(display_hangman(tries))
            print(word)
            guessed = True

       else:
            tries -= 1
            print(f'Нет, буквы "{char}" нет в слове. Осталось попыток: {tries}')
            
            if tries == 0:
                print(f'\nВы проиграли. Загаданное слово было: "{word}"')
                print(display_hangman(tries))
                print(word)
                guessed = True

while True:
    word = get_word()
    play(word)
    again = input('\nХотите сыграть ещё? (да/нет): ').lower()
    if again != 'да':
       print('Спасибо за игру! До свидания!')
       break