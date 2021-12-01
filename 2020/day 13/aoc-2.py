input = '7,13,x,x,59,x,31,19'

buses = []
for i,bus in enumerate(input.split(',')):
    if bus != 'x':
        bus = int(bus)
    buses.append(bus)

def checkForCascade(buses, referenceDep):

    for bus in buses:
        print('checking if bus {} has departure one minute after {}'.format(bus, referenceDep))
        print('{} + 1 % {} = {}'.format(referenceDep, bus, (referenceDep + 1) % bus))
        if (referenceDep + 1) % bus != 0:
            return False
        print('Match for bus {}'.format(bus))
        referenceDep += 1

    return True

buses = sorted(buses)
i = 0
cascadeFound = False

increase = min(buses)
buses = buses[1:]
#timestamp = 0
#print('Checking buses {}, increase: {}'.format(buses, increase))
#while not cascadeFound:
#    timestamp = i * increase
#    cascadeFound = checkForCascade(buses, timestamp)
#    i += 1
#print('Found cascade at timestamp {}'.format(timestamp))

timestamp = 1068781
print('Does known cascade work? {}'.format(checkForCascade(buses, timestamp)))
