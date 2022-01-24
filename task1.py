def solution(A, B):
    testCase = A * B
    ones = bin(testCase).replace("0b", "").count("1")
    return ones

print(solution(5, 7))
