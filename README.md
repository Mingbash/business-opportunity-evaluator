# Business Opportunity Evaluator

**Decide whether a business idea is worth trying with the time and money you have.**

Tell your agent what you want to sell, who would pay, and what you can put into it. The skill looks at the market and your own path to a first sale. It shows which parts of the case are supported, where you'd be guessing, and what you could test before committing more.

[简体中文](README.zh-CN.md) · [See a worked example](examples/local-service.md) · [Quick start](docs/QUICKSTART.md)

## Try an idea you’re weighing

Install the skill in Codex.

```sh
npx skills add Mingbash/business-opportunity-evaluator --skill business-opportunity-evaluator -a codex
```

Then paste your idea into a new chat. For example:

> Use `$business-opportunity-evaluator` to look at a weekend bicycle repair service that picks up bikes around my town. I have six hours a week. I don’t know yet whether people would pay for pickup.

You’ll get a short assessment and a suggested next step. In this case, it might start with whether local riders would pay for pickup and whether the round trip leaves enough time for repairs. Ask for a deeper, sourced review if you want to go further.

You can also download the skill from [Releases](https://github.com/Mingbash/business-opportunity-evaluator/releases) and copy the full folder into your agent’s skills directory. That route works without Node.js. [See the install steps and what we tested.](docs/QUICKSTART.md)

## How it looks at an idea

The assessment starts with one offer and one kind of buyer. It follows the work from reaching that buyer through getting paid, including the hours you’ll spend selling and delivering. You get separate judgments on the market, your ability to enter, and the overall opportunity.

The eight criteria use adjustable weights. A Saturday side gig can look very different if you need it to replace a salary. The S–F grades summarize the case as it stands. Missing evidence stays visible, and a review based on your notes is provisional until you check the market.

## Where it came from

I built this while comparing AI services and digital products. I kept coming back to what would happen between having an offer and getting the first customer to pay. Three notes from those conversations shaped the skill. These are translations from Chinese.

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
