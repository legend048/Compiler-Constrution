from First_12 import compute_first

def compute_follow(grammar, start):
    first = compute_first(grammar)
    follow = {nt: set() for nt in grammar}
    follow[start].add('$')
    eps = 'ε'
    changed = True
    while changed:
        changed = False
        for nt, productions in grammar.items():
            for prod in productions:
                for i, sym in enumerate(prod):
                    if sym not in grammar:
                        continue
                    before = len(follow[sym])
                    beta = prod[i + 1:]
                    nullable = True
                    for b in beta:
                        if b in grammar:
                            follow[sym] |= {x for x in first[b] if x != eps}
                            if eps not in first[b]:
                                nullable = False
                                break
                        else:
                            follow[sym].add(b)
                            nullable = False
                            break
                    if not beta or nullable:
                        follow[sym] |= follow[nt]
                    changed |= len(follow[sym]) != before
    return follow

grammar = {
    'E': [['T', "E'"]],
    "E'": [['+', 'T', "E'"], ['ε']],
    'T': [['F', "T'"]],
    "T'": [['*', 'F', "T'"], ['ε']],
    'F': [['(', 'E', ')'], ['id']]
}

print("Grammar:")
for nt in sorted(grammar):
    print(f"{nt} → {' | '.join(' '.join(prod) for prod in grammar[nt])}")

first = compute_first(grammar)
follow = compute_follow(grammar, 'E')
print("\nFIRST Sets:")
for nt in sorted(first):
    print(f"{nt}: {{{', '.join(sorted(first[nt]))}}}")
print("\nFOLLOW Sets:")
for nt in sorted(follow):
    print(f"{nt}: {{{', '.join(sorted(follow[nt]))}}}")
