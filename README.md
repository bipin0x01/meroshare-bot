# Documentation Draft for MeroShare IPO Application Entry Bot

Step 1. Download the respective Chrome driver binary for your installed chrome version from the link below.
 ``` https://chromedriver.chromium.org/downloads ```
 
 ###Note: I am working on a solution to remove this step for users.

Step 2. Go to the parent directory and run the following commands to install all the pre-requisites.

  ```pip3 install -r requirements.txt```
  
Then, edit the 'demats.txt' file and add all the accounts' information each account separated by a line break and each information separated by commas ','

After adding the account info's, execute the following command from the parent directory.

  ```python3 ./main.py```
  
