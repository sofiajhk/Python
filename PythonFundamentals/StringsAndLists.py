words = "It's thanksgiving day. It's my birthday, too!"
#find and print the first occurence of the word day
print words.find("day")
#replace word day with month in a new string
newWords = words.replace('day', 'month')
print newWords

x = [7, -10, 18, 42, -98, 0]
#print the min and max of this list
print 'maximum:', max(x)
print 'minimum:', min(x) 

x = ["what's", 6, -14, 59, 0, -29, 78, "up?"]
#print first and last values of the list
print "first value:", x[0]
print "last value:", x[len(x)-1]
#create new list with first and last value
newX = [x[0], x[len(x)-1]]
print newX

newList = [29, 4, -17, 84, 0, -3, 98, -67, 11, 32, -11]
#sort the list
sortedList = sorted(newList)
print sortedList
#split list in half
halfList = sortedList[:len(sortedList)/2]
halfList2 = sortedList[len(sortedList)/2:]
print "first half:", halfList
print "second half:", halfList2
#combine the list with the first half at index 0 of second half
halfList2.insert(0,halfList)
print "combined list:", halfList2
