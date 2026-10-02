# A terminal-retained switching endpoint recaptures its omitted entrance or the host endpoint on every maximum path

## Statement

Let f={v,x,u} be an ascending nonspecial edge of rank r with unique entrance x and terminals v,u. Suppose, in a gap-one switching state at host endpoint v, that u is the retained off-v vertex on the chosen maximum host path P while x is omitted. Then every maximum endpoint path P_u ending at u contains x or v. More precisely, if P_u uses f then phi(u)=r and P_u enters f through x, so x lies on P_u; if P_u does not use f, then avoidance of both x and v would allow f to be appended through terminal u, contradicting the rank/unique-entrance property of f.

## Body

Put s=phi(u). Because u is a terminal of the rank-r edge f, s>=r. Let P_u be any maximum s-edge path ending at u. If P_u contains f, then since f has rank r no path using f as its last edge can have length exceeding r. Thus s<=r, so s=r. A longest r-edge path ending in nonspecial f must enter f through its unique entrance x; hence x lies on P_u. Now suppose P_u does not use f. If it avoided both x and v, then P_u,f would be a linear (s+1)-edge path ending in f and entering f through terminal u. Since s>=r, this path has length at least r+1, contradicting phi(f)=r; even at length r it would contradict unique entrance. Therefore P_u contains x or v.