# The Wide-Mouthed frog! 8
def mouth_size(animal):
    with_our_register = animal.lower()
    if with_our_register == 'alligator':
        return "small"
    else:
        return "wide"

# Does my number look big in this? 6
def narcissistic( value ):
    str_value = str(value)
    l = len(str_value)
    n = 0
    for ch in str_value:
        n += pow(int(ch), l)
    if n == value:
        return True
    return False

# Split Strings 6
def split_string( string ):
    result = []
    if len(string) % 2 != 0:
        string += "_"

    for i in range(0, len(string), 2):
        appended = string[i] + string[i+1]
        result.append(appended)
        appended = ""
    return result

# Remove B M W 7
def remove_bmw(string):
    black_list = ["b","m","w","B","M","W"]
    for ch in string:
        if ch in black_list:
            string = string.replace(ch,"")
    return string


