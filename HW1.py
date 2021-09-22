wrong_alphabet = 'BbDdEeFfHhIiJjKkLlMmNnOoPpQqRrSsVvWwYyZz'
while True:
    print("Enter command")
    command = str(input())
    if command == "exit":
        print("Good luck!")
        break
    elif command!="transcribe" and command!="reverse" and command!="complement" and command!="reverse complement":
        print("The command doesn't exist. Try again!")
        continue
    else:
        permission = True
        while permission:
            print("Enter sequence")
            NA = str(input())
            n = 0
            for i in wrong_alphabet:
                if i in NA:
                    n += 1
            if n > 0:
                print("Invalid alphabet. Try again!")
                continue
            if ("U" in NA and "T" in NA) or ("u" in NA and "t" in NA) or ("U" in NA and "t" in NA) or ("u" in NA and "T" in NA):
                print("Only RNA or DNA can be processed. Try again!")
                continue
            else:
                if command == "transcribe":
                    if "U" not in NA and "u" not in NA:
                        for i in NA:
                            if i == "A":
                                print("U", end="")
                            elif i == "a":
                                print("u", end="")
                            elif i == "T":
                                print("A", end="")
                            elif i == "t":
                                print("a", end="")
                            elif i == "G":
                                print("C", end="")
                            elif i == "g":
                                print("c", end="")
                            elif i == "C":
                                print("G", end="")
                            elif i == "c":
                                print("g", end="")
                        print("", end="\n")
                    else:
                        print("Error: RNA cannot be transcribed")
                    break
                elif command == "reverse":
                    print(NA[::-1])
                    break
                elif command == "complement":
                    for i in NA:
                        if i == "A":
                            if "U" in NA or "u" in NA:
                                print("U", end="")
                            else:
                                print("T", end="")
                        elif i == "a":
                            if "U" in NA or "u" in NA:
                                print("u", end="")
                            else:
                                print("t", end="")
                        elif i == "T":
                            print("A", end="")
                        elif i == "t":
                            print("a", end="")
                        elif i == "G":
                            print("C", end="")
                        elif i == "g":
                            print("c", end="")
                        elif i == "C":
                            print("G", end="")
                        elif i == "c":
                            print("g", end="")
                    print("", end="\n")
                    break
                elif command == "reverse complement":
                    for i in NA[::-1]:
                        if i == "A":
                            if "U" in NA or "u" in NA:
                                print("U", end="")
                            else:
                                print("T", end="")
                        elif i == "a":
                            if "U" in NA or "u" in NA:
                                print("u", end="")
                            else:
                                print("t", end="")
                        elif i == "T":
                            print("A", end="")
                        elif i == "t":
                            print("a", end="")
                        elif i == "G":
                            print("C", end="")
                        elif i == "g":
                            print("c", end="")
                        elif i == "C":
                            print("G", end="")
                        elif i == "c":
                            print("g", end="")
                    print("", end="\n")
                    break