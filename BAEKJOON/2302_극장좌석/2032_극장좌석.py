def seating(N, VIP):
    # 각 좌석에 앉을 수 있는 경우의 수를 저장할 dp 리스트를 초기화합니다.
    # dp[i]는 i개의 연속된 일반 좌석에서 앉을 수 있는 경우의 수를 나타냅니다.
    # dp[0]과 dp[1]은 각각 1가지 방법으로 앉을 수 있으므로 1로 초기화합니다.
    dp = [0 for _ in range(N+1)]
    dp[0], dp[1] = 1, 1

    # 2부터 N까지 각각의 좌석 수에 대한 경우의 수를 계산합니다.
    # i개의 좌석에서 앉을 수 있는 경우의 수는 (i-1)개의 좌석에서 앉을 수 있는 경우의 수와
    # (i-2)개의 좌석에서 앉을 수 있는 경우의 수의 합과 같습니다.
    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    # VIP 좌석 정보에 좌석 시작과 끝을 나타내는 0과 N+1을 추가합니다.
    VIP.insert(0, 0)
    VIP.append(N+1)

    # 최종적으로 계산할 답을 저장할 변수를 1로 초기화합니다.
    answer = 1

    # 각 VIP 좌석 사이의 구간에 대해 경우의 수를 계산하고, 이를 answer에 곱합니다.
    # VIP[i] - VIP[i-1] - 1은 i번째 VIP 좌석과 (i-1)번째 VIP 좌석 사이의 일반 좌석 수를 나타냅니다.
    # 이 일반 좌석 수에 대한 경우의 수는 dp 배열에서 찾을 수 있습니다.
    for i in range(1, len(VIP)):
        answer *= dp[VIP[i] - VIP[i-1] - 1]

    # 최종적으로 계산된 답을 출력합니다.
    return answer


N = int(input())
M = int(input())
VIP = [int(input()) for _ in range(M)]
print(seating(N, VIP))
