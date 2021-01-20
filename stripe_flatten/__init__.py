from typing import MutableMapping, Optional


def flatten_namespace(d: MutableMapping,
                      separator: str = '.',
                      prefix: Optional[str] = None) -> MutableMapping:
    n = {}
    for key, value in d.items():
        flattened = separator.join([prefix, key]) if prefix is not None else key
        if isinstance(value, dict):
            n.update(flatten_namespace(value, prefix=flattened))
        else:
            n[flattened] = value

    return n
