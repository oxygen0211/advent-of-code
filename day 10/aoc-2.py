import copy

input = [
38,
23,
31,
16,
141,
2,
124,
25,
37,
147,
86,
150,
99,
75,
81,
121,
93,
120,
96,
55,
48,
58,
108,
22,
132,
62,
107,
54,
69,
51,
7,
134,
143,
122,
28,
60,
123,
82,
95,
14,
6,
106,
41,
131,
109,
90,
112,
1,
103,
44,
127,
9,
83,
59,
117,
8,
140,
151,
89,
35,
148,
76,
100,
114,
130,
19,
72,
36,
133,
12,
34,
46,
15,
45,
87,
144,
80,
13,
142,
149,
88,
94,
61,
154,
24,
66,
113,
5,
73,
79,
74,
65,
137,
47
]

conbinations = [
    {
        'currentOutput': 0,
        'adapters': [],
        'finished': False
    }
]
internalAdapterJolts = max(input) + 3
done = False
possibilityCache = {}

while not done:
    for combination in conbinations:
        if combination['finished']:
            continue
        if not combination['currentOutput'] in possibilityCache.keys():
            possibleAdapters = []
            for jolts in input:
                joltDiff = jolts - combination['currentOutput']
                if joltDiff > 0 and joltDiff <= 3:
                    possibleAdapters.append(jolts)
            combination['currentOutput'] = possibleAdapters
        else:
            possibleAdapters = combination['currentOutput']

        if len(possibleAdapters) <= 0:
            combination['finished'] = True
            continue

        changeableCombinations = [combination]
        for i in range(1, len(possibleAdapters)):
            changeableCombinations.append(copy.deepcopy(combination))

        for i, comb in enumerate(changeableCombinations):
            adapter = possibleAdapters[i]
            comb['adapters'].append(adapter)
            comb['currentOutput'] = adapter

            if comb['currentOutput'] >= internalAdapterJolts - 3:
                combination['finished'] = True
            if i > 0:
                conbinations.append(comb)

    done = True
    for combination in conbinations:
        done = done and combination['finished']

    print('{} combinations. Done? {}'.format(len(conbinations), done))
print(len(conbinations))
