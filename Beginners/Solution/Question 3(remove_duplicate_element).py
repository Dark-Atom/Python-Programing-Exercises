def remove_element(input_list):
        updated_list=list(set(input_list))
        return list(map(int,updated_list))

print(remove_element(input().split(",")))
    
