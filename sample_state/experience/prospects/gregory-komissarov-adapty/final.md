# Final — Gregory Komissarov (Adapty.io)

**Subject:** PSP credential state on self-hosted k8s

Six PSPs absorbed into a self-hosted k8s cluster after the FunnelFox launch is the kind of integration where the credential-state of each PSP — keys, rotation, scoped roles, secret ages — accretes faster than anyone declares a baseline against.

What that exposes operationally isn't at the request/response layer (which oack and the rest of the observability stack already cover) — it's at the secret-scoping-and-rotation layer, surfaced before something fails on rotation week.

Transilience does that part — IAM policy, credential rotation, and cluster-side secret scoping baselined live, additive to whatever observability already runs.

How is credential state currently tracked at the cluster level?

— Transilience
The Security Operating System for the Cloud
