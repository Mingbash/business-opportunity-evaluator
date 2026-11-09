# Scoring and tier rules

Read this file when scoring, ranking, or comparing opportunities.

## Dimension scale

Use `U` when evidence is insufficient. Do not substitute 0, a neutral score, or an invented estimate.

| Score | Meaning |
|---:|---|
| 5 | Unusually strong for the stated scope and objective; supported by current, relevant evidence |
| 4 | Clearly favorable; important risks exist but have credible mitigations |
| 3 | Mixed but workable; one or two material uncertainties or tradeoffs remain |
| 2 | Unfavorable; improvement requires a meaningful assumption or redesign |
| 1 | Severe structural or entry weakness |
| 0 | Demonstrably absent, blocked, uneconomic, or invalid for the defined business—not merely unknown |

Score the evidence-supported reality at the evaluation date, not the best imaginable version of the business.

## Evidence gates before scoring

- **Paid demand 4–5:** require evidence broader than an isolated listing, product, review, or seller claim. The evidence must support the defined payer/job and say something about repeated buying, adoption, budget, or serviceable capacity.
- **Competition 3–5:** identify the remaining payable job after direct, free, platform-native, AI/DIY, internal-team, manual, and service alternatives. Compare current penetration and the likely direction and speed of demand growth versus supply growth.
- **Distribution 3–5:** require a credible route to qualified buyers plus a reason they would buy from this seller. Contactability, a directory, or a partner badge alone does not establish distribution quality: use U if the route is unestablished. A low numeric score requires affirmative evidence of weakness, not just missing proof. An overlapping service provider without evidenced capacity overflow, technical gap, cost advantage, geography/compliance access, white-label need, or other complementarity is a competitor, not a channel.
- **Entry 3–5:** require a plausible path from identification through trust, quote or checkout, payment, and delivery. A job post proves one procurement event, not an available partnership or repeatable channel.

Use `U` when a decision-critical part of a dimension remains unestablished. Do not fill every cell merely to produce a total. Score the original atomic business before any repair; never transfer a redesigned variant's score back to it.

## Weights

These weights are a transparent judgment framework, not statistically calibrated predictors. Users may supply nonnegative weights with a positive total; normalize to 100 and disclose the effective weights. Keep evidence gates intact and use the same weights for comparable options. Missing dimensions remain U; never renormalize them away to inflate a score.

| Dimension | Company/main business | Side hustle |
|---|---:|---:|
| Paid demand and market capacity | 20 | 15 |
| Competition, substitutes, and supply change | 15 | 10 |
| Distribution and buyer reachability | 15 | 20 |
| Entry difficulty and first cash | 5 | 15 |
| Unit economics | 15 | 15 |
| Solution | 10 | 10 |
| Business-model quality | 15 | 10 |
| Timing and durability | 5 | 5 |
| **Total** | **100** | **100** |

For a short-term cash-bridge service, use the side-hustle weights but explain the service ceiling rather than penalizing it as if it were a venture-scale company.

## Three distinct tiers

The objective-mode weights above produce the **Overall Tier consistency score**.

1. **Market Structure Tier** uses paid demand, competition/payable gap, unit economics, solution, business-model quality, and timing. Judge it independently, or renormalize only those dimensions to 100 when a numeric subscore materially helps. It answers whether the business structure is attractive for a capable entrant.
2. **Current Entry Tier** emphasizes distribution, entry difficulty, first cash, the user's assets and constraints, and any payment, license, data, or platform gate. Judge it independently, or renormalize only the relevant dimensions when useful. It answers whether this user can enter now at acceptable cost.
3. **Overall Tier** answers what the user should do now under the selected objective. Use the weighted score as a consistency check, then apply evidenced gates and bottlenecks. Do not average the first two tiers.

## Tier bands

Use weighted scores as a consistency check, not a substitute for judgment.

| Tier | Indicative score | Decision meaning |
|---|---:|---|
| S | 85–100 | Exceptional structure and executable entry; deserves priority commitment |
| A | 75–84 | Attractive, with a clear paid validation or entry path |
| B | 65–74 | Worth a bounded test; 1–2 pivotal uncertainties remain |
| C | 50–64 | Do not commit; only cheap validation, redesign, or monitoring |
| D | 35–49 | Unfavorable now; hold or choose another structure |
| F | 0–34 | Defined business is blocked, invalid, or economically broken |

Attach confidence (`high`, `medium`, or `low`) separately. Early opportunities may be `B, low confidence`; missing revenue history alone does not force C/D.

When one or more weighted dimensions are `U`, calculate a plausible score range only if doing so helps the decision. Otherwise give a provisional working tier and state what could move it. Never average only the known favorable dimensions and present the result as complete.

## Gates and caps

Apply a cap only when a blocking condition is evidenced, not merely unresearched.

- Undefined payer, job, offer, or revenue mechanism: narrow the atomic business before final scoring.
- Demonstrably unavailable legal, payment, authorization, data, or fulfillment path: Current Entry is D/F until the path changes.
- Negative contribution under a plausible price and full-cost scenario: Overall cannot exceed D without redesign.
- A substitute completes the same job well enough with trivial switching cost and no remaining payable gap: Market Structure cannot exceed D for that offer.
- If the remaining payable gap or the only proposed acquisition path is a decision-critical unknown, Overall is provisional and normally cannot exceed C until verified. This cap applies only when that unknown could invalidate the recommendation, not to every early-stage uncertainty.
- B requires a credible payer and acquisition hypothesis sufficient for a bounded sellable test. If the proposed test is only trying to discover whether anyone needs the offer or whether an intermediary has any reason to buy, use provisional C.
- A critical gate that remains unknown makes the tier provisional; it does not automatically score zero.
- Founder-linear delivery is not an automatic no-go for a cash bridge or side hustle. Reflect it in Business-model quality and state the ceiling.

## Comparison and ranking

- Compare opportunities only within the same objective or explain the different objectives.
- Name one preferred option and one fallback when the user is choosing.
- Explain the smallest evidence change that would reverse the ranking.
- Research the 1–2 unknowns most likely to reverse the ranking before naming a preferred option; otherwise label the ranking provisional.
- A GO means worth entering with bounded cost, not guaranteed success. A NO-GO applies to the defined business form, not the entire industry.
