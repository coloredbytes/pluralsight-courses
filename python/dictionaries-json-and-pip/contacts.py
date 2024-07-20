
contacts = {
    'number': 4,
    'students':
        [
            {'name': 'Joshua Ross', 'email':'josh@example.com'},
            {'name': 'Harry Potter', 'email':'harry@example.com'},
            {'name': 'Herminoe Granger', 'email':'hermione@example.com'},
            {'name': 'Ron Weasley', 'email':'ron@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])