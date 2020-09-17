def isPalindrome(self, x: int) -> bool:
    s = str(x)
    return s == s[::-1]  # a[i:j:s] i起始，j结束，s步长（s<0且i,j缺省时，表示倒序）
