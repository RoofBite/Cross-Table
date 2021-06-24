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

    


    divided_all=[]


    #Looping through columns containing occurrences of answers, and calculating percent
    for occurrences_column in all_answers_count:
        divided_for_column=[]
        for answer in occurrences_column:
            if sum(occurrences_column)!=0:
                divided= (answer/sum(occurrences_column))*100
                divided = "{:.2f}%".format(divided)
                divided_for_column.append(divided.replace('.',','))
            else:
                divided_for_column.append(None)
        divided_all.append(divided_for_column)
    #print(answers_for_columns[0])
    #print(divided_all)
    return divided_all

def format_output_for_excel(answers_for_columns,divided_all,questions_number_int,quesion_0_possible_answers_number_int):
    output_string='Answers column\tAll answers form main question\t'
    print(answers_for_columns,'answers_for_columns')
    x=[[0.5, 0.5], [None, None], [1.0, 0.0], [1.0, 0.0]]
    for i in range(1,questions_number_int+1):
        output_string+=f'Question {i}'
        
        if i==questions_number_int:
            output_string+='\r\n'     
        else:
            output_string+='\t'
    
    for i in range(quesion_0_possible_answers_number_int):
        output_string+=f'{answers_for_columns[0][i]}'
        for index in range(questions_number_int+1):
            
            output_string+=f'\t{divided_all[index][i]}'
            
            if index==questions_number_int:
                
                output_string+='\r\n'




    print(output_string)
    
    return output_string

    