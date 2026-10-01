# A trapped five-side yields an equal-Phi pairwise repartition or a displayed-edge reversal

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover that is Phi-minimal in a trapped pairwise-repartition component, with |X|=5 and |P|,|Q|>=7. Then at least one of the following holds:

(1) there is a legal pairwise repartition preserving the component-order multiset and Phi, obtained by exchanging one vertex x of X with a displayed endpoint of P or Q;

(2) some tight triple reverses a displayed edge of one of the two long components P,Q.

Thus the no-swap five-side residue is already a standard reversed-edge disturbance.

## Body

Apply the certified five-side two-sided-lock theorem astra003fivetwosidedlock.

Its first alternative is exactly (1). Otherwise there are a vertex x in X and one of the long components R=(r_1,...,r_m) such that x is noninsertable into every position of the displayed order of R.

Apply acdec36ae3ca to this displayed path R and exterior vertex x. Since every displayed insertion position fails, that theorem gives a tight triple reversing one displayed edge of R. This is alternative (2).

No further use of the detailed failed-insertion alternatives is needed.
