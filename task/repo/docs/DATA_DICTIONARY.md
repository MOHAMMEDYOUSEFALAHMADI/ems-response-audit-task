# Data dictionary (canonical model)

| Field | Meaning |
|---|---|
| `call_at` | Time the emergency call was **created/received at the PSAP** (call-taker answers). |
| `dispatched_at` | Time a unit was assigned. |
| `on_scene_at` | Time the unit arrived on scene. |
| `district_code` | One of OLY, MLZ, NSM, SWD, NKH, RWD. |

## Response time (KPI)
`response time = on_scene_at - call_at` (call-to-arrival, the Red Crescent KPI). It must **not** start at dispatch.

## Reporting
Monthly buckets use **Asia/Riyadh local time (UTC+3)** of `call_at`. Median uses the standard definition (mean of the two middle values for even counts).

## Duplicate call policy (OPS-7)
During surges several calls may be logged for the same emergency, each with its own `incident_id`.
Two records are the same incident when they have the **same `caller_phone_hash`, the same `district_code`,
and `call_at` within 600 seconds (inclusive) of the first record of that group**. Keep only the earliest record.
Records from the same phone in a different district, or more than 600 s later, are separate incidents.
