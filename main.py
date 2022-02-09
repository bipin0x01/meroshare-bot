from modules.func import login, goto_asba, apply_ipo, open_ipo_lister,ipo_selector,quit_browser,reader,input_parser

input_file = reader('demats.txt')
input = input_parser(input_file)

try:
    for account in input:
        account_data_length = len(account)
        name, dp_id, username, password, crn, txn_pin = [account[i] for i in range(account_data_length)]
        print("Logging in with {}'s account".format(name))
        try:
            login(dp_id,username,password)
        except Exception as e:
            print(e)
            break
        goto_asba()
        open_ipo_lister()
        try:
            print(ipo_selector(0))
        except Exception as e:
            print('You are either not eligible or have already applied for this ipo')
            break
        apply_ipo('10',crn,txn_pin)
        print("{}'s account successfully applied for IPO".format(name))
    quit_browser()
except Exception as e:
    print(e)
    quit_browser()

    