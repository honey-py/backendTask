def remove_duplicates(input_list, output_list):
    for i in range(len(input_list)):
        if input_list[i] not in output_list:
            output_list.append(input_list[i])
