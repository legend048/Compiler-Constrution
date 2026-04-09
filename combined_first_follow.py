"""
Combined FIRST and FOLLOW Set Computation for LL(1) Parsing
This program computes both FIRST and FOLLOW sets and demonstrates 
their use in building LL(1) predictive parsing tables.
"""

def compute_first_sets(grammar):
    """Compute FIRST sets for all non-terminals"""
    first = {non_terminal: set() for non_terminal in grammar}
    epsilon = 'ε'
    
    changed = True
    while changed:
        changed = False
        for non_terminal, productions in grammar.items():
            for production in productions:
                if len(production) == 1 and production[0] in ['epsilon', 'ε', '']:
                    if epsilon not in first[non_terminal]:
                        first[non_terminal].add(epsilon)
                        changed = True
                else:
                    for symbol in production:
                        if symbol in grammar:
                            for terminal in first[symbol]:
                                if terminal != epsilon and terminal not in first[non_terminal]:
                                    first[non_terminal].add(terminal)
                                    changed = True
                            if epsilon not in first[symbol]:
                                break
                        else:
                            if symbol not in first[non_terminal]:
                                first[non_terminal].add(symbol)
                                changed = True
                            break
                    else:
                        if epsilon not in first[non_terminal]:
                            first[non_terminal].add(epsilon)
                            changed = True
    
    return first


def compute_follow_sets(grammar, start_symbol, first_sets):
    """Compute FOLLOW sets for all non-terminals"""
    follow = {non_terminal: set() for non_terminal in grammar}
    epsilon = 'ε'
    
    follow[start_symbol].add('$')
    
    changed = True
    while changed:
        changed = False
        for non_terminal, productions in grammar.items():
            for production in productions:
                for i, symbol in enumerate(production):
                    if symbol in grammar:
                        beta = production[i + 1:]
                        first_beta = set()
                        all_epsilon = True
                        
                        for sym in beta:
                            if sym in grammar:
                                for terminal in first_sets[sym]:
                                    if terminal != epsilon:
                                        first_beta.add(terminal)
                                if epsilon not in first_sets[sym]:
                                    all_epsilon = False
                                    break
                            else:
                                first_beta.add(sym)
                                all_epsilon = False
                                break
                        
                        for terminal in first_beta:
                            if terminal not in follow[symbol]:
                                follow[symbol].add(terminal)
                                changed = True
                        
                        if (all_epsilon and beta) or not beta:
                            for terminal in follow[non_terminal]:
                                if terminal not in follow[symbol]:
                                    follow[symbol].add(terminal)
                                    changed = True
    
    return follow


def get_first_of_sequence(sequence, first_sets):
    """Get FIRST of a sequence of symbols"""
    first = set()
    epsilon = 'ε'
    
    for symbol in sequence:
        if symbol in first_sets:
            for terminal in first_sets[symbol]:
                if terminal != epsilon:
                    first.add(terminal)
            if epsilon not in first_sets[symbol]:
                break
        else:
            first.add(symbol)
            break
    else:
        first.add(epsilon)
    
    return first


def build_ll1_parsing_table(grammar, start_symbol, first_sets, follow_sets):
    """Build an LL(1) predictive parsing table"""
    table = {}
    epsilon = 'ε'
    
    for non_terminal, productions in grammar.items():
        for prod_idx, production in enumerate(productions):
            # Get FIRST of the production
            first_prod = get_first_of_sequence(production, first_sets)
            
            # For each terminal in FIRST(production)
            for terminal in first_prod:
                if terminal != epsilon:
                    key = (non_terminal, terminal)
                    table[key] = (prod_idx, production)
            
            # If epsilon is in FIRST(production), use FOLLOW(non_terminal)
            if epsilon in first_prod:
                for terminal in follow_sets[non_terminal]:
                    key = (non_terminal, terminal)
                    table[key] = (prod_idx, production)
    
    return table


