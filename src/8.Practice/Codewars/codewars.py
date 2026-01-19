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
        return symbol[player1]
    else:
        return symbol[player2]

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
    return -1

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

# Spanish DNI Validation Algorithm 7
def is_valid_dni(s: str) -> bool:
    num = int(s[:-1]) # сдедать валидацию (корректно ли введен аргумент
    d = num % 23
    dni_letter_map = {0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G', 5: 'M', 6: 'Y', 7: 'F', 8: 'P', 9: 'D', 10: 'X', 11: 'B',
                      12: 'N', 13: 'J', 14: 'Z', 15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L', 20: 'C', 21: 'K', 22: 'E'}
    letter = dni_letter_map[d]
    if letter == s[-1]:
        return True
    else:
        return False

# Don't give me five! 7
def dont_give_me_five(start,end):
    res = end - start + 1
    print(res)
    for n in range (start, end + 1):
        if "5" in str(n):
            print(n, "find")
            res -= 1
    return res

# Brute Force Detector 6
def detect_brute_force(logs):
    ip_fail_count = {}
    suspicious_ips = set()

    for log in logs:
        parts = log.split(" ")
        ip = parts[0]
        status = parts[1]

        if status == "LOGIN_SUCCESS":
            ip_fail_count[ip] = 0
        elif status == "LOGIN_FAIL":
            if ip in ip_fail_count:
                ip_fail_count[ip] = 1
            else:
                ip_fail_count[ip] += 1
        if ip_fail_count[ip] >= 3:
            suspicious_ips.add(ip)
    return suspicious_ips


logs = [
    "192.168.1.1 LOGIN_FAIL user=admin",
    "192.168.1.1 LOGIN_FAIL user=admin",
    "192.168.1.1 LOGIN_FAIL user=root",
    "10.0.0.5 LOGIN_FAIL user=test",
    "10.0.0.5 LOGIN_SUCCESS user=test"
]

# Sorted? yes? no? how? 7
def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return "yes, ascending"
    if arr == sorted(arr, reverse=True):
        return "yes, descending"
    else:
        return "no"

