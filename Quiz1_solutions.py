# GIS Python Programming Quiz #1
# Created By: Jordan McMillan
# Created On: October 23, 2015

#Question 2.)
#computes the value of the 10 numbers ranging from 0 to 99 with an increment of 11
my_values = 0
for i in range(0,101,11):
    my_values = my_values + i
print(str(float(my_values)/10))


#Question 3.)
#Adds all the letters into a list except for white spaces and periods
listOfXs = []
sentence = "The fox is jumping over another fox that turns out to be a lynx. Foo Bar."
length = len(sentence)
for i in range(len(sentence)):
    if sentence[i] != " " and sentence[i] != ".": # skip if character is a space or period
       letter = sentence[i]
       listOfXs.append(letter)
print(listOfXs)



#Question 8.)
# takes a word and a suffix and returns True if the suffix is the suffix of the word
def hasSuffix(word, suffix):
    j =  len(word)- len(suffix)
    isTrue = 0
    for i in range(len(suff)):
        if word[j] == suffix[i]:
            j = j+1
            isTrue = isTrue + 1
    if isTrue == len(suffix):
        return True        
    return False

#test
w = "example"
suff = "ple"
print (hasSuffix(w, suff))


#Question 9.)
# returns the n-th largest number
def nTh_LargestNum(nums, num):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == num:
            print ('The ' + str(num)+'th largest number in the list is: ' +str(nums[i]))


nums1 = [1,5,10,15,2,4,1]
num1 = 3
print('list of numbers: ' + str(nums1))
nth_LargestNum(nums1, num1)
