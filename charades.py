import sys
import random

genres = ['movies', 'tv', 'characters', 'actions', 'all']

def all_files():
    all = []

    for file in genres:
        words = [line.strip() for line in open('genres/' + file + ".txt", 'r')]
        all += words

    return all

def read_in(g):
    if g == "all":
        return all_files()
    else:
        return [lines.strip() for lines in open("genres/" + g + ".txt", 'r')]

def main():
    g = input("Enter topic:")

    if g not in genres:
        print("Genre not found!")
    else:
        genre = read_in(g)
        used = []

        while len(used) < len(genre):
            rnum = random.randint(0, len(genre) - 1)

            if genre[rnum] not in used:
                used.append(genre[rnum])
                inp = input("_" * 45 + "[Press enter for next charade]" + "_" * 45)
                spaces = int((120 - len(genre[rnum])) // 2)
                print("\n" * 14 + " " * spaces + genre[rnum] + "\n" * 14)
        
        print("_" * 50, "[No more charades]", "_" * 50)

if __name__ =="__main__":
    main()