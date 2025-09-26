from typing import Tuple, Set, Dict, Optional
from .ast_nodes import Literal, Epsilon, EmptySet, Concat, Union, Star, RegexNode
from .automata import AFND

class _StateCounter:
    def __init__(self):
        self.c = 0
    def next(self) -> int:
        v = self.c
        self.c += 1
        return v

def thompson(ast: RegexNode, sigma: Set[str]) -> AFND:
    counter = _StateCounter()

    def build(node: RegexNode):
        T: Dict = {}
        S: Set[int] = set()
        def add(s, sym, t):
            T.setdefault((s, sym), set()).add(t)
            S.add(s); S.add(t)

        if isinstance(node, Literal):
            s = counter.next(); f = counter.next()
            add(s, node.symbol, f)
            return s, f, T, S
        if isinstance(node, Epsilon):
            s = counter.next(); f = counter.next()
            add(s, None, f)
            return s, f, T, S
        if isinstance(node, EmptySet):
            s = counter.next(); f = counter.next()
            S.update([s, f])
            return s, f, T, S
        if isinstance(node, Concat):
            s1, f1, T1, S1 = build(node.left)
            s2, f2, T2, S2 = build(node.right)
            T = {**T1}
            for k,v in T2.items(): T.setdefault(k, set()).update(v)
            S = S1.union(S2)
            T.setdefault((f1, None), set()).add(s2)
            S.update([f1, s2])
            return s1, f2, T, S
        if isinstance(node, Union):
            s = counter.next(); f = counter.next()
            s1, f1, T1, S1 = build(node.left)
            s2, f2, T2, S2 = build(node.right)
            T = {**T1}
            for k,v in T2.items(): T.setdefault(k, set()).update(v)
            S = S1.union(S2)
            T.setdefault((s, None), set()).update({s1, s2})
            T.setdefault((f1, None), set()).add(f)
            T.setdefault((f2, None), set()).add(f)
            S.update([s, f, f1, f2, s1, s2])
            return s, f, T, S
        if isinstance(node, Star):
            s = counter.next(); f = counter.next()
            si, fi, Ti, Si = build(node.node)
            T = {**Ti}; S = set(Si)
            T.setdefault((s, None), set()).update({si, f})
            T.setdefault((fi, None), set()).update({si, f})
            S.update([s, f, si, fi])
            return s, f, T, S
        raise TypeError("Nodo AST no soportado")

    s, f, T, S = build(ast)
    return AFND(start=s, finals={f}, transitions=T, sigma=set(sigma), states=S)
