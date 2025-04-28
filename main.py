from stats import wordcount, charcount, sortedstats
import sys

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    text = get_book_text(path)
    wc = wordcount(text)
    cc = charcount(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    sc = sortedstats(cc)
    for i in sc:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
    
main()
