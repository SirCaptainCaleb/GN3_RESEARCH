# Any long terminal path captures a lower-rank ascending edge

## Statement

Let e={x,v,u} be an ascending nonspecial edge of rank q, with unique entrance x and terminal vertices v,u. Let P be any linear path of length p>=2q-1 ending at v. Then P contains all three vertices x,v,u of e. More precisely, u occurs among the final q-2 precursor edges before the last edge of P, and x occurs within the final q-1 edges of a prefix of P ending at u.

## Body

If e itself occurs on P, then because P has last vertex v and nonconsecutive path edges are disjoint, e must be the penultimate edge: it cannot be the last edge since p>=2q-1>q=φ(e). Thus u lies in the final precursor edge, and a prefix ending at u has length p-1>=q; its final q-1 edges contain x because x lies in e. Hence the stated localization holds. Now assume e is not an edge of P. Consider the final q-1 edges of P. If e met this suffix only at the last vertex v, then appending e through v would give a q-edge linear path ending in e with entrance label v. Since φ(e)=q and e is nonspecial with unique entrance x≠v, this is impossible. Hence e meets one of the final q-2 precursor edges at x or u. If the forced contact were x, then because the earliest such precursor edge has index p-q+2, a prefix ending at x would have length at least p-q+1>=q, contradicting φ(x)=q-1. Thus u occurs in the final q-2 precursor edges. Let R be a prefix of P ending at u; as above |R|>=p-q+1>=q. Take the final q-1 edges S of R. The last vertex v of P does not occur in S. If x were absent from S, then S followed by e through u would be a q-edge linear path ending in e with entrance label u, again contradicting the unique entrance x. Therefore x occurs in S. Thus P contains x,u,v, with the stated localization.
