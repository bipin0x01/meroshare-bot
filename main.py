from modules import *

input = input_parser()

for demats in input:
    name, dp_id, username, password, crn, txn_pin = [demats[i] for i in range(len(demats))]
    print("Logging in with {}'s account".format(name))
    try:
        login(dp_id,username,password)
    except Exception as e:
        print(e)
        break
    goto_asba()
    open_ipo_lister()
    ipo_selector()
    apply_ipo('10',crn,txn_pin)
    quit_browser()