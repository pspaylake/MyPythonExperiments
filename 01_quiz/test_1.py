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

    print(f"Your final score: {score}/2")

if __name__ == "__main__":
    quiz()
