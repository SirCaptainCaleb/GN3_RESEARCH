# Top-boundary q,(q+1)^3 obstructions have at least two visible high entrances

## Statement

In the top-boundary q,(q+1)^3 four-slot normal form, at least two of the three rank-(q+1) charged competitors have their unique entrances visible in the four central slots. Indeed c,d are always entrance slots when occupied, and the left pair a,b cannot both be terminal-only witnesses. Hence the obstruction contains at least two distinct visible vertices of potential q adjacent to the universal low entrance x of potential q-1.

## Body

Retain the top-boundary four-slot normal form 28445330afcc:
the three rank-(q+1) witnesses occupy three of
  {a,b,c,d},
where c,d can only be entrance witnesses, while terminal-only witnesses are possible only at a,b.

By d7ba83f0ce44 (equivalently by df8ad4c65be0 plus f0c177137b7f), two absent-entrance high competitors cannot have witness slots {a,b}: any pair of terminal-only high witnesses must have slots {a,c} or {a,d} in the present notation.

Now count visible entrances.

If both c and d are occupied, both are entrances, so there are at least two visible high entrances.

If exactly one of c,d is occupied, then because three of four slots are occupied, both a and b are occupied. The occupied right slot is an entrance. The pair a,b cannot both be terminal-only witnesses, so at least one of a,b is also an entrance.

(The case neither c nor d is occupied is impossible because only two left slots exist but three distinct high witnesses are required.)

Therefore at least two of the three rank-(q+1) charged competitors have their unique entrances visible among {a,b,c,d}. Each such entrance y satisfies
  phi(y)=q
by ascendingness.