def print_results(grammar, start_symbol, first_sets, follow_sets):
    """Print all computation results"""
    print("\n" + "="*70)
    print("GRAMMAR")
    print("="*70)
    for nt in sorted(grammar.keys()):
        prods = grammar[nt]
        for idx, prod in enumerate(prods):
            if idx == 0:
                print(f"{nt:15} → {' '.join(prod)}")
            else:
                print(f"{'':15} | {' '.join(prod)}")
    
    print("\n" + "="*70)
    print("FIRST SETS")
    print("="*70)
    for nt in sorted(first_sets.keys()):
        terminals = sorted(first_sets[nt])
        print(f"FIRST({nt:15}) = {{ {', '.join(terminals)} }}")
    
    print("\n" + "="*70)
    print("FOLLOW SETS")
    print("="*70)
    for nt in sorted(follow_sets.keys()):
        terminals = sorted(follow_sets[nt])
        print(f"FOLLOW({nt:15}) = {{ {', '.join(terminals)} }}")
    
    # Build and display parsing table
    table = build_ll1_parsing_table(grammar, start_symbol, first_sets, follow_sets)
    
    print("\n" + "="*70)
    print("LL(1) PREDICTIVE PARSING TABLE")
    print("="*70)
    
    if not table:
        print("(Empty - Grammar may not be LL(1))")
    else:
        # Get all non-terminals and terminals for table headers
        terminals = set()
        non_terminals = sorted(grammar.keys())
        
        for (nt, term) in table.keys():
            terminals.add(term)
        
        terminals = sorted(terminals)
        
        # Print header
        header = f"{'Non-Terminal':<15} |"
        for term in terminals:
            header += f" {term:12} |"
        print(header)
        print("-" * len(header))
        
        # Print entries
        for nt in non_terminals:
            row = f"{nt:<15} |"
            for term in terminals:
                if (nt, term) in table:
                    prod_idx, production = table[(nt, term)]
                    prod_str = " ".join(production)[:10]
                    row += f" {prod_str:12} |"
                else:
                    row += f" {'':12} |"
            print(row)


# EXAMPLE 1: Expression Grammar
print("\n" + "▓"*70)
print("EXAMPLE 1: Expression Grammar (Dangling Else Problem)")
print("▓"*70)

grammar1 = {
    'E': [['T', 'E_prime']],
    'E_prime': [['+', 'T', 'E_prime'], ['ε']],
    'T': [['F', 'T_prime']],
    'T_prime': [['*', 'F', 'T_prime'], ['ε']],
    'F': [['(', 'E', ')'], ['id']]
}

first1 = compute_first_sets(grammar1)
follow1 = compute_follow_sets(grammar1, 'E', first1)
print_results(grammar1, 'E', first1, follow1)


# EXAMPLE 2: Simple Assignment Grammar
print("\n" + "▓"*70)
print("EXAMPLE 2: Simple Assignment Grammar")
print("▓"*70)

grammar2 = {
    'S': [['A', 'a', 'b'], ['b', 'a', 'c'], ['B', 'a']],
    'A': [['d']],
    'B': [['e']]
}

first2 = compute_first_sets(grammar2)
follow2 = compute_follow_sets(grammar2, 'S', first2)
print_results(grammar2, 'S', first2, follow2)


# EXAMPLE 3: Declaration Grammar
print("\n" + "▓"*70)
print("EXAMPLE 3: Declaration Grammar")
print("▓"*70)

grammar3 = {
    'program': [['decl', 'stmt']],
    'decl': [['type', 'id', ';', 'decl'], ['ε']],
    'stmt': [['id', '=', 'expr', ';'], ['if', '(', 'expr', ')', 'stmt']],
    'type': [['int'], ['float']],
    'expr': [['id'], ['num']]
}

first3 = compute_first_sets(grammar3)
follow3 = compute_follow_sets(grammar3, 'program', first3)
print_results(grammar3, 'program', first3, follow3)


# EXAMPLE 4: While Loop Grammar
print("\n" + "▓"*70)
print("EXAMPLE 4: While Loop Grammar")
print("▓"*70)

grammar4 = {
    'S': [['while', '(', 'E', ')', '{', 'S', '}'], ['assign']],
    'E': [['id', 'cond', 'id']],
    'assign': [['id', '=', 'num']]
}

first4 = compute_first_sets(grammar4)
follow4 = compute_follow_sets(grammar4, 'S', first4)
print_results(grammar4, 'S', first4, follow4)


# Interactive Mode
if __name__ == "__main__":
    print("\n" + "="*70)
    print("INTERACTIVE MODE - Enter Your Own Grammar")
    print("="*70)
    print("""
Format:
  Non-Terminal1: production1, production2, ...
  Non-Terminal2: production1, production2, ...
  
Symbols separated by spaces. Use 'ε' or 'epsilon' for epsilon.
Type 'DONE' when finished.
Example:
  E: T E_prime, (E)
  E_prime: + T E_prime, ε
  T: F T_prime, (T)
  T_prime: * F T_prime, ε
  F: ( E ), id
""")
    
    try:
        grammar = {}
        while True:
            line = input("\nEnter production (or DONE): ").strip()
            
            if line.upper() == 'DONE':
                if grammar:
                    break
                else:
                    print("Please enter at least one production.")
                    continue
            
            if ':' in line:
                parts = line.split(':')
                non_terminal = parts[0].strip()
                productions_str = parts[1].strip()
                
                productions = []
                for prod in productions_str.split(','):
                    symbols = prod.strip().split()
                    productions.append(symbols)
                
                grammar[non_terminal] = productions
        
        if grammar:
            start = input("\nEnter start symbol: ").strip()
            
            first = compute_first_sets(grammar)
            follow = compute_follow_sets(grammar, start, first)
            print_results(grammar, start, first, follow)
    
    except KeyboardInterrupt:
        print("\n\nProgram interrupted.")
