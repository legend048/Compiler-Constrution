from First_12 import compute_first

def compute_follow(grammar, start):
    first = compute_first(grammar)
    follow = {nt: set() for nt in grammar}
    eps = 'ε'
    follow[start].add('$')
    changed = True
    while changed:
        changed = False
        for nt, productions in grammar.items():
            for prod in productions:
                for i, symbol in enumerate(prod):
                    if symbol in grammar:
                        beta = prod[i + 1:]
                        before = follow[symbol].copy()
                        for b in beta:
                            if b in grammar:
                                follow[symbol] |= {x for x in first[b] if x != eps}
                                if eps not in first[b]:
                                    break
                            else:
                                follow[symbol].add(b)
                                break
                        else:
                            follow[symbol] |= follow[nt]

                        if not beta:
                            follow[symbol] |= follow[nt]
                        if follow[symbol] != before:
                            changed = True
    return follow

grammar = {
    'E': [['T', "E'"]],
    "E'": [['+', 'T', "E'"], ['ε']],
    'T': [['F', "T'"]],
    "T'": [['*', 'F', "T'"], ['ε']],
    'F': [['(', 'E', ')'], ['id']]
}

print("Grammar:")
for nt in sorted(grammar.keys()):
    prod_str = " | ".join([" ".join(p) for p in grammar[nt]])
    print(f"{nt} → {prod_str}")

first = compute_first(grammar)
print("\nFIRST Sets:")
for nt in sorted(first.keys()):
    print(f"{nt}: {{{', '.join(sorted(first[nt]))}}}")

follow = compute_follow(grammar, 'E')
print("\nFOLLOW Sets:")
for nt in sorted(follow.keys()):
    print(f"{nt}: {{{', '.join(sorted(follow[nt]))}}}")
