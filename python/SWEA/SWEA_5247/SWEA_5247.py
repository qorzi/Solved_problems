import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = set() # 리스트보다 셋이 빠름, 셋 안에는 튜플만 들어감
    total = []
    cnt = -1
    ans = 0

    start = [[N, cnt]]
    while start:
        print('start', start)
        current = start.pop(0)
        cnt = current.pop()
        cnt += 1
        current_num = len(current)
        print('->', current, '카운트', cnt)
        for _ in range(current_num):
            tmp = []
            now = current.pop(0)
            visited.add(now)
            print('visited', now, '->', visited)

            if now == M:
                ans = cnt
                start = []
                break

            # d -> +1, -1, *2, -10
            for j in range(4):
                if j == 0:
                    go = now + 1
                elif j == 1:
                    go = now - 1
                elif j == 2:
                    go = now * 2
                elif j == 3:
                    go = now - 10

                if (go not in visited) and go >= 1:
                    tmp.append(go)
            if tmp:
                tmp = list(set(tmp))
                tmp.append(cnt)
                print(now, '경로', tmp,'마지막은 카운트')
                start.append(tmp)

    print('#{} {}'.format(tc, ans))