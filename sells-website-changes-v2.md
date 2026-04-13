# Sells Advisory — PDF vs. Code Differences (Corrected)

Every difference verified by careful comparison of each PDF page against the code. Organized by page.

---

## GLOBAL / SITEWIDE

### 1. Footer — Bottom border should be gold dotted
**PDF:** A gold dotted horizontal line separates the footer columns from the bottom copyright row.
**Code:** `.footer-bottom` has `border-top: 1px solid rgba(255, 255, 255, 0.15)` — a thin white line.
**Fix:** Change to `border-top: 2px dotted var(--gold);`

### 2. Footer — LinkedIn icon should be filled, not outline
**PDF:** The LinkedIn icon in the footer is a FILLED navy/dark circle with white "in" text.
**Code:** `.linkedin-icon` uses `border: 2px solid #fff; background: transparent;` — an outline circle.
**Fix:** Add `background: var(--navy);` to `.linkedin-icon` so it's a filled circle.

### 3. All hero sections (For Buyers, About, Difference, Leadership, Insights, Contact) — Missing actual photos
**PDF:** Every page hero has a real photo on the RIGHT side:
- For Buyers: Two men talking in warehouse/office
- About Sells: Two men looking at a tablet
- Our Difference: Gold Sells diamond stamp/seal close-up
- Leadership Team: Coffee mug with Sells diamond logo, notebook, pen on desk
- Insights: Hands using a tablet
- Contact: Two men (older + younger) with tablets (same as About, extends below hero)
**Code:** All these pages use `<div class="hero-right">Photo placeholder</div>` with no actual image.
**Fix:** Add `<img>` tags with the correct photo for each hero. The images likely need to be added to `images/photos/` if they don't already exist.

### 4. All "Let's Talk" sections (For Buyers, About, Difference, Leadership, Insights) — Missing photo
**PDF:** Every Let's Talk section has the photo of two men (older in light blue, younger in dark) on the LEFT side with gold triangle accents.
**Code:** These pages all use `<div class="photo-placeholder">Photo placeholder</div>`.
**Fix:** Replace each placeholder with `<img src="images/photos/letstalk-people.png" alt="Let's Talk">` styled to fill the container. The Home and For Sellers pages already have this correctly.

### 5. Testimonial sections (For Buyers, About) — Wrong background color
**PDF:** All testimonial sections across every page use a WHITE/light background with gold quote marks and gold triangular accents. They are styled identically to the For Sellers testimonial.
**Code:** The For Buyers and About pages use `.testimonial-section` which has `background: var(--blue)` — a blue background.
**Fix:** Change these to match the For Sellers testimonial style: white background, gold quote marks, gold triangle accent on the right side. Use the `.fs-testimonial` class structure or create a consistent white-background testimonial style for all pages.

---

## HOME PAGE (PDF Page 1)

### 6. Diamond cards — Corner photos are hidden
**PDF:** Each diamond card has small diamond-shaped thumbnail photos visible at the top-left and top-right corners of the visual area. These are clearly visible in the mockup.
**Code:** `.hp-card-corner`, `.hp-card-corner--tl`, `.hp-card-corner--tr` are all set to `display: none`.
**Fix:** Remove `display: none` from all three classes. Style them as small (~25% width) diamond-shaped images using `clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%)`, positioned at the top-left and top-right of each `.hp-card-visual`. Ensure the background-image URLs point to actual photos.

### 7. "The Sells Difference" section — Button style
**PDF:** The "See the Difference" button appears to be a gold OUTLINE hexagonal button on the navy background (the inner area shows navy, not solid gold fill).
**Code:** Uses `class="pill pill-gold"` which is a FILLED gold button.
**Fix:** Change to `class="pill pill-outline"` and ensure `.hp-diff-top .pill-outline::after { background: var(--navy); }` is set (it already is in the code) so the inner fill matches the navy background. Also ensure `.hp-diff-top .pill-outline { color: #fff; }` (also already present).

