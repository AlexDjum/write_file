user_language = input('Какой язык вы изучаете?')
user_time = input('Как давно?')
user_institution = input('Где?')

with open('answers.txt', 'wt', encoding='utf-8') as file:
    file.write(f'{user_language}\n')
    file.write(f'{user_time}\n')
    file.write(f'{user_institution}\n')
