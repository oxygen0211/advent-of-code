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

currentOutput = 0
differences = []
internalAdapterJolts = max(input) + 3

while len(input) > 0:
    possibleAdapters = []
    for jolts in input:
        joltDiff = jolts - currentOutput
        if joltDiff > 0 and joltDiff <= 3:
            possibleAdapters.append(jolts)

    nextAdapter = min(possibleAdapters)
    differences.append(nextAdapter - currentOutput)
    currentOutput = nextAdapter
    input.remove(nextAdapter)

print('Sorted Adapters. Differences: {}'.format(differences))
differences.append(internalAdapterJolts - currentOutput)

diff1Count = 0
diff3Count = 0
for diff in differences:
    if diff == 1:
        diff1Count += 1

    elif diff == 3:
        diff3Count += 1

print('{} differences of 1, {} differences of 3 -> output value: {}'.format(diff1Count, diff3Count, diff1Count * diff3Count))
