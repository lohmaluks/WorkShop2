# Ex1
thsiset = {"apple", "bannana", "cherry"}
thsiset.remove("banana")
print(thsiset)  # output: {'cherry', 'apple',  'orange'}

# Ex2
thsiset = {"apple", "bannana", "cherry"}
thsiset.discard("banana")
print(thsiset)  # output: {'cherry', 'apple'}

# Ex3
thsiset = {"apple", "bannana", "cherry"}
x = thsiset.pop()
print(thsiset)  # output: {'cherry', 'banana'}

# Ex4
thsiset = {"apple", "bannana", "cherry"}
thsiset.clear()
print(thsiset)  # output: set()