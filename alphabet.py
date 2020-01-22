print("Enter a letter from the alphabet: ");
letter = str(input());
vowels=["a","e","i","o","u","A","E","I","O","U"]

if (letter in vowels):
    print("Your letter is a vowel!")
elif ((letter=="y")or(letter=="Y")):
    print("The letter 'y' is sometimes a vowel and sometimes a consonant")
else:
    print("Your letter is a consonant")    