# #формулы булевой алгебры
# print(1,2,3,4,5,6,7,'ans')
# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             print(int(not(c)), int(b*(not(c))), int(a!=b*(not(c))),
#                   int(c==(a!=b*(not(c)))), int(not(b)), int(a*(not(b))),
#                   int(a*(not(b))or c), int((not(a*(not(b))or c))or(c==(a!=b*(not(c))))))
#
# print('1\t','2\t','ans')
# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             print(int(not(b*(not(a)))or a or c),'\t', int(not(c)or a*b),'\t', int((not(c)or a*b)==(not(b*(not(a)))or a or c)))



# #бинарные деревья
#
# PRE=[]
# POST=[]
# IN=[]
#
# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# def pre_order(node):
#     if node:
#         PRE.append(node.value)
#         pre_order(node.left)
#         pre_order(node.right)
#
# def post_order(node):
#     if node:
#         post_order(node.left)
#         post_order(node.right)
#         POST.append(node.value)
#
# def in_order(node):
#     if node:
#         in_order(node.left)
#         IN.append(node.value)
#         in_order(node.right)
#
# tree = TreeNode(45)
# tree.left = TreeNode(37)
# tree.right = TreeNode(65)
# tree.left.left = TreeNode(13)
# tree.left.right = TreeNode(41)
# tree.right.left = TreeNode(57)
# tree.right.right = TreeNode(63)
# tree.right.right.left = TreeNode(66)
# tree.right.right.right = TreeNode(73)
#
# pre_order(tree)
# post_order(tree)
# in_order(tree)
#
# print('Pre-order')
# print(PRE)
# print('Post-order')
# print(POST)
# print('In-order')
# print(IN)


PRIORITY = {1: ['+', '-'], 2: ['*', '/']}

def priority(value: str) -> int:
    for k, v in PRIORITY.items():
        if value in v:
            return k
    return -1

def pol_notation(expr: str):
    result = []
    stack = []
    for element in expr:
        if element not in '+-*/':
            result.append(element)
        else:
            last = None if not stack else stack[-1]
            while priority(last) >= priority(element):
                result.append(stack.pop())
                last = None if not stack else stack[-1]
            stack.append(element)
    for e in reversed(stack):
        result.append(e)
    return ''.join(result)

print(pol_notation('3+5/2+14+2'))