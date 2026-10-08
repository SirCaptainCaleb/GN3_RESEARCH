# Positive alternating double occurrences have support at most eight — preserved pre-item development

## Development

## Reflected positive alternating double occurrences have support at most eight

The reflected-double obstruction can also be removed for the alternating type without dual polarity.

**Proposition.** Let \(0101\) occur at reflected starts \(a<b\), and suppose no positive witness on a strictly more central unsigned edge occurs. Then \(b-a=2\). Consequently the full determining span has at most eight vertices. A centered single occurrence has six vertices.

**Proof.** For alternating reflection, \(a+b=m-2\). More central span-two starts are \(a+1,\ldots,b\), and more central alternating starts are \(a+1,\ldots,b-1\). Thus the entire status interval
\[
[a+1,b+2]
\]
avoids \(001,011,0101\): every occurrence contained in that interval has one of those strictly inward starts.

The left \(0101\) occurrence gives
\[
\epsilon_{a+2}=0,
\]
while the right occurrence gives
\[
\epsilon_{b+1}=1.
\]
If \(b-a\ge3\), these two positions are separated by at least two. The exact forbidden-word criterion then forces a positive forbidden occurrence inside the protected interval, a contradiction.

The remaining separation one is impossible because overlapping \(0101\) occurrences shifted by one prescribe opposite values to the shared second bit. Therefore separation two is the only possible noncentered case. Two six-vertex windows shifted by two have union order eight. \(\square\)

The inward-start ranges can be read directly from the interlaced reflection pairs. Between the alternating edge \(\{a,b\}\), where \(a+b=m-2\), and the center lie the span-two pairs with starts \(a+1,\ldots,b\), whose reflection sum is \(m-1=a+b+1\), and the alternating pairs with starts \(a+1,\ldots,b-1\).

Together with [[positive_protection_eliminates_exclusive_disjoint_alternating_carriers]], this removes all unbounded alternating terminal geometry from the positive-word route: exclusive disjoint alternating carriers do not exist, and double alternating occurrences are supported on at most eight vertices.

This does not prove the analogous statement for span-two doubles. There the more-central protected interval is \([a+1,b+1]\). A left \(011\) and right \(001\) can coexist while the interior has form \(1^*0^*\); [[positive_reflected_double_carriers_have_unbounded_local_spans]] realizes precisely this obstruction. Nor does the present proposition by itself construct nested outward carriers.
