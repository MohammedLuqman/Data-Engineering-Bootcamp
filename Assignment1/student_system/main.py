import models
import analytics
import utils


def main_menu():
    my_class = models.Classroom()
    utils.load_from_csv(my_class)
    
    while True:
        print("\n    Student Management System   ")
        print("1. Add Student      2. Remove Student")
        print("3. Search Student   4. View Class Average")
        print("5. Top/Low Student  6. View Rankings")
        print("7. Grade Stats      8. Save & Exit")
        
        choice = input("\nSelect an option: ")  
                  
        if choice == '1' :
            name = input("Enter Student Name: ")
            student_id = input("Enter Student ID: ")
            grades_input = input("Enter grades (comma separated): ")
            grades = [float(g.strip()) for g in grades_input.split(',') if g.strip()]
            my_class.add_student(models.Student(name, student_id, grades))
        
        elif choice == '2':
            student_id = input("Enter ID to remove: ")
            my_class.remove(student_id)
                
        elif choice == '3':
            pass
            student_id = input("Enter ID to search: ")
            s= my_class.search(student_id)
            if s: print(f"Found: {s.name}, Average: {s.calculate_avg()}")

        elif choice == '4':
            print(f"Class Average: {my_class.calculate_classroom_avg():.2f}")

        elif choice == '5':
            top = analytics.top_student(my_class)
            low = analytics.lowest_student(my_class)
            if top: print(f"Top: {top.name} | Lowest: {low.name}")

        elif choice == '6':
            print("\n Ranking ")
            ranked_students = analytics.ranking_student(my_class)
            rank = 1
            for i in ranked_students:
                avg = i.calculate_avg()
                print(f"{rank}. {i.name} ({avg:.2f})")
                rank = rank + 1
            
        elif choice == '7':
            print(f"Distribution: {analytics.grade_distribution(my_class)}")

        elif choice == '8':
            utils.Save_to_csv(my_class)
            print("Saved and Thank you for using our system")
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
     main_menu()