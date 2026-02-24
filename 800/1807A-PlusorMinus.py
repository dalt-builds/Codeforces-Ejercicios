n = int(input())
j = 0
for i in range(n):
    nums = list(map(int, input().split()))
    if nums[j] + nums[j + 1] == nums[j + 2]:
        print("+") 
    else:
        print("-")
    