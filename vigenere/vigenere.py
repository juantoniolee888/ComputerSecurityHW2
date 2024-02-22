import string

def count_repetitions():
    input_string = ""
    repeated_string = {}

    for line in open("vigenere.input", "r").readlines():
        input_string = line.replace(" ","")
    for i in range(len(input_string), 1, -1):
        for start in range(0, len(input_string)-i+1):
            if input_string.count(input_string[start:start+i]) > 1:
                unique = True
                for keys, values in repeated_string.items():
                    if input_string[start:start+i] in keys:
                        unique = False
                        break
                if input_string[start:start+i] not in repeated_string and unique:
                    final_index = -1
                    for j in range(input_string.find(input_string[start:start+i])+1, len(input_string)-len(input_string[start:start+i])):
                        if input_string[start:start+i] == input_string[j:j+i]:
                            final_index = j
                    repeated_string[input_string[start:start+i]] = [input_string.find(input_string[start:start+i]), final_index]

    for keys, values in repeated_string.items():
        print(keys, values, values[1]-values[0])

def develop_alphabet():
    input_string = ""
    alphabet = {}

    for line in open("vigenere.input", "r").readlines():
        input_string = line.replace(" ","")

    for i in range(0,len(input_string), 5):
        end = 5 if len(input_string) - i > 0 else len(input_string) - i
        for j in range(0,end):
            if j not in alphabet:
                alphabet[j] = input_string[i+j]
            else:
                alphabet[j] += input_string[i+j]
    
    for key, value in alphabet.items():
        letter = dict.fromkeys(string.ascii_uppercase, 0)
        for char in value:
            letter[char] += 1
        print(letter)
        # print(key, value)


if __name__ == "__main__":
    count_repetitions()
    develop_alphabet()