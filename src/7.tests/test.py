def get_formated_name(first, last):
    '''Строит форматированное полное имя'''
    full_name = f"{first} {last}"
    return full_name.title()

a = get_formated_name("Jon","Snow")
print(a)
