question=[["which is the city of India is called as the nanocity","Bengaluru","chennai","dehli","patna", 1],
["which is the city of India is called as the nanocity","Bengaluru","chennai","dehli","patna", 1 ],
["which is the city of India is called as the nanocity","Bengaluru","chennai","dehli","patna", 1 ],
["which is the city of India is called as the nanocity","Bengaluru","chennai","dehli","patna", 1 ],
["which is the city of India is called as the nanocity","Bengaluru","chennai","dehli","patna", 1 ],
["which is the city of India is called as the nanocity","Bengaluru","chennai","dehli","patna", 1 ],
["which is the city of India is called as the nanocity","Bengaluru","chennai","dehli","patna", 1 ]]

levels= [1000,2000,3000, 4000, 5000, 10000 ,200000 ,30000, 40000,50000,1000000,5000000,10000000]
money=0
i=0
for i in range(0,len(question)):
    questions = question[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"{questions[0]}")
    print(f"a.{questions[1]}  b.{questions[2]}")
    print(f"c.{questions[3]}  d.{questions[4]}")
    reply=int(input("enter your answer(1-4): "))

    if(reply==questions[-1]):
        print(f"correct answer! you won RS.{levels[i]}\n\n")
    else:
        print("wrong answer!\n\n")
        break

    
    # print(f"well played,better luck next time {level[i]}\n\n")

