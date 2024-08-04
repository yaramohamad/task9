
user_input = input("Enter a list of numbers separated by spaces: ")  
number_list = list(map(int, user_input.split()))  

check_values = [0, 2, 5]  


for x in check_values:  
    count = number_list.count(x)  
    if count > 1:  
        print(f"{x} occurs {count} times in the list.")  
    else:  
        print(f"{x} occurs {count} time(s) in the list.")  
  
    if count > 1:  
        filtered_list = [item for item in number_list if item != x]  
        print(f"List after removing {x}: {filtered_list}")