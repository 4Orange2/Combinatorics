from itertools import combinations 

def possible_sums(answer, N, non_neg=False):
    '''Evaluates equation of type x1 + x2 + x3...xN = answer
        by finding all the possible combinations (order matters)
        in positive integers
        Returns a list of all possible sums
    Args:
        N: the number of variables
        answer: the desired answer
        non_neg: if desired, the function 
            will calculate for non-negative integers
    returns tuples of all possible sums
    '''
    end_list = []
    if N > answer:
        print("Error: the number of variables must be <= the sum")
        return None
    if N <= 0:
        return None
    if (N-1) == 0:
        end_list.append(answer)
        return answer
    spaces = list(range(answer + N - 1)) if non_neg else list(
        range(1, answer))
    #print(spaces)
    comb = list(combinations(spaces, N - 1))
    #print(comb)
    # C(m - 1, k - 1)
    #print(f"Space index list: {comb}")
    val = 0
    for element in comb:
        case = []
        for i in range(N - 1):
            if i == 0:
                val = int(element[i])
                #print(val)
            else:
                diff = int(element[i]) - int(element[i-1])
                val = (diff - 1) if non_neg else diff
            case.append(val)
            #print(case)
        final_val = answer - sum(case)
        case.append(final_val)
        end_list.append(case)
    return end_list
    #math.comb(answer - 1, N - 1)

# Tests:

'''
print(possible_sums(6, 2))

print("***")
print(possible_sums(5, -1))
print("***")
print(possible_sums(5, 3))
print("***")
print(possible_sums(5, 1))

equation = possible_sums(21, 3)
print(len(equation))


print(possible_sums(5, 3, non_neg=True))
print(len(possible_sums(5, 3, non_neg=True)))
'''

def eliminate_equal(sorted_list):
    '''Identifies all equal elements of a sorted list
        and eliminates them
    Args:
    list: any list'''
    distinct = []
    for i in range(len(sorted_list)):
        element = sorted_list[i]
        if len(element) >= 2:
            print(f"element considered: {element}")
            for i in range(1, len(element)):
                #print(f"element index: {element[i]}")
                if ((element[i] != element[i - 1]) or (
                    i == (len(element) - 1))):
                    if (i == (len(element) - 1)) and (element[i] != element[i - 1]):
                        distinct.append(element[i - 1])
                        distinct.append(element[i])
                        print(f"element to be added: {element[i - 1]}")
                        print(f"element to be added: {element[i]}")
                    else:
                        # figuring out total amount of equal variables
                        print(f"element to be added: {element[i - 1]}")
                        distinct.append(element[i - 1])
        else:
            distinct.append(sorted_list[i]) # appends case with all 1's
    print(f"distinct list: {distinct}")
    return distinct

def partitions(n):
    '''returns all partitions of integer n
    Args:
    n: the number which we want to partition
    '''
    sorted_possible = []
    sums = []
    for i in range(2, n + 1):
        sums.append(possible_sums(n, i))
    print(f"this is sums: {sums}")
    new_list = []
    for element in sums:
        new_list = []
        for item in element:
            item.sort()
            new_list.append(item)
        new_list.sort()
        print(f"Sorted new list: {new_list}")
        sorted_possible.append(new_list)
    sorted_possible.sort()
    print(f"this is sorted_possible: {sorted_possible}")
    # all possibilities sorted from greatest to least
    partitions = eliminate_equal(sorted_possible)
    partitions.append([n])
    return partitions

print(partitions(6))
print(len(partitions(6)))
