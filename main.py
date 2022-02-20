from utils.func import *
from utils.file_reader import file_reader
from utils.input_parser import input_parser

input_file = file_reader('demats.txt')

# Gets the value from the lines of the input file
input = input_parser(input_file)

try:
    for account in input:
        # Loops through each account in the input file
        account_data_length = len(account)
        # Gets the length of the account data
        # Gets the user creds from the account data
        name, dp_id, username, password, crn, txn_pin = [account[i] for i in range(account_data_length)]
        print("Logging in with {}'s account".format(name))
        try:
            login(dp_id,username,password)
        except Exception as e:
            print(e)
            break
        # goto_asba()
        # open_ipo_lister()
        # try:
        #     print(ipo_selector(0))
        # except Exception as e:
        #     print('You are either not eligible or have already applied for this ipo')
        #     break
        # apply_ipo('10',crn,txn_pin)
        # print("{}'s account successfully applied for IPO".format(name))
    quit_browser()
except Exception as e:
    print(e)
    quit_browser()

    