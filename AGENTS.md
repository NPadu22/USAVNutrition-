# AGENTS.md: USA Volleyball Nutrition app

Instructions for AI coding agents (Codex, Claude, etc.) and developers working in this repository.

## What this is

A private, mobile-first web app for USA Volleyball national team athletes (all adults), run by the USAV sports dietitian. Hosted free on GitHub Pages from the `main` branch root. There is no build step and no framework: plain HTML, CSS and JavaScript.

## Files

- `index.html`: the whole app (styles, markup and script in one file).
- Image files sit next to `index.html`: `logo.jpg`, `usa-mark.png`, `qr-code.png` and the education graphics (`guide-*.jpg`).
- `manifest.webmanifest`, `icon-*.png`: home-screen app install.
- `README.md`: how the dietitian updates content.

## Where content comes from

Menus, smoothies, recipes, court snacks, stations, announcements and settings load at runtime from a Google Sheet (`CONFIG.sheetId` in `index.html`) through
`https://docs.google.com/spreadsheets/d/<id>/gviz/tq?tqx=out:csv&sheet=<Tab>`.
See `loadSheet()` near the end of the script. The JSON in `<script id="af-data">` is only the fallback if the sheet can't load.

- **Do not rename sheet tabs or column headers in code.** The dietitian edits the sheet directly. Tabs: Settings, Announcements, Breakfast, Lunch, Stations, Smoothies, Recipes, Snacks.
- Menus rotate by date from `Rotation start` (a Monday). Each tab has its own cycle length (the number of weeks in that tab). No pausing.
- Dinner is never served at the facility. The "Away from the facility" section (`DINNERS` in the script) covers dinners and weekends.

## Content kept in code

- `CONFIG`: WhatsApp number and username, Calendly booking link, sheet ID.
- `FAQ`: Learn tab "Quick answers". **Every answer must cite a real, verifiable source** (position stand, consensus statement or peer-reviewed study). Never invent citations.
- `GUIDES`: Learn tab visual guides. Each has a topic (`k`), title, one-line summary, image path and full alt text.
- `SESSIONS`, `POSITIONS`, `ALLERGENS` (the 9 major US allergens).

## Rules

- **Allergens are safety-critical.** Never remove the allergen line, the red flag for an athlete's own allergens, the "Confirm allergens" note for unconfirmed items, or the allergy review step after setup.
- **Privacy:** athlete profiles (including allergies), session requests and food feedback are sent only to the RD's Google Form inbox (`CONFIG.inboxForm`, `sendInbox()`), which the RD approved. Journal entries stay in the athlete's browser. Never send athlete data anywhere else, and never store it in this repo or the content sheet.
- No calorie or macro tracking for athletes. The journal is intentionally a food journal only.
- Keep supplement content anti-doping safe: third-party tested (NSF Certified for Sport or Informed Sport), and check with the RD first.
- Brand (USAV brand book): Pantone 187C red `#A6192E`, 2768C navy `#071D49`, white, 117C gold `#C99700`. Keep the logo on its white tile with clear space. Don't recolor, stretch or redraw the logo.
- Design language: rounded, calm, content-first. Lineup-card menus, amber scoreboard digits, five gold stars, OLED-friendly dark mode with a light mode. Respect `prefers-reduced-motion`.
- Must work at phone width (about 390 px) in dark and light mode, with no horizontal scrolling.
- Keep everything static: no server, no build tools and no paid services.
- The in-app content editor (`vEdit`, `publishData`, `window.claude`) only works when hosted on Claude. On GitHub Pages it stays hidden. Leave it in place or remove it cleanly; don't half-remove it.

## Keeping the offline backup in sync

`<script id="af-data">` is what athletes see if the sheet can't load. After any sheet change, export every tab (header row included) to a JSON file `{tab: [[...],[...]]}` and run `python3 tools/sync_fallback.py index.html tabs.json`. It runs the app's own sheet loader against those rows, so the backup always matches what the live sheet produces.

## Before you finish a change

1. Open `index.html` locally and check Home, Food (all tabs), Journal, RD, Learn and Me with a sample profile.
2. Check the browser console for errors.
3. Keep the sheet loader working: the app must still render if the sheet fails to load.
