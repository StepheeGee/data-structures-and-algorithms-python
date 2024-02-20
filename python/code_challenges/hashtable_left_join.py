from data_structures.hashtable import Hashtable

def left_join(hash_table1, hash_table2):
    result = []

    for key in hash_table1.keys():
        value1 = hash_table1.get(key)
        value2 = hash_table2.get(key, "NONE")
        result.append([key, value1, value2])

    # Sort the result before returning
    result.sort()

    return result


