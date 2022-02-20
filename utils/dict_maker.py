
def IPODict(list):
        aaa=[]
        for i in list:
            ipo_details = i.text.split('\n')
            aaa.append(ipo_details)
        IPOs = []
        for ipo in aaa:
            name = ipo[0]
            type = ipo[4] +" " + ipo[3]
            ipo_data = [name, type]
            IPOs.append(ipo_data)
        for i in IPOs:
            ipo_detail = {'key':IPOs.index(i),'name':i[0],'type':i[1]}
            print(ipo_detail)
