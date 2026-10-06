# Fluent in Kid

A slang phrasebook for parents. Pick your generation (Boomer, Gen X, Millennial, Gen Z) and your kid's (Gen Z, Gen Alpha, Gen Beta), and every term is explained with the slang you grew up with.

- **Decoder**: paste what your kid said; slang is highlighted and translated into your generation's terms.
- **Phrasebook**: 87 terms (updated October 2026) with pronunciation, an example, a "back in your day" equivalent, how current it is, and whether a parent should ever say it. Some words carry a heads-up for parents.
- **Pop quiz**: five words from your kid's generation.
- **Words I heard**: jot down new slang to decode later (stored in your browser).

## Run it on your network

```bash
python3 serve.py          # default port 8080
python3 serve.py 3000     # or pick a port
```

Open the printed `http://<your-ip>:<port>` address on any device on the same Wi-Fi. Edits to `fluent-in-kid.html` show up on refresh.

The "Ask Claude" button only appears when the page is opened as a claude.ai artifact.

## Adding words

Add an entry to the `TERMS` array in `fluent-in-kid.html`. Each entry has the term, pronunciation, meaning, an example, an equivalent for each parent generation (`b`, `x`, `m`, `z`), and a "should you say it" rating.

## Sources for the October 2026 update

- [The Top 24 Gen Alpha Slang Terms of 2026](https://www.mentalfloss.com/language/slang/top-gen-alpha-slang-2026), Mental Floss, Sept 19 2026
- [Google searches reveal most confusing Gen Alpha slang terms of 2026](https://traveltomorrow.com/google-searches-reveal-most-confusing-gen-alpha-slang-terms-of-2026/), Travel Tomorrow, Sept 30 2026
- [Scuba, Crine and Larping](https://mix97.com/2026/09/28/scuba-crine-and-larping-a-guide-to-slang-you-might-hear-in-2026/), Mix 97, Sept 28 2026
- [SC's most searched school-year slang terms can help spot bullying](https://abcnews4.com/news/local/scs-most-searched-school-year-slang-terms-can-help-spot-bullying), ABC News 4, Aug 2026
- [2026 Teen Slang & Text Codes](https://www.bark.us/blog/teen-text-speak-codes-every-parent-should-know/), Bark, July 2026
- [Most-searched slang words of 2026](https://thehill.com/blogs/in-the-know/6059615-these-are-the-most-searched-slang-words-of-2026-how-many-do-you-know/), The Hill (Google Trends, Jan–Aug 2026)
- [New Year, New Slang 2026](https://social.colostate.edu/best-practices/new-year-new-slang-words-social-media-managers-should-know-in-2026/), Colorado State University, Jan 2026
- [100+ Teen Slang Words 2026](https://www.weareteachers.com/teen-slang/), WeAreTeachers
- [Teen slang parent guide](https://axis.org/resource/a-parent-guide-to-teen-slang/), Axis
