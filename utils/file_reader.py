def file_reader(file_name):
    """
    Reads a file and returns a list of each lines as individual element.
    """
    # loop through each line separately
    with open(file_name, 'r') as f:
        file = f.readlines()
        # create a list and append each line of file to it after splitting it by comma
        a = [line.split(',') for line in file]
        return a

