colors = [1,2,3,4,5,89]
print(dir(colors))
def merge_sort(colors):
    if len(colors) > 1:
        mid = len(colors)
        print(mid)
        left = colors[:mid]
        print(left)
        right = colors[mid:]
        print(right)

merge_sort(colors)

l = 0
r = len(colors) -1

print(l)
print(r)

print(help(:))
