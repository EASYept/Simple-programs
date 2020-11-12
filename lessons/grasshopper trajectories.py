#https://www.youtube.com/watch?v=EdhN_gEDfUM&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=10

def count_trajectories(N, allowed:list):
    """кузнечик прыгает +2 или +2, или +3
    есть запрещёные клетки
    allowed - список True и False значений разрешенных клеток
    """

    K=[0, 1, int(allowed[2])]+[0]*(N-3)
    for i i range(3, N+1):
        if allowed[i]:
            K[i]=K[i-1]+K[i-2]+K[i-3]


def count_min_cost(N, price:list):
    """+1 и +2""""
    C=[float("-inf"), price[1], price[1]+price[2]]+[0]*(n-2)
    for i in range(3,N+1):
        C[i]=price[i]+min(C[i-1], C[i-2])
    return C[N]