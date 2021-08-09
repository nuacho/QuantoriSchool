# problem 6
print((sum([k for k in range(1, 101)])**2) -
      (sum([i**2 for i in range(1, 101)])))

# problem 40
print(eval(str(tuple([(int(("".join(str(i) for i in range(1, 1000000)))[10**i - 1]))
                      for i in range(7)])).replace(',', '*')))

# problem 48
print(int((str(sum([i**i for i in range(1, 1001)])))[-10:]))

# problem 9

# for a in range(1, 1000):
#     for b in range(1, 1000):
#         c = 1000 - a - b
#         if c*c == a*a+b*b and a+b+c == 1000 and a < b < c:
#             print(a, b, c)
#             print(a*b*c)

print([a*b*c for a in range(1, 1000) for b in range(1, 1000)
      for c in [1000-b-a] if a*a+b*b == c*c and a < b and b < c][0])
