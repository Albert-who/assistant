nums = {0:'', 1:'один ', 2:'два ', 3:'три ', 4:'четыре ', 5:'пять ', 6:'шесть ', 7:'семь ', 8:'восемь ', 9:'девять ',
        10:'десять ', 11:'одиннадцать ', 12:'двенадцать ', 13:'тринадцать ', 14:'четырнадцать ', 15:'пятнадцать ',
        16:'шестнадцать ', 17:'семнадцать ', 18:'восемнадцать ', 19:'девятнадцать ', 20:'двадцать ', 30:'тридцать ',
        40:'сорок ', 50:'пятьдесят ', 60:'шестьдесят ', 70:'семьдесят ', 80:'восемьдесят ', 90:'девяносто ', 100:'сто ',
        200:'двести ', 300:'триста ', 400:'четыреста ', 500:'пятьсот ', 600:'шестьсот ', 700:'семьсот ',
        800:'восемьсот ', 900:'девятьсот ',}

thousands = {0:'тысяч ', 1:'\b\b\b\b\bодна тысяча ', 2:'\b\b\b\bдве тысячи ', 3:'тысячи ', 4:'тысячи ', 5:'тысяч ',
             6:'тысяч ', 7:'тысяч ', 8:'тысяч ', 9:'тысяч ',}
millions = {0:'', 1:'миллион ', 2:'миллиона ', 3:'миллиона ', 4:'миллиона ', 5:'миллионов ', 6:'миллионов ',
            7:'миллионов ', 8:'миллионов ', 9:'миллионов ',}
billions = {0:'', 1:'миллиард ', 2:'миллиарда ', 3:'миллиарда ', 4:'миллиарда ', 5:'миллиардов ', 6:'миллиардов ',
            7:'миллиардов ', 8:'миллиардов ', 9:'миллиардов ',}

def get_key(value):
    for i in nums.keys():
        if nums[i] == value+' ':
            return i
    return 0

def num_to_str(number):
    
    if number >= 1000000000000:
        return 'очень большое число'
    elif number == 0:
        return 'ноль'

    num_str = ''
    sign = ''
    if number < 0:
        sign = 'минус '

    num_units = number % 1000
    num_thousands = number % 1000000 // 1000 
    num_millions = number % 1000000000 // 1000000
    num_billions = number % 1000000000000 // 1000000000

    if num_billions != 0:
        num_str += nums[num_billions // 100 * 100]
        if num_billions % 100 // 10 < 2:
            num_str += nums[num_billions % 100]
        else:
            num_str += nums[num_billions % 100 // 10 * 10]
            num_str += nums[num_billions % 10]
        num_str += billions[num_billions % 10]

    if num_millions != 0:
        num_str += nums[num_millions // 100 * 100]
        if num_millions % 100 // 10 < 2:
            num_str += nums[num_millions % 100]
        else:
            num_str += nums[num_millions % 100 // 10 * 10]
            num_str += nums[num_millions % 10]
        num_str += millions[num_millions % 10]

    if num_thousands != 0:
        num_str += nums[num_thousands // 100 * 100]
        if num_thousands % 100 // 10 < 2:
            num_str += nums[num_thousands % 100]
        else:
            num_str += nums[num_thousands % 100 // 10 * 10]
            num_str += nums[num_thousands % 10]
        if num_thousands % 100 // 10 == 1:
            num_str += 'тысяч '
        else:
            num_str += thousands[num_thousands % 10]
    
    num_str += nums[num_units // 100 * 100]
    if num_units % 100 // 10 < 2:
        num_str += nums[num_units % 100]
    else:
        num_str += nums[num_units % 100 // 10 * 10] 
        num_str += nums[num_units % 10]

    return sign + num_str


def str_to_num(string):
    sign = 1
    if 'минус' in string:
        sign = -1
    num_thousands=''
    num_millions=''
    num_billions=''

    if ('тысяч' in string):
        num_thousands = string.split(' тысяч')[0].split('миллион')[-1]
    if ('миллион' in string):
        num_millions = string.split(' миллион')[0].split('миллиард')[-1].replace('ов', '')
    if ('миллиард' in string):
        num_billions = string.split(' миллиард')[0].replace('ов', '')
    num_units = string.split('миллиард')[-1].split('миллион')[-1].split('тысяч')[-1]

    number = 0

    for i in num_units.split():
        number += get_key(i)

    val=''
    for i in num_thousands.split():
        if i == 'две':
            val = 'два'
        else:
            val = i
        number += get_key(val) * 1000

    for i in num_millions.split():
        number += get_key(i) * 1000000

    for i in num_billions.split():
        number += get_key(i) * 1000000000

    return sign * number