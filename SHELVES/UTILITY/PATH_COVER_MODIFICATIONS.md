# Path-cover modification and comparison lemmas

## 1. Exterior barriers at Hamilton path ends

### Proposition 1.1

Let \`H\` be a boundary tournament, let \`X\subsetneq V(H)\` induce a Hamiltonian boundary tournament, and let \`D\subseteq V(H)-X\` be nonempty. Assume \`H[X\cup\{d\}]\` is non-Hamiltonian for every \`d\in D\`.

If some Hamilton path of \`H[X]\` begins with \`(u,v)\`, then \`(v,u,d)\` is tight for every \`d\in D\`.

If some Hamilton path of \`H[X]\` ends with \`(u,v)\`, then \`(d,v,u)\` is tight for every \`d\in D\`.

Consequently no ordered pair \`(u,v)\` can begin a Hamilton path of \`H[X]\` while \`(v,u)\` ends a Hamilton path of \`H[X]\`.

**Proof.**
Let \`P\` be a Hamilton path of \`H[X]\` beginning with \`(u,v)\`, and fix \`d\in D\`. If \`(d,u,v)\` were tight, prepending \`d\` to \`P\` would give a Hamilton path of \`H[X\cup\{d\}]\`, contrary to hypothesis. Boundary antisymmetry therefore gives \`(v,u,d)\` tight.

Dually, if \`Q\` is a Hamilton path of \`H[X]\` ending with \`(u,v)\` and \`(u,v,d)\` were tight, appending \`d\` would give a Hamilton path of \`H[X\cup\{d\}]\`. Hence \`(d,v,u)\` is tight.

If \`(u,v)\` begins one Hamilton path and \`(v,u)\` ends another, the first conclusion gives \`(v,u,d)\` while the second, applied to the terminal pair \`(v,u)\`, gives \`(d,u,v)\`; these are reverses, a contradiction. ∎

## 2. Cutting one path and adjoining the other two components

### Proposition 2.1

Let \`H\` satisfy \`pc(H)>2\`, and let
\`M=(m_0,\ldots,m_t)\mid A=(a_0,\ldots,a_r)\mid B=(b_0,\ldots,b_s)\`
be a spanning three-path cover by nonempty tight paths.

For every \`0\le i<t\`, consider the two spanning vertex sequences
\`M[0,i]A\` and \`BM[i+1,t]\`.
Every consecutive triple in these sequences is inherited from \`M,A,B\` except possibly the following present triples:
\`(m_{i-1},m_i,a_0)\` when \`i\ge1\`,
\`(m_i,a_0,a_1)\` when \`r\ge1\`,
\`(b_{s-1},b_s,m_{i+1})\` when \`s\ge1\`,
and \`(b_s,m_{i+1},m_{i+2})\` when \`i+2\le t\`.
At least one present triple is non-tight.

The same statement holds after interchanging \`A\` and \`B\`.

**Proof.**
The two displayed vertex sequences are disjoint and span \`V(H)\`. Every consecutive triple lying wholly inside \`M\`, \`A\`, or \`B\` is inherited and tight. At the join from \`M[0,i]\` to \`A\`, the only possible new triples are \`(m_{i-1},m_i,a_0)\` and \`(m_i,a_0,a_1)\` when they exist. At the join from \`B\` to \`M[i+1,t]\`, the only possible new triples are \`(b_{s-1},b_s,m_{i+1})\` and \`(b_s,m_{i+1},m_{i+2})\` when they exist.

If all present new triples were tight, both spanning sequences would be tight paths and would form a spanning two-path cover of \`H\`, contrary to \`pc(H)>2\`. Interchanging \`A,B\` gives the symmetric statement. ∎

## 3. Two-sided concatenation obstruction

### Proposition 3.1

Let \`H\` be a boundary tournament with \`pc(H)>2\` and let
\`V(H)=V(A)\sqcup W\sqcup V(B)\`,
where \`A,B\` are nonempty tight paths and \`W\` has a cover \`P\mid Q\` by two nonempty tight paths.

Then either neither \`AP\` nor \`AQ\` is tight, or neither \`PB\` nor \`QB\` is tight.

**Proof.**
Suppose \`A\` concatenates with one of \`P,Q\`, say \`P\`. If \`B\` concatenates after \`Q\`, then \`AP\mid QB\` is a spanning two-path cover of \`H\`. If \`B\` concatenates after \`P\`, then \`APB\mid Q\` is a spanning two-path cover. Both are impossible. Therefore, once one left concatenation exists, no right concatenation exists with either middle path. The same argument with left and right interchanged proves the dichotomy. ∎

## 4. Comparing nested deletion covers

### Proposition 4.1

Let \`K\` be a boundary tournament with \`pc(K)>2\`, let \`a,b\` be distinct vertices, let \`F=P\mid Q\` be an exact two-path cover of \`K-a\` in which the component containing \`b\` is nontrivial, and let \`T=R\mid S\` be an exact two-path cover of \`K-\{a,b\}\`.

If \`b\` is an endpoint of its component in \`F\`, let \`c\` be its path neighbor. If that component begins \`(b,c,\ldots)\`, then \`(c,b,a)\` is tight. If it ends \`(\ldots,c,b)\`, then \`(a,b,c)\` is tight.

If \`b\` is internal in its component in \`F\`, then deleting \`b\` from \`F\` gives an exact three-path cover of \`K-\{a,b\}\`, and some ordinary edge of \`T\` has endpoints in two different components of \`F-b\`.

**Proof.**
Suppose first that \`b\` is an endpoint of its component in \`F\`. Because the component is nontrivial, it has a path neighbor \`c\`.

If the component begins \`(b,c,\ldots)\` and \`(a,b,c)\` were tight, prepending \`a\` would enlarge that component to a tight path and, together with the other component of \`F\`, would give a spanning two-path cover of \`K\`. Hence \`(a,b,c)\` is non-tight and \`(c,b,a)\` is tight.

If the component ends \`(\ldots,c,b)\`, the same argument shows that \`(c,b,a)\` cannot be tight, since appending \`a\` would two-cover \`K\`; hence \`(a,b,c)\` is tight.

Now suppose \`b\` is internal in its component of \`F\`. Deleting \`b\` splits that component into two nonempty tight subpaths, while the other component of \`F\` remains nonempty. Thus \`F-b\` is an exact three-path cover of \`K-\{a,b\}\`. By \`TOOLKIT/COVER_COMPARISON.md\` Section 1, some ordinary edge of the exact two-path cover \`T\` has endpoints in two distinct components of \`F-b\`. ∎

## 5. Endpoint alternatives after deleting two vertices

### Proposition 5.1

Let \`K\` be a boundary tournament with \`pc(K)>2\`, let \`a,b\` be distinct vertices, and let \`T=P\mid Q\` be an exact two-path cover of \`K-\{a,b\}\`. If \`P=(p_0,\ldots,p_r)\` with \`r\ge1\`, then each of the following disjunctions holds:

1. \`(p_0,b,a)\` or \`(p_1,p_0,b)\` is tight;
2. \`(p_0,a,b)\` or \`(p_1,p_0,a)\` is tight;
3. \`(a,p_r,p_{r-1})\` or \`(b,a,p_r)\` is tight;
4. \`(b,p_r,p_{r-1})\` or \`(a,b,p_r)\` is tight.

**Proof.**
Prepend \`(a,b)\` to \`P\`. The only new consecutive triples are \`(a,b,p_0)\` and \`(b,p_0,p_1)\`. They cannot both be tight, since otherwise the enlarged path together with \`Q\` would two-cover \`K\`. Reversing a non-tight triple gives \`(p_0,b,a)\` or \`(p_1,p_0,b)\`. Prepending \`(b,a)\` gives the second disjunction.

Appending \`(a,b)\` to \`P\` creates exactly the two possible new triples \`(p_{r-1},p_r,a)\` and \`(p_r,a,b)\`; reversing a non-tight one gives \`(a,p_r,p_{r-1})\` or \`(b,a,p_r)\`. Appending \`(b,a)\` gives the fourth disjunction. ∎
