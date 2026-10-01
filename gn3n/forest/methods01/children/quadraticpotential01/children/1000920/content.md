# Above order seventeen global quadratic minima reduce to the 4|4 and 4|5 plateaus or minimum side six

## Statement

Let H be a minimum counterexample of order n>=18, and let C=A|B|D be a spanning three-cover minimizing
Phi(C)=|A|^2+|B|^2+|D|^2
among all spanning three-covers of H. Write a>=b>=c for the component orders.

Then at least one of the following holds:

(1) c>=6;

(2) H contains explicit order disagreement between Hamiltonian paths on overlapping induced supports;

(3) c=4 and b=4, so the size profile is (n-8)|4|4;

(4) c=4 and b=5, so the size profile is (n-9)|5|4.

Thus, in the absence of order disagreement, every global quadratic minimum of order at least eighteen either has all three component orders at least six or lies on one of the two narrow four-side plateaus 4|4|(n-8) and 4|5|(n-9). In particular, minimum side five is impossible, and a four-side with both complementary paths of order at least six is impossible.

## Body

Let a>=b>=c be the component orders.

First suppose c<=3. Since a global Phi-minimum is in particular Phi-minimal in its own pairwise-repartition component, 1000917 applies. At n>=18 its small-side thresholds force an immediate strict Phi descent, contradicting global minimality. Hence c>=4.

Suppose c=5. Then a+b=n-5>=13, so a>=7. Apply fiveside_descent_or_disagree01 to the five-side and the displayed path of order a. That theorem gives either an immediate strict pairwise-repartition descent or explicit order disagreement. Global minimality excludes the descent, so c=5 implies outcome (2).

It remains to consider c=4. If b>=6, then the four-side and the two complementary displayed paths satisfy the hypotheses of 1000592: the cover is globally Phi-minimal, the four-side is Hamiltonian, and both complementary paths have order at least six. The conclusion of 1000592 includes unavoidable order disagreement among Hamiltonian paths on the associated cross-endpoint six-set deletion family. Hence, in the absence of outcome (2), one must have b<=5.

Since b>=c=4, this leaves only b=4 or b=5. Because a+b+c=n, these give respectively the profiles
(n-8,4,4)
and
(n-9,5,4).

These cases together exhaust all possibilities.