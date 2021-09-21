def arithmetic_arranger(problems, answer = False):

    if len(problems)>5:
        return("Error: Too many problems.")

    splitted = list()
    firstOperand = list()
    secondOperand= list()
    operators = list()
    results = list()

    spacing = list()
    firstRow = str()
    secondRow = str()
    dashRow = str()
    thirdRow = str()

    for i in problems:
        i.rstrip()
        i.lstrip()
        splitted = i.split(" ")

        if len(splitted[0]) > 4 or len(splitted[2]) > 4:
            return("Error: Numbers cannot be more than four digits.")

        #check if the operator is either + or -
        if not (splitted[1] == "+" or splitted[1] == "-"):
            return("Error: Operator must be '+' or '-'.")

        try:
            firstOperand.append(splitted[0])
            secondOperand.append(splitted[2])

            #add the operands if the operator is +. else substract the operands
            if splitted[1] == "+":
                results.append(int(splitted[0]) + int(splitted[2]))
            else:
                results.append(int(splitted[0]) - int(splitted[2]))

        except:
            return("Error: Numbers must only contain digits.")

        operators.append(splitted[1])

    #create the structure
    rounds = 0
    while rounds < len(firstOperand):
        longestOperand = max(len(firstOperand[rounds]), len(secondOperand[rounds]))
        spacing.append(longestOperand)

        #first line
        for j in range((spacing[rounds] + 2) - len(firstOperand[rounds])):
            firstOperand[rounds] = " " + firstOperand[rounds]
        firstRow = firstRow + firstOperand[rounds] + "    "

        #second line
        for k in range((spacing[rounds] + 1) - len(secondOperand[rounds])):
            secondOperand[rounds] = " " + secondOperand[rounds]
        secondRow = secondRow + operators[rounds] + secondOperand[rounds] + "    "

        #dash line
        for l in range((spacing[rounds] + 2 )):
            dashRow = dashRow + "-"
        dashRow = dashRow + "    "

        #answer line
        for m in range((spacing[rounds] + 2) - len(str(results[rounds]))):
            results[rounds] = " " + str(results[rounds])
        thirdRow = thirdRow + results[rounds] + "    "

        rounds = rounds + 1

    if answer == False:
        arranged_problems = firstRow.rstrip() + "\n" + secondRow.rstrip() + "\n" + dashRow.rstrip()
    else:
        arranged_problems = firstRow.rstrip() + "\n" + secondRow.rstrip() + "\n" + dashRow.rstrip() + "\n" + thirdRow.rstrip()

    return arranged_problems
