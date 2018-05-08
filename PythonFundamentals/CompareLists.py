#write program that compare two lists and prints message depending on if inputs are identical or not
#if identical, print "the lists are the same!"
#if not identical, print "the lists are not the same!"

def compare_lists(list_one, list_two):
    if list_one == list_two:
        print "the lists are the same!"
    else:
        print "the lists are different!"

#you must call the function for it to execute!
#lists can have the same name because python follows the order of the code!

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

compare_lists(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

compare_lists(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]

compare_lists(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compare_lists(list_one, list_two)
