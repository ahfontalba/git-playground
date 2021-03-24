from basic_calculator import calculate

with open('C:\\Development\\BCS-DevOps\\modules\\module01-general_purpose_coding\\labs\\python_calculator\\step_3.txt', mode='r') as f:
    text_string_list = f.read().splitlines()
    #print(len(text_string_list))


statement = text_string_list[1]
exec_statements = [statement]


statement_visited = False

while not statement_visited:

    calc_list = statement.split()

    if len(calc_list) > 2:
        calc_result = calculate(calc_list[2], int(calc_list[3]), int(calc_list[4]))
    else:
        calc_result = calc_list[1]

    statement = text_string_list[int(calc_result)]

    if not statement in exec_statements:
        exec_statements.append(statement)
        print(statement)
    else:
        print('Code stopping at line: ' + str(calc_result))
        statement_visited = True

    #print(calc_result)

