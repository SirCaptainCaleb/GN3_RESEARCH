# Proper tight cycles induce cyclic endpoint-barrier systems

Exploit a proper vertex-simple tight cycle by opening it at every cycle edge and comparing those Hamilton orders against a fixed two-cover of the complement. Each failed concatenation forces a local reverse barrier; study the cyclic pattern of these barriers for a forced endpoint reversal, bounded mixed Hamiltonian support, or defect compression.

Let C=(c_0,...,c_{r-1}) be a proper vertex-simple tight cycle in a minimum counterexample H, with indices modulo r. Opening C after any cycle edge gives a Hamilton path on V(C). Since V(C) is the support of a proper tight path, H-V(C) is non-Hamiltonian with path-cover number two; fix a two-cover P|Q.

Write P=(p_0,...,p_s), with s>=1. For every i, the Hamilton order on C ending with (c_i,c_{i+1}) cannot concatenate with P at p_0 and then Q. Hence at least one of
(c_i,c_{i+1},p_0), (c_{i+1},p_0,p_1)
is non-tight. By boundary reversal, for every i at least one of
(p_0,c_{i+1},c_i), (p_1,p_0,c_{i+1})
is tight.

Similarly, the Hamilton order on C beginning with (c_i,c_{i+1}) cannot be appended after P and paired with Q. Therefore for every i at least one of
(c_i,p_s,p_{s-1}), (c_{i+1},c_i,p_s)
is tight.

Thus each endpoint edge of each complement path generates a cyclic two-choice barrier system around the entire tight cycle. The useful next question is whether a change of barrier type around the cycle forces a positioned reversal or mixed Hamiltonian four/five-set, while a constant barrier type forces a long structured family that can be combined across the two ends of P (and similarly Q). This may turn the proper-cycle residue in four_side_gap_network_disturbance01 into the same endpoint-transport menu as the reversal residue rather than treating cycles separately.
