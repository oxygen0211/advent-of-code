earliestDeparture = 1000390
busLines = '23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,383,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,503,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37'

busID = ''
earliestBusDep = -1

for bus in busLines.split(','):
    if bus == 'x':
        continue

    departure = int(bus)
    while departure < earliestDeparture:
        departure += int(bus)

    if earliestBusDep < 0 or departure < earliestBusDep:
        earliestBusDep = departure
        busID = bus

print('bus: {}, departure: {}'.format(busID, earliestBusDep))
waitTime = earliestBusDep - earliestDeparture
print('wait time: {}'.format(waitTime))
answer = waitTime * int(busID)
print('Puzzle answer: {}'.format(answer))
