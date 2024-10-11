def caeser_decrypt_brute_force(cipher_text):
    plain_text=""
    char_set="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" # character set
    for i in range(1,26):
        plain_text=""
        for char in cipher_text:
            if char in char_set:
                plain_text+=char_set[(char_set.index(char)-i)%len(char_set)]
            else:
                plain_text+=char
        print(f"Shift {i}: {plain_text}")
        
password="YZH(878GBC 8BFC87 8C7999 F8AFB ADA8GG 8GGCC7 A7F9EG 8BFDAB)"
caeser_decrypt_brute_force(password)



# # def caeser_decrypt1(cipher_text): #remove non-alphabetic chararcters and consider only the letters
# #     plain_text=""
# #     char_set="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# #     for i in range(1,26):
# #         plain_text=""
# #         for char in cipher_text:
# #             if char in char_set:
# #                 plain_text+=char_set[(char_set.index(char)-i)%len(char_set)]
# #         print(f"Shift {i}: {plain_text}")
        
# def caeser_decrypt2(cipher_text): #keep non-alpahabetic characters as it is
#     plain_text=""
#     char_set="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     for i in range(1,26):
#         plain_text=""
#         for char in cipher_text:
#             if char in char_set:
#                 plain_text+=char_set[(char_set.index(char)-i)%len(char_set)]
#             else:
#                 plain_text+=char
#         print(f"Shift {i}: {plain_text}")
        
# #caeser_decrypt1(password)
# caeser_decrypt2(password)