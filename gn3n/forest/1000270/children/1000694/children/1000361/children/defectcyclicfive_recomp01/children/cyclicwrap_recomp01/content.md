# Proper minimum-span cyclic defect types except the five-run split into single-wrap and double-wrap geometry

## Statement

Let H be a minimum counterexample with minimum defect span three and proper cyclic defect graph Gamma, excluding the five-run type. Then every remaining type is either single-wrap or double-wrap. The single-wrap types are {1,1,1} and {3,1} in the linear 111 branch. The double-wrap types are {2,1,1}, {3,2}, and {3,1} in the linear 101 branch; in every double-wrap case the reversed wrap triples form the tight four-path S=(v_2,v_1,v_n,v_{n-1}) and H-S has path-cover number two.

## Body

By the certified five-type classification, the proper possibilities are {1,1,1},{2,1,1},{3,1},{3,2},{5}. Excluding {5}, compare deletion of the original cut vertex with the linear 101 or 111 defect pattern. The cut removes exactly one wrap defect in {1,1,1} and in {3,1} arising from 111, and exactly two wrap defects in {2,1,1},{3,2}, and {3,1} arising from 101. These are precisely the single-wrap and double-wrap cases. In a double-wrap case, boundary antisymmetry reverses the two failed wrap triples into two consecutive tight triples, so S=(v_2,v_1,v_n,v_{n-1}) is a tight four-path. Since S is a proper Hamiltonian support, the minimum-counterexample deletion property gives pc(H-S)=2.
