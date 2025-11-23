print("Welcome to Kaun Banega Crorepati cricket edition!")
import random 
questions=[
[
    "Who is the most successful indian captain in test cricket?",
    "Rohit Sharma","MS Dhoni","Sachin Tendulkar","Virat Kohli",4
],
[
    "Who has the highest centuries from 2014 to 2019?",
    "Australia","Pakistan","Virat/Shikhar/Rohit","England",3
],
[
    "Against which team did sachin tendulkar scored his 49th ODI century?", 
    "England","Australia","Pakistan","Bangladesh",4
],
[
    "Who is considered as The Best Fielder in Cricket History?", 
    "Jhonty Rhodes","Ravindra Jadeja","Glenn Phyllips","AB Devilliers",1
],
[
    "Which bowler has taken the most number of wickets in test cricket?", 
    "Kapil Dev","Muthiah Muralidaran","Jimmy Anderson","Dale Steyn",2
],
[
    "Against which team did Virat Kohli scored his first test century?", 
    "Australia","Pakistan","Sri lanka","Bangladesh",3
],
[
    "Who has the fastest bowl record in cricket history?", 
    "Andy Roberts","Brett Lee","Glenn McGrath","Shoaib Akhtar",4
],
[
    "Who was known as The Whispering Death?", 
    "Joel Garner","Malcom Marshall","Michael Holding","Andy Roberts",3
],
[
    "Who has won the most awards by ICC?", 
    "Virat Kohli","Jacques Kallis","Ricky Ponting","Sachin Tendulkar",1
],
[
    "Who is considered as The Best Captain in Cricket History?", 
    "Michael Clarke","Ricky Ponting","Rohit Sharma","MS Dhoni",2
],
[
    "How many centuries does Adam Gilchrist have in international cricket?", 
    "33","40","36","31",1
],
[
    "Who has the most dismissals in international cricket?", 
    "Kumar Sangakara","Adam Gilchrist","Mark Boucher","MS Dhoni",3
],
[
    "Who is the fastest batsman to reach 27k runs in international cricket?", 
    "Virat Kohli","Ricky Ponting","Kumar Sangakara","Sachin Tendulkar",1
],
[
    "Who has the recorf for fastest running between the wickets in cricket history?", 
    "David Warner","AB Devilliers","Virat Kohli","MS Dhoni",4
],
[
    "Who has the most runs in T20 cricket?", 
    "Kieren Pollard","Babar Azam","Chris Gayle","Rohit Sharma",3
],
]

level=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

money=0

random.shuffle(questions)

for i in range(0,len(questions)):

    question=questions[i]
    
    print(f"\n\nThe Question for Rs.{level[i]}")
    print(question[0])

    print(f"a. {question[1]}    b. {question[2]}")
    print(f"c. {question[3]}    d. {question[4]}")

    reply=int(input("Enter your option (1-4) or enter 0 to stop playing: "))

    if reply == 0:
        if i == 0:
            money = 0
        else:
            money = level[i-1]
        print(f"Aapne jeete hai Rs.{money}. Khel samapt karte hai")
        break

    if reply == question[-1]:
        print("Sahi jawaab , Aap jeet te hai Rs.",level[i])

        if i == 4:
            money = 10000
            print(f"Mubarak ho , Aapne Rs.{money} surakshit kar liya hai")
            reply2 = input("Kya aap aage khelna chahte hai? (yes/no): ").lower()
            if reply2 == "no":
                print(f"Aap Rs.{level[i-1]} lekar jaa rahe hai.")
                break

        if i == 9:
            money = 320000
            print(f"Mubarak ho , Aapne Rs.{money} surakshit kar liya hai")
            reply3 = input("Kya aap aage khelna chahte hai? (yes/no): ").lower()
            if reply3 == "no":
                print(f"Aap Rs.{level[i-1]} lekar jaa rahe hai.")
                break

    else:
        print(f"Galat jawaab! Aapka khel yahi samapt hota hai. Aap jeet te hai Rs.{money}")
        break