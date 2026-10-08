# Two fixed suffixes can absorb at most four labels when predecessor triples are blocked — preserved pre-item development

## Two fixed suffixes can absorb at most four labels when predecessor triples are blocked

Let S_1,S_2 be vertex-disjoint tight paths, each of length at least two, and let W be disjoint from both. For i=1,2 write the first two suffix labels as z_i,q_i and set
J_i={v in W:h(v,z_i,q_i)=1},
E_i={(u,v):u!=v in W, v in J_i, h(u,v,z_i)=1}.
Assume for each i, each (u,v) in E_i, and every t in W-{u,v}, that h(t,u,v)=0.

Consider two-path covers of W union V(S_1) union V(S_2) in which each S_i is retained as a contiguous final segment of its path. Such a cover exists exactly when W admits a disjoint partition U_1 union U_2 with each U_i of one of these forms:
empty;
{v} with v in J_i;
{u,v} admitting an ordering (u,v) in E_i.

Proof. Since two disjoint nonempty suffixes cannot both be final segments of one path, they occupy distinct paths. Neither path can use labels from the other suffix. Thus its prefix uses only W. The forbidden-predecessor argument in [[forbidden_predecessor_triples_give_an_exact_frozen_suffix_two_cover_criterion]] bounds each prefix by two labels and gives precisely the listed possibilities. Conversely, append each suffix to the corresponding allowed ordered prefix. The paths are disjoint and cover all vertices.

In particular |W|<=4 is necessary. If |W|=4, the exact criterion is a partition into two pairs, with one ordering allowed by E_1 and one by E_2. If |W|=3, it is a pair allowed at one suffix and a singleton allowed at the other.

More generally, for r disjoint fixed tight suffixes with the same blocking condition, an r-path cover retaining all suffixes as final segments exists exactly when W partitions into r allowed prefix supports of size at most two. Hence |W|<=2r.

Application and scope. A six-label packet cannot be absorbed by two such fixed suffixes, however many unrooted local two-cover certificates the packet has. This is a conditional obstruction to insisting on two unchanged suffixes, not an obstruction to unrestricted two-covers. It does not claim that an Article VII protected carrier necessarily satisfies the blocking hypotheses at both boundaries. A reflected two-ended repair must either disprove one blocking hypothesis, move a suffix boundary, or change the ordering inside a suffix. This theorem specifies exactly where the fixed-suffix restriction runs out of room.
