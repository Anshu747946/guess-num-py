import random as rd

# taking input as A and B
A = int(input('enter the start of range: '))
B = int(input('enter the end of the range: '))
# selecting number randomly using randint function
computer = rd.randint(A, B)
counter = 0
wrong = 0
while True:
    # checking if user guessed for 3 times then taking exit
    if wrong < 3:
        player = int(input("Guess the Number between range :"))
        if player == 00:
            print('Your Score is :', counter)
            print('You ended the game.')
            break
        elif player == computer:
            print('you guessed correct, You get a point collected in your wallet. ')
            counter += 1
            A = int(input('enter the start of range: '))
            B = int(input('enter the end of the range: '))

            computer = rd.randint(A, B)
            wrong *= 0
        else:
            wrong += 1
            if player > computer:
                print('Have one more try ,your guess was high.')

                continue
            else:
                print('Have one more try, Your guess was low.')
                continue
    else:

        print('You have attempted maximum of three times wrong.')
        print('Your Score till now is :', counter)
        break



'''import random as rd
question={"The controversial Babli project is a barrage being built by Maharashtra Government across which among the following rivers?\n[A] Bhima River\n[B] Krishna River\n[C] Godavari River\n[D] Painganga River":'c'or'C',
"“Chandipur-on-sea” is located in which among the following states?\n[A] Odisha\n[B] Andhra Pradesh\n[C] West Bengal\n[D] Tamilnadu":'a'or 'A',
"Coir Industry is maximum concentrated in which among the following states of India?\n[A] Karnataka\n[B] Tamil Nadu\n[C] Kerala\n[D] Andhra Pradesh":'c'or 'C'or 'Kerala'or 'kerala',
"Which among the following mountain peaks is not in Himalayan Range?\n[A] K2\n[B] Kanchenjunga\n[C] Nanga parbat\n[D] Cho Oyu":'a'or 'A',
"The Chutak Hydroelectric Plant is located in which state/UT?\n[A] Karnataka\n[B] Puducherry\n[C] Odisha\n[D] Jammu & Kashmir":'d'or 'D',
"India’s largest petrochemical complex is located at:\n[A] Gujarat\n[B] Maharastra\n[C] Rajasthan\n[D] Assam":'a'or 'A',
"India’s largest inland saline wetland system is located in which of the following states ?\n[A] Gujarat\n[B] Rajasthan\n[C] Orissa\n[D] Andhra Pradesh":'b'or"B",
"Which among the following is not correctly matched?\n[A] Sukhna Lake – Chandigarh\n[B] Wandoor Beach – Andaman & Nicobar\n[C] Bangaram Beach – Lakshadweep\n[D] Devka Beach – Goa":'d'or 'D',




}
round=0
score=0
while True:
    if round<5:
        key,val=rd.choice(list(question.items()))
        print(key)
        player=input('enter which one is correct: ')
        if player==val:
            print('Congratulation!,you have scored a point in your wallet.')
            key,val=rd.choice(list(question.items()))
            score+=1
            round+=1
        else:
            print('your answer was wrong, Try again ')
            key,val=rd.choice(list(question.items()))
            round+=1
    else:
        print('your score is,',score)
        break'''