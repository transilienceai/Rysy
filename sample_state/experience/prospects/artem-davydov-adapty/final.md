# Final — Artem Davydov (Adapty.io)

**Subject:** Reconciliation between IaC and cluster state

The FunnelFox launch absorbed six PSP integrations into a self-hosted Kubernetes cluster in twelve days — every PSP added new IAM roles, new secret stores, new network policies, all declared in IaC and all subject to drift the moment the next iteration ships.

The reconciliation question — where IaC says X but the cluster and cloud actually do Y — doesn't usually surface until something breaks at the worst possible time, since static IaC checks run on a different cadence than the cluster's actual change rate.

Transilience reconciles IaC-declared state against effective cluster state continuously — IAM, secrets, and network policy together — surfacing drift before it accumulates into incidents.

Has declared-vs-effective checking been pulled into the deploy pipeline, or is it still incident-driven?

— Transilience
The Security Operating System for the Cloud
