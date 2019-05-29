d1 = {
    10: "a",
    20: "b"
}

d2 = {
    30: "c"
}

l1 = d1.items()  # returns a list
print(l1)

l2 = d2.items()
print(l2)

d3 = dict(l1)
print(d3)

d3.update(dict(l2))
print(d3)
