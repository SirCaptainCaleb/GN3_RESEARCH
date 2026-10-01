# A linear selected local family forces U-mass, early triangles, or early superlevel outputs

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path with last vertex v, and let F be a family of k distinct selected strict-gap switching edges through v from the local D+Y certificate system, each single on P. Split
  F = X disjoint_union U,
where X consists of edges whose unique off-v contact on P is their entrance, and U consists of edges whose unique contact is the opposite terminal.

Put
  C_p = 7+4 floor(log_2(p+2)).
Then at least one of the following holds:
(1) |U| >= k/2;
(2) there are at least k/16-C_p/4-O(1) distinct early doubly occupied certificate cells, hence that many linear switcher triangles;
(3) there are at least k/16-C_p/4-O(1) distinct early paid certificate cells with distinct standard output edges contained in V_{>=p}.

In (2) and (3), all counted cells have standard output index at most
  p-floor(k/16).
Consequently, whenever k=Omega(p), one of the three displayed currencies is Omega(p).

## Body

Set
  s=floor(k/16).
Apply the prefix-excess inequality cfa68aa6d0c5 to X. It gives
  k <= |U| + |{f in X:sigma_f>s}| + 4s + C_p,
where sigma_f=phi(x_f)-a_f and a_f is the first host occurrence of the entrance.

If |U|>=k/2, outcome (1) holds. Otherwise
  |{f in X:sigma_f>s}|
    > k/2-4s-C_p
    >= k/4-C_p-O(1),                                (1)
because 4 floor(k/16)<=k/4.

Let M be this high-excess X-subfamily. By 5a46bb34148e, the members of M occupy at least
  ceil(|M|/2) >= k/8-C_p/2-O(1)                     (2)
distinct early certificate cells, and every such cell carries at least one of:
- a D-certificate, hence is doubly occupied and supports a linear switcher triangle;
- a Y-certificate, hence is paid and has a standard output edge contained in V_{>=p}.

Choose one available certificate type for each cell. By pigeonhole, at least half of the cells in (2) have the same chosen type. Therefore either the triangle cells or the paid-output cells number at least
  k/16-C_p/4-O(1).
This gives (2) or (3).

For every member f of M, 5a46bb34148e also places its cell output no later than g_{p-s}; hence all counted cells/output edges lie in the stated early host portion.

The proof uses only the selected D+Y certificate semantics and the prefix-excess recurrence. Source-cleanliness and opposite-terminal singleness are not used in this trichotomy; they remain available for attacking the three residual branches.
