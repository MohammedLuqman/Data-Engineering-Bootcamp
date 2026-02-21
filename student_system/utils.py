import csv
from models import Student

def grade_validate(grade_input):
    #the helper function checks here wether the grade is more than 0 and less than 100
    try:
        grade = float(grade_input)
        if 0 <= grade <= 100:
            return grade
        return None
    
    except ValueError: 
        return None
    
def Save_to_csv(Classroom, filename="Students_data.csv"):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Student_ID', 'Grades'])
            
            for i in Classroom.Student_list:
                # here we join the marks using | like 90|85 and so on
                grades_str = "|".join(map(str, i.grades))
                writer.writerow([i.name, i._student_id, grades_str])
                
        print(f"Successfully Saved to {filename}")
    
    except Exception as e:
        print(f"Save error: {e}")
        
def load_from_csv(classroom, filename="Students_data.csv"):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                g_str = row.get('Grades', '')
                grades_list = [float(g) for g in g_str.split("|")] if g_str else []
                new_s = Student(row['Name'], row['Student_ID'], grades_list)
                classroom.add_student(new_s)                
                
    except FileNotFoundError:
        print("No previous data found. Starting fresh.")
        