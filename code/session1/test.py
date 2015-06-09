def flip_a_string(my_str):
    """
    Take a string and invert it, ie:
    >>>"Abi" to "iba"
    
    """
    my_str_list=list(my_str)
    my_str_list.reverse()
    my_str="".join(my_str_list)
    return my_str
    
def am_i_greater_than_forty(num):
        """
        check whether a number is indeed greater than forty returns a boolean"""
        return num>40    
        
        
def is_this_greater_than_forty(num):
            """ return 'yes' if the number is greater than forty, 'no' otherwise"""
            if am_i_greater_than_forty(num):
                return "yes"
            else:
                return "no"
     
def the_third_element(my_list):
 """ return the third element in amapping"""
 return my_list[2]


def which_numbers_are_greater_than_forty(num_list):
    """returns a list of boolean objects depending on whether each number is greater than 40"""
    my_list=[]
    for i in num_list:
        my_list.append(am_i_greater_than_forty(i))
    return my_list           