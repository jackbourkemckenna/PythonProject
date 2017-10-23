
...
import csv

user = [] #my users array
dates = [] #my dates aaray
height =[] #my heigh array
width = [] #my width array 
usrDates =[] #my array for users id and date sign up 
setHeight = "960"
setWidth = "640"
countsWH = 0 #counter for width and heigh 
totalspent = 0 #total spent

try:
	with open('sample_data.csv', 'rt') as csvfile: #opening 
	     readerCSV = csv.reader(csvfile, delimiter=',')
	     next(readerCSV, None)

	     for row in readerCSV:
	     	  
	          user = row[0] #passing in data in to my arrays
	          dates = row[1]
	          spent = row[2]
	          height = row[4]
	          width = row[5]
	          
	          
	          usrDates.append(f"{row[0]} {row[1]}") #using this for finding the first user who sign up
	         
	          totalUser = (len(user)) #total users 
	          totalspent +=int(spent) #total spent of the users 
	          if height and width == setWidth and setHeight: #checkig the width and heigh 
	          	countsWH += 1
	          firstSignUp = (min(dates)) #sorting the array 
	          dateIndex =  (dates.index((firstSignUp))) #gets the index of that date an
	     
	          

	      
	firstUserJoined = dateIndex-1 #taking 1 away from this because it jumps forword by 1 
except Exception: 
	print("Problem with reading the csv file")
	sys.exit(1)

print ("The total of users is:",totalUser,"\n")
print("The amount of users using",setWidth,"x",setHeight,"is:",countsWH,"\n")
print ("The total spent of all users is:", totalspent,"dolars","\n")
print ("The first date and user id who joined",usrDates[firstUserJoined],"\n")


         




			
			

