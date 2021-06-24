def calculate_cross_table(answers_for_columns,columns):
    
    root_answers_count=[]

    # Looping through selected root answers, count occurrences of them, append to root_answers_count
    for answer in answers_for_columns[0]:
        counter=columns[0].count(answer)
        root_answers_count.append(counter)


    output=[]

    # Looping in range of all columns besides root column
    for column_id in range(len(columns[1:])):
        # Reading column
        column= columns[1:][column_id]
        # Reading selected answers for column
        selected_answers=answers_for_columns[1:][column_id]

        answers=[]
        # Looping through answers to root question and answers to other columns
        for root_answer,row in (zip(columns[0],column)):
            # If answer to other columns (row) is selected one append it to answers
            if row in selected_answers:
                answers.append(root_answer)
                

        occurrences=[]

        #Looping through selected answers to root question
        
        for root_answer in (answers_for_columns[0]):

            #Counting occurrences of every answer and appending it 
            counter=answers.count(root_answer)
            occurrences.append(counter)
        output.append(occurrences)
        


    all_answers_count=[]
    all_answers_count.append(root_answers_count)
    for column in output:
        all_answers_count.append(column)

    print('all answers count for every column including root column',all_answers_count)


    divided_all=[]


    #Looping through columns containing occurrences of answers, and calculating percent
    for occurrences_column in all_answers_count:
        divided_for_column=[]
        for answer in occurrences_column:
            if sum(occurrences_column)!=0:
                divided= answer/sum(occurrences_column)
                divided_for_column.append(divided)
            else:
                divided_for_column.append(None)
        divided_all.append(divided_for_column)
    #print(answers_for_columns[0])
    #print(divided_all)
    return divided_all
'''
    #Workbook is created
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')


    for index, answer in enumerate(answers_for_columns[0]):
        sheet1.write(index+1,0,answer)
        for index2, divided_for_column in enumerate(divided_all):
            print(divided_for_column,'index2',index2,'index',index)
            print(divided_for_column[index])
            sheet1.write(index+1,index2+1,(divided_for_column[index]))



    for column_id in range(len(columns[0:])):
        default_question_name=f'Question {column_id}'
        sheet1.write(0,column_id+1, default_question_name)


    wb.save('CrossTable.xls')
'''
    
    #print(answers_for_columns[0])
    