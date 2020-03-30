from collections import Counter

def count(string):
    return Counter(string)

if __name__ == "__main__":
    print(count("aba"))
