import random


def create_pass():
    """This create_pass() is a function that accepts no arguments. This function is supposed to generate a 16 digit
    random password. This password involves symbols, digits, upper-case & lower-case alphabets. The return type of the
    function is a single string. Once function invoked it will return a string.
    p = create_pass()
    >> (KJCcZ1oGEr5Mu1r #This is an example.
    """
    max_len = 16  # Max length of the passkey.

    # Initializing strings.
    s1 = '0123456789'  # Digits from 0-9.
    s2 = 'abcdefghijklmnopqrstuvwxyz'  # All the 26 lower-case char.
    s3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # All the 26 upper-case char.

    # Initializing lists.
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']  # Symbols.
    digits = list(s1)
    lo_alp = list(s2)
    up_alp = list(s3)

    # Combined List.
    combined_list = digits + lo_alp + up_alp + symbols

    ''' We further select 4 random chars from the 4 various lists we have initialized, to make sure that all chars are 
     present.'''
    rand_dig = random.choice(digits)
    rand_sym = random.choice(symbols)
    rand_low = random.choice(lo_alp)
    rand_up = random.choice(up_alp)

    final_pass = list(rand_dig + rand_sym + rand_low + rand_up)
    cur = max_len - len(final_pass)

    while cur > 0:
        final_pass += random.choice(combined_list)
        cur -= 1

    # Lastly, we shuffle the list in order to avoid leaving a trail of pattern for the first 4 chars.
    random.shuffle(final_pass)

    # We join the elements of a list into a single 16 char string and return it to the main caller.
    password = ''.join(i for i in final_pass)
    return password


# Driver Code
if __name__ == '__main__':
    pk = create_pass()
    print(f'The 16 digit passkey generated is {pk}')
    # help(create_pass)  # Guide to use my function.

# Yash Tawde [New Horizon College of Engineering]
