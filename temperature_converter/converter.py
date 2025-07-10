def temp_converter():
    tmp = input('Enter the number of the temp:')
    typ = (input('Enter the temp type you want to switch to, F/C:')).upper()

    try: 
        tmp = int(tmp)
    except Exception as e:
         return print(e)
    
    if typ == 'F':
        converted_tmp = (tmp * 1.8) + 32
        print(f'The converted temp is: {converted_tmp}C')
        return 
    elif typ == 'C':
        converted_tmp = (tmp - 32) // 1.8
        print(f'The converted temp is: {converted_tmp}F')
        return
    else: 
        print('Please try again, your input was wrong.')



temp_converter()

