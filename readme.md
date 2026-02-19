# Compiler Construction

## Helper Commands

### Running Lex

```bash
# Generate the lexer from lex source file
lex <filename>.l

# Compile the generated lexer
gcc lex.yy.c -o <filename>

# Run the lexer
./<filename>
```

### Alternative: Single Command Chain

```bash
lex <filename> && gcc lex.yy.c -o <filename> && ./<filename>
```