from itertools import combinations

def possible_sums(answer, var_amount, non_neg=False, less_subt=0, great_restrict=0):
    '''Evaluates equation of type x1 + x2 + x3...xN = answer
        by finding all the possible combinations (order matters)
        in positive integers
        Returns a list of all possible sums
    Args:
        var_amount: the number of variables
        answer: the desired answer
        non_neg: if desired, the function
            will calculate for non-negative integers
        less_restrict: answer - less_subt = less_restrict
            (variables must be less than less_restrict)
        great_restrict: all variables must be greater than that number
    ** if non_neg, it's _______ or equal to (e.g. less than or equal to)
    returns list of all possible sums
    '''
    end_list = []
    barriers = var_amount - 1
    less_restrict = answer - less_subt
    if var_amount > answer:
        print("Error: the number of variables must be <= the sum")
        return None
    elif var_amount <= 0:
        return None
    elif var_amount == 1:
        end_list.append(list(answer))
        return end_list
    if non_neg:
        possible_values = list(range(1, answer + barriers))
        less_restrict += 1
        great_restrict -= 1
    else:
        possible_values = list(range(1, answer))
    #print(spaces)
    comb = list(combinations(possible_values, barriers))
    # list of all indexes for barriers
    #print(comb)
    # C(m - 1, k - 1)
    #print(f"Space index list: {comb}")
    val = 0
    for element in comb:
        case = []
        for barrier_num in range(barriers):
            if barrier_num == 0:
                val = int(element[barrier_num])
                #print(val)
            else:
                diff = int(element[barrier_num]) - int(element[barrier_num - 1])
                val = diff
            case.append(val)
            #print(case)
        final_val = answer - sum(case)
        case.append(final_val)
        end_list.append(case)
    end_list = extract_range(end_list, less_restrict)
    end_list = extract_range(end_list, great_restrict, less=False)
    return end_list
    #math.comb(answer - 1, N - 1)

def extract_range(combs, limit, less=True):
    ''' Function shaves off all combinations that don't floow the restrictions
    Checks to see if all elements in the given combination are under the limit
    (in case of less=True) or over (in the case of less=False) 
    and if so, allows the combination to pass on to the final list.'''
    extract_list = []
    for element in combs:
        all_indexes = len(element)
        append_True = 0
        for index in range(all_indexes):
            if less:
                if element[index] < limit:
                    append_True += 1
            elif less == False:
                if element[index] > limit:
                    #print(f"for greater: {element[index]}")
                    append_True += 1
        if append_True == all_indexes:
            extract_list.append(element)
    #print(f"this is extract_list: {extract_list}")
    return extract_list

print(possible_sums(10, 3, non_neg=True, less_subt=3, great_restrict=1))
print("HELLO")

print("---------------")
print(extract_range([[0, 0, 5], [0, 1, 4], [0, 2, 3], [0, 3, 2], [0, 4, 1], [0, 5, 0], [1, 0, 4], [1, 1, 3], [1, 2, 2], [1, 3, 1], [1, 4, 0], [2, 0, 3], [2, 1, 2], [2, 2, 1], [2, 3, 0], [3, 0, 2], [3, 1, 1], [3, 2, 0], [4, 0, 1], [4, 1, 0], [5, 0, 0]], 0, less=False))

def sort_list(unsorted, reverse=False, doublelayered=False):
    '''List sorting function that I created for sorting a list which contains two or one lists embedded within.'''
    sorted_list = []
    if doublelayered:
        for element in unsorted:
            new_list = []
            for item in element:
                item.sort(reverse=reverse)
                new_list.append(item)
            new_list.sort(reverse=reverse)
            #print(f"Sorted new list: {new_list}")
            sorted_list.append(new_list)
    else:
        for element in unsorted:
            element.sort(reverse=reverse)
            sorted_list.append(element)
    sorted_list.sort(reverse=reverse)
    return sorted_list

def eliminate_equal(sorted_list):
    '''Identifies all equal elements of a sorted list
        and eliminates them
    Args:
    list: any list'''
    distinct = []
    for i in range(len(sorted_list)):
        element = sorted_list[i]
        if len(element) >= 2:
            #print(f"element considered: {element}")
            for i in range(1, len(element)):
                #print(f"element index: {element[i]}")
                if ((element[i] != element[i - 1]) or (
                    i == (len(element) - 1))):
                    if (i == (len(element) - 1)) and (element[i] != element[i - 1]):
                        distinct.append(element[i - 1])
                        distinct.append(element[i])
                        #print(f"element to be added: {element[i - 1]}")
                        #print(f"element to be added: {element[i]}")
                    else:
                        # figuring out total amount of equal variables
                        #print(f"element to be added: {element[i - 1]}")
                        distinct.append(element[i - 1])
        else:
            distinct.append(element[i])
            # appends case with all 1's
    #print(f"distinct list: {distinct}")
    return distinct

def partitions(n, less_subt=0, great_restrict=0, summand_subt=0):
    '''returns all partitions of integer n
    Args:
    n: the number which we want to partition
    summand_subt: n - summand_subt = summand_limit
        amount of summands is less than or equal to that value
        meaning amount of terms that are added up
    less_subt: n - less_subt = less_restrict
        ** all summands less or equal to that value
    '''
    less_subt -= 1
    sorted_possible = []
    sums = []
    parts = []
    summand_limit = n - summand_subt
    for variable_amount in range(2, summand_limit + 1):
        sum_possib = possible_sums(
            n, variable_amount, less_subt=less_subt, great_restrict=great_restrict)
        if len(sum_possib) > 0:
            sums.append(sum_possib)
    #print(f"this is sums: {sums}")
    if len(sums) > 0:
        sorted_possible = sort_list(sums, doublelayered=True)
    #print(f"this is sorted_possible: {sorted_possible}")
    if len(sorted_possible) > 0:
        parts = eliminate_equal(sorted_possible)
    if less_subt == (-1):
        parts.append([n])
    return parts

# alternative function to len(partitions(...))
def num_of_parts(n, less_subt=0, great_restrict=0, summand_subt=0):
    number = len(partitions(n, less_subt=less_subt, great_restrict=great_restrict, summand_subt=summand_subt))
    return number

print(partitions(6))

print(partitions(9, less_subt=3))
print(partitions(9, great_restrict=8))
print(partitions(9, less_subt=1, great_restrict=2))
print(len(partitions(9, less_subt=1, great_restrict=2)))

# checking equivalence between summand_subt and less_subt
print(partitions(9, summand_subt=2))
print(len(partitions(9, summand_subt=2)))

print(partitions(9, less_subt=2))
print(len(partitions(9, less_subt=2)))

# Solving the problem set:

for i in range(1, 6): # Q 1 of Mathematics of Choice by Ivan Niven
    print(len(partitions(i)))

print(num_of_parts(4) - num_of_parts(4, summand_subt=2))
