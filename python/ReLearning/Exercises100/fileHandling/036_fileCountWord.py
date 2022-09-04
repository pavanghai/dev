#Create a function that takes a text file and returns the number of words
def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)

file = r"python\learning\Exercises100\fileHandling\words1.txt"
print(count_words(file))
