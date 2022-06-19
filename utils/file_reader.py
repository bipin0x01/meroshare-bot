def file_reader(file_name):
    """
    Reads a file and returns a list of each lines as individual element.
    """

    with open(file_name, 'r') as f:
        # create a list of each line of file after splitting it by comma
        return [line.split(',') for line in f.readlines()]

