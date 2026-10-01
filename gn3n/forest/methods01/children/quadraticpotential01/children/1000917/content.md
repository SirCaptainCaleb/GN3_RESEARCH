# Small sides one, two, and three have universal one-move descent thresholds

## Statement

Let C=A|B|D be any spanning three-cover of a boundary tournament, with component orders a>=b>=c. A single legal pairwise repartition strictly decreases the quadratic potential Phi in each of the following size regimes: (1) c=1 and a>=3, with potential drop 2a-4; (2) c=2 and a>=4, with potential drop 2a-6; (3) c=3 and a>=6, with potential drop at least 2a-8. Hence a cover that is Phi-minimal in its connected pairwise-repartition component must satisfy c=1 => a<=2, c=2 => a<=3, and c=3 => a<=5. In particular, on n>=14 vertices every componentwise Phi-minimal spanning three-cover has minimum component order at least four. The first two cases are elementary endpoint absorptions; the third is threesidedescent6. No trapped-component or minimum-counterexample hypothesis is used.

## Body

Order the component sizes a>=b>=c.

If c=1, then a+b=n-1, hence a>=ceil((n-1)/2). Let D={x} and write A=(a_1,...,a_a). Repartition D|A as the two-vertex path {x,a_1} together with the inherited path (a_2,...,a_a). Two-vertex paths are vacuously tight. The old contribution to Phi is 1+a^2 and the new contribution is 4+(a-1)^2, so the drop is
1+a^2-[4+(a-1)^2]=2a-4>0.

If c=2, write D for the two-side. Again a>=ceil((n-2)/2). Choose a displayed endpoint e of A. Every induced boundary tournament on three vertices has a tight Hamilton path, since one orientation in the relevant reversal pair is tight. Hence D union {e} has a Hamilton path. Repartition D|A into that three-path and the inherited path A-e. The potential drop is
4+a^2-[9+(a-1)^2]=2a-6,
which is positive because n>=14 gives a>=6.

If c=3, then a>=ceil((n-3)/2)>=6. Apply the certified arbitrary-state descent theorem threesidedescent6 to D|A. It gives one legal pairwise repartition with strict potential decrease. In its one-endpoint branch the drop is 2a-8; in its two-endpoint branch the drop is 4a-20. For a>=6 one has 4a-20>=2a-8, so the drop is at least 2a-8>0.

Therefore every three-cover with minimum component order at most three has an immediate strict descent. A Phi-minimum in its connected pairwise-repartition component can have none, so its minimum component order is at least four.