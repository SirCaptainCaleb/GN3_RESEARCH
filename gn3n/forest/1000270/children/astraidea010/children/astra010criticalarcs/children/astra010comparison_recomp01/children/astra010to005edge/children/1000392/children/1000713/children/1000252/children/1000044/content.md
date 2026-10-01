# The Hall obstruction has an alternating nonempty core

## Statement

Let G be an edge-orderable boundary tournament with a spanning two-cover A|B, where A=(a_0,...,a_m) is increasing and V(B)={x,y}. Let s=a_i and t=a_j, i<j, be inseparable by spanning two-covers. For each cut k with i<=k<j, define L_k and R_k as in 522bc40f56d4. Then the cuts with L_k and R_k both nonempty form an interval of integers, possibly empty. On every cut in this interval, L_k=R_k is a singleton; along consecutive cuts in the interval the singleton label alternates x,y,x,y,.... More precisely, if L_k is empty then L_h is empty for every i<=h<=k, and if R_k is empty then R_h is empty for every k<=h<j.

## Body

Write e_h=a_h a_{h+1} for the increasing path edges of A, so e_{h-1}<e_h whenever both are defined.

The certified Hall obstruction 522bc40f56d4 says that at every cut k between s and t, either L_k is empty, or R_k is empty, or L_k=R_k={z} for one companion label z.

First suppose R_k is empty and k<j-1. For either z in {x,y}, the failure z in R_k means z a_{k+1} is not less than e_{k+1}. Strict totality gives
e_{k+1}<z a_{k+1}.
Since e_k<e_{k+1}, we obtain e_k<z a_{k+1}, so z belongs to L_{k+1}. Thus L_{k+1}={x,y}. The Hall obstruction at cut k+1 therefore forces R_{k+1} to be empty. Induction shows that R_h is empty for every h with k<=h<j.

Dually, suppose L_k is empty and k>i. For either z in {x,y}, failure z in L_k gives
a_k z<e_{k-1}.
Since e_{k-1}<e_k, we have a_k z<e_k, so z belongs to R_{k-1}. Hence R_{k-1}={x,y}, and the Hall obstruction at cut k-1 forces L_{k-1} to be empty. Induction shows that L_h is empty for every h with i<=h<=k.

Consequently the cuts on which both L_k and R_k are nonempty form an interval C, possibly empty. For k in C the Hall obstruction gives L_k=R_k={z_k} for a unique z_k in {x,y}.

It remains to compare adjacent cuts in C. Let k,k+1 lie in C and write w for the companion label different from z_k. Since w is not in R_k, strict totality gives
e_{k+1}<w a_{k+1}.
Because e_k<e_{k+1}, it follows that e_k<w a_{k+1}; hence w lies in L_{k+1}. As both L_{k+1} and R_{k+1} are nonempty, the Hall obstruction forces
L_{k+1}=R_{k+1}={w}.
Thus z_{k+1}=w, so the singleton label alternates at every step across C.

Equivalently, inseparability with a two-vertex companion has only three possible cut regions: a left region in which the left splice set is empty, one contiguous alternating singleton core, and a right region in which the right splice set is empty; either outer region or the core may be empty. ∎
