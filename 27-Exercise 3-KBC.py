#Create a PROGRAM capable of displaying questions to user like KBC
#Use list datatype to store the questions and their correct answers
#Display the final amount the person is taking home after playing the game


# List of questions
questions = [["What is the capital of India?"," Mumbai", " Delhi", " Kolkata", " Chennai",2],
    ["Who is known as the Father of the Nation?", "Jawaharlal Nehru", " Bhagat Singh", " Mahatma Gandhi", " Sardar Patel",3],
    ["Which planet is known as the Red Planet?","Venus", " Mars", " Jupiter", " Saturn",2],
    ["Which is the largest mammal?", "Elephant", "Giraffe", "Whale", "Rhino",3],
    ["Which Indian cricketer is known as 'The Wall'?","Virat Kohli", "MS Dhoni", "Rahul Dravid", "Sachin Tendulkar",3]]

# Prize money for each correct answer
money = [100000,750000, 2000000, 5000000, 10000000,0]
# Variable to store total amount
total_amount = 0

for i in range(len(questions)):
    q = questions[i]
    print("\n\nQuestion for ₹", money[i], ' is on your computer screen--> ')  
    print("\nQuestion-", (i + 1), ":", q[0])
    print("A.", q[1], "B.", q[2])
    print("C.", q[3], "D.", q[4])

    ans = int(input('Select an Option (1/2/3/4): '))

    if ans == q[5]:
        total_amount = money[i]  # ✅ Save the last correct amount
        print("Correct answer✅, congrats! you won ₹", money[i])
    else:
        print("Uhh!, Wrong Answer❌, The correct answer was option", q[5])
        print("🏆 You won ₹", total_amount, "! Thanks for playing!")  # ✅ Use saved amount
        break
else:
    print("🏆 You won ₹", total_amount, "! Thanks for playing!") 