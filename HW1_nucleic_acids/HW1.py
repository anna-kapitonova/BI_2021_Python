true_alphabet = set("ATGCatgcUu")
not_compatible = [{"T", "U"}, {"T", "u"}, {"t", "u"}, {"t", "U"}]
transcribing_dictionary = {"A": "U", "a": "u", "T": "A", "t": "a", "G": "C", "g": "c", "C": "G", "c": "g"}
complement_dictionary_RNA = {"A": "U", "a": "u", "U": "A", "u": "a", "G": "C", "g": "c", "C": "G", "c": "g"}
complement_dictionary_DNA = {"A": "T", "a": "t", "T": "A", "t": "a", "G": "C", "g": "c", "C": "G", "c": "g"}
while True:
    print("Enter command")
    command = input()
    if command == "exit":
        print("Good luck!")
        break
    elif command not in {"transcribe", "reverse", "complement", "reverse complement"}:
        print("The command doesn't exist. Try again!")
        continue
    else:
        while True:
            print("Enter sequence")
            nucleic_acid = input()
            n = 0
            for i in nucleic_acid:
                if i not in true_alphabet:
                    n += 1
            for letter1, letter2 in not_compatible:
                if letter1 in nucleic_acid and letter2 in nucleic_acid:
                    n += 1
            if n > 0:
                print("Only RNA or DNA can be processed. Try again!")
                continue
            else:
                if command == "transcribe":
                    if "U" not in nucleic_acid and "u" not in nucleic_acid:
                        answer = []
                        for i in nucleic_acid:
                            answer.append(transcribing_dictionary[i])
                        print("".join(answer))
                        break
                    else:
                        print("Error: RNA cannot be transcribed")
                        continue
                elif command == "reverse":
                    print(nucleic_acid[::-1])
                    break
                elif command == "complement":
                    if "U" not in nucleic_acid and "u" not in nucleic_acid:
                        answer = []
                        for i in nucleic_acid:
                            answer.append(complement_dictionary_DNA[i])
                        print("".join(answer))
                        break
                    else:
                        answer = []
                        for i in nucleic_acid:
                            answer.append(complement_dictionary_RNA[i])
                        print("".join(answer))
                        break
                elif command == "reverse complement":
                    if "U" not in nucleic_acid and "u" not in nucleic_acid:
                        answer = []
                        for i in nucleic_acid[::-1]:
                            answer.append(complement_dictionary_DNA[i])
                        print("".join(answer))
                        break
                    else:
                        answer = []
                        for i in nucleic_acid[::-1]:
                            answer.append(complement_dictionary_RNA[i])
                        print("".join(answer))
                        break
