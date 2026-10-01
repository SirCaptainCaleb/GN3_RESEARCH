
EXCEPTIONAL ROLE OVERRIDE

Normal operator steering uses __template__.request_assignment(...). Requests preserve scheduler arbitration, continuity, collision avoidance, audit independence, and project priorities.

__template__.force_role(...) is retained only as an exceptional administrative escape hatch when the operator explicitly requires scheduler dispatch to be bypassed.

force_role:
- immediately supersedes the worker's current claim;
- may release reservations held by that worker;
- does not consume the displaced project need/audit obligation;
- still cannot bypass audit authorship independence, audit collisions, claim caps, special reasoning mode preparation/halt, or worker policy.

Because it is disruptive, do not infer force_role from ordinary task wording, preferred role wording, elapsed time, or "Continue." Do not use it merely because a request was deferred.

For ordinary role/task/focus steering use:
  __template__.request_assignment(worker_id,intent,priority,timing,scope)

See help('requests').
