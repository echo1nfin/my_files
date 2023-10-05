n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
for i in l:
	if i[2] == 0:
		print(['YES','NO'][i[0] != i[1]])
		continue
	packs = min(i[0],i[1])
	if i[0] >= 1 and i[1] >= 1 and abs(1-max(i[0], i[1])//packs) <= i[2]:
		print('YES')
	else:
		print('NO')