### 8. Stats bar — Number font size too small
**PDF:** The stat numbers ($3B+, 20+, 100+, etc.) are quite large and prominent — they dominate each stat box visually.
**Code:** `.hp-stat-num { font-size: 2.2rem; }` — this renders smaller than the PDF shows.
**Fix:** Increase to approximately `font-size: 2.8rem;` or `3rem;` to match the PDF proportions.

---

## FOR SELLERS PAGE (PDF Page 2)

### 9. "When the time is right" — Icons need gold circle backgrounds
**PDF:** Each of the four card icons (Retirement Planning, Growth Capital, Business Exit, Partial Cash-out) sits inside a GOLD CIRCLE. The icons are white on gold circular backgrounds.
**Code:** The icons are plain `<img>` tags without any gold circle wrapper.
**Fix:** Wrap each icon in a gold circle container. Add a wrapper div with styles: `width: 70px; height: 70px; border-radius: 50%; background: var(--gold); display: flex; align-items: center; justify-content: center; margin: 0 auto 12px;` and make the icons white/smaller inside (roughly 36-40px). Alternatively, if the icon PNGs already have gold circles baked in, verify they render correctly.

### 10. "Right people" section — Bullet style should use gold diamonds
**PDF:** The professional services list (Accounting, Tax Counsel, etc.) uses small gold diamond bullet markers.
**Code:** `.fs-rightpeople-list` uses `list-style: disc` — standard round bullets.
**Fix:** Remove `list-style: disc` and add custom gold diamond bullets either via `::before` pseudo-elements with `content: '\25C6'; color: var(--gold);` or using the diamond.png image.

---

## FOR BUYERS PAGE (PDF Page 3)

### 11. Intro section — Missing photo
**PDF:** RIGHT side of the intro has a real photo of two businessmen talking.
**Code:** Uses `<div class="photo-placeholder">Photo placeholder</div>`.
**Fix:** Replace with actual `<img>` tag.

### 12. Heading text is wrong — "Invest in people, purpose, and potential."
**PDF:** The centered heading reads "Invest in people, purpose, and potential."
**Code:** Says "Invest in people. Invest with purpose." — completely different text.
**Fix:** Change the heading to exactly: `Invest in people, purpose, and potential.`

### 13. Four-column section — All bullet text is wrong
**PDF:** Each column (Aligned, Strategic, Ethical, Proven) has very specific bullet points. For example:
- **Aligned:** "Focused on defining success beyond the number", "Aligned incentives: our fee structure rewards the best outcome for you", "Long-term relationship mentality vs. transactional", "Protecting what matters: employees, culture, brand, community impact"
- **Strategic:** "Market intelligence: we know who's buying, what they're paying, and why", "Proactive deal positioning—getting ahead of", "Sophisticated buyer targeting and qualification process", "Strategic storytelling: crafting the narrative that maximizes value", "Process tailored to your situation and goals", "Anticipating buyer objections and structuring around them", "Understanding consolidation trends and industry-specific dynamics", "Data-driven approach to valuation and market positioning", "Creating competitive tension to drive optimal terms", "Not just finding a buyer—finding the right buyer"
- **Ethical:** "Transparency in process, pricing, and expectations", "Honest about valuation—we won't overpromise to win business", "Protecting confidentiality throughout the process", "No pressure tactics or artificially rushed timelines", "Clear communication about risks, trade-offs, and deal structure implications", "Integrity in representing your business to buyers", "Fair dealings with all parties while fiercely advocating for our client", "Long-term reputation over short-term fees", "We turn down deals that aren't the right fit", "Compliance with all regulatory and professional standards"
- **Proven:** "$2B+ in closed M&A transactions", "Track record across home services, commercial services, and related industries", "Repeat clients and referral-based growth", "Trusted by both founders and institutional investors", "Deep buyer network cultivated over years of relationship building", "Successfully navigated complex deal structures and negotiations", "Portfolio of closed deals that speak for themselves"
**Code:** Has 4 short generic bullets per column — completely different content.
**Fix:** Replace ALL bullet text with the exact PDF text above. Note the PDF has many more bullets per column (7-10 each) vs. the code's 4 each.

