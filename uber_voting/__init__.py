from collections import defaultdict
from csv import reader
from typing import Dict, Set, TextIO


def top(in_file: TextIO, n: int = 3):
    seen_voters: Set[str] = set()
    candidate_votes_count: Dict[str, int] = defaultdict(lambda: 0)
    for voter_id, candidate_id in reader(in_file):
        if voter_id in seen_voters:
            raise Exception(f'{voter_id} has cast more than one vote')
        seen_voters.add(voter_id)
        candidate_votes_count[candidate_id] += 1

    return [c_id for c_id, _ in sorted(
        candidate_votes_count.items(),
        key=lambda x: x[1],
        reverse=True,
    )][:n]
