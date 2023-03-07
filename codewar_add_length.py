def add_length(word):
    converted_list = word.split()
    list_with_length = []

    for i in range(len(converted_list)):
        word_length = len(converted_list[i])
        word_length = str(word_length)
        list_with_length.append(converted_list[i] + ' ' + word_length)
    
    return list_with_length

add_length('Once Upon A Time')