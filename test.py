def student_helper(student) -> dict :
    return {
        "id": str(student["id"]),
        "fullname" : student["fullname"],
        "email" : student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],    
        "gpa" : student["gpa"],
         }

student = {
    "id" : 1814722,
    "fullname":"Ngo phu ty",
    "email" : "ngophuty@hcmut.edu.vn",
    "course_of_study" : "hello word",
    "year" : 3,
    "gpa"  : 3.5,
}

a= student_helper(student)
print(a)
# print(student["fullname"])