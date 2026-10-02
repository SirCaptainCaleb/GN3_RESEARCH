# Three noninsertable vertices on one path yield a four-vertex configuration or an interval path

**Summary:** Three noninsertable vertices on one path yield a four-vertex configuration or an interval path.

## Statement

Let B=(b_1,...,b_m) be a tight path in a boundary tournament, and let x,y,z be three distinct vertices outside B, each noninsertable into every position of the displayed order B. Then at least one of the following holds: (1) for one label w in {x,y,z}, a first-type failed-insertion window on w is either a Hamiltonian four-set or the cyclic non-Hamiltonian four-vertex configuration from smallset01, whose every one-vertex extension is Hamiltonian; (2) two labels have second-type obstructions at the same displayed gap, and together with that gap edge form a Hamiltonian four-set; (3) two labels have second-type obstruction gaps separated by at least one intervening gap, and are joined by a tight connector through the displayed interval between those gaps. In particular three noninsertable labels cannot produce only adjacent-gap cross residues.

## Body

Apply the failed-insertion normal form insert01 separately to x,y,z. If any label has alternative 1, apply 0425e03e2aa3 to its local four-vertex window. This gives outcome (1).

Assume therefore that all three labels have alternative 2. Let their obstruction gaps have indices i,j,k and sort them so i<=j<=k. If two indices coincide, the same-gap case of 36fccff06d48 gives a Hamiltonian four-set consisting of the two corresponding exterior labels and the two vertices of that displayed gap, yielding outcome (2). If all three indices are distinct, then i<j<k and k>=i+2. The separated-gap case of 36fccff06d48 applied to the labels at gaps i and k gives the tight connector from the first label through b_{i+1},...,b_k to the second, yielding outcome (3). These alternatives exhaust the failed-insertion normal forms.

## Metadata

- ID: three_noninsertables_finite_menu01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
