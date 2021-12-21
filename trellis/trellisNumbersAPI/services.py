ONES_MAP = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}


TENS_MAP = {
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

THOUSANDS_MAP = {
    1: 'thousand',
    2: 'million',
    3: 'billion',
    4: 'trillion',
    5: 'quadrillion',
    6: 'quintillion',
    7: 'sextillion',
    8: 'septillion',
    9: 'octillion',
    10: 'nonillion',
    11: 'decillion',
    12: 'undecillion',
    13: 'duodecillion',
    14: 'tredecillion',
    15: 'quattuordecillion',
    16: 'quindecillion',
    17: 'sexdecillion',
    18: 'septendecillion',
    19: 'octodecillion',
    20: 'novemdecillion',
    21: 'vigintillion',
    22: 'unvigintillion',
    23: 'duovigintillion',
    24: 'trevigintillion',
    25: 'quattuorvigintillion',
    26: 'quinvigintillion',
    27: 'sexvigintillion',
    28: 'septenvigintillion',
    29: 'octovigintillion',
    30: 'novemvigintillion',
    31: 'trigintillion',
    32: 'untrigintillion',
    33: 'duotrigintillion',
    34: 'tretrigintillion',
}


def get_thousands_index (number: int):
    num_len = len(str(number))
    places = list(THOUSANDS_MAP.keys())
    # probably a more pythonic way of doing this.
    for idx, place in enumerate(places):
        if num_len <= place * 3:
            return idx


def get_number_words_list(number: int, result=[]):
    if number == 0:
        return ['zero']
    if number < 0:
        raise ValueError('Invalid number')
    if number < 20:
        return [*result, ONES_MAP.get(number)]
    # Might be some other maths to make 100s work similar to 1000s but it's late. <3
    if number < 100:
        remain  = number % 10
        tens = (number - remain) / 10 
        return get_number_words_list(remain, [TENS_MAP.get(tens), *result])
    if number < 1000:
        remain = number % 100
        hundreds = int((number - remain) / 100)
        right = get_number_words_list(remain)
        return  [ONES_MAP.get(hundreds), 'hundred', *right]
    

    thousands_idx = get_thousands_index(number)
    remain = number % 10 ** (thousands_idx * 3)
    thousands = int((number - remain) / 10 ** (thousands_idx * 3))
    thousands_word = THOUSANDS_MAP.get(thousands_idx)
    right = get_number_words_list(remain)
    left = get_number_words_list(thousands)    
    
    return [*left, thousands_word, *right]

def num_to_english(number: int):
    return ' '.join(get_number_words_list(number)).strip()