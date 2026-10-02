# Canonical p=5 entrance paths must cross the rank-five terminal edge itself

## Statement

In the p=5 charged pattern (4,4,4,5), retain the notation of 7d676959b033. Write the rank-five charged edge
  e5={d,v,w},
where d=g4∩e5 is its unique entrance and v is the common charged terminal.

For the rank-four edge
  f_b={b,v,u_b},
let R_b be any canonical three-edge entrance path ending at b and avoiding v,u_b.

Then R_b must meet e5. Since R_b avoids v, it contains at least one of d,w.

Moreover phi(d)=4 and phi(w)>=5.

## Body

Suppose R_b were disjoint from e5.

By definition of the canonical entrance path for the ascending rank-four edge f_b, the concatenation
  R_b,f_b
is a four-edge linear path ending in f_b through its unique entrance b, and R_b avoids the two terminals v,u_b. Hence f_b meets R_b only at b.

The edge e5 meets f_b at v. Since R_b avoids v and is assumed disjoint from e5, the concatenation
  R_b,f_b,e5
is a five-edge linear path ending in e5.

Its predecessor f_b meets e5 at v, so this five-edge path enters e5 through v.

But e5 is nonspecial of rank five, and v is a terminal of e5. Its unique rank-five entrance is d=g4∩e5, contradiction.

Therefore R_b meets e5. Since R_b avoids v, the contact is with d or w.

Finally e5 is ascending of rank five, so its unique entrance d has
  phi(d)=4.
Because e5 is potential-charged at v and phi(v)=5, its opposite terminal w satisfies
  phi(w)>=5.