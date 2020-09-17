def romanToInt(self, s: str) -> int:
    numDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = [0]
    for c in s:
        nums.append(numDict[c])
    result = nums[-1]
    while True:
        if nums == [0]:
            break

        m = nums.pop()
        if m > nums[-1]:
            result -= nums[-1]
        if m <= nums[-1]:
            result += nums[-1]

    return result


