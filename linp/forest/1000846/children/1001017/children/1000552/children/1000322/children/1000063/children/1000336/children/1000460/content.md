# Far-end deletion forces motion, rank progress, or a flat terminal adjacency

## Statement

For a boundary ascending nonspecial edge e={x,y,z} of rank q=delta, delete the far first edge of a canonical (q-1)-edge x-ending entrance path. At the new opposite endpoint either a safe clean extension exists, a safe single-blocker rotation exists, or there is a terminal-clean edge f through y or z that is special or has rank at least q. If the latter f is nonspecial, ascending, and has rank exactly q, then its shared terminal v in {y,z} is also a terminal of f; hence every rank-flat ascending transfer is an adjacency in the ascending terminal-pair graph.

## Body

Let Q=(g_1,...,g_{q-1}) be the canonical x-ending entrance path and R=(g_2,...,g_{q-1}), whose opposite endpoint is b_2. If b_2 has a safe clean extension or safe single-blocker rotation, we obtain the first two alternatives. Otherwise the exact deficiency-two sink classification supplies at least one clean edge f through b_2 containing y or z. The terminal-clean witness lemma gives two (q-1)-edge witnesses with distinct entrance labels for f, so either f has rank q-1 and is special or phi(f)>=q.

Now suppose this transfer edge f is nonspecial, ascending, and phi(f)=q, and let v in {y,z} be its shared terminal with e. The original rank-q path ending in e through entrance x has physical last vertex v, so phi(v)>=q. If v were the unique entrance of ascending f, then phi(v)=phi(f)-1=q-1, contradiction. Since f is nonspecial, it has exactly one entrance label, and therefore v is one of its two terminals. Thus e and f are adjacent at v in the ascending terminal-pair graph. The only lexicographically flat transfers are therefore terminal adjacencies; every other terminal-clean transfer is special or raises rank.
