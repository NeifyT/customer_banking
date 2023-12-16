# Contains utility functions for type validation with user input

def clean_input_to_float(user_input):
    """
    Removes common punctuation associated with requested user input of 
    dollar value or percentage and tries to convert to a float value.

    Repeats request for user input on type cast error.

    Args:
        user_input (string): as typed by user from input()
    Tries: 
        type casting to float()
    Raises: 
        ValueError: could not convert string to float
    Returns:
        value as a float 
    """
    not_float = True
    while not_float:
        user_input = user_input.replace(",", "")
        user_input = user_input.replace("$", "")
        user_input = user_input.replace("%", "")
        # a negative number? just in case users are silly
        user_input = user_input.replace("-", "")
        try:
            input_val = float(user_input)
            not_float = False
        except:
            user_input = input("Invalid entry, please try again: ")
    
    return input_val

def clean_input_to_int(user_input):
    """
    Utilizing clean_input_to_float(), first assures user input is
    able to be converted to a float, then makes a fancy typecast 
    from splitting a string at the decimal place and type casts
    just the whole value to int.

    Args:
        user_input (string): as typed by user from input()
    Returns:
        value as a int
    """
    # utilizes the code to validate user input including loop to request retry on fail
    user_input = clean_input_to_float(user_input)
    # now let's drop the decimal via string split and recast only left of the decimal
    int_val = int(str(user_input).split(".")[0])
    
    return int_val
