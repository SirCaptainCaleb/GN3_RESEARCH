# Adjacent insertions give a one-defect ordering on the two-label enlargement

## Statement

Let B be a tight path and let x,y be exterior vertices insertable into two adjacent positions, with x immediately before an old vertex v and y immediately after v. Then the ordering obtained by making both insertions has every consecutive triple tight except possibly (x,v,y). Consequently B union {x,y} always has a spanning two-path cover obtained by cutting at that local cross triple; if (x,v,y) is tight the combined ordering is Hamiltonian, while otherwise its unique local defect has reverse orientation (y,v,x) tight.

## Body

Write the displayed path locally as L,v,R, where x inserts in the gap immediately before v and y in the gap immediately after v. Form the combined ordering L,x,v,y,R. Any consecutive triple not containing both x and y is a consecutive triple of one of the two individually successful insertion paths, hence is tight. The only triple not certified in that way is (x,v,y). If it is tight, the whole combined ordering is a tight Hamilton path. If it is non-tight, splitting the ordering immediately before or immediately after v gives two tight paths whose supports partition B union {x,y}; all triples internal to either piece are among the already certified triples. Boundary antisymmetry also gives (y,v,x) tight. Endpoint-adjacent positions are included, with the empty prefix or suffix omitted.
