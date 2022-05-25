import random

user = input("Enter your Pop Email").capitalize()
if ("@pop.ac.uk" or "@POP.AC.UK") in user:
    print("This account is correct")

else:
    exit()

name = user[:user.index("@")]
domain = user.split("@")[0]

if random.random() <= 9:
    operator = ["Jordan", "Bob", "Luke", "James", "Jane", "Sarah", "Jack", "Alice", "Owen"]
    op_response = random.choice(operator)
    print("Hello!", name, "I am", op_response, "it's be my pleasure to help you today!")
    reply = input("Please input your question here!")

    if "Library" in reply:
        print("The Library is closed today")

    elif "Wifi" in reply:
        print("Wifi is excellent across campus") or random.random()

    elif "Deadline" in reply:
        print("Your deadline has been extended by two working days") or random.random()

    elif "Courses" in reply:
        print("You have many choices to pick from!") or random.random()

    elif "Timetable" in reply:
        print("You timetable will be given out soon enough!") or random.random()

    elif "Research" in reply:
        print("The university has many research projects ongoing!") or random.random()

    bk = ["Hmm", "Oh, I see", "Tell me more", "Interesting", "That's fascinating!"]
    bk_response = random.choice(bk)

    if len(reply) == 0:
        print(bk_response)

    if reply == "bye" or "exit" or "Bye" or "Exit":
        exit(print("Have a good day!"))
else:
    exit(print("Network Disconnect"))
