# A unique large side yields small orders or a smaller non-Hamiltonian complement

## Statement

Let H be a minimum counterexample and let P|Q|X be a globally Phi-minimal spanning three-cover with p=|P|>=q=|Q|>=c=|X|. Assume the endpoint-square alternative of twosourceblockade_recomp01 is absent and p>=q+2. Then q=c and p is c+2 or c+3. If P is globally longest, the ambient profile is one of 5|3|3 at order 11, 6|3|3 at order 12, or 7|4|4 at order 15. If P is not globally longest, then every globally longest path L has non-Hamiltonian complement of order at most 2c-1.

## Body

# Proof

By global_sizegap_maximin_bypass01, the hypotheses force q=c and p in {c+2,c+3}. Also the maximin parameter is rho=c.

If P is globally longest, apply unique_large_longest_smallorders01 to obtain exactly the three listed finite ambient profiles.

Assume P is not globally longest, and let L be any globally longest tight path. Then |L|>=p+1. Since the displayed profile has total order n=p+2c,

|V(H)-V(L)| = n-|L| <= p+2c-(p+1)=2c-1.

Because L is a proper tight path in a minimum counterexample, the minimum-counterexample complement lemma gives path-cover number two for H-V(L), and this complement cannot be Hamiltonian (otherwise L together with its Hamilton path would two-cover H). Thus L has a non-Hamiltonian complement of order at most 2c-1. ∎
