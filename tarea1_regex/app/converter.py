from typing import Dict, Set, Tuple, Optional, FrozenSet
from .automata import AFND, AFD

def epsilon_closure(afnd: AFND, states: Set[int]) -> Set[int]:
    stack = list(states)
    closure = set(states)
    while stack:
        s = stack.pop()
        for (p, sym), targets in afnd.transitions.items():
            if p == s and sym is None:
                for t in targets:
                    if t not in closure:
                        closure.add(t)
                        stack.append(t)
    return closure

def move(afnd: AFND, states: Set[int], a: str) -> Set[int]:
    out = set()
    for s in states:
        out.update(afnd.transitions.get((s, a), set()))
    return out

def afnd_to_afd(afnd: AFND) -> AFD:
    sigma = set(afnd.sigma)
    start_set = frozenset(epsilon_closure(afnd, {afnd.start}))
    dfa_states = {start_set: 0}
    finals: Set[int] = set()
    transitions: Dict[Tuple[int, str], int] = {}
    unmarked = [start_set]
    next_id = 1

    def is_final(state_set: Set[int]) -> bool:
        return any(s in afnd.finals for s in state_set)

    if is_final(set(start_set)):
        finals.add(0)

    while unmarked:
        T = unmarked.pop()
        T_id = dfa_states[T]
        for a in sigma:
            U = epsilon_closure(afnd, move(afnd, set(T), a))
            U_f = frozenset(U)
            if not U_f:
                continue
            if U_f not in dfa_states:
                dfa_states[U_f] = next_id
                if is_final(set(U_f)):
                    finals.add(next_id)
                unmarked.append(U_f)
                next_id += 1
            transitions[(T_id, a)] = dfa_states[U_f]

    # completar sumidero
    sink_id = None
    for dfa_id in range(len(dfa_states)):
        for a in sigma:
            if (dfa_id, a) not in transitions:
                if sink_id is None:
                    sink_id = next_id; next_id += 1
                transitions[(dfa_id, a)] = sink_id
    if sink_id is not None:
        for a in sigma:
            transitions[(sink_id, a)] = sink_id

    states = set(range(next_id))
    return AFD(start=0, finals=finals, transitions=transitions, sigma=sigma, states=states)
