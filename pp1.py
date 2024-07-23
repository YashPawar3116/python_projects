marks = []

n = int(input("Enter the number of students : "))

for i in range( 0 , n ):
 
    mks= int(input("Enter the Marks : "))
    
    marks.append(mks)
    
print(marks)

def avg():
	total = 0 
	for mks in marks:
		if mks >0 :
			total = total +mks 
	avg= total /len(marks)
	
	print ("Average of marks is ", avg)



def score():
	high = 0
	low = 100
	
	students = []
	
	for i in marks:
		if i != -1:
			students.append(i)
	
	for mks in students:
		if mks > high :
			high = mks
	for mks in students:
	 	if mks < low:
	 	  	low = mks 
	print("Highest is = ", high)
	print("Lowest is = ", low)
	


def attend():
	n = 0
	for mks in marks:
		if mks == -1:
			n+=1
 
	print ( "Number students absent are ",n)


def display_marks_with_highest_frequency():
	
	freq = 0
	for i in range (len(marks)):
	 count = 0
	 if (marks[i]!= -1):
			for j in range(len(marks)):
				if (marks[i] == marks[j]):
					count += 1
	if (freq < count):
			Marks = marks[i]
			freq = count 
			print ("\n Marks with highest frequency is %d(%d)" %(Marks,freq))
				

     			

def main():

 FDS_Marks=[]
 
 while True:
 	
 	print("\t\t1 : Accept FDS Marks")
 	print("\t\t2 : Average score of class")
 	print("\t\t3 : Highest and Lowest score of the class")
 	print("\t\t4 : Count of the students who were absent for the test")
 	print("\t\t5 : Display marks with highest frequency")
 	print("\t\t6 : Exit")

	ch = int(input("Enter your choice number = "))
	if (ch == 6):
		print("End of Program")
		break
	
	
	elif (ch == 1):
		print(n)
		print(marks)
		
	elif (ch == 2):
	 avg()
	 
	elif (ch == 3):
	 score()
	 
	elif (ch == 4):
	 attend()
	 
	elif (ch == 5):
	 display_marks_with_highest_frequency()
	 
	else:
		print("Wrong choice entered! Try Again!!!")
	 
main()
				
     			
     			
     			
     			
     			
     			
     			
























































