from tkinter import Tk, Entry, ttk, StringVar
import os

# list of your saved accounts
ACCOUNTS = [{"name": "Amazon",
             "e_mail": "john.smith@mymail.com",
             "password_id": "001",
             "version": "0",
             "character_list": "FULL",
             "extra": ""},
            {"name": "Bank",
             "e_mail": "john.smith@mymail.com",
             "password_id": "000",
             "version": "0",
             "character_list": "NUM",
             "extra": "User ID: 123456"}]

# possible character sets
CHAR = {"NUM": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "BASIC": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f",
                  "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                  "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
        "PAYPAL": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f",
                   "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                   "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                   "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "~", "!",
                   "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "?", ">", "<", ".",
                   ",", "/"],
        "FULL": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f",
                 "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                 "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                 "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "`", "~",
                 "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}",
                 "[", "]", "|", ":", ";", "'", "<", ">", ",", ".", "?", "/"]}


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # DO NOT MODIFY UNDER HERE !!!! # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# elements needed for AES 128-bit encryption/decryption
SUBBYTES = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
            [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
            [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
            [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
            [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
            [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
            [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
            [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
            [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
            [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
            [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
            [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
            [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
            [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
            [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
            [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]

INV_SUBBYTES = [[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
                [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
                [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
                [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
                [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
                [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
                [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
                [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
                [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
                [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
                [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
                [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
                [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
                [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
                [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
                [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]]

RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

MIXCOL = [[0x02, 0x03, 0x01, 0x01],
          [0x01, 0x02, 0x03, 0x01],
          [0x01, 0x01, 0x02, 0x03],
          [0x03, 0x01, 0x01, 0x02]]

INV_MIXCOL = [[0x0e, 0x0b, 0x0d, 0x09],
              [0x09, 0x0e, 0x0b, 0x0d],
              [0x0d, 0x09, 0x0e, 0x0b],
              [0x0b, 0x0d, 0x09, 0x0e]]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def account_combobox_selected(index):
    root.focus()
    selected_account = ACCOUNTS[index]
    email.set(selected_account.get("e_mail"))
    extra.set(selected_account.get("extra"))
    text_to_cript = "myPassword!!" + selected_account.get("version") + selected_account.get("password_id")
    add_to_clipboard(get_password(text_to_cript, Key_Entry.get(), CHAR.get(selected_account.get("character_list"))))


def get_password(pass_text, key_text, char_list):
    # ensuring that key_text is at least 16 characters long
    while len(key_text) < 16:
        key_text += "0"

    pass_state = text_to_state(pass_text)
    key_state = text_to_state(key_text)
    return state_to_text(crypt(pass_state, key_state), char_list)


def add_to_clipboard(text_to_add):
    with open("temp.txt", "w") as file:
        file.write(text_to_add.strip())
    os.system("clip < temp.txt")
    os.remove("temp.txt")


def subbyte(n):
    j = n & 0x0F
    i = n >> 4
    return SUBBYTES[i][j]


def inv_subbyte(n):
    j = n & 0x0F
    i = n >> 4
    return INV_SUBBYTES[i][j]


def state_subbyte(state_in):
    output_state = state_in.copy()
    for i in range(4):
        for j in range(4):
            output_state[i][j] = subbyte(output_state[i][j])
    return output_state


def back_state_subbyte(state_in):
    output_state = state_in.copy()
    for i in range(4):
        for j in range(4):
            output_state[i][j] = inv_subbyte(output_state[i][j])
    return output_state


def gf_mult(a, b):
    p = 0
    while a != 0 and b != 0:
        if b & 1:
            p ^= a
        if a & 0x80:
            a = (a << 1) ^ 0x11b
        else:
            a <<= 1
        b >>= 1
    return p


def shift_rows(state_in):
    value_saved1 = state_in[1][0]
    state_in[1][0] = state_in[1][1]
    state_in[1][1] = state_in[1][2]
    state_in[1][2] = state_in[1][3]
    state_in[1][3] = value_saved1

    value_saved1 = state_in[2][0]
    value_saved2 = state_in[2][1]
    state_in[2][0] = state_in[2][2]
    state_in[2][1] = state_in[2][3]
    state_in[2][2] = value_saved1
    state_in[2][3] = value_saved2

    value_saved1 = state_in[3][3]
    state_in[3][3] = state_in[3][2]
    state_in[3][2] = state_in[3][1]
    state_in[3][1] = state_in[3][0]
    state_in[3][0] = value_saved1


def back_shift_rows(state_in):
    value_saved1 = state_in[1][3]
    state_in[1][3] = state_in[1][2]
    state_in[1][2] = state_in[1][1]
    state_in[1][1] = state_in[1][0]
    state_in[1][0] = value_saved1

    value_saved1 = state_in[2][0]
    value_saved2 = state_in[2][1]
    state_in[2][0] = state_in[2][2]
    state_in[2][1] = state_in[2][3]
    state_in[2][2] = value_saved1
    state_in[2][3] = value_saved2

    value_saved1 = state_in[3][0]
    state_in[3][0] = state_in[3][1]
    state_in[3][1] = state_in[3][2]
    state_in[3][2] = state_in[3][3]
    state_in[3][3] = value_saved1


def mix_columns(state_in):
    # initializing output
    output_state = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    # computing galois field matrix product
    for i in range(4):
        for j in range(4):
            new_value = 0x0
            for k in range(4):
                new_value = new_value ^ gf_mult(MIXCOL[i][k], state_in[k][j])
            output_state[i][j] = new_value

    return output_state


def back_mix_columns(state_in):
    # initializing output
    output_state = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    # computing galois field matrix product
    for i in range(4):
        for j in range(4):
            new_value = 0x0
            for k in range(4):
                new_value = new_value ^ gf_mult(INV_MIXCOL[i][k], state_in[k][j])
            output_state[i][j] = new_value

    return output_state


def xor(state_in, key):
    output_state = state_in.copy()
    for i in range(4):
        for j in range(4):
            output_state[i][j] = state_in[i][j] ^ key[i][j]
    return output_state


def next_key(key_in, rcon):
    # initializing output
    output_key = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]

    # storing columns
    col_1 = [key_in[0][0], key_in[1][0], key_in[2][0], key_in[3][0]]
    col_2 = [key_in[0][1], key_in[1][1], key_in[2][1], key_in[3][1]]
    col_3 = [key_in[0][2], key_in[1][2], key_in[2][2], key_in[3][2]]
    col_4 = [key_in[0][3], key_in[1][3], key_in[2][3], key_in[3][3]]
    new_col = col_4.copy()

    # shifting last column
    value_saved = new_col[0]
    new_col[0] = new_col[1]
    new_col[1] = new_col[2]
    new_col[2] = new_col[3]
    new_col[3] = value_saved

    # substituting last column
    for i in range(4):
        new_col[i] = subbyte(new_col[i])

    # XOR with rcon and 1st column
    for i in range(4):
        output_key[i][0] = new_col[i] ^ col_1[i]
    output_key[0][0] = output_key[0][0] ^ rcon

    # computing 2nd column of new key
    for i in range(4):
        output_key[i][1] = output_key[i][0] ^ col_2[i]

    # computing 3rd column of new key
    for i in range(4):
        output_key[i][2] = output_key[i][1] ^ col_3[i]

    # computing 4th column of new key
    for i in range(4):
        output_key[i][3] = output_key[i][2] ^ col_4[i]

    return output_key


def expand_key(key_in):
    key_list = [key_in]
    for i in range(10):
        key_list.append(next_key(key_list[i], RCON[i]))
    return key_list


def crypt(message_in, key_in):
    key_list = expand_key(key_in)

    state = xor(message_in, key_list[0])
    for i in range(1, 11):
        state = state_subbyte(state)
        shift_rows(state)
        if i != 10:
            state = mix_columns(state)
        state = xor(state, key_list[i])
    return state


def decrypt(cipher_text, key_in):
    key_list = expand_key(key_in)

    state = xor(cipher_text, key_list[10])
    for i in range(9, -1, -1):
        back_shift_rows(state)
        state = back_state_subbyte(state)
        state = xor(state, key_list[i])
        if i != 0:
            state = back_mix_columns(state)
    return state


def text_to_state(text):
    # initializing output
    output_state = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]

    # converting text to ASCII value
    for j in range(4):
        for i in range(4):
            output_state[i][j] = ord(text[4 * j + i])

    return output_state


def state_to_text(state_in, char_list):
    # initializing output
    text_out = ""

    # converting to text using only the characters
    # present in char_list
    list_length = len(char_list)
    for j in range(4):
        for i in range(4):
            text_out += char_list[state_in[i][j] % list_length]

    return text_out


# debug functions # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def print_state(state_in):
    dummy_state = state_in.copy()
    for i in range(4):
        for j in range(4):
            print(hex(dummy_state[i][j]), end=" \t")
        print("")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# GUI
root = Tk()
root.title("PASSWAN")
root.iconbitmap("Swan.ico")
root.resizable(False, False)

# Creating string variables
email = StringVar()
extra = StringVar()

# Defining constant values
WIDTH = 40
PADX = 2
PADY = 2

# Entry to insert the key
Key_Entry = Entry(root, width=WIDTH, show='*')
Key_Entry.pack(padx=PADX, pady=PADY)

# Read only entry where the e-mail will be displayed
Email_Entry = Entry(root, width=WIDTH, state="readonly", textvariable=email)
Email_Entry.pack(padx=PADX, pady=PADY)

# Read only entry where extra information will be displayed
Extra_Entry = Entry(root, width=WIDTH, state="readonly", textvariable=extra)
Extra_Entry.pack(padx=PADX, pady=PADY)

# Combobox to select the account
Account_Combobox = ttk.Combobox(root, width=WIDTH-5, values=[account.get("name") for account in ACCOUNTS])
Account_Combobox.bind("<<ComboboxSelected>>", lambda event: account_combobox_selected(Account_Combobox.current()))
Account_Combobox.pack(padx=PADX, pady=PADY)

root.mainloop()
