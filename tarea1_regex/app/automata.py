from dataclasses import dataclass
from typing import Dict, Set, Tuple, Optional

Symbol = str
State = int
EPS = '_'  # salida para epsilon

@dataclass
class AFND:
    start: State
    finals: Set[State]
    transitions: Dict[Tuple[State, Optional[Symbol]], Set[State]]  # (state, symbol|None) -> set
    sigma: Set[Symbol]
    states: Set[State]

    def add_transition(self, s: State, sym: Optional[Symbol], t: State):
        key = (s, sym)
        self.transitions.setdefault(key, set()).add(t)
        self.states.add(s); self.states.add(t)

    def to_pretty(self) -> str:
        K = "{" + ",".join(f"q{i}" for i in sorted(self.states)) + "}"
        Sigma = "{" + ",".join(sorted(self.sigma)) + "}"
        parts = []
        for (s, sym), targets in sorted(self.transitions.items(), key=lambda x: (x[0][0], '' if x[0][1] is None else x[0][1])):
            sym_out = EPS if sym is None else sym
            for t in sorted(targets):
                parts.append(f"(q{s},{sym_out},q{t})")
        Delta = "{"+",".join(parts)+"}"
        s = f"q{self.start}"
        F = "{" + ",".join(f"q{i}" for i in sorted(self.finals)) + "}"
        return f"""AFND M:

K={K}

Sigma={Sigma}

Delta:{Delta}

s={s}

F={F}
"""

@dataclass
class AFD:
    start: State
    finals: Set[State]
    transitions: Dict[Tuple[State, Symbol], State]
    sigma: Set[Symbol]
    states: Set[State]

    def move(self, s: State, a: Symbol) -> Optional[State]:
        return self.transitions.get((s, a))

    def to_pretty(self) -> str:
        K = "{" + ",".join(f"q{i}" for i in sorted(self.states)) + "}"
        Sigma = "{" + ",".join(sorted(self.sigma)) + "}"
        parts = []
        for (s, sym) in sorted(self.transitions.keys(), key=lambda x: (x[0], x[1])):
            t = self.transitions[(s, sym)]
            parts.append(f"(q{s},{sym},q{t})")
        delta = "{\n\n" + ",\n".join(parts) + "\n\n}"
        s = f"q{self.start}"
        F = "{" + ",".join(f"q{i}" for i in sorted(self.finals)) + "}"
        return f"""AFD M:\n\nK={K}\n\nSigma={Sigma}\n\ndelta:{delta}\n\ns={s}\n\nF={F}\n"""
