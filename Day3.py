def register_check(d):
    count = 0
    for v in d.values():
        if v == "yes":
            count += 1
    return count

# Inputs
register = {
    'Michael':'yes',
    'John':'no',
    'Peter': 'yes',
    'Mary' : 'yes'
}

print(register_check(register))