# Extremal total cut defect in the Hamiltonian regular design

## Composition

(none yet)

## Development

In the Hamiltonian regular-cut state of root 55, let Delta be the total Johnson cut defect from root 52. If h_i is the overlap of consecutive cuts and a_i records whether the next cycle coordinate is already present one cut early, then Delta_i = p-1-h_i+a_i. Reading the regular incidence matrix by columns, let r_j be the number of cyclic runs of ones in column j and let b_j record whether row j-2 also contains coordinate j. Then Delta = sum_j (r_j-1+b_j). For p at least 2 every column contributes at least one: if r_j is at least 2 this is immediate, while if r_j=1 the unique run ends at mandatory row j-1 and has length at least 2, forcing b_j=1. Hence Delta is at least n. For p=1 every column has only its mandatory one, Delta=0, and the cuts are exactly the one-token Johnson cycle L_i={x_{i+1}}. Therefore no Hamiltonian regular obstruction has total defect strictly between 0 and n. Equality Delta=n forces every column to be extremal: either one consecutive run ending at j-1, or exactly two runs with b_j=0.
