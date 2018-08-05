s = 'my name is \033[4;98;255m%(name)s\033[0m, and my hoby is %(hobby)s.'

print(s % {'name': 'sam cheung', 'hobby': 'coding'})