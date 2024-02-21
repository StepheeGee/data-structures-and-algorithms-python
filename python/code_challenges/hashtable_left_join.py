from data_structures.hashtable import Hashtable

def left_join(synonyms, antonyms):
    result = []

    for key in synonyms:
        row = [key, synonyms[key]]

        if key in antonyms:
            row.append(antonyms[key])
        else:
            row.append("None")

        result.append(row)

    return result





















