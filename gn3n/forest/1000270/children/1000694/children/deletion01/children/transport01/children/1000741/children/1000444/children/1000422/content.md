# The rigid minimum-side two-crossing block gives a one-move strict quadratic descent

## Statement

Let H be a minimum counterexample, let mu be the globally minimum smaller-component order among deletion covers, and let H-y=R|Q be a deletion cover with |R|=mu<=|Q|. Let z be a displayed endpoint of R, and suppose a deletion cover T of H-z lies in the rigid two-crossing block branch of 89d96023752d with inherited orders preserved. Then the singleton lift R|Q|{y} admits one legal pairwise repartition with strictly smaller quadratic potential. Hence the rigid two-crossing branch has no neutral residue.

## Body

It suffices to treat the case that z is the terminal endpoint of R; write R=(A,z), so |A|=mu-1>=2. By the rigid branch of 89d96023752d, Q splits into two nonempty inherited-order blocks Q_1,Q_2, one of which is an entire T-component and the other of which occurs with y and the intact A-block in the mixed component. Up to the two possible mixed-component orientations, T has form Q_1 | (Q_2,y,A) or Q_1 | (A,y,Q_2). The first orientation is impossible: since A is the terminal block and has order at least two, appending z creates only the final consecutive triple formed by the last two vertices of A and z, which is inherited from R. Thus (Q_2,y,A,z) | Q_1 would be a spanning two-cover of H. Therefore T=Q_1 | (A,y,Q_2).

Now (y,Q_2) is a contiguous suffix of the tight mixed component and is therefore a tight path. The two paths Q_1 and (y,Q_2) partition V(Q) union {y}. Hence from the singleton lift R|Q|{y} we may make one legal pairwise repartition of the pair Q|{y}, replacing it by Q_1 | (y,Q_2) and leaving R unchanged. Put r=|Q_1| and t=|Q_2|. Both blocks are nonempty, so t>=1. Since Q_1 is a component of the deletion two-cover T of H-z and mu is the globally minimum deletion-cover component order, r>=mu>=3. The changed pair orders are r+t,1 -> r,t+1, so the quadratic-potential change is r^2+(t+1)^2-(r+t)^2-1 = 2t(1-r), which is strictly negative. The initial-end case is symmetric. Thus every rigid two-crossing endpoint probe supplies an immediate one-move strict descent.
