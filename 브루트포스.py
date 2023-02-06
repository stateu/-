# # 7568 덩치
# import sys
# N = int(sys.stdin.readline())
# wh_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# rank_list = []
#
# for idx in range(N):
#     k = 0
#     for jdx in range(N):
#         if idx == jdx:
#             continue
#
#         if wh_list[idx][0] < wh_list[jdx][0] and wh_list[idx][1] < wh_list[jdx][1]:
#             k += 1
#     rank_list.append(k+1)
# print(*rank_list)

# # 1018 체스판 다시  칠하기
# M,N = map(int,input().split())
#
# mat = [list(input()) for _ in range(M)]
#
# init_list = ['WBWBWBWB', 'BWBWBWBW'] * 10
# init_w = [list(str_temp) for str_temp in init_list[:8]]
# init_b = [list(str_temp) for str_temp in init_list[1:9]]
#
# min_val = 50*50
#
# for row in range(M-8+1):
#     for col in range(N-8+1):
#         new_mat = [[mat[r][c] for c in range(col,col+8)] for r in range(row, row+8)]
#         cnt = 0
#         ccnt = 0
#
#         for idx in range(0, len(new_mat)):
#             for jdx in range(0 ,len(new_mat[0])):
#                 if new_mat[idx][jdx] != init_w[idx][jdx]:
#                     cnt += 1
#         if cnt < min_val:
#             min_val = cnt
#
#         for idx in range(0, len(new_mat)):
#             for jdx in range(0 ,len(new_mat[0])):
#                 if new_mat[idx][jdx] != init_b[idx][jdx]:
#                     ccnt += 1
#         if ccnt < min_val:
#             min_val = ccnt
#
# print(min_val)

# # 1436 영화감독 숌
# idx = 666
# N = 1
# n = int(input())
#
# while True:
#     if N == n:
#         break
#
#     idx += 1
#
#     if '666' in str(idx):
#         N += 1
#
# print(idx)