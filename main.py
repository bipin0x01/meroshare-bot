from time import sleep
from utils.func import *
from utils.file_reader import file_reader
from utils.input_parser import input_parser

input_file = file_reader('demats.txt')

# Gets the value from the lines of the input file
demats = input_parser(input_file)

# List all open IPOS in a table using the first account given by user
try:
    number_of_accounts = len(demats)
    print(f'Number of accounts Detected: {number_of_accounts}')

    for account in demats:
        name, dp_id, username, password, crn, txn_pin = [account[i] for i in range(6)]

        try:
            while web_driver.driver.current_url != "https://meroshare.cdsc.com.np/#/dashboard":
                login(dp_id,username,password)
                sleep(2)

                if web_driver.driver.current_url == "https://meroshare.cdsc.com.np/#/dashboard":
                    break
        except:
            print('Could not login! Please try again')
            break

        goto_asba()
        open_ipo_lister()

        break

except Exception as e:
    print(e)
    quit_browser()

share = int(input('Press Enter the respective option to continue:'))
number_kitta = int(input('Press Enter the number of units(kitta) to be applied.'))

try:
    for account in demats:  # Loops through each account in the input file
        name, dp_id, username, password, crn, txn_pin = [account[i] for i in range(6)]  # Gets the user creds from the account data

        try:
            while web_driver.driver.current_url != "https://meroshare.cdsc.com.np/#/dashboard":
                login(dp_id,username,password)
                sleep(2)

                if web_driver.driver.current_url == "https://meroshare.cdsc.com.np/#/dashboard":
                    break

        except Exception as e:
            print('Could not login. Please check the login credentials and try again.')
            break

        print("Applying {} kitta IPO with {}'s account".format(number_kitta,name))
        goto_asba()
        sleep(1)

        try:
            # select the ipo chosen from the list by the user
            ipo_selector(share)

        except Exception as e:
            termcolor.cprint('Looks like you have already applied for this IPO from {}\'s account'.format(name), 'red')
            continue

        sleep(1)
        apply_ipo(number_kitta,crn,txn_pin)
        sleep(1)

    quit_browser()

except Exception as e:
    print(e)
    quit_browser()
