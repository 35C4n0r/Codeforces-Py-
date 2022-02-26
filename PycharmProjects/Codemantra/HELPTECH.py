x_l = []
p_l = []
m_l = []
result = []
ind_l = []
for _ in range(int(input())):
    for i in range(int(input())):
        x, p, m = list(map(str, input().split()))
        x_l.append(x)
        p_l.append(p)
        m_l.append(m)
        average = sum(m_l) / len(m_l)
        for marks in m_l:
            if marks < average:
                



