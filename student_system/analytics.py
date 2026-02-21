def top_student(Classroom):
    if not Classroom.Student_list:
        return None
    #lamda takes multiple expresstion and then returns back with the highest student and so on for the other functions
    return max(Classroom.Student_list, key=lambda i: i.calculate_avg())    

def lowest_student(ClassRoom):
    if not ClassRoom.Student_list:
        return None
    return min(ClassRoom.Student_list, key=lambda i: i.calculate_avg()) 
  
def ranking_student(Classroom):
    return sorted(Classroom.Student_list, key=lambda i: i.calculate_avg(), reverse=True)

def grade_distribution(Classroom):
    grade= {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    
    for i in Classroom.Student_list:
        letter = i.grade_category()
        grade[letter] = grade[letter] + 1
        
    return grade   