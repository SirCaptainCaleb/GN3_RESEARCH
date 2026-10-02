# Above order seventeen global quadratic minima have minimum side at least six unless order disagreement occurs

## Statement

Let H be a minimum counterexample of order n>=18, and let C=A|B|D be a spanning three-cover minimizing
Phi(C)=|A|^2+|B|^2+|D|^2
among all spanning three-covers of H. Write a>=b>=c for the component orders.

Then either

(1) c>=6; or

(2) H contains explicit order disagreement between Hamiltonian paths on overlapping induced supports.

Equivalently, if H has no explicit order disagreement, every globally quadratic-minimal spanning three-cover has all three component orders at least six.

Thus at order at least eighteen none of the small-side profiles c<=5 can survive at a global quadratic minimum: sides one, two, and three admit immediate descent; side five admits descent or disagreement; and every four-side case either forces disagreement or falls into a trapped 4|4|a or 4|5|a plateau already excluded or disagreement-forcing by the certified local plateau theorems.

## Body

Let a>=b>=c be the component orders.

If c<=3, apply one_two_and_three_have_universal_onemove_descent_thresholds. Since a global Phi-minimum is also componentwise Phi-minimal, the local small-side descent contradicts global minimality.

If c=5, then a+b=n-5>=13, so a>=7. Apply fiveside_descent_or_disagree01 to the five-side and the a-side. Its strict repartition descent contradicts global minimality, leaving explicit order disagreement.

Now let c=4. If b>=6, apply with_a_fourvertex_component_forms_a_rigid_nonhamiltonian_sixset to the globally Phi-minimal four-side state: its cross-endpoint six-set deletion family forces explicit order disagreement.

Hence, in the absence of order disagreement, c=4 implies b is 4 or 5.

If b=4, the profile is (n-8,4,4), with n-8>=10. Because H is a minimum counterexample, no spanning two-cover exists, so the pairwise-repartition component of C is trapped. The cover C is Phi-minimal in that component. This contradicts quadratic_minimum_cannot_have_profile_44a_with_a_at_least_six, which excludes every trapped componentwise Phi-minimum of profile 4|4|a for a>=6.

If b=5, the profile is (n-9,5,4), with n-9>=9. The same trappedness and componentwise minimality apply, so local_4by5long_quadratic_minimum_forces_order_disagreement forces explicit order disagreement.

Thus every case c<=5 either contradicts global minimality/trappedness or yields order disagreement. Therefore, absent order disagreement, c>=6.