# Real hash functions (SHA-256, MD5) are complex, but their core idea is simple:
# product a fixed-size fingerprint from any input. A tiny change to the input completely changes the hash.
# Task: Build an eudcational (non-secure) hash: sum all ASCII values weighted by position, XOR with a magic onstant, and return a fixed-length hex string

def simple_hash(text):
    total = 0
    for i, ch in enumerate(text, 1):
        total += ord(ch) * i
    total ^= 0xDEAD
    total %= 65536
    return f"{total:04x}" # 4-character lwoercase hex string

def main():
    print("Simple Hash (Not secure)")
    text = input("Enter the text to hash: ")
    hash = simple_hash(text)
    print("Hash:", hash)

if __name__ == "__main__":
    main()