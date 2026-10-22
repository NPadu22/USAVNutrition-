# USA Volleyball Nutrition

Athlete nutrition app for USA Volleyball national team athletes: menus, smoothies, court snacks, a food journal, nutrition answers and RD booking.

## Updating content (no coding)

Menus, smoothies, recipes, court snacks and announcements come from the Google Sheet **USAV Nutrition App Content**. Edit the sheet and athletes see the change the next time they open the app. The "How to edit" tab in the sheet explains each column.

Rules that keep it working:
- Don't rename the tabs or the header row.
- Week = 1, 2, 3…; Day = Mon–Fri.
- Allergens: Dairy, Egg, Wheat/Gluten, Peanut, Tree nut, Soy, Fish, Shellfish, Sesame (comma separated).
- Smoothie flavor names must match the Recipes tab exactly.
- Keep the sheet's sharing at "Anyone with the link can view".

If the sheet can't be reached, the app falls back to the content built into `index.html`.

## Settings in `index.html`

Near the top of the script, `CONFIG` holds:
- `whatsapp`, `whatsappUser`, `whatsappLink`: Nutrition 411 contact
- `bookingLink`: Calendly page
- `sheetId`: the Google Sheet ID (the long code in the sheet's address between `/d/` and `/edit`)

## Privacy

Athlete profiles, allergies and food journal entries stay on each athlete's phone. Nothing about athletes is stored in this repository or in the content sheet.

## Hosting

Served with GitHub Pages from the `main` branch root.
