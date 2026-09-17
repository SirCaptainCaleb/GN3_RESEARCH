# S9017 — Five-Vertex Non-Hamiltonian Boundary Tournaments Are Edge-Orderable

## Theorem
Let H be a boundary 3-tournament on exactly five vertices. If H has no directed tight Hamilton path, its line-graph comparison orientation Gamma(H) is acyclic. Equivalently there is a total order on E(K_5) realizing every tight turn as an increasing consecutive-edge comparison. In contrapositive form, any nonintegrable five-vertex boundary tournament is Hamiltonian.

Consequently, in any boundary tournament with pc(H)>2, the five-vertex complement of any proper tight path is edge-orderable.

## Proof
Assume that H has no tight Hamilton P5. We prove that Gamma(H) is acyclic.

We use one forcing rule. If W=v_0v_1v_2v_3v_4 is a five-vertex word and two of its three consecutive turns are already tight, the third turn must be bad, since otherwise W is a Hamilton P5. Boundary antisymmetry therefore makes the complete reversal of that third turn tight. In the tables

    W => xyz

means that the other two turns of W are already tight and this rule forces xyz. Each row is read from left to right.

By the line-graph comparison theorem S9011, a shortest directed comparison cycle is a star triangle, an ordinary triangle, or a vertex-simple ordinary cycle. A comparison five-cycle itself gives a Hamilton P5, so only an ordinary four-cycle and the two triangle types remain.

### Ordinary four-cycle
Normalize the cycle as

    oa -> ab -> bc -> co -> oa,

so

    oab, abc, bco, coa

are tight, with d the fifth vertex. The following branches are exhaustive.

| branch | successive forced turns | contradiction |
| --- | --- | --- |
| acd, oac | bcoad=>dao; boacd=>aob; daobc=>cbo; cdaob=>adc; adcbo=>bcd; oabcd=>bao | oab and bao |
| acd, cao | dbcoa=>cbd; doabc=>aod; caodb=>bdo; acbdo=>bca; bcaod=>doa; doabc=>bao | oab and bao |
| dca, bac | coabd=>dba; odbac=>bdo; abcod=>doc; bdoca=>aco; dbaco=>abd; coabd=>bao | oab and bao |
| dca, cab | dcabo=>oba; dabco=>bad; obadc=>cda; cobad=>boc; bocda=>dco; dcoab=>bao | oab and bao |

Thus no shortest comparison cycle has length four.

### Star triangle
Normalize the star triangle at o:

    aob, boc, coa

are tight. Put

    S(d)={u in {a,b,c}: uod is tight}.

Cyclically permuting a,b,c preserves the root. Passing to the complete-reversal dual preserves Hamiltonicity after reversing paths; after swapping b and c it restores the root and sends |S(d)| to 3-|S(d)|. Hence only |S(d)|=0 and 1 need be treated.

If |S(d)|=0, then doa,dob,doc are tight. The following nested complementary branches are exhaustive.

| branch | successive forced turns | contradiction |
| --- | --- | --- |
| obc | dobca=>acb; doacb=>cao; dcaob=>acd; aobcd=>dcb; daobc=>oad; oadcb=>cda; bocda=>dco; bdcoa=>cdb; acdbo=>obd; caobd=>oac | oac and cao |
| cbo, oda, oba, bdc | bdcoa=>ocd; bocda=>adc; obadc=>dab; odabc=>cba; docba=>bco; dbcoa=>cbd; aobdc=>dbo; adboc=>bda; cbdao=>oad; bcoad=>dao | oda and dao |
| cbo, oda, oba, cdb | dobac=>cab; cdoba=>odc; odcab=>acd; acdbo=>obd; caobd=>oac; oacdb=>cao | oac and cao |
| cbo, oda, abo, oac | abocd=>dco; daboc=>bad; badco=>cda; cdaob=>oad; coadb=>bda; bcoad=>ocb; ocbda=>dbc; doacb=>bca; odbca=>bdo; bdoac=>cao | oac and cao |
| cbo, oda, abo, cao | dcaob=>acd; abocd=>dco; bdcoa=>cdb; acdbo=>obd; caobd=>oac | oac and cao |
| cbo, ado, obd | caobd=>oac; badoc=>dab; daboc=>oba; dobac=>cab; cdoba=>odc; odcab=>acd; aobdc=>cdb; oacdb=>cao | oac and cao |
| cbo, ado, dbo | adboc=>bda; cadob=>dac; bdaco=>oca; dboca=>obd | obd and dbo |

If |S(d)|=1, cyclically normalize S(d)={c}; thus doa,dob,cod are tight. Then:

