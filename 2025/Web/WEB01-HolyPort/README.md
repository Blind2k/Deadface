## Description

Players will be given a PDF file. The flag is embodied and divided into three UTF-8 characters. This technique was published by Paul Butler.

Points: **30**
Created by: @blind2k
Dependency: N/A
Attempts: N/A

## Challenge

> Mirveal landed an interview at Spooky Coffee using a resume that whispers in Unicode and charms every AI it touches. Those who can read between the glyphs say it speaks in riddles, crafted to bypass filters and impress any CAPTCHA-checking HR daemon.
>
> Analyze the resume PDF. Can you find Mirveal secret string? Enter the answer as flag{here\_is\_the_answer}.
>
> [Download PDF](https://tinyurl.com/2x2e7jpv "‌")
>
> SHA1: `ca123313ffe8e0d04d8ec5492c507f6ef37194eb`

## Hints

1. The flag `deadface{i_COuLD_ENJOy_A_pIzzA_rIGHt_NOw}` is fake.
2. Do you know that exiftool can dump the binary of a specific Metadata?
3. In 2024, a cybersecurity researcher discovered it was possible to obfuscate a string inside an Emoji. That string can hide inside UTF-8 characters.

## Solution (updated by @syyntax )

After downloading the PDF, players should extract the file’s Metadata using `exiftool`.

```
exiftool lambiresume.pdf
```

The flag is inside the `User Comment` value, where an emoji and extra characters are shown.

![image.png](https://trello.com/1/cards/6836e768d48105c234279911/attachments/68e860745ddd294753d18288/download/image.png)

If the flag is broken/not full. Give hint #2.

```
exiftool -b -UserComment lambiresume.pdf | xxd
```

I added a [GhostTown thread](https://ghosttown.deadface.io/t/whispering-through-emojis "‌") that brings up “Mr. Butler” (aka Paul Butler) to help guide players in this direction.

Go to [this link](https://emoji.paulbutler.org/?mode=decode "‌") and:

- Make sure it’s on **decode**.
- Paste the emoji.

![image.png](https://trello.com/1/cards/6836e768d48105c234279911/attachments/68e860ca4b81f5c4b0ba2216/download/image.png)

## Flag

`deadface{Look_@_m3!!!}`