# Minimum-run flat replacements alternate sides and have only one residual two-step drift — preserved pre-item development

## Composition

(none yet)

## Development


Use the arbitrary-scan flat replacement theorem. Among all one-change deletion carriers in a minimum coboundary-flat ternary counterexample, including reversals and color complements, choose one

O=(v_1,...,v_m)

with normalized word 0^p1^q and globally minimum first-run length p. Let x be omitted and let s_i=alpha(x,v_i,v_{i+1}).

Because replacing v_p by x would shorten the first run by two or three whenever s_{p+1}=1, minimality forces

s_{p+1}=0.

The blocking-scan core theorem then gives

s_{p+1}=s_{p+2}=s_{p+3}=0.

Hence the good replacement is on the right: replace y=v_{p+3} by x.

Its bridge is

(0,0,s_{p+4}).

Let

d=2 if s_{p+4}=1,
d=3 if s_{p+4}=0.

The new deletion carrier O' has run lengths

(p+d,q-d)

and omitted coordinate y.

If q=d, O' is monochromatic and the full instance closes immediately, so in a surviving counterexample the second phase remains nonempty.

Now examine the blocker scan s' of y relative to O'.

### The next branch is forced left

If d=2, the new switch rank is p'=p+2. The central scan bit controlling the replacement theorem is

s'_{p'+1}
=
alpha(y,x,v_{p+4})
=
1-alpha(x,y,v_{p+4})
=
1-s_{p+3}
=
1.

If d=3, the new switch rank is p'=p+3. Then

s'_{p'+1}
=
alpha(y,v_{p+4},v_{p+5})
=
w_{p+3}
=
1,

using the inherited old 1-phase. If this window does not exist because the old second phase is exhausted, the preceding right replacement already produced a monochromatic carrier and closes.

Thus in either surviving case the next good replacement is necessarily the left replacement at the new switch.

Let its shortening distance be e in {2,3}. The resulting run lengths are

(p+d-e, q-d+e).

Since p was globally minimal,

p+d-e >= p,

so e<=d.

Therefore the forbidden combination is d=2,e=3.

The only two-step possibilities are:

1. d=e=2, giving the original run profile (p,q);
2. d=e=3, giving the original run profile (p,q);
3. d=3,e=2, giving the unique residual drift (p+1,q-1).

Hence minimum-run protected dynamics cannot wander arbitrarily. They alternate right then left, and after two moves either restore the same run lengths or transfer exactly one unit from the second run to the first.

The remaining closure problem is correspondingly narrow:
- analyze the same-profile return packets, especially the exact inverse d=e=3 case;
- rule out indefinite repetition of the residual drift (p,q)->(p+1,q-1), or show it eventually creates a carrier with first run below the global minimum after reorientation.
