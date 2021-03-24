from basic_calculator import calculate

with open('C:\\Development\\BCS-DevOps\\modules\\module01-general_purpose_coding\\labs\\python_calculator\\step_2.txt', mode='r') as f:
    text_string_list = f.read().splitlines()

total = 0
for item in text_string_list:
    item_list = item.split()
    calc_result = calculate(item_list[1], int(item_list[2]), int(item_list[3]))
    print(calc_result)
    total += calc_result
    

print('Total: ' + str(total))


#25335.305773048156