---
name: business-opportunity-evaluator
description: Help the user decide whether a business idea, startup, or side hustle is worth trying. Turn a broad idea into up to three concrete businesses and compare which to test first. Assess the buyer, alternatives, path to a first sale, and full costs. Give separate market, current entry, and overall judgments across eight dimensions. Use for viability or opportunity comparisons.
license: MIT
---

# Business Opportunity Evaluator

Environment: Needs current sources for time-sensitive conclusions; supplied evidence supports provisional analysis when browsing is unavailable. No mandatory spreadsheet or script runtime.

Assess a concrete business as it exists **at the evaluation date**, then tell the user what to do. Do not confuse an attractive market with an opportunity the current user can enter.

Respond in the user's language.

## Turn the idea into businesses you can compare

Define each business using:

`payer × user × trigger × job/outcome × offer boundary × revenue mechanism × acquisition path`

Classify the objective as:

- **Company/main business:** prioritize repeatable revenue, organizational leverage, retention, and a credible path beyond founder labor.
- **Side hustle:** prioritize reachable buyers, time to cash, net cash contribution, founder hours, and maintenance burden.

If the user has not specified the objective, infer the more plausible mode and state it.

- **Broad idea:** Use the stated goal, available time, budget, skills, buyer access and supplied evidence to propose up to three plausible businesses. State working assumptions and ask only about missing information that would materially change the choice. For each path, name the payer, what they buy, what you deliver and support, how you charge, and where you would reach the buyer. Do not score the umbrella label or invent options to fill the shortlist.
- **Concrete idea or explicit comparison:** Lock each requested business and route before research. Evaluate it as supplied. Keep improvements separate and compare all explicitly requested candidates, even when there are more than three.
- **Business versus route:** A material change in payer, buyer job, what is delivered, or revenue mechanism creates a separate business. A change in platform, channel, partner, or implementation method by itself is a route within the same business. Compare route-specific dependencies and entry conditions separately, without counting the routes as additional businesses. A partner who actually pays for a different offer can be a new payer.

Compare candidates against the same objective, constraints and evidence standard. Show the decisive differences and the first path to validate, the first concrete test, and the evidence that could change the order. Label a provisional preference and its assumptions. Leave the ranking open when a decision-changing unknown prevents a defensible preference.

## Default: compact evaluation

Unless the user asks for a deep dive, evaluate these eight dimensions concisely:

1. **Paid demand and market capacity:** payer, trigger, problem/loss, frequency, buying evidence, and potential serviceable users. Use the supplied business geography; otherwise infer a defensible scope from buyer/job and delivery constraints, state it, and ask only if geography could reverse the decision. A global view is appropriate only when the business supports it. Apply geographic, regulatory, language, payment, fulfillment, and channel exclusions. Keep global theoretical capacity, business-model-serviceable capacity, and the user's currently reachable capacity distinct.
2. **Competition, substitutes, and supply change:** why the old solution is insufficient; paid, free, platform-native, AI/DIY, self-build, manual, and service alternatives; their coverage of the buyer's job; their penetration of the target market; and which substitute supply is likely to expand or contract over the next 1–3 years. End with the remaining payable gap.
3. **Distribution and buyer reachability:** how buyers can be reached, what platforms, partners, content, relationships, or permissions this depends on, and how difficult that is for the current user. Keep market demand, reachable buyers, and the user's existing channel separate.
4. **Entry difficulty and first cash:** skills, credibility, licenses, data, capital, setup work, sales-cycle burden, and the distance to the first withdrawable payment. Count research, trust-building, sales, contracting, and collection—not only production.
5. **Unit economics:** collected price minus acquisition, tools, delivery, revisions, support, refunds, payment delay, and channel share; include complete founder hours.
6. **Solution:** describe the product/service and key value in one sentence. State what it makes faster, more certain, or cheaper, for whom, and within what responsibility boundary.
7. **Business-model quality:** reuse, customization, recurring payment, retention, continuing labor, maintenance, and whether founder hours can grow slower than revenue. Recurring billing is not autonomy; distinguish recurring revenue from recurring work.
8. **Timing and durability:** why now, expected window, market trajectory, and the technology, competition, platform, or regulatory changes that would invalidate the thesis.

Verify temporally unstable or decision-critical claims with current sources before scoring. If current sources are unavailable, disclose the cutoff and limitation, use supplied evidence only within its scope, and keep affected scores/tier provisional or U; do not fabricate a search or turn missing access into a no-go. A compact answer is not permission to rely on stale recall; keep research proportionate to the decision.

