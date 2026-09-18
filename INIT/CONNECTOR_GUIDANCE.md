# Connector and retrieval guidance

**Status: STARTUP MECHANICS.**

This file describes only how to retrieve the startup files named in `START.md`. It does not define startup routing or role policy.

## GitHub connector

For a fresh startup, pin one `main` commit and retrieve the required files from that revision when practical.

For a long file, obtain its exact blob SHA and use the connector's whole-blob retrieval path. If ordinary file retrieval is truncated, do not treat the truncated response as the file.

Do not mix startup policy, proof-spine, research-tree, or toolkit files from unrelated revisions merely because `main` advances during initialization.

## Shell Git

When shell Git is available, a sparse checkout may be used to fetch only the paths named in `START.md`. Pin or record the revision used for startup.

## Retrieval failure

If a required file cannot be retrieved completely, stop and repair retrieval rather than proceeding from fragments.
