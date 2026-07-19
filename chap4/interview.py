# "https://github.com/narayan09/Python-Interview-Questions/tree/main"

# # #Problem 1: Remove duplicates from a list while preserving order
# # def no_dupli(lst):
# #     seen = set()
# #     res = []

# #     for num in lst:
# #         if num not in seen:
# #             res.append(num)
# #             seen.add(num)

# #     return res

# # lst = [1,2,2,2,3,3,4,4,5,5]
# # res = no_dupli(lst)
# # print(res)

# # #What if we have nested lists (unhashable types)?
# # def no_dupli(lst):
# #     res = []
# #     for num in lst:
# #         if num not in res:
# #             res.append(num)
# #     return res
# # lst = [1,2,2,2,3,3,4,4,5,5]
# # res = no_dupli(lst)
# # print(res)

# # # Remove duplicates from a string
# # def no_dupli(string):
# #     res = []
# #     for ch in string:
# #         if ch not in res:
# #             res.append(ch)
# #     return ''.join(res)
# # string = (input("enter string : "))
# # res = no_dupli(string)
# # print(res)

# #Remove duplicates but count occurrences
# def no_dupli(string):
#     res = []
#     count = {}
#     for ch in string:
#         if ch not in res:
#             res.append(ch)
#             count[ch] = count.get(ch, 0)+1
# string = (input("enter string : "))
# res = no_dupli(string)

# count = no_dupli(string)
# print(res)
# print("Occurrences:", count)

# "-------------------------------------------------"
# Problem 2: Find the second largest element
def sec_lar(lst):
    if len(lst)<2:
        return None
    lar = sec_lar = float('-inf')
    for num in lst:
        if num > lar:
            sec_lar = lar
            lar = num
        elif num > sec_lar and num != lar:
            sec_lar = num
    if sec_lar == float('-inf'):
        return None
    return sec_lar
print(sec_lar([3,7,1,9,4,9]))

#Using Sort 
def sec_lar(lst):
    if len(lst)<2:
        return None
    uni = set(lst)
    if len(uni)<2:
        return None
    return sorted(uni)[-2]
print(sec_lar([3,7,1,9,4,9]))

## Problem A: Find the third largest element
def third_largest(lst):
    if len(set(lst)) < 3:   # fewer than 3 unique elements
        return None
    lar = sec_lar = third_lar = float('-inf')
    for num in lst:
        if num > lar:
            third_lar = sec_lar
            sec_lar = lar
            lar = num
        elif num > sec_lar and num != lar:
            third_lar = sec_lar
            sec_lar = num
        elif num > third_lar and num != lar and num != sec_lar:
            third_lar = num
    return third_lar if third_lar != float('-inf') else None
print(third_largest([3, 7, 1, 9, 4, 9]))  # Output: 4

'''
# Problem A: Find the third largest element
# Input: [3, 7, 1, 9, 4, 9] → Output: 4
def third_largest(lst):
    # Your code here
    pass

# Problem B: Find the second smallest element
# Input: [3, 7, 1, 9, 4, 9] → Output: 3
def second_smallest(lst):
    # Your code here
    pass

# Problem C: Find the largest and second largest in one function
# Input: [3, 7, 1, 9, 4, 9] → Output: (9, 7)
def largest_and_second(lst):
    # Your code here
    pass'''

