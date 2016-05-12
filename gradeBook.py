grades = [[100, 99, 98, 99, 100],
		  [95, 0, 85, 0, 70],
		  [90, 91, 95, 97, 99],
		  [75, 82, 87, 98, 64]]
		  
		  
def average_rows(grades):
	
	averages = []
	for row in grades:
		total = 0
		for item in row:
			total += item
		averages.append(total/len(row))
	return averages	
	
	
	
print("The student's averages are {}".format(average_rows(grades)))	

studentsGrades = average_rows(grades)

total = 0
for item in studentsGrades:
	total += item
	
classAverage = total/len(studentsGrades)	
	
print("The class average is {}".format(classAverage))
		  
		  