import collections

def solution(data, n):
    if len(data) >= 100:
        return None, None
    occurrences = collections.Counter(data)
    return [k for k in data if occurrences[k] <= n]
