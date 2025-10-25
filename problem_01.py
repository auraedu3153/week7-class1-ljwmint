# 요구사항은 https://www.acmicpc.net/problem/1018을 확인하세요
def min_count_of_squares(board: list[list[str]]) -> int:
    nboard=[[((board[j][i]=="B")+i+j)%2 for i in range(len(board))] for j in range(len(board[0]))];return 32-abs(32- max([sum([nboard[i+_][j+__] for _ in range(8) for __ in range(8)]) for i in range(len(board)-7) for j in range(len(board[0])-7)]))
