def anagram(str1, str2):
    if ''.join(sorted(str1.lower())).strip() == ''.join(sorted(str2.lower())).strip():
        print("True")
        return True
    else:
        print("False")
        return False


str1 = "abcdE f"
str2 = "bacdE f"

anagram(str1, str2)