# Knowlet profile design

An original visual identity for [Albert Hsieh / knowlet](https://github.com/knowlet).

The profile uses a geometric wordmark, a wireframe signal sculpture, quiet motion,
and four project panels. The editorial direction follows the public portfolio:
systems, security, and applied AI. It does not claim employment, performance
numbers, production readiness, or private contact information.

## Editing

The profile itself is `README.md`. The public default branch is `develop`.
All image paths are relative, so a review branch renders its own assets.

Rebuild the original assets with Python 3.10 or later; no packages or network
access are required:

```sh
python3 scripts/build_identity.py
python3 scripts/build_cards.py
```

Edit the identity colors, copy, and paths in `scripts/build_identity.py`.
Edit project titles, descriptions, and symbols in `scripts/build_cards.py`.
Keep image alt text and the Markdown project index in sync with the cards.

Desktop and mobile compositions are independent, with dark and light palettes.
The `<picture>` sources select the compact composition below 640 CSS pixels and
the appropriate color scheme. The light image is the default fallback.
The hero's only animation is a slow signal on the outer ring; the SVG disables
that motion when `prefers-reduced-motion: reduce` matches.

Assets are committed SVGs. They contain no script, `foreignObject`, external
images, external fonts, analytics, live metrics, or service-dependent cards.
The wireframe is decorative artwork, not a diagram of a real deployed system.

## Visual system

| Token | Dark | Light |
| --- | --- | --- |
| Surface | `#0b1418` | `#f3f6f2` |
| Text | `#edf5ee` | `#122d2a` |
| Secondary text | `#9ab1b5` | `#536864` |
| Rule | `#24373c` | `#d1ddd7` |
| Accent | `#cbf278` | `#497323` |
| Signal | `#66d7ca` | `#007e78` |

The KNOWLET wordmark is drawn as original paths. Supporting text uses local
sans-serif and monospace fallbacks. Project panels are full-width links; the
same descriptions also appear in accessible alt text and a real Markdown index.

## References

These informed the information hierarchy and GitHub implementation. The visual
assets and code in this repository were created specifically for knowlet;
no template artwork or source code was copied.

- [GitHub's profile README quickstart](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github): `<picture>`, theme variants, alt text, and expandable sections.
- [GitHub's writing syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax): relative image paths.
- [GitHub Markup](https://github.com/github/markup): the HTML sanitization boundary.
- [W3C SVG 2 processing modes](https://www.w3.org/TR/SVG2/conform.html#secure-animated-mode): animation in SVG image contexts.
- [Anthony Fu](https://github.com/antfu/antfu): concise destination navigation.
- [Braydon Coyer](https://github.com/braydoncoyer/braydoncoyer): a locally hosted hero and short introduction.
- [Simon Willison](https://github.com/simonw/simonw): concrete project descriptions with traceable links.
- [Sindre Sorhus](https://github.com/sindresorhus/sindresorhus): a consistent personal visual language.

## Public sources for profile copy

Reviewed on 2026-10-19. Recheck repository READMEs before changing maturity or
compatibility claims.

- [Public identity and destinations](https://github.com/knowlet)
- [rdp2vnc](https://github.com/knowlet/rdp2vnc/blob/develop/README.md)
- [Panelshift](https://github.com/knowlet/panelshift/blob/develop/README.md)
- [AgentWorld Web Simulator](https://github.com/knowlet/agentworld-web-simulator/blob/develop/README.md)
- [RPGDynamicTranslation](https://github.com/knowlet/RPGDynamicTranslation/blob/main/README.md)
- [JevGuard-NSFA](https://github.com/knowlet/JevGuard-NSFA/blob/develop/README.md)
- [MasqueCat](https://github.com/knowlet/MasqueCat/blob/main/README.md), a fork of [tailscale/tailcat](https://github.com/tailscale/tailcat)
- [Blog](https://knowlet3389.blogspot.com/) and [talk archive](https://slides.com/knowlet)
