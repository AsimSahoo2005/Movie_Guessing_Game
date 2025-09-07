import random
movies = ['anand','sholay','drishyam','lagaan','3 idiots','singham','queen','pk','chhichhore','andhadhun']
def create_question(pick):
    n=len(pick)
    letters=list(pick)
    temp = []
    for i in range(n):
        if letters[i] == ' ':
            temp.append(' ')
        else:
            temp.append('_')
    qn=''.join(str(x) for x in temp)
    return qn
def is_present(letter, pick):
    c=pick.count(letter)
    if c==0:
        return False
    else:
        return True
def unlock(qn, pick, letter):
    ref = list(pick)
    qn_list = list(qn)
    temp = []
    n=len(pick)
    for i in range(n):
        if ref[i] == letter or ref[i] == ' ':
            temp.append(ref[i])
        else:
            if qn_list[i] == '_':
                temp.append('_')
            else:
                temp.append(qn_list[i])
    qn_new = ''.join(str(x) for x in temp)
    return qn_new
def play():
    print("Welcome to the Movie Guessing Game!")
    p1name = input("Enter Player 1's name: ")
    p2name = input("Enter Player 2's name: ")
    print(f"{p1name} and {p2name}, get ready to guess the movie!")
    pp1=0
    pp2=0
    turn = 0
    willing= True
    while willing:
        if turn % 2 == 0:
            print(f"{p1name}'s turn:")
            pick = random.choice(movies)
            qn=create_question(pick)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input("Your letter: ")
                if(is_present(letter, pick)):
                    modified_qn= unlock(modified_qn, pick,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to guess the movie  or 2 to unlock another letter:- "))
                    if d==1:
                        ans=input("Your answer:- ")
                        if ans == pick:
                            pp1=pp1+1
                            print("Correct")
                            not_said = False
                            print(p1name,"Your score:- ",pp1)
                        else:
                            print("Wrong answer, try again!")
                else:
                    print(letter,'not in the movie name')
            c=int(input("Press 1 to continue or 0 to quit:-"))
            if c == 0:
                print(p1name, "your score is", pp1)
                print(p2name, "your score is", pp2)
                print("Thanks for playing!")
                willing = False
            turn += 1
        else:
            print(f"{p2name}'s turn:")
            pick = random.choice(movies)
            qn=create_question(pick)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input("Your letter: ")
                if(is_present(letter, pick)):
                    modified_qn= unlock(modified_qn, pick,letter)
                    print(modified_qn)
                    d=int(input("Press 1 to guess the movie  or 2 to unlock another letter:- "))
                    if d==1:
                        ans=input("Your answer:- ")
                        if ans == pick:
                            pp2=pp2+1
                            print("Correct")
                            not_said = False
                            print(p2name,"Your score:- ",pp2)
                        else:
                            print("Wrong answer, try again!")
                else:
                    print(letter,'not in the movie name')
            c=int(input("Press 1 to continue or 0 to quit:- "))
            if c == 0:
                print(p1name, "your score is", pp1)
                print(p2name, "your score is", pp2)
                print("Thanks for playing!")
                willing = False
            turn += 1
play()