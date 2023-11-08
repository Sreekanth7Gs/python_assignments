def lvl_hrd():
    score = 30
    return score

def lvl_mdm():
    score = 20 
    return score

def lvl_easy():
    score = 10 
    return score

count_easy = 0
count_mdm = 0
count_hrd = 0

score_hrd = 0
score_mdm = 0
score_easy = 0

print("Welcome to Quiz")
Q1 = "Q1. The World Largest desert is ?"
choice = "A.Thar B.Kalahari C.Sahara D.Sonoran"
print(Q1)
print(choice)
print("Enter your choice")
user_choice = input().upper()
if user_choice == 'C':
    print("Your Correct..")
    count_easy += 1
    score_easy += lvl_easy()
else:
    print("Your Wrong")

Q2 = "Q2.Which one of the following river flows between Vindhyan and Satpura ranges?"
choice = "A. Narmada B.Mahanadi C.Son D.Netravati"
print(Q2)
print(choice)
print("Enter your choice")
user_choice = input().upper()
if user_choice == 'A':
    print("Your Correct..")
    count_easy += 1
    score_easy += lvl_easy()
else:
    print("Your Wrong")

Q3 = "Q3.The Central Rice Research Station is situated in?"
choice = "A. Chennai B.Cuttack C.Mumbai D.Delhi"
print(Q3)
print(choice)
print("Enter your choice")
user_choice = input().upper()
if user_choice == 'B':
    print("Your Correct..")
    count_easy += 1
    score_easy += lvl_easy()
else:
    print("Your Wrong")

Q4 = "Q4.Who among the following wrote Sanskrit grammar?"
choice = "A.Kalidasa B.Charak C. Panini D.Aryabhatt"
print(Q4)
print(choice)
print("Enter your choice")
user_choice = input().upper()
if user_choice == 'C':
    print("Your Correct..")
    count_mdm += 1
    score_mdm += lvl_mdm()
else:
    print("Your Wrong")

Q5 = "Q5.Which among the following headstreams meets the Ganges in last?"
choice = "A. Alaknanda B.Pindar C.Mandakini D.Bhagirathi"
print(Q5)
print(choice)
print("Enter your choice")
user_choice = input().upper()
if user_choice == 'D':
    print("Your Correct..")
    count_mdm += 1
    score_mdm += lvl_mdm()
else:
    print("Your Wrong")

Q6 = "Q6.Patanjali is well known for the compilation of _"
choice = "A. Yoga Sutra B.Panchatantra C.Brahma Sutra D.Ayurveda"
print(Q6)
print(choice)
print("Enter your choice")
user_choice = input().upper()
if user_choice == 'A':
    print("Your Correct..")
    count_mdm += 1
    score_mdm += lvl_mdm()
else:
    print("Your Wrong")

Q7 = "River Luni originates near Pushkar and drains into which one of the following?"
choice = "A.Rann of Kachchh B.Arabian Sea C.Gulf of Cambay D.Lake Sambhar"
print(Q7)
print(choice)
print("Enter your choice")
user_choice = input().upper()
if user_choice == 'A':
    print("Your Correct..")
    count_hrd += 1
    score_hrd += lvl_hrd()
else:
    print("Your Wrong")

Q8 = "Q8.Which one of the following rivers originates in Brahmagiri range of Western Ghats?"
choice = "A.Pennar B.Cauvery C.Krishna D.Tapti"
print(Q8)
print(choice)
print("Enter your choice")
user_choice = input().upper()
if user_choice == 'B':
    print("Your Correct..")
    count_hrd += 1
    score_hrd += lvl_hrd()
else:
    print("Your Wrong")

Q9 = "Q9.The country that has the highest in Barley Production?"
choice = " A.China B.India C.Russia D.France"
print(Q9)
print(choice)
print("Enter your choice")
user_choice = input().upper()
if user_choice == 'C':
    print("Your Correct..")
    count_hrd += 1
    score_hrd += lvl_hrd()
else:
    print("Your Wrong")

total_score = score_easy + score_mdm + score_hrd
total_correct = count_easy + count_mdm + count_hrd

print(f"In hard, you answered {count_hrd} out of 3 are correct")
print(f"You scored {score_hrd} points in hard questions")
print("\n")
print(f"In medium, you answered {count_mdm} out of 3 are correct")
print(f"You scored {score_mdm} points in medium questions")
print("\n")
print(f"In easy, you answered {count_easy} out of 3 are correct")
print(f"You scored {score_easy} points in easy questions")
print("\n")
print(f"Total Score is {total_score} out of 180")
print(f"Total correct answers : {total_correct}")
