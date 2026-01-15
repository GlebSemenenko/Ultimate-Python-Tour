import random

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

# Remove BMW 7
def remove_bmw(string):
    black_list = ["b","m","w","B","M","W"]
    for ch in string:
        if ch in black_list:
            string = string.replace(ch,"")
    return string

# The Office I - Outed 7
def outed(meet, boss):
    count = 0
    res = 0
    for k, v in meet.items():
        if k == boss:
            v = v * 2
        count += 1
        res += v
        print(count, res)
    return res / count

# The Office II - Boredom Score II 7
def boredom(staff):
    dep = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "change": 5,
        "IS": 10
    }
    res = 0
    for _, v in staff.items():
        res +=dep[v] # достать значение по ключу и прибавить его к результату
        print(res)

# Rock Paper Scissors! 8
def rps():
    symbol = {1:"камень", 2:"бумага", 3:"ножницы"}
    # рандомное число от 1 до 3
    player1 = random.randint(1,3)
    player2 = random.randint(1,3)
    print(symbol[player1], symbol[player2])

    if player1 == player2:
        print("Ничья! Играем ещё раз.")
        return rps()

    wins = [(1, 3), (2, 1), (3, 2)]
    if (player1, player2) in wins:
        print(f"Победитель — Игрок 1 ({symbol[player1]})!")
    else:
        print(f"Победитель — Игрок 2 ({symbol[player2]})!")

# Sum Arrays 8
def sum_array(arr):
    return sum(arr)

# Number of Decimal Digits 7
def digits(n):
    return len(str(n))

# Letterbox Paint-Squad 7
def paint_letterboxes(start, finish):
    result = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    while start <= finish:
        print(start, finish)
        str_value = str(start)
        for ch in str_value:
            if ch in result:
                result[ch] = result[ch] + 1
        start += 1
    return result

# Find the odd int 6
def find_it(seq):
    mp = {}
    for n in seq: # Проверить кол-во вхождений каждого числа
        if n in mp:
            mp[n] += 1
        else:
            mp[n] = 1
    for k, v in mp.items():
        if v % 2 != 0:
            return k
    return -1\

# max diff - easy 7
def max_diff(lst):
    return max(lst) - min(lst)

# Sum of Multiples 8
def sum_mul(n, m):
    res = []
    for i in range (n, m):
        if i % n == 0:
            res.append(i)
    return sum(res)

print(sum_mul(4, 123))