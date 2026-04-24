import numpy as np

data = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No'],
    ['Sunny','Warm','High','Strong','Cool','Change','Yes']
]

S = ['0'] * 6
G = [['?' for _ in range(6)]]

for row in data:
    attributes = row[:-1]
    label = row[-1]

    if label == 'Yes':
        for i in range(len(S)):
            if S[i] == '0':
                S[i] = attributes[i]
            elif S[i] != attributes[i]:
                S[i] = '?'

        G = [g for g in G if all(g[i] == '?' or g[i] == S[i] for i in range(len(S)))]

    else:
        new_G = []
        for g in G:
            for i in range(len(S)):
                if g[i] == '?':
                    if attributes[i] != S[i]:
                        new_h = g.copy()
                        new_h[i] = S[i]
                        new_G.append(new_h)
        G = new_G

print("Final Specific Hypothesis S:", S)
print("Final General Hypothesis G:", G)