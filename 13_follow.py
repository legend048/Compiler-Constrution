def compute_first(grammar):
    first = {nt: set() for nt in grammar}
    eps = 'ε'
    changed = True
    while changed:
        changed = False
        for nt, productions in grammar.items():
            for prod in productions:
                if prod == [eps]:
                    if eps not in first[nt]:
                        first[nt].add(eps)
                        changed = True
                else:
                    for symbol in prod:
                        if symbol in grammar:
                            first[nt] |= {x for x in first[symbol] if x != eps}
                            if eps not in first[symbol]:
                                break
                        else:
                            first[nt].add(symbol)
                            break
                    else:
                        first[nt].add(eps)
                        changed = True
    return first

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
                        beta_first = set()
                        if beta:
                            if beta[0] in grammar:
                                beta_first = {x for x in first[beta[0]] if x != eps}
                            else:
                                beta_first.add(beta[0])
                        
                        follow[symbol] |= beta_first
                        if not beta or all(eps in first.get(s, set()) for s in beta
                                          if s in grammar):
                            follow[symbol] |= follow[nt]
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
