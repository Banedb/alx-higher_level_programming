#!/usr/bin/python3
"""100-matrix_mul module"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if any(type(row) is not list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(type(row) is not list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if any(type(i) not in (int, float) for row in m_a for i in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(type(i) not in (int, float) for row in m_b for i in row):
        raise TypeError("m_b should contain only integers or floats")
    size_a = len(m_a[0])
    size_b = len(m_b[0])
    if any(len(i) != size_a for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(i) != size_b for i in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if size_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    # new_list = []
    # for row_a in m_a:
    #     sub_list = []
    #     num = 0
    #     for num in range(size_b):
    #         result = 0
    #         for j, row_b in enumerate(m_b):
    #             result += row_a[j] * row_b[num]
    #         sub_list.append(result)
    #     new_list.append(sub_list)
    # return new_list
    return [
        [
            sum(m_a[line_a][line_b] * m_b[line_b][idx_b]
                for line_b in range(len(m_b))) for idx_b in range(size_b)
        ]
        for line_a in range(len(m_a))
    ]
