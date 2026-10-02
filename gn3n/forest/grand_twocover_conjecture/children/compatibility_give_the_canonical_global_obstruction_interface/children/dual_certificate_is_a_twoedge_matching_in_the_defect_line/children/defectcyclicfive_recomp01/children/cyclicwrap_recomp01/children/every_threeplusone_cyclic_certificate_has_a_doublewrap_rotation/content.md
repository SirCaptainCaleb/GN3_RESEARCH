# Every three-plus-one cyclic certificate has a double-wrap rotation

## Statement

Let H be a minimum counterexample and let pi be a minimum-defect-span-three ordering whose proper cyclic defect graph Gamma has run multiset {3,1}. Then the same cyclic ordering has a cut q for which Gamma-q consists of two isolated defect edges. Hence the corresponding rotation has linear defect pattern 101, both wrap triples are non-tight, S=(v_2,v_1,v_n,v_{n-1}) is a tight four-path in that rotation, and pc(H-S)=2.

## Body

Write the three-edge run of Gamma as x_0x_1,x_1x_2,x_2x_3 and let e be the isolated defect edge. Because these are distinct cyclic runs, e is separated from the three-run by nondefect edges and is disjoint from the surviving end edge below. Cut at q=x_1 (symmetrically x_2). Then Gamma-q deletes the two incident defect edges x_0x_1 and x_1x_2, leaving x_2x_3 together with e. These are two isolated edges, so nu(Gamma-q)=2. By the cyclic defect certificate identity c(pi_q)=1+nu(Gamma-q), the rotation pi_q has contiguous-path number three and its linear defect graph is exactly the 101 pattern. Since q is internal to the three-edge run, the two cyclic defect edges incident with q are precisely the two wrap tests of the rotated linear order; thus both wrap triples are non-tight. Boundary antisymmetry reverses them to the tight triples (v_1,v_n,v_{n-1}) and (v_2,v_1,v_n), which overlap consecutively, so S=(v_2,v_1,v_n,v_{n-1}) is a tight four-path. S is a proper Hamiltonian vertex set, so the minimum-counterexample deletion calculus gives pc(H-S)=2.