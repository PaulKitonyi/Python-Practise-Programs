def get_formatted_name(first, last, middle=''):
    """A function to format a name"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()



# print(get_formatted_name('paul', 'kitonyi'))