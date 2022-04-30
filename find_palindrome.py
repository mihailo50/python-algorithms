
def is_palindrome(n):
    m = n[::-1]
    if m == n:
        return True
    else:
        return False


print(is_palindrome(input("Insert number: ")))