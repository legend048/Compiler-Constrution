def compute_first(grammar):
    first = {nt: set() for nt in grammar}
    eps = 'ε'
    changed = True
    while changed:
        changed = False
        for nt, productions in grammar.items():
            old_size = len(first[nt])
            for prod in productions:
                if prod == [eps]:
                    if eps not in first[nt]:
                        first[nt].add(eps)
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
            if len(first[nt]) > old_size:
                changed = True
    return first


if __name__ == '__main__':
    grammar = {
        'E': [['T', "E'"]],
        "E'": [['+', 'T', "E'"], ['ε']],
        'T': [['F', "T'"]],
        "T'": [['*', 'F', "T'"], ['ε']],
        'F': [['(', 'E', ')'], ['id']]
    }

    print("Grammar:")
    for nt in sorted(grammar):
        prod_str = " | ".join([" ".join(prod) for prod in grammar[nt]])
        print(f"{nt} → {prod_str}")

    first = compute_first(grammar)
    print("\nFIRST Sets:")
    for nt in sorted(first):
        print(f"{nt}: {{{', '.join(sorted(first[nt]))}}}")
