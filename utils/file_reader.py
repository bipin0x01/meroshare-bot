def file_reader(file_name):
    """
    Reads a file and returns a list of each lines as individual element.
    """
    # loop through each line separately
    with open(file_name, 'r') as f:
        file = f.readlines()
        # create an empty array of name a
        a = []
        # loop each line of file
        for line in file:
            # split each line into a list
            a.append(line.split(','))
        f.close()
        return a

