from time import sleep


from utils.func import *
from utils.file_reader import file_reader
from utils.input_parser import input_parser

input_file = file_reader('demats.txt')

# Gets the value from the lines of the input file
demats = input_parser(input_file)


try:
    number_of_accounts = len(demats)
    print('Number of accounts Detected: %d' % number_of_accounts)
    for account in demats:
        name, dp_id, username, password, crn, txn_pin = [account[i] for i in range(6)]
        try:
            login(dp_id,username,password)
        except:
            print('Could not login')
            break
        goto_asba()
        open_ipo_lister()
        break
except Exception as e:
    print(e)
    quit_browser()
minimize_browser()
    
share = int(input('Press Enter the respective option to continue:'))
number_kitta = int(input('Press Enter the number of units(kitta) to be applied.'))

maximize_browser()
try:
    for account in demats:
        # Loops through each account in the input file
        account_data_length = len(account)
        # Gets the user creds from the account data
        name, dp_id, username, password, crn, txn_pin = [account[i] for i in range(6)]
        print("Logging in with {}'s account".format(name))
        try:
            login(dp_id,username,password)
        except Exception as e:
            print('Could not login. Please check the login credentials and try again.')
            break
        sleep(1)
        goto_asba()
        sleep(1)
        try:
            # select the ipo choosen from the list by the user
            ipo_selector(share)
        except Exception as e:
            termcolor.cprint('Looks like you have already applied for this IPO from {}\'s account'.format(name), 'red')
            continue
        sleep(1)        apply_ipo(number_kitta,crn,txn_pin)
        sleep(1)
    quit_browser()
except Exception as e:
    print(e)
    quit_browser()