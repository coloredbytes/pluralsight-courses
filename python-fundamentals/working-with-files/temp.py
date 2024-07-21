acronym = input('What acronym do you want to add?\n')
definition = input('What is the definition?')
with open('input.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')
    
