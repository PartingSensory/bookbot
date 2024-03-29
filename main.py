def main():

    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    #print(file_contents)  # this line will print your file content to the console
    words = file_contents.split()
    lowered_string = file_contents.lower()
    letter_counts = {}
    for letter in lowered_string:
        if letter.isalpha():
           
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    print(f"--- Begin report of books/frankenstien.txt ---")
    print(f"{len(words)} words found in the document")
    sorted_letters = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_letters:
        print(f"The '{char}' character was found {count} times")
    print(f"--- End report ---")
if __name__ == "__main__":
    main()

