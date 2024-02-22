class Pairs():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __str__(self):
        return self.left + " " + self.right
    

PC_1 = "57 49 41 33 25 17 9 1 58 50 42 34 26 18 10 2 59 51 43 35 27 19 11 3 60 52 44 36 63 55 47 39 31 23 15 7 62 54 46 38 30 22 14 6 61 53 45 37 29 21 13 5 28 20 12 4".split(" ")
PC_2 = "14 17 11 24 1 5 3 28 15 6 21 10 23 19 12 4 26 8 16 7 27 20 13 2 41 52 31 37 47 55 30 40 51 45 33 48 44 49 39 56 34 53 46 42 50 36 29 32".split(" ")
lft_shifts = "1 1 2 2 2 2 2 2 1 2 2 2 2 2 2 1".split(" ")
def key_generation():
    original = "0100110001001111010101100100010101000011010100110100111001000100"
    # original = "0001001100110100010101110111100110011011101111001101111111110001"
    key = ""
    key_set = []

    for i in range(0, 56):
        key += original[int(PC_1[i])-1]
    setPair = [Pairs(key[:len(key)//2], key[len(key)//2:])]

    for i in range(0,16):
        shift_count = int(lft_shifts[i])
        left = setPair[-1].left
        right = setPair[-1].right
        setPair.append(Pairs(left[shift_count:] + left[:shift_count],right[shift_count:]+right[:shift_count]))

    setPair.pop(0)
    for pair in setPair:
        total = pair.left + pair.right
        temp_key = ""
        for j in range(0, 48):
            temp_key += total[int(PC_2[j])-1]
        key_set.append(temp_key)
    
    return key_set

IP_1 = "40 8 48 16 56 24 64 32 39 7 47 15 55 23 63 31 38 6 46 14 54 22 62 30 37 5 45 13 53 21 61 29 36 4 44 12 52 20 60 28 35 3 43 11 51 19 59 27 34 2 42 10 50 18 58 26 33 1 41 9 49 17 57 25".split(" ")
Ebit = "32 1 2 3 4 5 4 5 6 7 8 9 8 9 10 11 12 13 12 13 14 15 16 17 16 17 18 19 20 21 20 21 22 23 24 25 24 25 26 27 28 29 28 29 30 31 32 1".split(" ")
def xor(a, b):
    x = ""
    for i in range(len(a)):
        if a[i] == "1" or b[i] == "1":
            if a[i] == "1" and b[i] == "1":
                x += "0" 
            else:
                x += "1"
        else:
            x += "0"
    return x


P = "16 7 20 21 29 12 28 17 1 15 23 26 5 18 31 10 2 8 24 14 32 27 3 9 19 13 30 6 22 11 4 25".split(" ")
def stable_conversion(num):
    temp_table = []
    tables = []
    for line in open("Stables.txt", "r").readlines():
        if line.isspace():
            tables.append(temp_table)
            temp_table = []
        else:
            temp_table.append(line.strip().split(" "))
    tables.append(temp_table)

    output = ""
    for i in range(len(tables)):
        table = tables[i]
        current_bits = num[i*6:i*6+6]
        
        new_bits = str(bin(int(table[int(current_bits[0]+current_bits[-1],2)][int(current_bits[1:-1],2)])))[2:]
        if len(new_bits) < 4:
            new_bits = "0"*(4-len(new_bits)) + new_bits
        output += new_bits

    P_output = ""
    for i in range(len(P)):
        P_output += output[int(P[i])-1]

    return P_output


IP = "58 50 42 34 26 18 10 2 60 52 44 36 28 20 12 4 62 54 46 38 30 22 14 6 64 56 48 40 32 24 16 8 57 49 41 33 25 17 9 1 59 51 43 35 27 19 11 3 61 53 45 37 29 21 13 5 63 55 47 39 31 23 15 7".split(" ")
def cipher(keys):
    ciphertext = "1100101011101101101000100110010101011111101101110011100001110011"
    # ciphertext = "1000010111101000000100110101010000001111000010101011010000000101"
    R16L16 = ["0"]*len(ciphertext)
    for i in range(len(IP_1)):
        R16L16[int(IP_1[i])-1] = ciphertext[i]
    R16L16 = "".join(R16L16)

    left = R16L16[len(R16L16)//2:]
    right = R16L16[:len(R16L16)//2]

    for i in range(16):
        # Rn_1 = "11110000101010101111000010101010"
        Rn = right
        Rn_1 = left
        E_r = ""
        for i in range(len(Ebit)):
            E_r += Rn_1[int(Ebit[i])-1]

        key = keys.pop(-1) # change to -1 for backwards
        E_r = xor(key, E_r)
        E_r = stable_conversion(E_r)

        Ln_1 = xor(Rn, E_r)
        right = Rn_1
        left = Ln_1

    total = left + right
    msg = [0] * len(IP)
    for i in range(len(IP)):
        msg[int(IP[i])-1] = total[i]
    print(total)
    print("msg", "".join(msg))


if __name__ == "__main__":
    keys = key_generation()
    decipher = cipher(keys)

