# The singleton-star cube forces a source-anchored mass-four birth on an actual rank-two trimer edge

**Workspace:** D17
**State:** established
**Key:** `three-spoke-singleton-star-small-trimer-source-crossing`

**Summary:** In the SV98784 singleton-star residue, puncture each source-internal spoke s from the retained top source cover U|V and compare the resulting three-cover with the synchronized rank-two cover J_{tu}|B on W+{t,u}. For at least one s, a selected edge of the physical three-vertex path J_{tu} itself joins two components of U|V-s. Otherwise for every s the connected set {t,u,v} would lie in one punctured-source component; this forces p,q,r,v onto one source rail, and deleting the middle of p,q,r separates the other two, contradiction. Choose a spoke endpoint x of such a crossing edge xy. Since x is source-internal and s!=x, its component after deleting s is nontrivial; choose an old source neighbor h of x in that component. R3 on {h,x,y} makes either (h,x,y) or (y,x,h) tight, so the old dimer at x is respectively tail- or head-signed by y. This support is disjoint from the deleted spoke source trimer (a,s,c). Pair it with the opposite terminal dimer of (a,s,c): (s,c) if the new dimer is tail-signed, or (a,s) if it is head-signed. Thus the common parent contains a direct mass-four balanced pair whose nontrivial support, witness, actual rank-two cross edge, punctured-source component and deleted source spoke are all retained. This is stronger provenance than an anonymous R159 output but is not claimed to close or descend.

### 1. Singleton-star input
Retain the fully synchronized residue of SV98784. Thus H is a hypothetical smallest counterexample,

  H-{a,c}=U|V

is the retained exact source frame, and p,q,r are distinct internal vertices of its displayed rails satisfying

  (a,p,c), (a,q,c), (a,r,c)

tight. Put P={p,q,r} and W=V(H)-({a,c} union P). The synchronized lower cube has

  F=(v)|B

as an exact two-cover of W, with v in W, and for every pair {t,u}=P-{s} the rank-two fiber W+{t,u} has the literal exact cover

  T_s = J_{tu} | B,

where J_{tu} is a tight trimer on the physical support {v,t,u}. No orientation of J_{tu} is normalized here.

### 2. Puncturing the source gives three literal three-covers
Fix s in P and write {t,u}=P-{s}. Because s is internal on its source rail in U|V, deleting s splits that rail into two nonempty old-order intervals while the other source rail remains nonempty. Hence

  R_s := (U|V)-s

is a literal three-cover of exactly W+{t,u}.

The synchronized rank-two representative T_s is a literal two-cover of the same support. Any selected T_s-state joining two R_s-components is therefore an actual source-visible component-drop crossing. The point below is that for at least one s such a crossing is forced to lie INSIDE J_{tu}, not anonymously somewhere on B.

### 3. At least one small trimer crosses the punctured source components
Suppose contrariwise that for every s in P neither of the two selected edges of J_{tu} joins distinct R_s-components. Since J_{tu} is a connected three-vertex path, all three vertices

  {t,u,v}

then lie in one component of R_s for every s.

Apply this first with s=p. The two surviving spokes q,r must lie on the same source rail. With s=q, the spokes p,r must lie on the same source rail. Hence p,q,r all lie on one source rail. The common component condition also places v on that same rail.

Now take the middle one of p,q,r in the literal linear order of that source rail and call it s. Deleting s separates the other two spokes into the two opposite nonempty old-order intervals of that rail. They therefore lie in distinct R_s-components, contradicting that {t,u,v} lies in one component.

Thus for at least one s there is a selected edge xy of the actual trimer J_{tu} whose endpoints lie in two distinct components of R_s.

### 4. Root the small crossing at a surviving source spoke
The edge xy has two endpoints and at most one of them is v. Hence at least one endpoint is one of the surviving source spokes t,u. Rename the physical endpoints if necessary only for this local argument so that

  x in {t,u}.

No reversal of the selected J_{tu} state is asserted; x is simply the chosen physical endpoint at which we root the R3 test. Because x was internal in the original source frame and s is a different vertex, the R_s-component containing x is nontrivial: deletion of s can remove at most one of x's two old source neighbors, leaving at least one old-order neighbor h in that component.

The vertices h,x,y are distinct because y lies in a different R_s-component. Apply R3. Exactly one of

  (h,x,y),   (y,x,h)

is tight.

If (h,x,y) is tight, the oriented old source dimer

  D=(h,x)

is TAIL-signed by witness y. If (y,x,h) is tight, the oriented old source dimer

  D=(x,h)

is HEAD-signed by witness y. In either branch D retains the exact old source edge {h,x}, the actual small-trimer cross endpoint y, and the puncture label s.

### 5. The deleted source trimer supplies the opposite terminal mate
The retained source turn

  J_s=(a,s,c)

has the two natural terminal signs

  (a,s) TAIL-signed by c,
  (s,c) HEAD-signed by a.

The support of D lies in W+{t,u}=V(H)-{a,c,s}, so it is physically disjoint from both terminal dimers of J_s. Therefore:

- if D is TAIL-signed, pair D with the HEAD-signed source dimer (s,c);
- if D is HEAD-signed, pair D with the TAIL-signed source dimer (a,s).

In either case the two supports are disjoint, have opposite polarity, and have total support mass four. Hence the common source parent contains a direct balanced mass-four pair.

This pair is not anonymous. Retain exactly:

- the deleted spoke s and source trimer (a,s,c);
- the rank-two trimer J_{tu} and the actual selected crossing edge xy;
- the crossed R_s-components;
- the surviving spoke endpoint x;
- its old source neighbor h;
- the orientation/polarity of D; and
- the exact witness y.

### 6. Two-root strengthening and the sole one-dimer asymmetry
If both physical endpoints of the chosen crossing edge are surviving source spokes, the same argument may be rooted at each endpoint separately, because both punctured-source components are nontrivial. This gives two source-anchored mass-four births through the SAME deleted source trimer J_s, with their two exact old source neighbors retained.

More generally, if the other endpoint is v but v also lies in a nontrivial R_s-component, it too may be rooted by the same R3 construction, again producing a second signed old-source dimer and hence a second mass-four mate through J_s. The only case in which this symmetric second dimer construction is unavailable is when the crossing joins a surviving spoke to v and v is itself a singleton component of R_s. The first spoke-rooted mass-four birth remains valid in that case.

### 7. Scope
This theorem is a provenance sharpening of the singleton-star residue, not its extinction. It does not count a balanced pair or PAYABLE-FOUR birth as strict progress and does not braid any paid descendants. Its content is that the final Boolean-cube nucleus cannot hide all three source component drops in the spectator Hamilton rail B: at least one drop is physically realized on a three-vertex star cell and directly remints into a mass-four pair anchored to the deleted source trimer. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
