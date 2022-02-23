# Documentation

### Step 1. Download the respective Chrome driver binary for your installed chrome version from the link below.

`https://chromedriver.chromium.org/downloads`

_Note: I am working on a solution to remove this step for users._

### Step 2. Activate the virtual env using following command

[Install & activate virtual environment in the project root folder](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)


### Step 3. Edit the 'demats.txt' file and add all the accounts' information each account separated by a line break and each information separated by commas ','

#### Example

`Bipin Thapa,DP-ID,USERNAME,PASSWORD,CRN,TXN-PIN`

### Step 3. After adding the account info's, execute the following command from the parent directory.

`python3 ./main.py`
