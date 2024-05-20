class Student:
    def __init__(obj, name, major, portfolio_score, project_score, exam_score):
        obj.name = name
        obj.major = major
        obj.portfolio_score = portfolio_score
        obj.project_score = project_score
        obj.exam_score = exam_score
    
    def print_details(obj):
        print(f"Name: {obj.name}, Major: {obj.major}, Portfolio Score: {obj.portfolio_score}, "
              f"Project Score: {obj.project_score}, Exam Score: {obj.exam_score}")

# Example of using the class
student1 = Student("Qi Hengxing", "BMI", 95, 90, 88)  #Input position
student1.print_details()