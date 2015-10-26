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
    print ('The ' + str(num)+' largest number in the list is: ' +str(nums[len(nums)-num]))

#test
nums1 = [1,5,10,15,2,4,1]
num1 = 2 #nth largest number in this case the 2nd largest which is 10
print('list of numbers: ' + str(nums1))
nTh_LargestNum(nums1, num1)

"""
#Question 10.) (currently not working and im not sure why)
# Given a list this will return the standard deviation of the list.
import math
def standardDeviation(nums):
    mean = 0
    summation = 0
    for i in range(0,len(nums)):#calculate mean
        mean = mean+nums[i]
    for j in range(0, len(nums)):#calculate sqrt(nums[i]-mean)
        summation = summation + (math.pow((nums[j]-mean),2)
    sd = math.sqrt((summation)/(len(nums)) #summation of all numbers
    return sd


#test
list1 = [1,2,4,5,6,7,8,9,10]
print (str(standardDeviation(list1)))
"""
"""
#Question 11.) 

def deg2dms(decimalDeg):
    #deg1 = deg
    d = int(decimalDeg)
    print(str(d) + ' degrees')
    minutes = int(((decimalDeg-d) * 60))
    print(str(minutes)+' minutes')
    seconds = (decimalDeg-d-(minutes/60))*3600
    print(str(seconds)+ ' seconds')

#main
deg1 = 30.263888889
print deg1
deg2dms(deg1)

"""

#Quesiton 12.)
#Given an integer this function will print x number of rows of lists where the end two numbers in each
#row are added together
def tri(num):
    for i in range(0,num):



#test
num2 = 8
tri(8)


