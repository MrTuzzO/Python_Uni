import heapq


def sort_using_pq(lst):
    heapq.heapify(lst)

    sorted_lst = []
    while lst:
        sorted_lst.append(heapq.heappop(lst))

    return sorted_lst


lst = [5, 3, 8, 1, 2, 7]
st_list = sort_using_pq(lst)
print(st_list)
