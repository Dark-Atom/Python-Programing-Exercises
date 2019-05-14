def add_list(number):
    main_list=[]
    for i in range(number):
        main_list.append(int(input()))
    return main_list

if __name__=='__main__':
    number=int(input("How many number do you want to add:"))
    print(add_list(number))
