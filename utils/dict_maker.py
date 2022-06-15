
def IPODict(list):
        all_ipos = []
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
            ipo_detail = [IPOs.index(i)+1,i[0],i[1]]
            all_ipos.append(ipo_detail)
        return all_ipos