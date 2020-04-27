import collections

def get_words_number ( ):
    words_number = int ( input ( '\n Please enter the number of words: ' ) )
    return words_number

def creating_dictionary ( words_number ):
    online_dictionary = collections.OrderedDict ( )
    for digit in range ( words_number ):
        translated_word = input ( '\n Please enter the words and the meaning of them: ' )
        word, meaning = translated_word.split ( )
        online_dictionary [ word ] =  meaning
    string_for_translate = input ( '\n Please enter your sentence to translate it: \n' )
    return online_dictionary, string_for_translate

def translator ( dictionary, string ):
    words = ( string.split ( ) )
    translation = []
    for digit in range ( len ( words ) ):
        translation.append(dictionary.get(words[digit], words[digit]))
        return translation

def print_result(translation):
    for digit in range(len(translation)):
        print(translation.pop(0),'')

def main_program():
    online_dictionary, string_for_translate = creating_dictionary ( get_words_number ( ) )
    #    counter [ letter ] = counter.get ( letter, 0 ) + 1
    print_result(translator ( online_dictionary, string_for_translate ))

main_program()