### 14. "Why buyers trust Sells" section — Missing photo and wrong text
**PDF:** LEFT side has a large photo of two businessmen talking in a hallway/industrial setting. RIGHT side has:
- Heading: "Why buyers trust Sells:"
- Body: "Proprietary deal flow. Informed, committed founders and owners. A process built for efficiency—but never at the expense of transparency, integrity, or the human element." and "More than anything, investors and sponsors come back to Sells for a personalized experience that leaves everyone confident, satisfied, and energized about the future."
- "Optimizing Opportunity" sub-section with bullets: "Sells offers access to exclusive deal flow you won't find on the open market", "We foster long-term relationships with founders and owners—often over years", "We understand sellers' psychology and motivations", "We maintain ongoing sourcing partnerships and retainer relationships"
- "Guiding the Process" sub-section with bullets: "Sells offers end-to-end buy-side representation from sourcing to close", "We move with efficiency, precision, and professionalism"
**Code:** Photo is a placeholder. Body text and bullet points are different/rewritten.
**Fix:** Add the actual photo. Replace ALL text and bullets with the exact PDF content above.

---

## ABOUT SELLS PAGE (PDF Page 4)

### 15. Intro section — Text doesn't match PDF
**PDF:** The intro text includes specific language: "Sells is the middle-market investment bank and advisory firm people trust. We specialize in mergers & acquisitions for Main Street, where founders, owners and operators of private businesses can find investors, buyers, and sponsors who align with their priorities and share the desire to create lasting value." It continues about honoring the human element and bringing the relational back to the transactional.
**Code:** The paragraphs are rewritten with different language.
**Fix:** Replace all intro paragraphs with the exact text from the PDF.

### 16. "Above all, we value trust" — Photo missing + paragraph text wrong
**PDF:** LEFT has a real photo of two men. RIGHT has heading "Above all, we value trust." followed by: "Without trust, we're simply doing transactions. Without trust, none of this works. So, everything we do helps create and support an environment of trust where people feel safe, confident, and free to pursue mutually rewarding outcomes. We believe trust happens when we follow these principles:"
**Code:** Photo is placeholder. Paragraph says "Trust isn't just a word in our name..."
**Fix:** Add the actual photo. Replace the paragraph with the exact PDF text.

### 17. "Above all, we value trust" — Numbered principles text is wrong
**PDF:** The three principles have very specific short descriptions:
1. Dignity ·······► Empathy — "Respect for all leads to deeper understanding and connection."
2. Honesty ·······► Alignment — "Transparency and communication lead to shared interests and cooperation."
3. Integrity ·······► Process — "Discipline and precision lead to consistent, repeatable results."
**Code:** The descriptions are multi-sentence paragraphs about 3-4 lines each — much longer and different text.
**Fix:** Replace each description with the single-sentence version from the PDF.

### 18. "Above all, we value trust" — Dotted arrow style between words
**PDF:** The arrow connecting paired words (e.g., Dignity → Empathy) is rendered as a DOTTED LINE leading to a filled arrowhead (·······►), not a simple arrow character.
**Code:** Uses `<span class="arrow">&rarr;</span>` — a plain arrow character.
**Fix:** Replace the arrow with a styled dotted line + arrowhead. Use CSS to create a dotted border with a triangle at the end, or use an inline SVG/image that matches the PDF's dotted-line-to-arrow style.

