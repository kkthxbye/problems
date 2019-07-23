def cons(a, b):
    """Construct a pair."""
    def pair(f):
        return f(a, b)
    return pair


def car(c):
    """Return the first element of the pair."""
    return c(container)[0]


def cdr(c):
    """Return the last element of the pair."""
    return c(container)[1]


def container(*args):
    """Get container for cons product."""
    return tuple(args)
