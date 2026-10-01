# Deletion-sparse longest complements reduce to pervasive three-crossing or a bounded slack bridge

## Statement

Let H be a minimum counterexample, let A be a globally longest tight path of order lambda, let U=V(H)-V(A), let D={u in U:H[U-u] is Hamiltonian}, and put sigma=2lambda-(|V(H)|-1). Assume |D|<=3. For u in U-D let kappa(u) be the minimum number of ordinary path edges crossing A|(U-u) among exact two-covers of H-u. Then kappa(u)>=2 for every u in U-D. Moreover either (I) kappa(u)>=3 for every u in U-D, or (II) for some u in U-D there is an exact two-cover T of H-u with exactly two crossings, and after cutting those crossings T has exactly two A-blocks and two (U-u)-blocks and has one of two forms: crosswise, with each component consisting of one A-block and one (U-u)-block; or a unique non-crosswise form C_1-A_1-C_2 together with the remaining A-block, where C_1 union C_2=U-u and |A_1|<=sigma. In particular all non-crosswise minimum-crossing behavior is confined to at most sigma consecutive vertices of the displayed longest path.

## Body

# Proof

For every u in U-D, the complement deletion U-u is non-Hamiltonian. The certified longest-path crossing theorem 6c4d3f1a8e27 therefore gives kappa(u)>=2.

If all kappa(u)>=3 we are in (I). Otherwise choose u with kappa(u)=2 and an exact cover T attaining this minimum. The equality analysis in 6c4d3f1a8e27 applies verbatim: cutting the two A|(U-u) crossings yields exactly two A-blocks and two (U-u)-blocks. Either the crossing edges lie in different components, giving the crosswise four-block form, or they lie in one component. The only possible non-crosswise arrangement is C_1-A_1-C_2 together with the remaining A-block, because the alternative A_1-C_1-A_2 would contain all lambda vertices of A plus a nonempty complement block and so exceed the global longest-path order. In the surviving non-crosswise form the mixed component has order |U|-1+|A_1|<=lambda, so |A_1|<=lambda-(|U|-1). Since |U|=|V(H)|-lambda, this is |A_1|<=2lambda-|V(H)|+1=sigma. ∎
