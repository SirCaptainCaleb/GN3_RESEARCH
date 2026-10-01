# Four common middle-path locks eliminate the adjacent-gap-only residue

## Statement

Assume the hypotheses of fixed_endpoint_matching_oriented_obstructions01. Then at least one of the following holds: (1) some x in X has a first-type insertion obstruction on M, whose associated four-set is Hamiltonian or is the cyclic non-Hamiltonian four-set from 0425e03e2aa3; (2) two labels of X have second-type obstructions at the same displayed gap of M, and together with that gap edge form a Hamiltonian four-set; (3) two labels of X have second-type obstruction gaps separated by at least one intervening gap, and they are joined by the tight path supplied by 36fccff06d48 through the corresponding interval of M. In particular the fixed-endpoint perfect-matching residue cannot terminate with only adjacent-gap cross configurations among the four short-side labels.

## Body

By fixed_endpoint_matching_oriented_obstructions01, all four vertices of X are noninsertable into the same displayed tight path M. Apply the failed-insertion normal form in insert01 to each of the four labels. If any label has a first-type obstruction, 0425e03e2aa3 gives outcome (1). Assume therefore that all four labels have second-type obstruction gaps. If two gap indices coincide, the same-gap case of 36fccff06d48 gives outcome (2). Otherwise the four gap indices are distinct. Ordering them i_1<i_2<i_3<i_4 gives i_4>=i_1+3, hence in particular i_4>=i_1+2. Applying the separated-gap case of 36fccff06d48 to the labels at i_1 and i_4 gives outcome (3). Thus the adjacent-gap case may occur for an individual pair but cannot be the only obstruction pattern across four simultaneously noninsertable labels.
