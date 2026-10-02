# Above order seventeen componentwise quadratic minima reduce to side six or a four-side six-support obstruction

## Statement

Let H be a minimum counterexample of order n>=18, and let C=A|B|D be a spanning three-cover minimizing the quadratic potential Phi within its connected pairwise-repartition component. Write a>=b>=c for the component orders.

Then at least one of the following holds:

(1) c>=6;

(2) H contains explicit order disagreement between Hamiltonian paths on overlapping induced supports;

(3) c=4, and H contains a proper Hamiltonian six-vertex support U such that H-U is non-Hamiltonian with path-cover number exactly two.

In particular, no componentwise Phi-minimum has minimum side 1,2, or 3; and a componentwise Phi-minimum with minimum side 5 necessarily forces order disagreement. Thus, in the absence of order disagreement, the only possible sub-six terminal side size is four, and every such four-side state carries a Hamiltonian-six path-cover-two obstruction.

Equivalently, every connected component of the pairwise-repartition graph has a Phi-minimal representative satisfying this trichotomy.

## Body

Let a>=b>=c be the component orders.

If c<=3, apply one_two_and_three_have_universal_onemove_descent_thresholds. Its local threshold theorem gives an immediate legal pairwise repartition with strictly smaller Phi in every possible c=1,2,3 case occurring at n>=18. This contradicts the assumed componentwise minimality of C.

Suppose c=5. Since a+b=n-5>=13, the larger of A,B has order a>=7. Apply fiveside_descent_or_disagree01 to the five-side D and the displayed path A. That theorem gives either a legal pairwise repartition of D|A with strictly smaller Phi, or explicit order disagreement. The first alternative remains in the same pairwise-repartition component as C and contradicts componentwise minimality. Hence c=5 forces order disagreement.

It remains to consider c=4. The other two displayed components A,B form a two-cover of H-D. Since n>=18, the hypotheses of by_descent_a_hamiltonian_sixwindow_or_order_disagreement hold. That theorem gives one of:
(i) an explicit spanning three-cover of strictly smaller Phi obtained from D|A|B;
(ii) a proper Hamiltonian six-support U whose complement is non-Hamiltonian with path-cover number two;
(iii) explicit order disagreement.
Again (i) contradicts componentwise Phi-minimality, leaving exactly alternatives (2) or (3) of the present theorem.

Therefore, unless c>=6, either order disagreement occurs or c=4 and the Hamiltonian-six obstruction is present.

Finally, every connected component of the finite pairwise-repartition graph contains a Phi-minimal vertex, so applying the proved trichotomy to such a representative gives the componentwise formulation.