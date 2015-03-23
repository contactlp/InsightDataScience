'''
The first part of the coding challenge is to implement your own version of Word
Count that counts all the words from the text files contained in a directory 
named wc_input and outputs the counts (in alphabetical order) to a file named 
wc_result.txt,which is placed in a directory named wc_output.

'''
###
import time
import os
import glob
import pickle 
import re
#begainning = time.time()
running_total = 0
def find_median():
    global running_total
    if running_total%2.0 ==0.0:
        median= running_total//2
        #print 'this med', median
        
        global running_sum_sorted_number
        previous = 0 
        for index, number in enumerate(running_sum_sorted_number):
            if number !=0 and number ==median:
                first = index
                break
            if number !=0 and number <=median:
                if previous !=0:
                    first = previous 
                    break
                else:
                    first = index
                    break
            if number !=0:
                previous = index
        #print "fst", first,previous
        if running_sum_sorted_number[first]>median:
            return first
        else:
            
            return (first+previous)/2.0
        
    else:
        median= running_total//2+1
        #print "me",median
        
        previous = 0 
        for index, number in enumerate(running_sum_sorted_number):
            if number !=0 and number ==median:
                return index
            if number !=0 and number <=median:
                if previous !=0:
                    return previous 
                else:
                    return index
            if number !=0:
                previous = index

    
def revious_running_sum(index):
    global running_sum_sorted_number
    lst =running_sum_sorted_number 
    if index ==len(lst)-1:
        return 0
    else:
        for i in xrange(index+1,len(running_sum_sorted_number)):
            #print i,lst[i]
            if lst[i]>0:
                return lst[i]
                break
        else:
            return 0
            
def radd(length_sentence):
    global running_sum_sorted_number
    
    try:
        if running_sum_sorted_number[length_sentence] ==0:
             running_sum_sorted_number[length_sentence] = revious_running_sum(length_sentence)+1
        else:
            running_sum_sorted_number[length_sentence] +=1
    
    except IndexError:
        running_sum_sorted_number = running_sum_sorted_number+[0 for i in range(len(running_sum_sorted_number),length_sentence+1)]
        if running_sum_sorted_number[length_sentence] ==0:
             running_sum_sorted_number[length_sentence] = revious_running_sum(length_sentence)+1
        else:
            running_sum_sorted_number[length_sentence] +=1
    
    running_sum = 0
    global running_total
    do_it = True
    
    for i in xrange(length_sentence-1,-1,-1):
    
        if running_sum_sorted_number[i] !=0:
            running_sum_sorted_number[i] += 1
        
            running_total = running_sum_sorted_number[i]
            do_it = False
            
    if do_it: 
        running_total = running_sum_sorted_number[length_sentence]
####



# finding txt filename
files=  glob.glob('wc_input/*.txt')

# reading data of txt files
running_sum_sorted_number = [0 for i in xrange(0,20)]
word_count = {}
running_median_list =[]
for file_name in files:
        
    with open(file_name) as f:
        data = f.read().strip().splitlines()
        for line in data:
            
            #spliting words
            line= re.findall(r"[\w']+", line)
            
            #counting words for every line
            for word in line:
                
                word = word.lower()
                
                if word not in word_count:
                    word_count[word] =1 
                else:
                    word_count[word] +=1
                    
            #cacluating running median of words per line
            
            
            #print line
            length = len(line)
            radd(length)
            a= find_median() 
            running_median_list.append(a)
            
directory = 'wc_output'
if not os.path.exists(directory):
    #making dir
    os.makedirs(directory)

#wrting  results in txt file
with open(directory+'/med_result.txt','w') as f:
    for item in running_median_list:
        f.write(str(float(item))+'\n')
                
            
            
            


directory = 'wc_output'
if not os.path.exists(directory):
    #making dir
    os.makedirs(directory)

#wrting  results in txt file
with open(directory+'/wc_result.txt','w') as f:
    for word, freq in  sorted(word_count.items()):
        f.write(str(word)+" "+str(freq)+'\n')
###        
#end = time.time()
#print end - begainning
