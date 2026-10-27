<!-- note_key: c843f0a5e020 -->
<!-- note_type: AnkiOpsQA -->
Q: Welcome to AnkiOps!
A: Anki decks ↔ Markdown files, in perfect sync
E: Edit in your text editor, review in Anki.

![](<media/sync_arrows.png>){width=150}
M: Neat!

---

<!-- note_key: fab3cd657339 -->
<!-- note_type: AnkiOpsCloze -->
T: AnkiOps supports {{c1::cloze deletions}} and even {{c1::multiple}} {{c2::clozes}} in one card.

---

<!-- note_key: 814beddbdd28 -->
<!-- note_type: AnkiOpsChoice -->
Q: What is this?
C1: A multiple choice question
C2: with
C3: automatically randomized answers.
A: 1,3
E: The order changes dynamically between each review.

---

<!-- note_key: 3832c0a5c9cc -->
<!-- note_type: AnkiOpsQA -->
Q: What Markdown features are supported?
A: **Bold text**, *italic text*, ==highlighted text==, ~~strikethrough~~, `inline code`,

> blockquotes,
> another one,

1. ordered lists,
   - even nested unordered items,

| Beautiful | Tables, |
| --- | --- |
| inline formula: | \(E = mc^2\), and |

\[\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi},\] and, of course, code blocks:

```python
def truth():
    print("AnkiOps is awesome")
```
E: *Everything renders beautifully on desktop and mobile.*

---

<!-- note_key: e6943cbd4780 -->
<!-- note_type: AnkiOpsQA -->
Q: How do I get started?
A: Run `ankiops fa` to sync files --> Anki

Run `ankiops af` to sync Anki --> files
E: ==Note==: AnkiOps only acts on note types defined within the `note_types/` folder.

Check the README for detailed documentation!
