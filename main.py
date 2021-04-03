# Name: Conner Foster
# Date: Feb 6, 2021
# ASGN: Activity Selection HW 4 (CS325 section 2)
#DESC: This program takes a list of activities with their start and end time and organizes them into a schedule with non conflicting times. This means no every activity will get done but the most possible will.


#function to fin the best fit schedule from the list of activities and their times
def sortSchedule(schedule, pos):
  finalSchedule = []    #create an array to store the selected activities for the final schedule
  finalSchedule.append(schedule[pos][0])    #save the last activity as the first activity in the list
  
  pos -= 1    #decrement the position of the schedule to analyze the previous activity int he list
  i = 0   #variable to store the position of the final schedule list
  
  while pos != 0:   #while the entire list hasnt been analyzed
    if schedule[pos][2] <= schedule[finalSchedule[i]-1][1]:   #if the end time of the current activity is less than or equal to the start time of the activity saved in the schedule.
      finalSchedule.append(schedule[pos][0])    #save that activity as there is no time conflict
      pos -= 1    #decrement the position of the activity list
      i += 1    #increment the position of the final results list
    
    elif schedule[pos][1] >= schedule[pos+1][2]:   #else if the start time of the current activity is later than the end time of the pervious activity checked
      finalSchedule.append(schedule[pos][0])  #save that activity as there is no time conflict
      pos -= 1    #decrement the position of the activity list
      i += 1    #increment the position of the final results list
    
    else:   #else if there is a time conflict
      pos -= 1    #decrement to the next position of the activity to check analyze next

  length = len(finalSchedule)   #find the number of activities saved
  finalSchedule.reverse()   #puts the activities in order for a cleaner print 
  print("Number of activities selected = " + str(length) + "\nActivities: ", end = "")    ##print all final results
  print(*finalSchedule, sep = ' ' ,end="\n\n")


#function to parse file array and create the seperate schedules
def makeSchedule(numbers):
  setNum = 1    #variable that stores the current set number for printing purposes. It starts at 1 so the print starts with "Set 1"
  for i in numbers:   #for loop to parse through file input array
    if len(i) == 1:   #if the current position of the file input array is indicating a new list by only having 1 number within that position
      n = i[0]    #variable to store the current amount of activities
      schedule = [0]*n    #create a list the size of the number of activties
      pos = 0   #variable to store the position of the schedule list when itterating through it
    
    else:   #else if an activity is in the current position of the for loop parse, copy the information untill the end of the set of activities
      schedule[pos] = i   #copy the current activity into the schedule array
      pos += 1    #increment the position of the schedule array for next save in loop
      if pos == n:    #if the end of the activity set is reached
        print("Set " + str(setNum))   #print the current set number
        setNum += 1   #increment the current set number for next loop itteration
        sortSchedule(schedule, pos-1)   #call sort function to find the best fit schedule


#function to parse file and read it as input in the numbers list
def readFile(numbers):
  with open('act.txt') as fp:   #Open the file act.txt
    for line in fp:   #Iterate through each line of the file
      numbers.append([int(j) for j in line.split()])    #Append the line of numbers as a list to the result array to convert it into a "2D" array


# Driver Code
if __name__ == '__main__':
  numbers = [] #create a list to store the file input
  readFile(numbers) #call funtion to read file and fill
  makeSchedule(numbers) #call function to parse through file array and create the seperate schedules within