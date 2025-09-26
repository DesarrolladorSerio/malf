from typing import List, Tuple
from .automata import AFD

def find_matches(dfa: AFD, text: str) -> List[Tuple[int, str]]:
    matches = []
    n = len(text)
    for i in range(n):
        s = dfa.start
        last_accept = None
        for j in range(i, n):
            a = text[j]
            s2 = dfa.move(s, a)
            if s2 is None:
                break
            s = s2
            if s in dfa.finals:
                last_accept = j
        if last_accept is not None:
            matches.append((i, text[i:last_accept+1]))
    return matches
