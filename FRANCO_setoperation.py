A = {"a", "g", "d", "f", "c", "b"}
B = {"l", "m", "o", "c", "h", "b"}
C = {"h", "c", "d", "f", "k", "i", "j"}

#How many elements are there in set A and B
print(len(A|B))

#How many elements are there in B that is not part of A and C
print(len(B - (A | C)))

#{h, i, j, k}
print(C-A)

#{c, d, f}
print(A&C)

#{b, c, h}
print((B&C)|{"b"})

#{d, f}
print((A&C)-B)

#{c}
print(A&B&C)

#{l, m, o}
print(B-(A|C))