# Witness verdict -- cyrille-david-coalesce

**Verdict**: ship

## What works

The v2-to-v3 revision addressed the core failure precisely. v2's observation was a security truism dressed in Catalog's name; v3 names the actual architectural seam: catalog metadata declares policy, but IAM roles, Snowflake roles, and cloud-config are the enforcement surface, and those are different systems that update on different timelines. That is a real observation about how data catalog governance works, not a generic statement about controls-needing-verification. Cyrille, who commits code to this product daily, would recognize the seam being described as something that lives in his architecture -- not as something a stranger projected onto it. The failure mode -- "a control turns out not to have been doing what the catalog implied" -- is specific enough to be credible and quiet enough not to perform expertise the writer has not earned. The three-sentence structure, dry register, conditional CTA, and absent vendor language all fit the portrait: a brevity practitioner with zero tolerance for salesmanship affect who will not read past sentence four.

## What fails

The subject line -- "Coalesce Catalog and the controls cadence" -- is the weakest element. "The controls cadence" is an abstraction that does not appear in the body of the email; v3 moved away from the cadence framing into a gap framing (policy-in-catalog vs. control-in-cloud), but the subject line still carries v2's language. It is not fatal -- the subject line is short and names the product, which is enough to earn the open -- but it is a residual seam from a prior draft's concept. A subject line that matched the body's actual argument (the gap between catalog metadata and enforcement primitives) would be tighter. This is not worth a rewrite cycle; it is a minor misalignment in an otherwise cohesive email.
