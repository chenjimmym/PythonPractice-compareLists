list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']
answer = True

if len(list_one) != len(list_two):
    answer = False
else:
    for i in range(0,len(list_one)):
        if list_one[i] != list_two[i]:
            answer = False

if answer == True:
    print "Lists are the same"
else:
    print "Lists are NOT the same"