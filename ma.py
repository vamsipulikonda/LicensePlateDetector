n = int(input())
marksheet = [[input(),float(input())] for _ in range(n)]
marksheet = marksheet.sort()
print(marksheet)    
print(marksheet[-1][0])
print(marksheet[-2][0])
