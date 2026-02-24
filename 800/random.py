nums = list(map(int, input().split()))
target = int(input())

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] + nums[j] == target:
            break

print(f"[{j},{i}]")
print(f"[{j},{i}]")