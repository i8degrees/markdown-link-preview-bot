---
---

# TODO

This is the project's initial TODO list. Items beyond this list **must** be 
filed at the official project web site at [i8degrees/markdown-link-preview-bot: Issues][0].

## general

- [ ] consider limiting the number of returned Markdown links to ~10.
- [ ] finish Docker build scripts
- [ ] document the user-defined env variables for tweaking bot
    - `DEBUG`
    - `EXPERIMENTAL`
    - `SUPPRESS_EMBED`
    - `DISCORD_BOT_TOKEN`
- [x] give example input and output of this script in the `README.md`
- [ ] finish re-structuring our project `README.md`
- [x] split the non-Discord bits of code out to another source file
- [x] ensure that our `requirements.txt` syntax is correct
- [x] ensure that we are using a [Docker image without any known
vulnerabilities][1] as per the report seen inside of vscode

[0]: https://github.com/i8degrees/markdown-link-preview/issues
[1]: https://hub.docker.com/layers/library/python/3.14-slim-trixie/images/sha256-ac25e5afbfdb4a94ff99cc24b0345719210133144481480bcba6085efa36a341

