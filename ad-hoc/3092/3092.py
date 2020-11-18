from functools import reduce
import re


def fun(txt):
    global special_cards

    txt = re.sub(r'(\D)\1+', r'\1', txt)
    txt = re.sub(r'\d', '', txt)

    for i in xrange(len(txt)):
        j = find_index(special_cards, txt[i])

        if j > 0 and special_cards[j - 1] not in txt[0:i]:
            txt = txt[:i] + '0' + txt[i+1:]

    return re.sub(r'\d', '', txt)


def find_index(txt, char):
    try:
        return txt.index(char)
    except ValueError:
        return None


special_cards = 'QJKA'
if __name__ == '__main__':
    for _ in xrange(input()):
        ideal_sequence = fun(raw_input())
        indexes = [find_index(ideal_sequence, card) for card in special_cards]

        if reduce(lambda a, b: a < b, indexes):
            print 'Agora vai'
        else:
            print 'Agora apertou sem abracar'
