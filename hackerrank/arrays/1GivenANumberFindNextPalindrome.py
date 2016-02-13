def is_palindrome(number):
    num_str = str(number)
    low = 0
    high = len(num_str) - 1
    while low < high:
        if num_str[low] is not num_str[high]:
            return False
        low += 1
        high -= 1

    return True

def find_next_palindrome(number):
    var_num = number

    if is_palindrome(var_num):
        var_num += 1
    
    while not is_palindrome(var_num):
        var_num += 1

    return var_num

print find_next_palindrome(23545), "expected", "23632"
print find_next_palindrome(99), "expected 101"
print find_next_palindrome(6789876), "expected 6790976"
print find_next_palindrome(8998), "expected 9009"
