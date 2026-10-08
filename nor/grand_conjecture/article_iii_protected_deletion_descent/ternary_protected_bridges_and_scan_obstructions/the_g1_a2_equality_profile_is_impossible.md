# The g=1 A2 equality profile is impossible

## Composition

For the audited g=1 A2 transport, the boundary-safe replacement changes the profile from (p,q) to (p+4,q-4) with explicit retained scan data. If q-p<4 minimality is contradicted; if q-p>4 phase imbalance decreases; and in the equality case q=p+4 the corrected arbitrary-scan replacement theorem forces a phase below the global minimum, with the short terminal case closing directly. Hence repeated g=1 transport is terminating when its stated boundary provenance is retained.

## Development


Work in the recurrent coboundary-flat ternary A2 branch with g=1. The audited boundary-safe surgery produces a genuine one-change deletion carrier

O'=(...,A,B,a,C,b,D,E,F,...)

omitting the third residual coordinate c, with local carrier word

000001

and global run profile

(p+4,q-4).

The A2 identities together with the audited companion boundary constraints force the scan of c across the displayed consecutive pairs to be

alpha(c,A,B),
alpha(c,B,a),
alpha(c,a,C),
alpha(c,C,b),
alpha(c,b,D),
alpha(c,D,E),
alpha(c,E,F)

=
0,0,1,1,0,0,0.

In particular the switch-control scan bit on the right side of the new threshold is 0.

Now consider the only phase-imbalance equality profile from the protected transport trichotomy:

q=p+4.

Then O' has profile

(p+4,p).

### Case p>=3

Apply the corrected arbitrary-scan flat replacement theorem to O'. Because the central control bit is 0, its guaranteed good protected replacement is on the right side of the threshold. That replacement shortens the second phase by 2 or 3.

But the second phase of O' already has length p, the globally minimum normalized phase length over all deletion carriers and their reversals. The resulting deletion carrier would therefore have a phase of length p-2 or p-3, contradiction after reversal.

Hence the equality case is impossible for p>=3.

### Case p=2

The audited p=2 arbitrary-scan boundary lemma applies. It enters exactly the same distance-2/distance-3 protected replacement dynamics, and a right replacement from the profile (6,2) would shorten the second phase below the global minimum 2 or close immediately in the truncated case. Thus p=2 is impossible as well.

### Case p=1

Here q=5, so O' has profile (5,1). Its six local statuses 000001 exhaust the entire deletion word: the displayed eight coordinates A,B,a,C,b,D,E,F form the whole deletion order.

The forced first scan value is

alpha(c,A,B)=0.

Prepend the omitted c. The full spanning word is therefore

0,0,0,0,0,0,1,

which has one change. Contradiction.

### Conclusion

The unique nondecreasing phase-imbalance case q=p+4 of the g=1 A2 protected boundary exit cannot occur.

Combined with the phase-transfer trichotomy:
- if q-p<4, the g=1 exit contradicts global minimum phase immediately;
- if q-p>4, it strictly decreases phase imbalance;
- if q-p=4, the argument above gives a contradiction.

Therefore repeated g=1 A2 boundary transport is terminating. The g=1 A2 branch is not a recurrent flat-sector obstruction.
