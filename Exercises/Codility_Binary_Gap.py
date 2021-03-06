MAXINT = 2147483647


def solution(N):
    """
    Determines the maximal 'binary gap' in an integer
    :param N: a positive integer (between 1 and maxint or 2million odd)
    :return: a count of the longest sequence of zeros in the binary representation of the integer
    """
    # protect against crazy inputs
    if not isinstance(N, int):
        raise TypeError("Input must be an integer")
    if N < 1:
        raise ValueError("Input must be a positive integer")
    if N > MAXINT:
        raise ValueError("Input must be a positive integer less than 2,147,483,647")

    # convert the number to a string containing '0' and '1' chars
    binary_string = str(bin(N))[2:]

    # the longest binary gap: use None to indicate no 'gap' yet found (set to zero at the first flip)
    max_count = None
    # count the bits in the sequence
    this_count = 0
    # true if the last bit was a zero
    was_zero = None

    # loop over all the 0/1 chars in the string
    for bit in binary_string:
        is_zero = bit == '0'

        # if the bit value has flipped
        if bool(was_zero) != bool(is_zero):
            # the first sequence doesn't count eg: 1111001 has a result of 2
            if max_count is None:
                max_count = 0
            # save the biggest gap
            elif this_count > max_count:
                max_count = this_count
            # reset the counter
            this_count = 1
        else:
            # increment the length of the sequence
            this_count += 1

        # track what the last bit was
        was_zero = is_zero

    #print "%s: %s = %s" % (N, binary_string, max_count)
    if max_count is not None:
        return max_count
    else:
        # no binary gaps found
        return 0

print(solution(666))