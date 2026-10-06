# Fluent in Kid

A slang phrasebook for parents. Pick your generation (Boomer, Gen X, Millennial, Gen Z) and your kid's (Gen Z, Gen Alpha, Gen Beta), and every term is explained with the slang you grew up with.

- **Decoder**: paste what your kid said; slang is highlighted and translated into your generation's terms.
- **Phrasebook**: 55 terms with pronunciation, an example, a "back in your day" equivalent, how current it is, and whether a parent should ever say it. Some words carry a heads-up for parents.
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
