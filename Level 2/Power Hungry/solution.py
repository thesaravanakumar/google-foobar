def solution(xs):
    positives = list()
    negatives = list()

    for x in xs:
        if x > 0:
            positives.append(x)
        elif x < 0:
            negatives.append(x)
    if len(negatives) % 2 != 0:
        negatives.remove(max(negatives))
    if len(positives) + len(negatives) == 0:
        return str(0)
    max_power= 1
    for x in positives:
        max_power *= x
    for x in negatives:
        max_power *= x

    return str(max_power)