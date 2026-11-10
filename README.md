# Idea Validation

**Decide whether a business idea is worth trying with the resources and expectation you have.**

Tell your agent what you’re considering and what you can put into it. A broad idea like “make money with websites” can turn into a few very different businesses. The skill compares who pays, how you reach them, and what it takes to deliver and collect. If you already have a specific offer and buyer in mind, it starts there.

[简体中文](README.zh-CN.md) · [See the website case](examples/website-paths.md) · [Quick start](docs/QUICKSTART.md)

## Try an idea you’re weighing

Install the skill in Codex.

```sh
npx skills add Mingbash/business-opportunity-evaluator --skill idea-validation -a codex
```

The repository URL stays the same. The old `--skill business-opportunity-evaluator` install command remains supported with the same evaluation instructions. Install either name, not both.

Then paste your idea into a new chat. For example:

> Use `$idea-validation` to look at a weekend bicycle repair service that picks up bikes around my town. I have six hours a week. I don’t know yet whether people would pay for pickup.

You’ll get an eight-part assessment, separate grades for the market, your ability to enter, and the overall opportunity, plus one thing to test first. For bicycle pickup and repair, that might be whether riders would pay for pickup after you factor in the round trip.

Give it a broader idea and it will compare up to three concrete paths. Each spells out who pays, what you deliver, how you charge, and where you would find buyers. You’ll see which path to test first and what could change that call.

Earlier releases keep the `business-opportunity-evaluator` name and invocation. You can download those versions from [Releases](https://github.com/Mingbash/business-opportunity-evaluator/releases) and copy the full folder into your agent’s skills directory. That route works without Node.js. [See the install steps and what we tested.](docs/QUICKSTART.md)

## How it looks at an idea

In a September 26, 2026 assessment, I compared three ways to make money from website templates as a side business.

| Path | Who pays and what they get | What I would do first |
|---|---|---|
| General website template | Individuals and small businesses buy a general site layout | Pass. Free and cheap layouts already cover much of the job. |
| Framer kit for one kind of agency project | Small agencies and freelance designers buy a site, reusable components, content examples, and handoff materials | Test this first. Pick one type of project and see if an agency will pay to reuse the kit. |
| Squarespace site for bridal makeup artists | Independent artists and small studios buy a portfolio site with an inquiry and booking flow | Hold production. Show a preview to ten artists and look for two preorders. |

Those were decisions at the time, based on the research and assumptions then available. [Read the full historical case.](examples/website-paths.md)

**The short assessment** starts with the business, date, geography, buyer, and goal. It gives a score or an unknown for each dimension, with the reason.

1. Paid demand and the market you can serve
2. Competitors and alternatives
3. How you reach buyers
4. What it takes to enter and get paid
5. What one sale costs and contributes
6. What you deliver and why the buyer wants it
7. How repeatable the revenue and work are
8. Why now and what could change

You get a market grade, a grade for your current ability to enter, and an overall grade, with confidence shown separately. The recommendation names the first test, the unknowns that matter, and when to stop.

**The full analysis** adds five sections. The decision overview records the preferred entry and what would change it. The opportunity detail traces the buyer, alternatives, acquisition and delivery. The scoring table shows the weights and conditions that limit a grade. An evidence log records which source supports each claim. A separate assumptions and scenarios table lets you see what changes if price, sales or hours differ. [See the complete field list.](skills/idea-validation/references/full-schema.md)

## Why “Help me find a profitable business in 2026” falls short

One of the early answers told me to find clients on a service marketplace. I wrote back, “Just saying ‘service marketplace’ doesn’t solve my problem.” I still needed to know where a real project gets posted, how to recognize a buyer with a problem, and how to get a first customer without a portfolio.

“Sell website templates” leaves the same gap. The website case asks whether a specific buyer would pay for something they could use on a real job. For an agency, that might mean a kit they can reuse across projects. For a bridal makeup artist, it means getting from a portfolio visit to a usable inquiry. Those lead to different tests and different decisions.

## Where it came from

I built this while comparing AI services and digital products. I kept coming back to what would happen between having an offer and getting the first customer to pay. Three notes from those conversations shaped the skill.

> “You've again overlooked acquisition barriers and how welcoming the market is to new entrants.” — September 24, 2026

That brought customer acquisition into the assessment as a question of its own. A buyer list is a starting point. You still have to work out how you’ll reach those buyers and what they already do about the problem.

> “Business is not a science; before execution produces market feedback, research and deduction cannot deliver a conclusion with 100% confidence.” — September 25, 2026

That’s why the review ends with something you can learn from. If pickup fees would make or break the bicycle service, ask riders about the fee before building a booking site.

> “Main-business and side-hustle evaluation rubrics need to be different.” — September 26, 2026

That gave the skill room to weigh a modest cash business on its own terms. The same hours spent on each order matter more when your goal is to grow beyond your own time.

[Read the original notes and design choices.](docs/ORIGIN.md)

## Use it on your own terms

The skill replies in your language and uses the region your business serves. It returns Markdown by default. Ask for a CSV or workbook if you want to compare ideas side by side. You can start with a paragraph in chat, without setting up an account or running Python.

[What we tested](docs/VALIDATION.md) · [Contributing](CONTRIBUTING.md) · [MIT license](LICENSE)
