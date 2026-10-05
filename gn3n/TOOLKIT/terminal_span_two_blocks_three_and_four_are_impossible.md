# Terminal span-two blocks of order three or four are impossible

**Summary:** In the terminal disjoint-window span-two branch, the bridging block cannot have order three or four. Hence the only surviving block size is two.

## Statement

Assume a terminal nearest span-two witness with disjoint determining windows. Under the audited bound alpha,beta<=2 and |B|=alpha+beta, the cases |B|=3 and |B|=4 contradict boundary antisymmetry together with the fact that the four central statuses are monochromatic in every chamber.

## Body

The four status positions between the two reflected span-two witness windows avoid all six nearer local witnesses. Thus in every terminal chamber they are monochromatic; write their common value as the terminal state. For |B|=3, by symmetry take alpha=1,beta=2 and write a block order as (x,y,z). The state depends only on the singleton left support, so write it C(x). The central triples give h(x,y,z)=C(x). Reordering the same support as (x,z,y) gives h(x,z,y)=C(x). Boundary antisymmetry then gives h(y,z,x)=1-C(x). But in the chamber with B-order (y,z,x), the same central triple equals C(y). Hence C(y)=1-C(x) for every distinct x,y. On three vertices this is impossible. For |B|=4, alpha=beta=2. The state depends only on the unordered left support pair; write it C({x,y}). For every block order (x,y,z,w), a central triple gives h(x,y,z)=C({x,y}). Reversal and the order (z,y,x,w) give C({y,z})=1-C({x,y}) for every three distinct x,y,z. Thus every two edges of K4 sharing a vertex would have opposite C-colors. Taking three edges incident with one vertex gives an immediate contradiction. Therefore neither block size three nor four can occur, leaving only alpha=beta=1 and |B|=2.

## Metadata

- ID: terminal_span_two_blocks_three_and_four_are_impossible
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: passed
- Refutation: unrefuted
- Toolkit status: Limbo
