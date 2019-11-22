#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest`
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuplesnamed cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    error=predictions-net_worths
    #print(net_worths)
    num_elements=len(error)

    removing_num_elements=int(round(num_elements*0.1))
    print(removing_num_elements)
    #print(error)

    print(len(net_worths))
    import numpy as np
    for x in range(0,removing_num_elements,1):
	max_error=max(error)
        index_loc=np.where(error==max_error)
	print(index_loc)
	if(len(index_loc)>1):
		y=0
		net_worths=np.delete(net_worths,index_loc[y])
	        error=np.delete(error,index_loc[y])
		ages=np.delete(ages,index_loc[y])
		print(net_worths[index_loc[y]])
		print(y)
				
	else:		
		net_worths=np.delete(net_worths,index_loc)
		print(net_worths[index_loc])
		ages=np.delete(ages,index_loc)	
		error=np.delete(error,index_loc)
		print(x)	
    

    print(len(net_worths))
    print(len(ages))
    print(len(error))
    print(net_worths)
    cleaned_data =[ages,net_worths,error]
    print(type(cleaned_data))
    ### your code goes here

    
    return cleaned_data

