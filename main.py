print("Welcome to Vr Demonstration")
print("Here you can book ticket for vr")
print("please write your name")
name = input("")
print(f"So hello {name} for starting with the ticket booking please type start")
startask = input("")
if startask == "start":
    print("""Please select any one video for following with length and price
    1.) Rhino Video = 1:00 (Rs. 20)
    2.) Virat Kohli Net Practice = 3:00 (Rs.60)
    3.) Solar System = 2:00 (Rs 40)""")
    print("Please input the video's SN for selecting video")
    vid_input = input("")
    if vid_input == "1":
        print("Your video's ticket has been booked. Now please pay the amount of Rs 20 for the video. Enjoy the video")
    elif vid_input == "2":
        print("Your ticket has been booked for Virat's Net session for Rs 60. Enjoy the video")
    elif vid_input == "3":
        print("Your ticket has been booked for Solar System tour for Rs 40. Enjoy the video")
elif startask != "start":
    print("For some reason our app couldnt start with the procedure")
print("Thank you for your valueable time")