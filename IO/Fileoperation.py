# read file is used for reading the file
def ReadFile(filename):
    """
    :param filename: file name is given
    :return: file will open
    """
    with open(filename, 'r') as f:  # Open File As test.txt
        lst = f.read().split()  # Read File And Store In List
        f.close()
    return lst


# overwrite is used for the over writing file
def OverWrite(lst, filename):
    """
    :param lst: work you want to update
    :param filename:  filename where we want to update
    :return: file updated
    """
    f = open(filename, 'w')  # Open File In write mode
    for item in lst:  # Loop Through All Items in List
        f.write("%s " % item)  # Write In the File
    f.close()
