def quiz():
    score = 0
    print("MY TEST")

    # Question 1
    print("Q1: Print the items in the text file?")
    print("(A) cat file.txt")
    print("(B) ls")
    print("(C) echo")
    print("(D) test")
    ans1 = input("Your answer: ").upper()
    if ans1 == "A" or ans1.lower() == "cat file.txt":
        print("CORRECT")
        score += 1
    else:
        print("Wrong. The answer is cat file.txt.")

    # Question 2
    print("Q2: What does this ^$ mean?")
    print("(A) cat file.txt")
    print("(B) matches empty lines")
    print("(C) echo")
    print("(D) test")
    ans2 = input("Your answer: ").upper()
    if ans2 == "B" or ans2.lower() == "matches empty lines":
        print("CORRECT")
        score += 1
    else:
        print("Wrong. The answer is (matches empty lines).")

    # Question 3
    print("Q3: What does this d mean?")
    print("(A) cat file.txt")
    print("(B) matches empty lines")
    print("(C) echo")
    print("(D) deletes them")
    ans3= input("Your answer: ").upper()
    if ans3== "D" or ans3.lower() == "matches empty lines":
        print("CORRECT")
        score += 1
    else:
        print("Wrong. The answer is (deletes them).")

    # Question 4
    print("Q4: What does this > file2 mean?")
    print("(A) output redirected to file2")
    print("(B) matches empty lines")
    print("(C) echo")
    print("(D) deletes them")
    ans4 = input("Your answer: ").upper()
    if ans4 == "A" or ans4.lower() == "output redirected to file2":
        print("CORRECT")
        score += 1
    else:
        print("Wrong. The answer is (output redirected to file2).")

    # Question 5
    print("Q5: What does editor primarily do?")
    print("(A) output redirected to file2")
    print("(B) matches empty lines")
    print("(C) stream and automate modify text and files")
    print("(D) deletes them")
    ans5 = input("Your answer: ").upper()
    if ans5 == "C" or ans5.lower() == "stream and automate modify text and files":
        print("CORRECT")
        score += 1
    else:
        print("Wrong. The answer is (stream and automate modify text and files).")

        # Question 6
        # when sythanx is being used
        print(r"Q6: What does \([0-9]\+\) mean?")
        print("(A) matches one or more digits")
        print("(B) matches empty lines")
        print("(C) stream and automate modify text and files")
        print("(D) deletes them")
        ans6 = input("Your answer: ").upper()
        if ans6 == "A" or ans6.lower() == "matches one or more digits":
            print("CORRECT")
            score += 1
        else:
            print("Wrong. The answer is (matches one or more digits).")

        # Question 7
        print(r"Q7: What does \$ mean?")
        print("(A) matches one or more digits")
        print("(B) matches empty lines")
        print("(C) stream and automate modify text and files")
        print("(D) match the literal dollar sign")
        ans7 = input("Your answer: ").upper()
        if ans7 == "D" or ans7.lower() == "match the literal dollar sign":
            print("CORRECT")
            score += 1
        else:
            print("Wrong. The answer is (match the literal dollar sign).")

        # Question 8
        print(r"Q8: What does \1 mean?")
        print("(A) matches one or more digits")
        print("(B) keeps one of the digits but removes $")
        print("(C) stream and automate modify text and files")
        print("(D) match the literal dollar sign")
        ans8 = input("Your answer: ").upper()
        if ans8 == "B" or ans8.lower() == "keeps one of the digits but removes $":
            print("CORRECT")
            score += 1
        else:
            print("Wrong. The answer is (keeps one of the digits but removes $).")

        # Question 9
        print(r"Q9: What does \1 mean?")
        print("(A) matches one or more digits")
        print("(B) keeps one of the digits but removes $")
        print("(C) stream and automate modify text and files")
        print("(D) match the literal dollar sign")
        ans8 = input("Your answer: ").upper()
        if ans8 == "B" or ans8.lower() == "keeps one of the digits but removes $":
            print("CORRECT")
            score += 1
        else:
            print("Wrong. The answer is (keeps one of the digits but removes $).")

            score=0
            print(f"Your final score: {score}/6")


if __name__ == "__main__":
    quiz()
