frankenstien = "books/frankenstien.txt"
with open(frankenstien, "r") as f:
    file_contents = f.read()
    #print(file_contents)
    words = file_contents.split()
    word_length = len(words)


    def split_strings_to_chars(words: list[str]):
          list_of_chars = []
          for string in words:
            for chars in string:
                list_of_chars.append(chars.lower())
          
          return list_of_chars
                

    letter_dict = {}
    def count_letters():
       list_of_chars = split_strings_to_chars(words)
       for letter in list_of_chars:
              if letter in letter_dict:
                      letter_dict[letter] += 1
              else:
                      letter_dict[letter] = 1
       return letter_dict
                  
count_letters()
print(f"------- Begin report of {frankenstien} ----------------------")
print(f"{word_length} words wer found in the document.")
for key in letter_dict:
     print(f"the {key} character was found {letter_dict.get(key)} times.")
