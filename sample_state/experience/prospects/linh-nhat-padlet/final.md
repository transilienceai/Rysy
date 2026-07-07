# Final — Linh Nhat (Padlet)

**Subject:** Arcade moderation without accounts

Sandbox shipped with content moderation as a top-priority engineering feature because user accounts gave you natural enforcement hooks. Arcade lands at a separate domain with no student login by design — same moderation problem, structurally harder because the policy-enforcement surface that Sandbox had isn't there.

Where it gets hard isn't the moderation decision itself — it's reconstructing what happened when something slips through, since without accounts the trace lives only across model inputs, outputs, and the request context around them.

Transilience treats that trace as something the platform produces continuously, not assembled when an incident review starts.

What does measurement look like for Arcade moderation right now?

— Transilience
The Security Operating System for the Cloud
