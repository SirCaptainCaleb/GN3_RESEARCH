# At path order seven the saturated endpoint shell forces an internal three-leaf transport clique

## Statement

Under the preceding locally minimal four-side setup, suppose |P|=7. Let R=(p_2,...,p_6), so R is a Hamiltonian five-set. Then there are r in R and a set X' subset X with |X'|>=3 such that, with D=R-{r}, every D union {x} for x in X' is a Hamiltonian five-set with non-Hamiltonian path-cover-two complement. Hence for every distinct x,y in X', the two leaves D+x and D+y share the four-core D and their six-set D union {x,y} carries the common-four-core transport dichotomy of 1000476. Thus the first long-path boundary m=7 collapses to a positioned three-leaf transport clique on four consecutive interior vertices.

## Body

When m=7, the interior R=(p_2,...,p_6) has order five and is a Hamiltonian five-set. By the saturated endpoint-shell lemma, R union {x} is non-Hamiltonian for every x in X.

Apply fivebadextensioncore01 to the Hamiltonian five-set R with exterior-label family X. Since all four six-set extensions R+x are non-Hamiltonian, there is a vertex r in R such that D=R-{r} satisfies
D union {x} Hamiltonian
for at least ceil(3*4/5)=3 labels x in X. Let X' be those labels.

Every D+x is a proper Hamiltonian five-set in a minimum counterexample, hence its complement is non-Hamiltonian with path-cover number two. For distinct x,y in X', the two Hamiltonian five-sets D+x and D+y share exactly the four-core D. Therefore 1000476 applies to their union D+{x,y}, giving its certified common-four-core six-set dichotomy and associated path-cover-two transport package. Since |X'|>=3, these packages occur on every edge of a three-leaf clique.
