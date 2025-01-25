def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = words(text)
    ccount = count_characters(text)
    ccount2 = char_dict2(ccount)
    ccount2.sort(reverse=True, key=sort_on)
    book_report(num_words, ccount2, book_path)

    


    
    
    
        

def words(text):
    wordcount = len(text.split())
    return wordcount

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    l_text = text.lower()
    char_count = {}
    for char in l_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def char_dict2(char_count):
    list_of_chars = []
    for key, value in char_count.items():
        if key.isalpha():
            list_of_chars.append({"char": key, "num": value})
    return list_of_chars

def sort_on(ccount2):
    return ccount2["num"]
    
def book_report(num_words, ccount2, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words foun in the document\n")

    for char_dict in ccount2:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print(f"--- End report ---")

  
    

main()

