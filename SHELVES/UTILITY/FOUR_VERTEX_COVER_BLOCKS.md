# Four-vertex structure inside an exact two-path cover

## 1. Degree and block counts

### Proposition 1.1

Let \`G\` be a boundary tournament with \`V(G)=S\sqcup Q\`, where \`|S|=4\` and \`G[S]\` is non-Hamiltonian. Let \`T\` be an exact two-path cover of \`G\` in which every vertex of \`S\` has ordinary degree two.

Put
\`e=|E(T[S])|\`,
let \`\delta\` be the number of ordinary edges of \`T\` joining \`S\` to \`Q\`,
and let \`b_Q\` be the number of nonempty components of \`T[Q]\`.

Then
\`e\in\{0,1,2\}\`,
\`\delta=8-2e\`,
and
\`b_Q=6-e\`.
Equivalently, \`(e,\delta,b_Q)\` is one of
\`(2,4,4)\`, \`(1,6,5)\`, \`(0,8,6)\`.

**Proof.**
Since \`G[S]\` is non-Hamiltonian, the path forest \`T[S]\` has at most two ordinary edges, so \`e\in\{0,1,2\}\`.

The sum of ordinary degrees over the four vertices of \`S\` is eight. Each edge of \`T[S]\` contributes two to this sum, while each edge joining \`S\` to \`Q\` contributes one. Hence
\`8=2e+\delta\`,
so \`\delta=8-2e\`.

Cut all \`\delta\` edges joining \`S\` to \`Q\`. The exact two-path forest becomes \`\delta+2\` maximal blocks lying entirely in one side. Since \`T[S]\` is a forest on four vertices with \`e\` edges, it has \`4-e\` components. Therefore
\`b_Q=(\delta+2)-(4-e)=6-e\`.
The three displayed cases follow. ∎

## 2. Alternation of the resulting blocks

### Proposition 2.1

Under the hypotheses of Proposition 1.1, contract every nonempty component of \`T[S]\` and every nonempty component of \`T[Q]\`. Every contracted component coming from \`S\` has degree two, and each of the two resulting path components alternates between components from \`Q\` and components from \`S\`, beginning and ending with a component from \`Q\`.

**Proof.**
Let \`B\` be one component of \`T[S]\`. Since \`G[S]\` is non-Hamiltonian, \`B\` has order at most three. If \`B\` is a singleton, its unique vertex has total ordinary degree two in \`T\`, so exactly two edges leave \`B\`. If \`B\` has order two, its one internal edge uses one incident edge at each endpoint, leaving exactly one outside edge at each endpoint. If \`B\` has order three, its two internal path edges leave one outside edge at each path endpoint and none at the middle vertex. Thus every contracted component coming from \`S\` has degree two.

After contracting all maximal same-side components, the two path components of the ordinary forest of \`T\` remain paths. Their vertices alternate between the two sides by maximality of the blocks. Since no contracted \`S\`-vertex has degree one, no path endpoint lies in \`S\`. Hence every contracted path begins and ends with a component from \`Q\`. ∎
