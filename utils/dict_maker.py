
def IPODict(list):
        aaa = [i.text.split('\n') for i in list]

        IPOs = [[ipo[0], f'{ipo[4]} {ipo[3]}'] for ipo in aaa]
        all_ipos = [[IPOs.index(i) + 1, i[0], i[1]] for i in IPOs]

        return all_ipos
