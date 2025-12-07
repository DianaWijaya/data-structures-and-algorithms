from __future__ import annotations
from threedeebeetree import Point
from ratio import Percentiles

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    """
        returns a list of Points which is ordered such that for any node in the 3DBT the negative offset of
        one of the three axis and positive offset of the same axis have a side ratio at most 1:7

        Args: 
        - my_coordinate_list (list[Point]): the list containing all the coordinates of the beehives to be added into a 3DBT

        Returns:
        - sorted_list (list[Point]): a sorted list of the coordinates such that it forms a balanced 3DBT when added in that order

        Raises:
        - None

        Complexity:
        - WCS: O(n log(n)), where n is the number of Points in the list given as the argument. 
        - BCS: O(n log(n)), same as WCS 
    """
    if len(my_coordinate_list) < 18 : # O(1)
        return my_coordinate_list # O(1)

    x_percentile = Percentiles() # O(1)
    y_percentile = Percentiles() # O(1)
    z_percentile = Percentiles() # O(1)
    for each in my_coordinate_list: # O(n)
        x_percentile.add_point(each[0]) # O(log(n))
        y_percentile.add_point(each[1]) # O(log(n))
        z_percentile.add_point(each[2]) # O(log(n))
    x_ratio_list = set(x_percentile.ratio(12.5, 12.5)) # O(O + log(n))
    y_ratio_list = set(y_percentile.ratio(12.5, 12.5)) # O(O + log(n))
    z_ratio_list = set(z_percentile.ratio(12.5, 12.5)) # O(O + log(n))

    sorted_list = [] # O(1)

    for each in my_coordinate_list : # O(n)
        if each[0] in x_ratio_list and each[1] in y_ratio_list and each[2] in z_ratio_list : # O(1)
            root = each # O(1)
            sorted_list.append(each) # O(1)
            my_coordinate_list.remove(each) # O(1)
            break # O(1)

    oct1 = [] # O(1)
    oct2 = [] # O(1)
    oct3 = [] # O(1)
    oct4 = [] # O(1)
    oct5 = [] # O(1)
    oct6 = [] # O(1)
    oct7 = [] # O(1)
    oct8 = [] # O(1)

    for each in my_coordinate_list : # O(n)
        if each[0] >= root[0] and each[1] >= root[1] and each[2] >= root[2] : # O(1)
            oct1.append(each) # O(1)
        elif each[0] < root[0] and each[1] >= root[1] and each[2] >= root[2] : # O(1)
            oct2.append(each) # O(1)
        elif each[0] < root[0] and each[1] < root[1] and each[2] >= root[2] : # O(1)
            oct3.append(each) # O(1)
        elif each[0] >= root[0] and each[1] < root[1] and each[2] >= root[2] : # O(1)
            oct4.append(each) # O(1)
        elif each[0] >= root[0] and each[1] >= root[1] and each[2] < root[2] : # O(1)
            oct5.append(each) # O(1)
        elif each[0] < root[0] and each[1] >= root[1] and each[2] < root[2] : # O(1)
            oct6.append(each) # O(1)
        elif each[0] < root[0] and each[1] < root[1] and each[2] < root[2] : # O(1)
            oct7.append(each) # O(1)
        elif each[0] >= root[0] and each[1] < root[1] and each[2] < root[2] : # O(1)
            oct8.append(each) # O(1)

    all_octs = [oct1, oct2, oct3, oct4, oct5, oct6, oct7, oct8] # O(1)

    for each in all_octs : # O(1)
        sorted_list.extend(make_ordering(each)) # O(n)

    # Another approach:
    # a_list = [[] for i in range(8)] 
    # for each in my_coordinate_list : # O(n)
    #     cord = int(each[0] >= root[0])*(2**2) + int(each[1] >= root[1])*(2**1) + int(each[2] >= root[2])*(2**0) 
    #     a_list[cord].append(each)

    # for each in a_list :
    #     sorted_list.extend(make_ordering(each))

    return sorted_list # O(1)

if __name__ == "__main__" :
    pass
