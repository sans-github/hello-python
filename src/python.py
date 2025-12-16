

def hello_python(): 
    
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    print('{}{}'.format("\n", "==START=="))
    print(numbers)
    print('{}{}'.format("\n", "===▼▼▼▼▼==="))
    
    # Slicing operations. [start:stop:step]
    # res=numbers[-3:] # Last 3. step defaults to 1
    # res=numbers[-4::2] # Start at -4, then print the rest skipping 2
    # res=numbers[-4:-2] # From -4 to -2
    res=numbers[:-2]# Everything except for last 2
    
    print(type(res))
    print(res)
    
    print(f"{"===▲▲▲▲===\n"}")


if __name__=='__main__':
    # hello_panda()
    hello_python()