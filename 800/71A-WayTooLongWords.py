import cProfile

def main():
    NumberOfWords = int(input())
    for i in range(NumberOfWords):
        words = input()
        if len(words) > 10:
            print(words[0] + str(len(words[1:len(words)-1])) + words[len(words)-1])
        else:
            print(words)

cProfile.run('main()')