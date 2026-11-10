# Semantic regression suite

Use this suite only when maintaining or materially revising the skill. Tests judge decision behavior, not exact wording or a predetermined tier. Run prompts in a clean context when practical. A pass requires every invariant listed for that case; unresolved current-market facts may remain `U`.

## Recent failure regressions

### R0 — Turn a broad idea into a shortlist

**Prompt:** I want to make money with websites. I can build a Framer site, have eight hours a week, and can spend US$150. I want my first paid order within a month.

**Pass invariants:**

- Identifies the side-hustle objective and applies the same time, budget and first-sale goal throughout.
- Proposes two or three distinct businesses if plausible, with payer, purchase outcome, deliverable, price mechanism and buyer access for each. Does not grade “websites” as one market or split otherwise identical businesses by platform or channel.
- Gives the eight dimensions, separate market/entry/overall judgments with confidence, a first test and the evidence that could reverse the preference. Uses U or a provisional judgment for unsupported conclusions.

### R1 — Preserve the original atomic business

**Prompt:** Evaluate an AI receptionist sold directly to independent auto-detailing shops through cold outreach.

**Pass invariants:**

- The scored original retains the direct-shop payer and cold-outreach route.
- Any agency, implementer, or reseller version is labeled as a separate structural repair and scored separately.
- A theoretically better repaired version never raises the original's score or tier.

### R2 — Do not manufacture a channel partnership

**Prompt:** Can I sell white-label websites to web-design agencies found in an expert directory?

**Pass invariants:**

- Agencies with the same core delivery capability are treated as competitors or self-sufficient providers by default.
- Cooperation is considered only with evidence of capacity overflow, a specialized technical gap, lower complete cost, geography/language/compliance access, white-label need, or another complementary asset.
- Directory presence proves identifiability only; use U for unestablished distribution rather than assigning a low number solely for missing evidence.

### R3 — Complete the competition and supply analysis

**Prompt:** Evaluate a generic AI phone assistant for local businesses now.

**Pass invariants:**

- Covers direct products, platform-native features, AI/DIY, internal/manual work, and service providers.
- Separates feature availability, adoption/penetration, failure points, and full-job coverage.
- Compares demand growth with substitutable-supply growth and states whether the remaining payable gap is widening or shrinking.
- Does not award Competition 3+ if the payable gap remains unestablished.

### R4 — Do not force unsupported numbers

**Prompt:** One Upwork job and one Etsy product show demand for this offer. Give all eight scores and a tier.

**Pass invariants:**

- Treats each item as occurrence evidence, not market capacity, typical price, or repeatable demand.
- Uses `U` for decision-critical dimensions that cannot be supported.
- Confidence remains separate from tier; no complete-looking total is manufactured from favorable known cells.

### R5 — Keep structural repair separate

**Prompt:** Evaluate direct-to-merchant website building; if it is weak, improve the business.

**Pass invariants:**

- Scores the requested direct model before repairs.
- A changed payer, buyer job, deliverable or revenue mechanism creates a separate atomic variant. A change in channel or delivery method alone creates a named repair route with the affected entry tier evaluated separately.
- Shows the new dependency and evidence needed; never silently merges or score-launders the redesign.

### R6 — Research the ranking-changing unknown first

**Prompt:** Compare five AI-enabled service ideas and choose one. For websites I propose Google Maps plus a tailored prototype and Loom; for podcast clips I propose sampling active mid-sized creators and sending one finished clip.

**Pass invariants:**

- Evaluates the user-proposed routes before substituting agencies or studios.
- Names and researches the 1–2 unknowns most likely to reverse the ranking.
- Does not announce a non-provisional winner while payer need, payable gap, or the only acquisition route is still assumed.
- Uses a bounded public-data sample when it can test the route before asking the user to interview buyers.

## Historical correction regressions

### H1 — Current goal overrides historical choices

**Prompt:** I previously rejected this market, but my objective and available assets have changed. Re-evaluate it.

**Pass invariants:** Treats the old decision as dated context, states the changed assumptions, and gives a replacement judgment with its effect on ranking and action.

### H2 — Do not ask the user to decide what research should decide

**Prompt:** I do not know which of 20 opportunities I prefer. Narrow them using the supplied market, channel, dependency, and cost fields.

**Pass invariants:** Uses objective constraints and available evidence first; does not ask the user to name the winner, contacts, or facts already in the table; after each elimination round, names the opportunities removed and why.

### H3 — Platform gates are part of feasibility

**Prompt:** A digital product appears attractive but its main marketplace may reject sellers from my jurisdiction.

**Pass invariants:** Verifies current eligibility, ownership/control, payment, and practical workarounds; downgrades or reroutes when the gate is not credibly solvable; does not confuse production ease with business feasibility.

### H4 — Business, offer, and channel are distinct

**Prompt:** Evaluate a Discord bot business that could also run on Slack and Feishu.

**Pass invariants:** Defines the buyer job and revenue mechanism independently of platform; treats Discord/Slack/Feishu as channel or deployment variants unless payer/job/revenue changes; avoids inflating the opportunity count.

### H5 — Usage frequency is not purchase frequency

**Prompt:** Compare a wedding-planning product used once per buyer with a pet-care handoff form used daily.

**Pass invariants:** Separates use frequency, repurchase frequency, and flow of new buyers; does not automatically prefer the daily-use product without purchase and willingness-to-pay evidence.

### H6 — Competitors are neither automatic saturation nor automatic opportunity

**Prompt:** A mature quoting product has visible sales in a vertical I do not know. Should I enter?

**Pass invariants:** Uses the competitor as demand evidence and supply pressure; evaluates task coverage, penetration, price, entry gap, incumbent response, and industry know-how acquisition; does not recommend entry merely because a competitor sells.

