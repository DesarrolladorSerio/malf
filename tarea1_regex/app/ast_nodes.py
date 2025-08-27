from dataclasses import dataclass

@dataclass
class RegexNode:
    pass

@dataclass
class Literal(RegexNode):
    symbol: str

@dataclass
class Epsilon(RegexNode):
    pass

@dataclass
class EmptySet(RegexNode):
    pass

@dataclass
class Concat(RegexNode):
    left: RegexNode
    right: RegexNode

@dataclass
class Union(RegexNode):
    left: RegexNode
    right: RegexNode

@dataclass
class Star(RegexNode):
    node: RegexNode
