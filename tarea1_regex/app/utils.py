
from .ast_nodes import Literal, Concat, Union, Star, Epsilon, EmptySet, RegexNode

def set_to_str(s):
    return "{" + ",".join(sorted(s)) + "}"


def collect_sigma(node: RegexNode) -> set[str]:
    if isinstance(node, Literal):
        return {node.symbol}
    if isinstance(node, (Epsilon, EmptySet)):
        return set()
    if isinstance(node, Concat) or isinstance(node, Union):
        return collect_sigma(node.left) | collect_sigma(node.right)
    if isinstance(node, Star):
        return collect_sigma(node.node)
    return set()
