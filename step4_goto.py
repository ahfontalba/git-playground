from basic_calculator import calculate

with open('C:\\Development\\BCS-DevOps\\modules\\module01-general_purpose_coding\\labs\\python_calculator\\step_4.txt', mode='r') as f:
    text_string_list = f.read().splitlines()
    #print(len(text_string_list))


statement = text_string_list[1]
exec_statements = [statement]


statement_visited = False

while not statement_visited:

    calc_list = statement.split()

    if 'calc' in calc_list:
        calc_result = calculate(calc_list[2], int(calc_list[3]), int(calc_list[4]))
    elif 'goto' in calc_list:
        calc_result = calc_list[1]
    elif 'remove' in calc_list:
        if int(calc_list[1]) < len(text_string_list):
            text_string_list.remove(int(calc_list[1]))
            print('item removed: ' + calc_list[1])
    elif 'replace' in calc_list:
        if int(calc_list[1]) < len(text_string_list) and int(calc_list[2]) < len(text_string_list):
            text_string_list[ int(calc_list[1]) ] = text_string_list[int(calc_list[2])]
            print('item replaced: ' + calc_list[1])


    calc_result_int = int(calc_result)
    if calc_result_int >= len(text_string_list):
        print('file out of bounds. Breaking free...')
        break

    statement = text_string_list[calc_result_int]

    if not statement in exec_statements:
        exec_statements.append(statement)
        print(statement)
    else:
        print('Code stopping at line: ' + str(calc_result_int))
        statement_visited = True

    #print(calc_result)

