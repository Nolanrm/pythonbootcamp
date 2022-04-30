import art as art
import os

auction_live = True
bids = {}
person_name = ""
person_bid = 0
winning_bid = 0
winner = ""

print(art.logo)


#get bids
while auction_live:
    person_name = input("name of our bidder? ")
    person_bid = int(input("What is you bid? "))
    bids[person_name] = person_bid
    os.system('CLS')
    add_bid = input("do we have another bidder?(y/n)").lower()

    if add_bid == 'y':
        pass
    else:
        auction_live = False

#determine winner
for keys in bids:
    if bids[keys] > winning_bid:
        winning_bid = bids[keys]
        winner = keys
    elif bids[keys] == winning_bid:
        winner = "tie"
    else:
        pass

print(f"our winner is {winner} with a bid of ${winning_bid}.")





# ###############
# ##Nesting
# ###############

# def add_new_game(Video_Games,genre, highlyRecommend, doNotRecommend):
#     #TODO  add logic to check if genre already exists
#     Video_Games.append({"Genre":genre, "Highly Recommend":highlyRecommend, "Don't Recommend":doNotRecommend})

# def does_genre_exist(genre):
#     for item in Video_Games:
#         print(item)
#         for key in item.keys():
#             print(key)
#             if genre == item[key]:
#                 genre_exists = True
#                 print(item[key])
#                 print("it does exists")
#     return genre_exists

# Video_Games = [
#     {"Genre":"Rougelikes"
#     ,"Highly Recommend":["Hades","Enter The Gungeon"]
#     ,"Don't Recommend":["Darkest Dungeon"]
#     },
#     {"Genre":"FPS"
#     ,"Highly Recommend":["Apex Legends","Halo Infinite"]}
# ]

# genre = input("What Genre?")
# genre_exists = does_genre_exist(genre)

# print(f"it is {genre_exists} that the genre exists")

# highlyRecommend = []
# adding_game = True



# while adding_game:
#     add_game_check = input(f"do you have a game to add for the {genre} genre that you would highly recommend? (Y/N)").lower()

#     if add_game_check == 'y':
#         game = input("what game?")
#         highlyRecommend.append(game)
#     else:
#         adding_game = False

# add_new_game(Video_Games,genre,highlyRecommend,doNotRecommend=["fortnite"])




# #Video_Games.append({"Genre":"Metrodvania","Highly Recommend":["Hollow Knight","Dead Cells"]})

# print(Video_Games[2]["Genre"])


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