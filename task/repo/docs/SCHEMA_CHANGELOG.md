# Schema changelog

## v2 (live 2025-07-01)
- Exporter switched from Windows-1256 to UTF-8. Older (v1) exports are unchanged on disk.
- Timestamps are now ISO-8601 **UTC** with a trailing `Z` (v1 used naive Riyadh local time).
- `call_received_at` renamed to `call_created_at` (same meaning).
- `unit_dispatched_at` -> `dispatched_at`, `unit_arrived_at` -> `on_scene_at`.
- `district` (Arabic name) replaced by `district_code` + `district_name`.
- New column `schema_version`.

## v1 (until 2025-06-30)
Columns: incident_id, call_received_at, unit_dispatched_at, unit_arrived_at, district, caller_name, caller_phone_hash, priority, hijri_date.
