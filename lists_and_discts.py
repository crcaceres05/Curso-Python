def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Renato", "lastname": "Caceres"}

    super_list = [
        {"firstname": "Cesar", "lastname": "Caceres"},
        {"firstname": "Renato", "lastname": "Avendano"},
        {"firstname": "Juan", "lastname": "Lopez"},
        {"firstname": "Maria", "lastname": "Suarez"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43],
    }

    # for key, value in super_dict.items():
    #     print(key,"-", value)
    
    for i in super_list:
        for key, values in i.items():
            print(key,":", values)

if __name__=='__main__':
    run()