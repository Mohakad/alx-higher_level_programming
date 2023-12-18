#!/usr/bin/python3
def new_in_list(my_list, idx, element):
<<<<<<< HEAD
	    new_list = []
	        for i in my_list:
	        	new_list.append(i)
	        if idx < 0 or idx >= len(new_list):
			        return new_list
				    new_list[idx] = element
				           return new_list
=======
    new_list = []
    for i in my_list:
        new_list.append(i)
    if idx < 0 or idx >= len(new_list):
        return new_list
    new_list[idx] = element
    return new_list
>>>>>>> 050317d9ac3030985d7b25477ff84c506fcd372c
