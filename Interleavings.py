def interleave(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1 == 0:
        return [s2]
    if n2 == 0:
        return [s1]
    result = []
    for i in range(n1):
        for j in range(n2):
            for inter in interleave(s1[i+1:], s2[j:]):
                result.append(s1[i] + inter)
            for inter in interleave(s1[i:], s2[j+1:]):
                result.append(s2[j] + inter)
    return result

s1 = input("Enter the first string : ")
s2 = input("Enter the secound string : ")
interleavings = interleave(s1, s2)
print(interleavings)
