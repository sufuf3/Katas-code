def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)

def lcm(m, n):
    return m * n / gcd(m, n)

m = int(input("輸入 m："))
n = int(input("輸入 n："))
print("Gcd: ", gcd(m, n))
print("Lcm: ", lcm(m, n))
