liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
"""Listeme örnek değerler atadım."""

def flatten(list1):
    flat_list = []
    for item in list1:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
            """Liste olup olmama kontrolü ! """
        else:
            flat_list.append(item)
    return flat_list

# Örnek kullanım
liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
düz_liste = flatten(liste)
print(düz_liste)
