#from typing import List, Tuple

from typing import List, Tuple
import numpy as np
import math

def count_chains(circles: List[Tuple[int, int, int]]) -> int:

    # your code here
    # 计算圆心距离，判断两圆是否相交,相交True，不相交返回False
    # 两个圆半径绝对值 < 两圆心距离 < 两个圆半径和，则两个圆相交
    def get_distances(c1, c2):
        p1 = np.array(c1[:2])
        p2 = np.array(c2[:2])
        p3 = p2 - p1
        p4 = math.hypot(p3[0], p3[1])  # 圆心距离
        R0 = abs(c1[-1] - c2[-1])  # 两个圆半径绝对值
        R1 = c1[-1] + c2[-1]  # 两个圆半径和
        return True if R0 < p4 < R1 else False
 
    Ncircles = []
    # 原列表重新分成子列表，相交圆的在一个子列表中
    for i in range(len(circles)-1):
        for j in range(i+1,len(circles)):
 
            # 判断两个圆是否已存在子列表中
            a, b = -1, -1
            for N in Ncircles:
                if circles[i] in N:
                    a = Ncircles.index(N)
            for N in Ncircles:
                if circles[j] in N:
                    b = Ncircles.index(N)
 
            # 两个圆不相交时
            if not get_distances(circles[i], circles[j]):
                if a == b == -1:
                    Ncircles.append([circles[i]])
                    Ncircles.append([circles[j]])
                elif a != -1 and b == -1:
                    Ncircles.append([circles[j]])
                elif a == -1 and b != -1:
                    Ncircles.append([circles[i]])
 
            # 两个圆相交时
            if get_distances(circles[i], circles[j]):
                if a == b == -1:
                    Ncircles.append([circles[i],circles[j]])
                elif a != -1 and b == -1:
                    Ncircles[a].append(circles[j])
                elif a == -1 and b != -1:
                    Ncircles[b].append(circles[i])
                elif a != -1 and b != -1 and a!=b:  # 两个圆相交，但在不同的子列表中，将两个子列表合并
                    Ncircles[a].extend(Ncircles.pop(b))
 
    return len(Ncircles)


if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")
