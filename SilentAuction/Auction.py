
###############
##Nesting
###############

Video_Games = [
    {"Genre":"Rougelikes"
    ,"Highly Recommend":["Hades","Enter The Gungeon"]
    ,"Don't Recommend":["Darkest Dungeon"]
    },
    {"Genre":"FPS"
    ,"Highly Recommend":["Apex Legends","Halo Infinite"]}
]

Video_Games.append({"Genre":"Metrodvania","Highly Recommend":["Hollow Knight","Dead Cells"]})

print(Video_Games[2]["Genre"])


###############
##Students
###############

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades = {}
    
# for key in student_scores:
#     grade = student_scores[key]
#     if grade >= 91:
#         student_grades[key] = "Outstanding"
#     elif grade >= 81:
#         student_grades[key] = "Exceeds Expectations"
#     elif grade >= 71:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
    
# print(student_grades)



###############
##First look at dictionaries
###############


# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected."
#     ,"Function": "A piece of code that you can easily call over and over again."
#     }

# #programming_dictionary["Bug"] = "test"

# print(programming_dictionary["Bug"])

# print("hello")