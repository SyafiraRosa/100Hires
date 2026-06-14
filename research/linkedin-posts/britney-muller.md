# LinkedIn Posts: Britney Muller

**Expert:** Britney Muller  
**LinkedIn Profile:** https://www.linkedin.com/in/britneymuller/  
**Collection Date:** June 2026  
**Source Type:** Manual collection of latest posts

---

## Post 1

**Date:** Early 2026  

> **ImageNet: How AI Learned to See**
>
> Before Gemini or Claude could "see" your images, there was ImageNet. In 2009, Stanford researcher Fei-Fei Li and her team built a dataset of 14 million images...
>
> What nobody talks about: what was IN those 14 million images? ImageNet didn't just have dogs and coffee mugs. It had a "person subtree" with 2,832 categories. Many included racial slurs, sexual slurs, and deeply offensive labels...
>
> These weren't edge cases buried in metadata! These were active labels training computer vision models. Models powering facial recognition, content moderation, hiring tools, surveillance, ETC. If a model is trained on slurs as category labels, that bias bakes into every downstream app.
>
> This isn't just AI history. Every AI visual tool in your marketing stack descends from this ecosystem. When a brand monitoring tool misidentifies people, when an image recognition API works better for some skin tones than others, when AI-generated stock photography defaults to narrow stereotypes, these aren't random bugs. They're reflections of what was (and wasn't) in the training data.
>
> AI tools are only as fair and accurate as the data they were trained on. When you spot something, say something. These systems don't fix themselves.

**Key Insight for AI-SEO Production:** For an Applicant Tracking System (ATS) company like 100Hires, the concept of "baked-in bias" in AI is critical. When generating AI content about "hiring best practices" or using AI to generate stock imagery for the blog, we must manually intervene to ensure the content does not inadvertently reflect historical hiring biases. AI is a tool for efficiency, but human editorial review is required for ethical alignment.

---

## Post 2

**Date:** Early 2026  

> **Context Window = AI's Working Memory**
>
> Ever had AI seem to "forget" instructions you gave it earlier in a long conversation? This is why: The context window is the amount of text, in tokens, that an AI model can consider at any one time...
>
> But here's what most people miss: bigger isn't always better! As the context window grows, model performance can actually start to degrade.
>
> There’s also a quirk called "Lost in the Middle": Models perform best when relevant information is toward the beginning or end of the context. Information buried in the middle is more likely to be missed or underweighted, even when it's technically 'in' the conversation.
>
> The same principle applies beyond research and writing: This is also why vibe coding tools like Base44 or lovable might break mid-build. You throw your entire app idea at it in one go, the context fills up fast & it loses track of what it was supposed to build.
>
> [Workarounds include:] Prompting for a summary and a new chat; using Claude Code's /compact command to retain specific info; using Claude to create a project spec sheet and feeding chunks one at a time.

**Key Insight for AI-SEO Production:** This dictates our AI prompt engineering SOP at 100Hires. Because of the "Lost in the Middle" phenomenon, we cannot feed an LLM a massive 15-page competitor research document and ask it to write a full comparison page in one shot. The workflow must be chunked: Generate the outline -> Feed context for Section 1 -> Generate Section 1 -> Feed context for Section 2, etc.

---

## Post 3

**Date:** Early 2026  

> **Stop Using Generic CTR Curves. Build Your Own in 60 Seconds**
>
> Many SEOs are still using industry agnostic CTR curves from 2020? Think about how much has changed since then. AI Overviews. Featured snippets everywhere. Completely different SERPs.
>
> The problem with generic CTR curves: they're averages across thousands of sites and industries, but your client's site is not average! A B2B SaaS brand and a local dentist have wildly different CTR curves. Especially when you break it down by brand vs. non-brand queries.
>
> The fix is simple. You already have the data sitting in Google Search Console. Export your queries. Upload your Queries.csv export to the below Colab Notebook. Get YOUR actual CTR curve broken out by brand and non-brand in SECONDS.
>
> Once you have your real numbers you can: Build way more accurate traffic projections, set realistic goals, estimate competitor traffic, and re-run quarterly to see how SERP changes are impacting your clicks.

**Key Insight for AI-SEO Production:** With AI Overviews (AIOs) dramatically altering click-through rates, relying on generic CTR studies is dangerous for forecasting. 100Hires needs to build its own proprietary CTR curve using GSC data and a Python/Colab script to accurately project the ROI of our AI content production efforts.
