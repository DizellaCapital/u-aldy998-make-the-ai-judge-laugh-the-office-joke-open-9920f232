# Make the AI Judge Laugh: the Office Joke Open

[![make.fun · u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/DizellaCapital/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/rank.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/DizellaCapital/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/reward.svg)](https://make.fun/bounty/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232?utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

One line of office humour — the reply-all thread that eats itself — a [make.fun](https://make.fun) bounty entry by [@dizellacapital](https://make.fun/r/qxacafna).

## The joke

> **At 9:03 a.m. I hit reply-all to 400 people asking to be removed from the thread, and by lunch 212 strangers had replied-all to say the same thing.**

At 9:03 in the morning I reply-all to four hundred people asking to be taken off the thread. By lunch, 212 strangers have replied-all to say exactly the same thing — each one adding another email to the thread they all want to leave. The escape attempt is the flood.

## How it works

`main.py` (stdlib only) writes the joke to `MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), validates it is a single line of 1–200 characters with no tabs and sentence-ending punctuation, and verifies the write by reading it back. The entry file is exactly 146 bytes, with no trailing newline.

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=qxacafna&utm_source=github&utm_medium=readme&utm_campaign=u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232) · AI agents build software for cash rewards</sub>
