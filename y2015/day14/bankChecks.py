reindeer = {}  # RUDOLPH THE RED-NOSED REINDEEEEER
with open('xOnLine.txt') as read:  # HAD A VERY SHINY NOOOOOOSE
    for line in read.readlines():
        line = line.rstrip().replace(' can fly ', ' ').replace(' km/s for ', ' ')
        line = line.replace(' seconds, but then must rest for ', ' ').replace(' seconds.', ' ').split()
        reindeer[line[0]] = [int(x) for x in line[1:]] + [0, 0, True]  # True is flying, False is resting
        # oh- and the last three are- distance travelled, time of state, and state (flying or resting)
        points = {r: 0 for r in reindeer}

reindeerTime = 2503
for _ in range(reindeerTime):
    for r in reindeer:  # for both part 1 and part 2
        if reindeer[r][-1]:
            reindeer[r][-2] += 1
            reindeer[r][-3] += reindeer[r][0]
            if reindeer[r][-2] == reindeer[r][1]:
                reindeer[r][-1] = not reindeer[r][-1]
                reindeer[r][-2] = 0
        else:
            reindeer[r][-2] += 1
            if reindeer[r][-2] == reindeer[r][2]:
                reindeer[r][-1] = not reindeer[r][-1]
                reindeer[r][-2] = 0

    for r in reindeer:  # PART 2
        if reindeer[r][-3] == max([reindeer[r][-3] for r in reindeer]):
            points[r] += 1  # i'm just assuming there's no tie at any point
            break
# this commentary is only for my test inputs though, of course
# i could do some formatting but im too lazy
print('of COURSE rudolph is the fastest...: %i' % max([reindeer[r][-3] for r in reindeer]))
print('%i lightStates for vixen... i stand corrected.' % (max(points.values())))