### 19. Sub-tabs bar — Missing small gold square accent
**PDF:** The sub-tabs bar (The Sells Difference / Leadership Team) has a small gold square/diamond accent at the far right end.
**Code:** No accent present.
**Fix:** Add `<img src="images/patterns/diamond.png" alt="" style="width: 10px; height: 10px; margin-left: 12px;">` at the end of the sub-tabs bar, or use a CSS pseudo-element.

### 20. "Right people" section — Photo is placeholder
**PDF:** RIGHT side shows a real photo (older man in light blue shirt).
**Code:** Placeholder div.
**Fix:** Replace with actual `<img>` tag.

---

## OUR DIFFERENCE PAGE (PDF Page 5)

### 21. Four value blocks — Should NOT be bordered cards
**PDF:** The four items below the diamond diagram (Seller Empathy, Buyer Alignment, Clear Process, Rewarding Outcomes) are clean CENTERED text blocks with NO borders, no card styling. Each has: small italic gold label on top (e.g., "Seller"), large bold heading below (e.g., "Empathy"), then a short centered description.
**Code:** `.value-card` has `border: 1px solid #e0e0e8; border-radius: 8px; border-top: 3px solid var(--gold); text-align: left;` — bordered cards with left-aligned text.
**Fix:** Remove all border, border-radius, and card styling from `.value-card`. Change to `text-align: center; border: none; border-top: none; padding: 20px;`. The headings need restructuring: add a small italic gold label above each heading word.

### 22. Four value blocks — Description text is wrong
**PDF descriptions:**
- Seller Empathy: "Discreet, respectful advocacy that protects your interests"
- Buyer Alignment: "Absolute transparency about strategy and objectives"
- Clear Process: "A smooth, simple pathway to success, led with precision"
- Rewarding Outcomes: "All parties feel confident, satisfied, and energized about their futures long after closing"
**Code:** Each has a 3-4 sentence paragraph of completely different text.
**Fix:** Replace all descriptions with the short single-sentence versions from the PDF.

### 23. "For Sellers, Sells Delivers" — Bullet text is wrong + photo missing
**PDF:** Five specific bullet points: "Principled, Aligned Investors", "Expert Guidance", "Maximum Valuation", "Success on Your Terms", "Support Beyond the Transaction". RIGHT side has a real photo (man in hard hat in manufacturing facility).
**Code:** Six different generic bullet points. Photo is a placeholder.
**Fix:** Replace bullets with the exact five from the PDF. Add the actual photo.

### 24. "For Buyers, Sells Delivers" — Bullet text is wrong
**PDF:** Four specific bullet points: "Proprietary Deal Flow", "Informed, Committed Sellers", "Strategic Alignment", "Value Beyond Price".
**Code:** Six different generic bullet points.
**Fix:** Replace with the exact four bullets from the PDF. Remove the two extra items.

### 25. Gold square accents next to buttons
**PDF:** Small gold square/diamond accents appear next to both the "More for Sellers" and "More for Buyers" buttons.
**Code:** These accents are missing.
**Fix:** Add `<img src="images/patterns/diamond.png" alt="" style="width: 10px; height: 10px; margin-left: 8px; display: inline-block; vertical-align: middle;">` next to each button.

---

## LEADERSHIP TEAM PAGE (PDF Page 6)

### 26. Intro text should be lorem ipsum
**PDF:** The body text under "Leading by serving" is lorem ipsum placeholder text: "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt..."
**Code:** Has rewritten text about "diverse expertise in investment banking, private equity, operations, and entrepreneurship..."
**Fix:** Replace the intro paragraph with the exact lorem ipsum text from the PDF.

### 27. Team member name discrepancy — "Richard Park" vs. "Blake Ashley"
**PDF Page 6 (main grid):** Shows "Richard Park — Chief Revenue Officer" as the 5th team member.
**PDF Page 7 (bio modal thumbnails):** Shows "Blake Ashley — Chief Technology Officer" in what appears to be the same slot.
**Code:** Uses "Richard Park — Chief Revenue Officer".
**Fix:** This is an inconsistency in the PDF itself. Verify with the designer which is correct. If the bio modal (page 7) is the updated version, change to "Blake Ashley — Chief Technology Officer" in both HTML and the `teamData` JavaScript array.

