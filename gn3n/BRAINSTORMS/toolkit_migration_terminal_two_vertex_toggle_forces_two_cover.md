# Toolkit migration — One-polarity two-vertex toggle has a canonical local two-cover

Preserved from the retired Toolkit Limbo object [[terminal_two_vertex_toggle_forces_two_cover]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 3,
    "created_at": "2026-10-05T00:11:31.590219+00:00",
    "updated_at": "2026-10-05T01:14:20.097136+00:00",
    "archived_at": null,
    "original_id": "terminal_two_vertex_toggle_forces_two_cover",
    "audit_status": "passed",
    "math_version": 3,
    "toolkit_type": "lemma",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        141
    ],
    "audited_math_version": 3
}

## Simplified statement

In the one-polarity 001/011/0101 witness scheme, the two-vertex toggle normal form decomposes its ten determining vertices into two tight paths; it is not a dual-polarity terminal case and does not by itself span H.

## Statement

For the one-polarity witness normal form with status segments (0,t,1,1,1,1,1-t,1) and (0,t,0,0,0,0,1-t,1), the ten determining vertices have path-cover number at most two. This lemma is not part of the nearest dual-polarity terminal chain.

## Body

This is the corrected convention-specific form of the local toggle calculation. Let the ten determining vertices be ordered as (a,b,c,d,x,y,e,f,g,h), with the two one-polarity toggle chambers having status segments (0,t,1,1,1,1,1-t,1) and (0,t,0,0,0,0,1-t,1). If t=0, (c,d,x,y,e,f,g,h) is a tight path and (a,b) is the second path. If t=1, boundary antisymmetry gives the tight path (g,f,e,x,y,d,c), while exactly one of (a,b,h) and (h,b,a) is tight, giving the second path. Thus the ten-vertex determining support is two-coverable. This normal form arises in the one-polarity witness analysis. Under the nearest dual-polarity convention it contains a strictly closer witness of the opposite polarity, so it must not be used as a dual-polarity terminal case.

## Direct premises at migration

[]

## Direct consumers at migration

[
    {
        "consumer_id": "every_terminal_local_witness_support_is_two_coverable",
        "consumer_kind": "toolkit",
        "consumer_title": "Every terminal local-witness support is two-coverable",
        "compatibility_status": "confirmed",
        "premise_math_version": 3,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    }
]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

{
    "body": "Let the ten determining vertices be ordered as (a,b,c,d,x,y,e,f,g,h), where swapping x,y changes the four central statuses. Normalize one chamber to have status segment (0,t,1,1,1,1,1-t,1) and the swapped chamber to have (0,t,0,0,0,0,1-t,1). If t=0, the six statuses from (c,d,x) through (f,g,h) are tight, so (c,d,x,y,e,f,g,h) is a tight path and (a,b) is the second path. If t=1, the forced statuses and boundary flips give the tight triples (g,f,e), (f,e,x), (e,x,y), (x,y,d), (y,d,c), hence Q=(g,f,e,x,y,d,c) is tight. The remaining vertices are {a,b,h}; exactly one of (a,b,h) and (h,b,a) is tight by boundary antisymmetry, giving a second path. Thus the induced ten-vertex determining support has path-cover number at most two. This statement does not assert that the local two-cover extends over vertices outside the determining support; that extension is the remaining carrier-terminalization problem.",
    "statement": "In the terminal disjoint span-two branch with alpha=beta=1, the ten determining vertices admit a two-path cover in both possible outer-bit cases. The conclusion is local to the determining support and requires a separate global splice/terminalization argument to extend to H.",
    "audited_by": 148,
    "created_at": "2026-10-05T01:13:58.73739+00:00",
    "research_id": "terminal_two_vertex_toggle_forces_two_cover",
    "audit_status": "passed",
    "math_version": 2,
    "refutation_status": "unrefuted",
    "author_session_ids": [
        141
    ],
    "simplified_statement": "The unique surviving two-vertex terminal toggle always decomposes its ten determining vertices into two tight paths; this is a local support certificate, not by itself a spanning two-cover of H."
}
