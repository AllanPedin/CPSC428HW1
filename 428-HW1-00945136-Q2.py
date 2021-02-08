while True:
    print("Enter an ip or type quit to quit")
    userInput = input()
    if userInput == "quit":
        break
    else:
        ipIsGood = True
        ip = userInput.split(".")
        if len(ip) != 4:
            print("Needs exactly 3 periods")
            ipIsGood = False
        else:
            count = 1
            for i in ip:
                if int(i) < 0:
                    print("Octet " + str(count) + " is too small")
                    ipIsGood = False
                if int(i) > 255:
                    print("Octet " + str(count) + " is too large")
                    ipIsGood = False

                count+=1
        if ipIsGood :
            print("Ip " + userInput + " is all good")
print("Thanks for playing")