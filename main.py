import heapq


def min_cost_cable_connection(cables):
 
    if not cables:
        return 0

    heapq.heapify(cables) 
    total_cost = 0

    while len(cables) > 1:
        #Виймаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        #Додаємо об'єднаний кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost


def merge_k_lists(lists):
    min_heap = []
    result = []

    #Додаємо перші елементи кожного списку у купу
    for i, lst in enumerate(lists):
        if lst: 
            heapq.heappush(min_heap, (lst[0], i, 0)) 

    while min_heap:
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        #Додаємо наступний елемент із того ж списку
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(min_heap, (next_val, list_idx, element_idx + 1))

    return result


# --Приклад використання обох задач--

if __name__ == "__main__":
    cables = [8, 4, 6, 12]
    total_cost = min_cost_cable_connection(cables.copy())  
    print("Мінімальні витрати на з'єднання кабелів:", total_cost)

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список після злиття k списків:", merged_list)
