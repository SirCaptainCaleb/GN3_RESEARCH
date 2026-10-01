# Every quadratic-minimal size gap yields two bounded insertion obstructions

## Statement

Let C=P|Q|R be a spanning three-path cover in a trapped Astra-003 move component, chosen to minimize Phi=sum |P_i|^2, and write P=(p_0,...,p_{a-1}) with |P|=a and |Q|=b. If a>=b+2, then neither endpoint p_0 nor p_{a-1} can be inserted anywhere into the displayed tight-path order of Q. Consequently the failed-insertion theorem applies separately to p_0 and p_{a-1}: for each endpoint there is a local obstruction involving that endpoint and at most four consecutive vertices of Q.

## Body

Let C=P|Q|R be Phi-minimal in a connected Astra-003 component containing no two-cover, with P=(p_0,...,p_{a-1}), |P|=a, |Q|=b, and a>=b+2.

By 9d023d8f93d9, both induced subtournaments H[V(Q) union {p_0}] and H[V(Q) union {p_{a-1}}] are non-Hamiltonian.

Fix e in {p_0,p_{a-1}}. If e could be inserted into any of the b+1 positions of the displayed tight-path order of Q, that insertion would itself be a Hamilton tight path of H[V(Q) union {e}], contradicting non-Hamiltonicity. Hence every insertion position for e fails.

Apply insert01, Section 3, to the displayed path Q and exterior vertex e. It gives an index t and one of its two certified local obstruction alternatives; every displayed comparison in that alternative involves only e together with at most four consecutive vertices of Q.

Doing this independently for e=p_0 and e=p_{a-1} gives the two asserted bounded insertion obstructions on the same smaller component Q. No assumption on the ambient order or on b beyond the hypotheses of the failed-insertion theorem is used.
