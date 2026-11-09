# Full analysis schema and presentation

Read this file only for a full analysis.

## Row grain

One atomic business has one payer, one buyer job/outcome, one offer boundary, and one revenue mechanism. Record a meaningfully different payer, job, or revenue mechanism as a separate business. Keep platform and channel variants inside the same business unless they change what is bought or who pays.

## Output format

Use readable inline Markdown by default; split large comparisons by topic. Honor requested formats. Offer CSV or a workbook only when useful and supported; no count threshold forces a spreadsheet dependency. For a workbook, separate decision, score, evidence and assumptions, retain source dates/URLs, and freeze identifying columns and headers.

## Table 1: Decision overview

- Atomic business definition
- Variant status: original / structural repair; identify the parent when repaired
- Evaluation cutoff date
- Geography and target segment
- Objective mode
- Market Structure Tier + confidence
- Current Entry Tier + confidence
- Overall Tier + confidence
- Current decision: prioritize / bounded test / redesign / hold / no-go
- Preferred exact entry
- Next action
- Stop or reversal condition

## Table 2: Opportunity detail

### Buyer, job, and solution

- Payer and user
- Trigger, job, and desired outcome
- Current/old solution and why it is insufficient
- One-sentence solution: what becomes faster, more certain, or cheaper
- Product/service deliverable and responsibility boundary
- Use frequency
- Purchase, repurchase, or new-buyer frequency

### Demand and market capacity

- Problem consequences: time, error, money, interruption, liability, or lost revenue
- Willingness-to-pay evidence: purchases, budgets, procurement, paid alternatives, or quote requests
- Global theoretical serviceable users
- Business-model-serviceable users after geography, regulation, language, payment, and fulfillment exclusions
- User's currently reachable buyers; never merge this with market capacity
- Market-capacity or SAM range with formula, assumptions, and exclusions

### Competition, substitutes, and supply change

- Direct paid competitors
- Adjacent paid products or services
- Free and platform-native alternatives
- AI/DIY, self-build, manual, and internal-team alternatives
- Coverage of the buyer's full job, including acceptance, integration, responsibility, and maintenance
- Target-market penetration or adoption evidence; distinguish this from feature availability
- Expected 1–3 year supply expansion or contraction and its speed
- Remaining payable gap and product's net added value
- Buyer's complete cost of solving the job without this offer

### Distribution and entry

- Evidence that the target buyer can be reached
- User's existing channel or relationship, if any
- Acquisition route, dependency, and practical difficulty for the user
- Route stage reached: identify / reach / relevant response / close and collect / deliver
- Why this payer or partner buys rather than completing the job internally
- Partner complementarity and evidence: capacity overflow, technical gap, cost advantage, geography/language/compliance access, white-label need, or other basis
- Full transaction path when decision-relevant: trust, buyer/approver, quote or checkout, payment/collection, and delivery
- Platform, payment, license, authorization, data, and legal gates
- User capability, credibility, assets, and transferable advantage
- Missing capabilities/resources and the time/cash to obtain them

### Delivery and economics

Use these six canonical fields; put detailed model variables in the assumptions table.

1. **Pricing and revenue mechanism:** one-time, project, license, subscription, commission, or hybrid; payer and payment timing.
2. **First-sellable investment:** assets, founder hours, cash, data, approvals, and setup needed before the first sale.
3. **Acquisition burden:** channel, sales effort, elapsed time, and cash needed to acquire and close one qualified buyer.
4. **Fulfillment burden:** delivery, configuration, customization, revisions, support, and maintenance per buyer; include reusable versus bespoke work.
5. **Unit cash contribution:** collected cash minus direct variable costs, with complete founder hours and cash-collection timing.
6. **Income quality and scalability:** orders, qualified leads, and founder hours needed at the target income; recurrence, retention, ARR conditions, and whether founder hours can grow slower than revenue.

### Timing, risk, and action

- Why now
- 1–3 year window and supporting mechanism
- Invalidation triggers
- Major risks and the corresponding entry, scope, price, channel, or validation change
- 1–3 pivotal unknowns
- Minimum validation, acceptance metric, budget/time limit, and stop condition
- Structural repair variants, when one hard defect masks an otherwise sound structure

## Table 3: Scoring

- Eight dimension scores, weights, and reasons
- `U` cells and why evidence is insufficient
- Known weighted score and plausible interval when useful
- Market Structure, Current Entry, and Overall tiers
- Confidence and any gate/cap applied
- Ranking and reversal condition when comparing options

## Table 4: Evidence registry

Use one row per evidence item:

- claim supported
- source type and title
- URL or local source
- publication date
- checked date
- geography/segment and applicability
- evidence status: fact / inference support / scenario input / conflicting evidence
- strength and limitations

## Table 5: Assumptions and scenarios

Keep model inputs editable and separate from facts:

- price and currency
- customer count
- qualified traffic/leads and conversion
- channel share, platform/payment fees, refunds, and direct tools
- acquisition, fulfillment, support, and maintenance hours
- payment/collection delay
- baseline, upside, and stop scenario
- one-time cash, net cash contribution, and recurring revenue/ARR as separate outputs

## Structural repair display

Highlight repairs inside the affected dimension as **Structural repair**. Show:

- original defect;
- smallest variable changed;
- redesigned atomic business;
- evidence that a changed payer or partner has an unmet need and incentive to buy;
- expected tier/score effect;
- new dependency and tradeoff.

Do not silently merge the redesigned variant into the original.
