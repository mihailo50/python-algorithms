

def bubble_sort(n: list) -> list:

    nl = len(n)

    for i in range(nl-1):
        print("---",i)
        for j in range(0, nl-i-1):
            print("***",j)
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]

nlb = [1, 5, 7, 9, 0, 10, 6, 100, 99, 40, 2]

bubble_sort(nlb)
print(nlb)