### 28. Bio modal — Left side photo should be hexagonal, not angled rectangle
**PDF (Page 7):** Tyler Sells' photo inside the bio card is displayed in a HEXAGONAL shape with a gold accent bar at the bottom of the hexagon.
**Code:** `.bio-card-left` uses `clip-path: polygon(0 0, 100% 0, 85% 100%, 0 100%)` which creates an angled rectangular shape.
**Fix:** Change the clip-path to a hexagonal shape: `clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)` or similar hexagonal polygon. Add a gold accent bar at the bottom of the hex shape.

### 29. Bio modal — LinkedIn icon style
**PDF:** The LinkedIn icon in the bio modal is a filled navy/blue circle with white "in" text — not just a text link.
**Code:** Uses a small inline circle element with outline styling.
**Fix:** Make the LinkedIn icon a filled circle: `background: var(--blue); color: #fff; border-radius: 50%; width: 36px; height: 36px;` centered with "in" text.

### 30. Bio modal — Gold square accent in top-right of card
**PDF:** There's a small gold square/diamond icon in the upper-right area of the bio card.
**Code:** Not present.
**Fix:** Add a small gold diamond image positioned absolutely in the top-right corner of `.bio-card-right`.

### 31. Bio modal — Thumbnail count
**PDF:** The bio modal shows 4 hexagonal thumbnails at the bottom for navigating between team members.
**Code:** Only has 4 `.bio-thumb` elements, but there are 8 team members.
**Fix:** Add thumbnails for all 8 team members, or at minimum ensure the thumbnails update dynamically to show the other team members when navigating.

### 32. "Right people" section — Photo is placeholder
**PDF:** RIGHT side shows a real photo of an older man in a light blue shirt.
**Code:** Placeholder div.
**Fix:** Replace with actual `<img>` tag.

---

## INSIGHTS PAGE (PDF Page 8)

### 33. Intro text should be lorem ipsum
**PDF:** Body text under "Intelligence at your disposal." is lorem ipsum.
**Code:** Has rewritten text about "market trends, transaction best practices..."
**Fix:** Replace with the exact lorem ipsum from the PDF.

### 34. Filter tabs — Should be plain text with "/" separators, not pill buttons
**PDF:** "Filter by: All / Sellers / Buyers / News" with a gold diamond at the end. Filters are separated by forward slash characters. They are PLAIN TEXT, not rounded pill buttons.
**Code:** `.filter-tab` has `border-radius: 50px; border: 2px solid #ddd; background: #fff;` — styled as pill buttons.
**Fix:** Remove border, border-radius, and background from `.filter-tab`. Change to plain text styling. Add "/" separator characters between filter options in the HTML. Active state should be gold text color or underline only. Add a small gold diamond image after the "News" filter.

### 35. Insight cards — All should use identical placeholder text
**PDF:** ALL 9 cards use the exact same placeholder text:
- Headline: "Headline of post goes in this style above the summary"
- Description: "Summary of blog post or the first 2 lines of the blog that will be automatically populated here by default based on the actual content within the post itself."
**Code:** Each card has unique different headlines and descriptions.
**Fix:** Replace all 9 card headlines and descriptions with the identical placeholder text from the PDF.

### 36. Insight cards — All text should be centered
**PDF:** The headline, description, and "Read More" button within each card are CENTER-ALIGNED.
**Code:** There's no explicit `text-align: center` on `.insight-card` — text defaults to left-aligned.
**Fix:** Add `text-align: center;` to `.insight-card`.

---

## BLOG POST PAGE (PDF Page 9)

### 37. Blog post intro text should be lorem ipsum
**PDF:** The blog post body text is all lorem ipsum placeholder text.
**Code:** Also uses lorem ipsum. This matches — no change needed.

