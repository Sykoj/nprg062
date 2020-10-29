def convert_bases(number_in_input_base, input_base=2, output_base=10):
    result_in_output_base = 0
    exponent = 1                                        # exponent starts as output_base^0 = 1

    while number_in_input_base > 0:             
        remainder = number_in_input_base % output_base
        number_in_input_base //= output_base
        result_in_output_base += remainder * exponent   # exponent is output_base^i
        exponent *= input_base                          # iterations: [output_base^0, output_base^1, output_base^2, ...]
    return result_in_output_base
