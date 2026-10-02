# Any rank-long terminal path has a terminal-tail blocker

## Statement

Let e={x,u,v} be a nonspecial edge with rank q=φ(e) and unique entrance x, with u,v its two terminal vertices. Let P=(g_1,...,g_r) be a linear path of length r>=q ending at u. Then either e is the last edge of P, necessarily r=q and the penultimate edge meets e at x, or P does not use e and one of x,v occurs in the final q-2 precursor edges g_{r-q+2},...,g_{r-1}. The analogous statement holds with u and v interchanged.

## Body

If e occurs on a path ending at terminal u, it must be the last edge; otherwise a later path edge would be nonconsecutive to e while the last edge contains u∈e. Then r<=φ(e)=q. Since r>=q, r=q, and P is a longest path ending in e. Nonspeciality forces its entrance label to be x, so x lies in the penultimate edge. Now assume e is not used by P. Consider the suffix S=(g_{r-q+2},...,g_r), which has q-1 edges and ends at u. If neither x nor v occurred in the first q-2 edges of S, then e would meet S only at u: linearity forbids x or v from also lying in g_r, since g_r already meets e at u. Therefore S followed by e would be a q-edge linear path ending in e through terminal label u. This is a longest path ending in e with entrance u≠x, contradicting nonspeciality. Hence x or v occurs in the stated final precursor tail. The argument is symmetric for paths ending at v.