
def find_acronym():
    look_up = input("What software acronym would you like to look up?\n")

    found = False
    with open('input.txt') as file:
        for line in file:
            if look_up in line:
                print(line)
                found = True
                break
    if not found:
        print('The acronym does not exsist')

def add_acronym():
    acronym = input('What acronym do you want to add?\n')
    definition = input('What is the definition?')
    with open('input.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')
    
def main():
    # Ask the user whether they want to find or add an acronym
    choice = input('Do you want to find(F) or add(A) an acronym?')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

main()
