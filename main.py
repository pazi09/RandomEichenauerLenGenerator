def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def ICG(n, a, c, seed):
    if (seed == 0):
        return c;
    return (a * modinv(seed, n) + c) % n;

seed = 1
n = 5
a = 2
c = 3
count = 10

for i in range(count):
    print(seed)
    seed = ICG(n, a, c, seed)
