# Local five-vertex forcing lemmas

## 1. Two exterior vertices across adjacent positions of a tight path

### Proposition 1.1

Let \`X=(x_0,\ldots,x_{m-1})\` be a tight path, let \`0\le i\le m-3\`, and let \`s,t\` be distinct vertices outside \`X\`. Suppose
\`(x_{i+1},s,x_i)\`,
\`(x_{i+1},t,x_i)\`,
\`(x_{i+2},s,x_{i+1})\`,
and
\`(x_{i+2},t,x_{i+1})\`
are all tight.

Then exactly one of
\`(x_{i+2},s,x_{i+1},t,x_i)\`
and
\`(x_{i+2},t,x_{i+1},s,x_i)\`
is a tight five-vertex path.

**Proof.**
Exactly one of \`(s,x_{i+1},t)\` and \`(t,x_{i+1},s)\` is tight.

If \`(s,x_{i+1},t)\` is tight, then
\`(x_{i+2},s,x_{i+1},t,x_i)\`
is tight, using the hypotheses \`(x_{i+2},s,x_{i+1})\` and \`(x_{i+1},t,x_i)\`.

If \`(t,x_{i+1},s)\` is tight, then
\`(x_{i+2},t,x_{i+1},s,x_i)\`
is tight, using the other two hypotheses. The two cases are exclusive by boundary antisymmetry. ∎

## 2. A five-vertex consequence of ordered matching blocks

### Proposition 2.1

Let \`b,c,r,s,u\` be distinct vertices. Suppose \`H[\{b,c,r,s\}]\` is represented by an edge order whose opposite-edge perfect matchings satisfy
\`\{bc,rs\}<\{br,cs\}<\{bs,cr\}\`.
Assume \`H[\{b,c,r,s,u\}]\` is non-Hamiltonian and \`(b,c,u)\` is tight.

Then exactly one of \`(r,u,s)\` and \`(u,s,c)\` is tight.

**Proof.**
The matching-block order gives, among others, the tight triples
\`(b,c,s)\`,
\`(s,c,r)\`,
\`(r,b,s)\`,
\`(c,s,b)\`,
\`(r,s,c)\`,
\`(b,r,c)\`,
and
\`(s,r,b)\`.

Let \`A\` denote the assertion that \`(r,u,s)\` is tight and \`B\` the assertion that \`(u,s,c)\` is tight.

If both are false, boundary antisymmetry gives \`(s,u,r)\` and \`(c,s,u)\` tight. Hence
\`(b,c,s,u,r)\`
is a Hamilton tight path, a contradiction.

Suppose both are true. Since the five-set is non-Hamiltonian, whenever two consecutive triples of a displayed five-vertex order are tight, the reverse of its third consecutive triple is forced. Applying this successively gives
\`b\,u\,s\,c\,r \Rightarrow (s,u,b)\`,
\`b\,r\,u\,s\,c \Rightarrow (u,r,b)\`,
\`c\,u\,r\,b\,s \Rightarrow (r,u,c)\`,
\`r\,u\,c\,s\,b \Rightarrow (s,c,u)\`,
\`r\,s\,c\,u\,b \Rightarrow (b,u,c)\`,
and
\`s\,u\,b\,r\,c \Rightarrow (r,b,u)\`.

Now \`(s,r,b)\`, \`(r,b,u)\`, and \`(b,u,c)\` are tight, so
\`(s,r,b,u,c)\`
is a Hamilton tight path, again a contradiction. Therefore the two assertions cannot agree, and exactly one of the two displayed triples is tight. ∎
