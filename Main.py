# RC4 - PRGA and Encrypt/Decrypt

def prga(S, out_len):
    # Make a copy so the original S array doesn't get changed
    S = S.copy()

    i = 0
    j = 0
    K_prime = []

    # Generate the keystream
    for x in range(out_len):
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        # Swap S[i] and S[j]
        S[i], S[j] = S[j], S[i]

        t = (S[i] + S[j]) % 256
        K_prime.append(S[t])

    return K_prime


def rc4_xor(data, keystream):
    # XOR each byte with the keystream
    return [d ^ k for d, k in zip(data, keystream)]


# S array from the slide
S = [101, 232, 172, 10, 166, 26, 46, 91, 2, 137,
     39, 243, 253, 25, 3, 30, 47, 238, 196, 38,
     94, 149, 15, 32, 248, 51, 158, 150, 106, 183,
     67, 219, 95, 177, 138, 152, 13, 188, 118, 108,
     207, 151, 41, 142, 236, 103, 55, 72, 20, 244,
     216, 14, 168, 90, 4, 42, 153, 64, 250, 129,
     97, 225, 87, 199, 204, 100, 16, 249, 191, 82,
     43, 131, 24, 169, 69, 54, 96, 77, 255, 84,
     1, 143, 242, 123, 21, 93, 61, 102, 224, 107,
     109, 79, 80, 23, 229, 6, 156, 181, 105, 159,
     33, 141, 18, 104, 9, 56, 233, 178, 127, 111,
     135, 206, 202, 128, 31, 71, 211, 222, 45, 66,
     163, 189, 167, 201, 124, 17, 251, 198, 170, 155,
     115, 57, 228, 98, 190, 76, 59, 239, 37, 147,
     180, 240, 197, 200, 19, 0, 213, 99, 125, 44,
     195, 164, 176, 121, 220, 212, 86, 186, 34, 214,
     230, 254, 40, 203, 194, 231, 162, 226, 187, 116,
     208, 22, 68, 88, 192, 140, 205, 234, 119, 83,
     136, 63, 12, 112, 217, 154, 184, 81, 70, 35,
     174, 78, 241, 179, 210, 215, 49, 144, 130, 48,
     133, 7, 209, 92, 73, 193, 28, 75, 117, 223,
     50, 113, 114, 148, 173, 29, 53, 160, 8, 139,
     246, 65, 252, 161, 221, 185, 27, 36, 11, 110,
     237, 165, 5, 182, 145, 171, 120, 157, 134, 175,
     122, 58, 235, 52, 62, 126, 85, 60, 132, 74,
     245, 227, 218, 89, 247, 146]

# The array from the slide already has the first swap done.
# Swap these back before running the PRGA.
S[1], S[124] = S[124], S[1]


# Message we are encrypting
message = [77, 97, 116, 104, 32, 51, 49, 48,
           32, 80, 114, 111, 118, 101, 115, 33]

message_text = bytes(message).decode("ascii")


# ---------------- PRGA ----------------

K_prime = prga(S, len(message))

print("PRGA")
print("i:     ", end="")
for i in range(len(K_prime)):
    print(f"{i:<5}", end="")
print()

print("K'[i]: ", end="")
for value in K_prime:
    print(f"{value:<5}", end="")
print()

print()
print("Keystream:", K_prime)


# ---------------- Encryption ----------------

ciphertext = rc4_xor(message, K_prime)

print("\nEncryption")
print("Message:", message_text)
print("Message ASCII:", message)
print("Ciphertext:", ciphertext)
print("Ciphertext hex:", bytes(ciphertext).hex())


# ---------------- Decryption ----------------

decrypted = rc4_xor(ciphertext, K_prime)
decrypted_text = bytes(decrypted).decode("ascii")

print("\nDecryption")
print("Decrypted ASCII:", decrypted)
print("Decrypted message:", decrypted_text)


# Check that the decrypted message is the same as the original
if decrypted == message:
    print("\nThe message was decrypted correctly!")
else:
    print("\nSomething went wrong.")