| branch | successive forced turns | contradiction |
| --- | --- | --- |
| odb, adc | codba=>abd; acodb=>oca; ocabd=>bac; dobac=>abo; abocd=>dco; badco=>dab; daboc=>oba | oba and abo |
| odb, cda | cdaob=>oad; acodb=>oca; bocad=>dac; dboca=>obd; obdac=>adb; coadb=>dao | oad and dao |
| bdo, bdc | bdcoa=>ocd; abocd=>oba; aobdc=>dbo; dboca=>aco; adboc=>bda; bdaco=>cad; cadob=>oda; codab=>bad; bocda=>adc; obadc=>abo | oba and abo |
| bdo, cdb | bdoac=>cao; dcaob=>acd; acdbo=>obd; caobd=>oac | oac and cao |

The duality handles |S(d)|=2 and 3. Hence a shortest comparison cycle is not a star triangle.

### Ordinary triangle
Normalize the comparison triangle as

    oa -> ab -> bo -> oa,

so

    oab, abo, boa

are tight, and let c,d be the other vertices. For w in {c,d} define

    o in M(w) iff bwa is tight,
    a in M(w) iff owb is tight,
    b in M(w) iff awo is tight.

If M(c) and M(d) shared a coordinate, the corresponding core vertex together with c,d would give three parallel source turns on common ordered endpoints. S9022 would then give a Hamilton P5. Thus M(c) and M(d) are disjoint.

Up to cyclic permutation of o,a,b and exchange of c,d, the disjoint pair is one of

    (empty,empty), (empty,{o}), (empty,{o,a}),
    (empty,{o,a,b}), ({o},{a}), ({o},{a,b}).

The match-set definition fixes the six exterior-core turns in each case. The remaining forcing is:

| M(c), M(d) | extra branch | successive forced turns | contradiction |
| --- | --- | --- | --- |
| empty, empty | none | bcoda=>doc; bdoca=>aco | oca and aco |
| empty, {o} | none | bcoda=>doc; bdoca=>aco | oca and aco |
| empty, {o,a} | none | bcoda=>doc; docab=>bac; odbac=>abd; odacb=>cad; bocad=>cob; cobda=>dbo; cdboa=>bdc; oabdc=>bao | oab and bao |
| empty, {o,a,b} | abc | abcod=>doc; badoc=>dab; dabco=>ocb | ocb and bco |
| empty, {o,a,b} | cba | cbado=>dab; cdabo=>adc; boadc=>dao; cbdao=>dbc; dbcoa=>aoc; bdaoc=>oad | oad and dao |
| {o}, {a} | ocd | bcoda=>doc; docab=>bac; odbac=>abd; oabdc=>cdb; aocdb=>coa; coabd=>bao | oab and bao |
| {o}, {a} | dco | ocadb=>dac; bodac=>dob; dobca=>cbo; dcboa=>bcd; cboad=>dao; bcdao=>adc; badco=>dab; daboc=>cob; adcob=>cda; bcdao=>oad | oad and dao |
| {o}, {a,b} | cod | codba=>abd; abcod=>cba; cbado=>dab; daboc=>cob; cdabo=>adc; adcob=>ocd; oabdc=>cdb; aocdb=>coa; coabd=>bao | oab and bao |
| {o}, {a,b} | doc | docab=>bac; odbac=>abd; badoc=>dab; daboc=>cob; cdabo=>adc; adcob=>ocd; oabdc=>cdb; aocdb=>coa; coabd=>bao | oab and bao |

The extra branches are complementary pairs, so these rows are exhaustive. Thus a shortest comparison cycle is not an ordinary triangle.

No directed comparison cycle remains. Gamma(H) is acyclic, and S9011 turns any topological ordering of Gamma(H) into the required total edge order.

For the final consequence, if Q is a proper tight path in a larger H with pc(H)>2 and its complement X has five vertices, then H[X] cannot have a Hamilton P5, since that path together with Q would be a spanning two-cover. Therefore H[X] is edge-orderable. QED.

## Why this is reusable
This is the exact five-vertex bridge from order-free boundary tournaments to ordinary edge orders. It replaces a former finite SAT certificate by a direct comparison-cycle argument with explicit human forcing tables.

## Scope and nonclaims
The theorem is specific to five vertices. It does not assert that every larger nonHamiltonian boundary tournament is edge-orderable.

## Provenance
Human repair of archived R902. The previous computer-assisted DPLL proof has been completely removed. The only nontrivial imported local ingredient is the independently human S9022 parallel-source P5 lemma.