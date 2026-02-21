class Student:
  def __init__(self,name,_student_id,grades = None):
    self.name = name
    self._student_id = _student_id
    self.grades= grades if grades is not None else[]
    
  @classmethod
  def initial_value(cls):
        return cls("Student", "00", [0])
    
  def calculate_avg(self):
    try :
      return sum(self.grades)/ len(self.grades)
    except :
      return 0
    
  
  def grade_category(self):
    student_grade = self.calculate_avg()
    if student_grade >= 90 : return "A"
    elif student_grade >= 80 : return "B"
    elif student_grade >= 70 : return "C"
    elif student_grade >= 60 : return "D"
    else : return "F"
    
class Classroom:
  def __init__(self):
    self.Student_list =[]
  
  def add_student(self,new_student):
    for i in self.Student_list :
      if i._student_id == new_student._student_id : 
        print("The Student already exists")
        return
    self.Student_list.append(new_student)
    print(f"{new_student.name} Student added successfully")

  def remove(self,wanted_id):
    for i in self.Student_list :
      if i._student_id == wanted_id:
        self.Student_list.remove(i)
        print("Student Deleted Successfully")
        return
    print("Student not found")
    
  def search(self,searched_student):
    for i in self.Student_list :
      if i._student_id == searched_student :
        return i
    print("Student not found")
    return 
  
  def calculate_classroom_avg(self):
    if not self.Student_list :
      return 0
    total = 0
    for i in self.Student_list :
      total = total + i.calculate_avg()
      
    return total / len(self.Student_list)
       