### H7 — Free and generic AI alternatives must be good enough, not merely present

**Prompt:** Paid and free templates look similar, and a buyer might build the add-on with generic AI.

**Pass invariants:** Tests full-job coverage, reliability, integration, support, acceptance, and switching effort; explains why the paid offer is materially better or concludes that no payable gap is established.

### H8 — Small supply does not prove marketplace opportunity

**Prompt:** A new marketplace has only 23 templates and 20 are paid. Is this a fast-entry opportunity?

**Pass invariants:** Separates low supply from low demand; checks marketplace age, users/traffic, seller access, transactions, external distribution, and demand-to-supply ratio before recommending entry.

### H9 — Model full acquisition and delivery economics

**Prompt:** This service is high-ticket, so only one or two deals are needed; this template needs about 66 monthly sales for $1,000 contribution.

**Pass invariants:** Includes discovery, outreach, trust, sales, collection delay, delivery, revision, support, maintenance, fees, refunds, and founder hours; does not infer attainability from low deal count or arithmetic sales targets.

### H10 — Main business and side hustle use different success criteria

**Prompt:** Compare a scalable subscription company with a small digital-product side hustle.

**Pass invariants:** States objective and currency; evaluates the company on repeatability, ARR, organization, and labor decoupling, and the side hustle on net cash, time, maintenance, and platform risk; does not compare raw scores without explaining the objectives.

### H11 — Distinguish recurring revenue from recurring labor

**Prompt:** A monthly service renews automatically but requires continuing custom production and support.

**Pass invariants:** Does not call it autonomous or software-like merely because billing recurs; states the labor ceiling and separates one-time cash, contribution, recurring revenue, and ARR conditions.

### H12 — Existing assets and current constraints affect entry, not eternal market truth

**Prompt:** I already have a local MVP, limited cash, and no current channel; I once said I disliked another industry.

**Pass invariants:** Credits the reusable MVP in first-sellable investment; includes the current cash/channel constraints in Current Entry; treats prior interests and exclusions as current choices rather than permanent market judgments.

### H13 — Validate value, not feature differentiation

**Prompt:** Incumbents cover the happy path; I can add exception queues, rules, and integrations.

**Pass invariants:** Determines whether the additions are must-have, performance, or delight features; ties them to a material customer-success outcome and budget; considers segment differentiation; recommends no-go when incumbents are already good enough and the remainder is merely nice-to-have.

### H14 — Prefer desktop evidence before expensive validation

**Prompt:** Design research and a POC for two shortlisted opportunities.

**Pass invariants:** Completes available market, competitor, platform, and public-data research first; gives both preferred and fallback options a minimal POC; asks the user for private facts, authorization, or real-world outreach only when those are the remaining decision-changing unknowns.

### H15 — Make the buyer and problem concrete

**Prompt:** The draft says “service market,” “implementation partner,” and “operations automation.” Make it decision-ready.

**Pass invariants:** Names geography, company size, industry, trigger, responsible role, current workflow, loss, buying event, and exact place/action for contact; explains unfamiliar terms and uses a bounded analogy when the relationship remains hard to understand.

### H16 — Risk must change the entry plan

**Prompt:** List the main risks and tell me whether to proceed.

**Pass invariants:** Converts each decisive risk into a narrower segment, offer boundary, price, channel, sequencing change, test, or stop condition; names one preferred option and one fallback; GO means bounded entry, and NO-GO applies to the defined business form rather than the whole industry.

### H17 — Scope market capacity and justify geography

**Prompt:** Estimate the market and choose between China, North America, and Europe for a vertical quoting engine.

**Pass invariants:** Defines payer, geography, segment, price/revenue unit, and exclusions; gives a transparent range or serviceable-capacity estimate rather than false precision; distinguishes global potential, business-model-serviceable capacity, and user-reachable buyers; chooses geography from demand, competition, payment, pricing power, regulation, distribution, and know-how—not merely the user's location.

### H18 — Early evidence, GO, and NO-GO retain their proper meaning

**Prompt:** An early opportunity has competitors and no public revenue history. Is it automatically weak, saturated, or proven?

**Pass invariants:** Does not downgrade solely for missing revenue history, does not infer saturation from competitor presence, and does not infer opportunity from competitor absence; separates fact reliability, entry priority, and scale probability; defines GO as a bounded test rather than a success guarantee and confines NO-GO to the evaluated business form and current constraints.

## Coverage map

| Demonstrated failure class | Regression cases |
|---|---|
| Original atomic business silently replaced | R1, R5 |
| Partner/channel proposed without buying logic | R2, R6, H15 |
| Competition coverage and supply change left incomplete | R3, H6, H7, H13 |
| Scores exceed evidence and unknowns disappear | R4, H3, H8 |
| Structural repair merged into the original | R1, R5 |
| Ranking announced before pivotal validation | R6, H2, H14 |
| Historical user corrections recur | H1–H18 |

## Public portability regressions

### P1 — Local service scope
**Prompt:** Evaluate a weekend bicycle-repair pickup service for one town, as a side hustle.
**Pass invariants:** Retains the local buyer/geography; does not require global TAM; counts travel and founder hours; no unsupported demand claims.

### P2 — No browsing or spreadsheets
**Prompt:** Compare four ideas from supplied notes only. No network or file tools are available.
**Pass invariants:** Gives inline provisional comparison, states evidence limits, uses U where needed, does not require Excel or claim current research.

### P3 — User weights
**Prompt:** Cash in 30 days matters most; weight first cash twice as heavily while preserving other relative weights.
**Pass invariants:** States normalized effective weights, retains evidence gates and unknowns, does not describe scores as success probabilities.
