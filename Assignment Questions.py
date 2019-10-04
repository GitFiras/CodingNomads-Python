people = [
            ['Bilbo', 'Baggins'],
            ['Gollum'],
            ['Tom', 'Bombadil'],
            ['Aragorn']
        ]

# Change everything below here to use while loops instead
for person in people:
    to_print = ""
    for name in person:
        to_print += name + " "
    print(to_print)



people = [
            ['Bilbo', 'Baggins'],
            ['Gollum'],
            ['Tom', 'Bombadil'],
            ['Aragorn']
        ]

# Change everything below here to use while loops instead
i = 0
while i < len(people):
    person = people[i]
    to_print = ""
    j = 0
    while j < len(person):
        name = person[j]
        to_print += name + " "
        j += 1
    print(to_print)
    i += 1
