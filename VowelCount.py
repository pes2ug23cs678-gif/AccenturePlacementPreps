#Entering the vowels in a string
def giveMeVowels(String):
    Str = "aeiouAEIOU"
    count = 0
    for i in String:
        if i in Str:
            count += 1
    return count
def main():
    String = input()
    VowelCount = giveMeVowels(String) #This is for the output part to be seen over here!!!
    print(VowelCount)
if __name__ == "__main__":
    main()
