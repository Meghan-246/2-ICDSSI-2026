import re

MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9'
}

def decode_bits(bits):
    bits = bits.strip('0')
    if bits == '1':
        return '.'
    groups = re.findall(r'1+|0+', bits)
    unit = min(len(g) for g in groups)
    result = ''
    for g in groups:
        n = len(g) // unit
        if g[0] == '1':
            result += '-' if n >= 3 else '.'
        else:
            if n >= 7:
                result += '   '
            elif n >= 3:
                result += ' '
    return result

def decode_morse(morseCode):
    return ' '.join(
        ''.join(MORSE_CODE.get(c, '') for c in word.split(' ') if c)
        for word in morseCode.strip().split('   ')
    )
