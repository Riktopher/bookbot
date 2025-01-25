def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = words(text)
    print(text)
    print(f"{num_words} words found in this document")
    
        

def words(text):
    wordcount = len(text.split())
    return wordcount

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

