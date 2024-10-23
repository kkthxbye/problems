from typing import Iterable, Tuple


def fizzbuzz(seq: Iterable, substitutions: Tuple[Tuple[int, str]] = ((3, 'Fizz'), (5, 'Buzz'))) -> Iterable[str]:
    return (''.join(
        repl for divisor, repl in substitutions
        if i % divisor == 0
    ) or str(i) for i in seq)
