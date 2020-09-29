def addition(a,b):

    result = []

    for (a_element, b_element) in zip(a, b):
        foo = list(map(lambda x, y: x + y, a_element, b_element))
        result.append(foo)




a = [
    [1,2],
    [3,4]
]

b = [
    [5,6],
    [7,8]
]


print(addition(a, b))