For each dimension, give a 0–5 score only when evidence supports it; otherwise mark `U`. Never turn unknown into zero or absence.

Output:

- evaluation date, geography, target buyer, and objective mode;
- one-sentence atomic business definition;
- one-sentence solution;
- a compact eight-dimension table with score/`U` and the decisive reason;
- **Market Structure Tier**, **Current Entry Tier**, and **Overall Tier**, each S–F with confidence;
- the recommended entry, bounded test, or no-go decision;
- the largest unproven assumption that could invalidate the tier;
- only the 1–3 unknowns most likely to change the decision and their stop conditions.

For multiple candidates, use a compact side-by-side table. Keep the business definitions, judgments and unknowns attributable to each candidate. Compare routes within their business.

Then ask whether the user wants the full source-backed analysis. Do not ask again if full analysis was already requested.

Read [references/scoring.md](references/scoring.md) when assigning tiers, comparing opportunities, or explaining a score.

## Qualify buyers, channels, and partners

Channel follows buying logic, not directory availability. Before treating an intermediary, implementer, agency, studio, consultant, or service provider as a buyer or channel, establish why it needs the user's contribution instead of doing the work itself.

Valid partnership logic may come from evidenced capacity overflow, a specialized technical gap, lower complete delivery cost, geography/language/compliance access, a white-label requirement, or another complementary asset. If the proposed partner already performs the same core job and no such complementarity or outsourcing motive is evidenced, classify it as a competitor or self-sufficient supplier—not a buyer.

A directory, expert listing, partner badge, audience, or ability to send an email proves only that a party can be identified. A job post proves procurement of that role, not a repeatable partnership market. Do not recommend a partner route or score distribution favorably until the party's unmet need, incentive, transaction path, and dependency are credible. When the user proposes a concrete direct-acquisition route, evaluate it before substituting an intermediary route.

## Repair a strong structure with one hard defect

If the underlying business structure is sound but one dimension has a hard defect, do not stop at a low score. In that dimension, highlight **Structural repair** and generate up to three adjacent variants by changing the smallest necessary variable: payer, user, channel, partner, offer boundary, delivery model, geography, or revenue mechanism.

Examples include changing a full platform to a narrow module or bespoke delivery to a fixed-scope offer. Change direct acquisition to partner-led distribution only after the partner-qualification test above passes; do not invent cooperation merely because the intermediary already has customers.

Keep the original and redesigned variants or routes separate. State what changed, the expected score effect, the new dependency or tradeoff, and re-evaluate the affected tier. Never silently replace the user's business or award the original a higher score merely because a theoretical repair exists.

## Full analysis

When the user accepts or directly requests full analysis:

1. Read [references/full-schema.md](references/full-schema.md).
2. Read [references/research-protocol.md](references/research-protocol.md) before research.
3. Use current sources for claims that can change over time; show the evaluation cutoff date.
4. Separate verifiable facts, inference, scenario assumptions, and unknowns.
5. Finish with a clear priority, exact entry, and next decision—not just a research summary.

Default presentation:

- Use readable inline Markdown by default, splitting large comparisons into compact tables.
- Offer CSV or a workbook when requested or when it materially improves a large comparison and suitable tools exist. File creation is not a requirement to evaluate more than three businesses.
- Keep decision, evidence and assumptions distinct in any format; follow the user-requested format.

Do not split channel variants into fake businesses merely to inflate the comparison. One row remains one payer, one job, and one revenue mechanism.

## Decision safeguards

- Competitor presence can prove demand and budgets; it does not prove saturation. Competitor absence can mean no market.
- Feature availability is not market penetration. “Not found” is not “does not exist.”
- A capable provider, implementer, or studio is not a channel by default. Without evidenced complementarity or outsourcing demand, treat overlapping capability as competition.
- Use frequency is not purchase frequency. A one-time customer event may still create a steady flow of new buyers.
- A platform's users, another seller's revenue, or visible demand do not prove the current user has a low-cost acquisition path.
- Suggested prices, arithmetic revenue scenarios, and time-boxed plans are not purchase evidence or forecasts.
- Keep one-time cash, net cash contribution, and recurring revenue/ARR separate.
- Treat market size as a scoped range or serviceable-capacity estimate with transparent inputs; do not fabricate statistical confidence.
- Turn risks into entry changes, offer boundaries, pricing changes, channel changes, or validation order. Complete desktop research before assigning the user research work.

When maintaining this skill, use [references/regression-tests.md](references/regression-tests.md) as the semantic regression suite; it is not required reading during ordinary evaluations.
