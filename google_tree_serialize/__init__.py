from json import dumps, loads
from typing import Any, NamedTuple, Optional


class Node(NamedTuple):  # noqa
    val: Any
    left: Optional['Node'] = None
    right: Optional['Node'] = None


def serialize(node: Node) -> str:
    return dumps({**{
        'val': node.val,
    }, **{k: serialize(v) for k, v in [
        ('left', node.left),
        ('right', node.right),
    ] if v is not None}})


def deserialize(s: Optional[str]) -> Optional[Node]:
    if s is None:
        return None
    values = loads(s)
    return Node(values.get('val'), deserialize(values.get('left')), deserialize(values.get('right')))