### 38. Blog post sidebar — Navy arrow/chevron
**PDF:** The sidebar has a navy blue right-pointing arrow/chevron shape at the top-right area, above the Sells logo.
**Code:** No arrow/chevron element present in the sidebar.
**Fix:** Add a navy blue right-pointing arrow shape (can use CSS `clip-path` or an image) positioned at the top of the sidebar, above the Sells logo.

---

## CONTACT PAGE (PDF Page 10)

### 39. Contact page hero — Photo extends below hero into content area
**PDF:** The Contact page has a UNIQUE layout where the hero photo on the RIGHT side extends DOWN below the navy hero section into the white content area below. There's a gold diagonal stripe where the photo transitions. The photo continues alongside the Address/Office Line info on the right.
**Code:** Uses the standard `.hero` class with a separate content section below. The photo doesn't extend down.
**Fix:** This requires significant layout restructuring. The hero photo needs to extend below the hero using negative margin, absolute positioning, or by combining the hero and content sections into a single layout grid. The photo should span from the hero top all the way down to roughly where the Address section ends, with a gold diagonal stripe accent.

### 40. Contact page — "Let's Talk" heading is in gold, not navy blue
**PDF:** The "Let's Talk" heading on the contact page is in GOLD color.
**Code:** Uses `.section-heading.text-gold` which should render gold — verify this renders correctly. The code has `<h2 class="section-heading text-gold">Let's Talk</h2>` which appears correct.
**Fix:** Verify rendering. This may already be correct.

### 41. Contact page — Form field layout doesn't match
**PDF:** Form layout is two columns side by side:
- LEFT column: All 6 input fields stacked vertically (First Name*, Last Name*, Title, Company*, Email*, Phone*)
- RIGHT column: "How can we help?" textarea spanning the full height
- Submit button centered below both columns
**Code:** Has First Name + Last Name side-by-side in a 2-column grid, then Title full-width, then Company full-width, then Email + Phone side-by-side.
**Fix:** Restructure the form to use a simple two-column grid: `grid-template-columns: 1fr 1fr;` with all 6 input fields in a stacked left column and the textarea in the right column.

### 42. Contact page — Address/Office Line is positioned next to the photo, not next to the form
**PDF:** The Address and Office Line info appears on the RIGHT side, below/alongside the extended hero photo. It's NOT in a 2-column layout with the form — instead, the form takes up the LEFT portion and the Address info is further RIGHT, visually tied to the photo area.
**Code:** Uses `two-col-55-45` putting the form on the left and address immediately to its right.
**Fix:** The address info needs to be repositioned to align with the right side of the page where the hero photo extends. This likely requires a 3-zone layout: form fields (left), textarea (center-left), photo+address (right).

---

## ITEMS FROM ORIGINAL LIST THAT WERE WRONG (REMOVED)

- ~~Original #2 "Contact button should be rounded pill"~~ — WRONG. The PDF clearly shows a hexagonal/diamond-pointed shape for the Contact button. The code's clip-path approach is correct.
- ~~Original #6 "Gold color might need adjustment"~~ — Speculative. Removed unless visually confirmed.
- ~~Original #37 about `<em>` tag~~ — The code already handles this correctly.
- ~~Original #56 partial description~~ — Replaced with more precise item #41 above.

---

## SUMMARY OF HIGHEST-IMPACT CHANGES

**Missing photos (affects 6+ pages):** Items 3, 4, 11, 16, 20, 23, 32
**Wrong body text (affects 5+ sections):** Items 12, 13, 14, 15, 17, 22, 23, 24, 26, 33, 35
**Layout/styling differences:** Items 6, 7, 8, 9, 10, 21, 28, 34, 36, 39, 41, 42
**Wrong background colors:** Item 5
**Missing decorative elements:** Items 19, 25, 30, 38
**Footer fixes:** Items 1, 2
