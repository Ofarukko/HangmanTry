import random
from collections import Counter


someWords = ''' elma muz mango cilek portakal uzum ananas seftali kayisi limon
kokonat kavun karpuz visne kiraz erik hurma '''
someWords = someWords.split(' ')
word = random.choice(someWords)
print('Bir harf Giriniz! İpucu: Bu bir meyve')
letterGuessed = ''
chances = len(word) + 3
correct = 0
flag = 0
try:
    while (chances != 0) and flag == 0:
        chances -= 1
        try:
            guess = str(input('\nBir Harf Giriniz: '))
        except:
            print('Harf Giriniz!')
            continue
        if not guess.isalpha():
            print('Harf Giriniz')
            continue
        elif len(guess) > 1:
            print('Sadece bir harf giriniz lütfen')
            continue
        elif guess in letterGuessed:
            print('Daha önceden girilmiş bir harf')
            continue
        if guess in word:
            k = word.count(guess)
            for _ in range(k):
                letterGuessed += guess
        for char in word:
            if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                print(char, end=' ')
            elif (Counter(letterGuessed) == Counter(word)):
                print("Harf:", word, end=' ')
                flag = 1
                print('\nTebrikler, Kazandınız !')
                break
            else:
                print('_', end=' ')

    if chances == 0 and (Counter(letterGuessed) != Counter(word)):
        print()
        print('Kaybettiniz! Tekrar Deneyiniz..')
        print('Kelimemiz {}'.format(word))
except KeyboardInterrupt:
    print()
    print('Bay! Tekrar Bekleriz.')
    exit()

