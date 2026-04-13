#!/usr/bin/env python3
"""
Comprehensive update script to make website match PDF mockup.
Implements all visual differences from the comparison document.
"""

import os

base = '/Users/jackschnall/Desktop/sells-advisory'
filepath = os.path.join(base, 'index.html')

with open(filepath, 'r') as f:
    html = f.read()

count = 0

def R(old, new, desc=''):
    global html, count
    if old not in html:
        print(f"WARNING: Not found — {desc}")
        return False
    html = html.replace(old, new, 1)
    count += 1
    print(f"  OK [{count}]: {desc}")
    return True


# ============================================================
# CSS CHANGES
# ============================================================
print("\n=== CSS CHANGES ===")

# 1. Add hero-right photo support + new CSS classes before </style>
R(
    '  </style>\n</head>',
    """    /* Hero right photo support */
    .hero-right.has-photo {
      background: none !important;
    }
    .hero-right.has-photo img.hero-bg {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: 0;
    }
    .hero-right.has-photo .hero-bar {
      z-index: 2;
    }

    /* Testimonial light variant (white/light bg) */
    .testimonial-light {
      background: #fff;
      padding: 60px 0;
      text-align: center;
      position: relative;
      overflow: hidden;
    }
    .testimonial-light::before {
      content: '';
      position: absolute;
      top: 0;
      right: 0;
      width: 300px;
      height: 100%;
      background: var(--gold);
      clip-path: polygon(40% 0, 100% 0, 100% 100%, 0% 100%);
      z-index: 0;
    }
    .testimonial-light .container {
      position: relative;
      z-index: 1;
    }
    .testimonial-light .testimonial-marks {
      color: var(--gold);
    }
    .testimonial-light .testimonial-quote {
      color: var(--navy);
    }
    .testimonial-light .testimonial-author {
      color: var(--navy);
    }
    .testimonial-light .testimonial-company {
      color: var(--text-muted);
    }

    /* Value cards 4-column layout */
    .value-cards-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
      text-align: center;
    }
    .value-card-slim {
      text-align: center;
      padding: 0 8px;
    }
    .value-card-slim .card-label {
      font-family: var(--font-heading);
      font-style: italic;
      font-size: 0.95rem;
      color: var(--navy);
      margin-bottom: 2px;
    }
    .value-card-slim h4 {
      font-family: var(--font-heading);
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--navy);
      margin-bottom: 10px;
    }
    .value-card-slim p {
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.5;
    }
    @media (max-width: 768px) {
      .value-cards-row {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    /* Filter tabs plain text style (matching PDF) */
    .filter-plain {
      display: flex;
      gap: 4px;
      justify-content: center;
      margin-bottom: 32px;
      flex-wrap: wrap;
      align-items: center;
      font-size: 0.95rem;
    }
    .filter-plain .filter-label {
      font-weight: 600;
      color: var(--text-muted);
      margin-right: 4px;
    }
    .filter-plain .filter-sep {
      color: var(--text-muted);
      margin: 0 2px;
    }
    .filter-plain .filter-link {
      cursor: pointer;
      font-weight: 500;
      color: var(--text-dark);
      padding: 2px 4px;
      transition: color 0.3s;
      border: none;
      background: none;
      font-family: var(--font-body);
      font-size: 0.95rem;
    }
    .filter-plain .filter-link:hover,
    .filter-plain .filter-link.active {
      color: var(--gold);
      font-weight: 700;
    }

    /* Contact page 3-column layout */
    .contact-layout {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 40px;
      align-items: start;
    }
    .contact-layout .contact-left {
      max-width: 100%;
    }
    .contact-layout .contact-right {
      padding-top: 0;
    }
    @media (max-width: 768px) {
      .contact-layout {
        grid-template-columns: 1fr;
      }
    }

    /* Values diagram arrows */
    .values-item {
      display: flex;
      align-items: flex-start;
      gap: 16px;
      margin-bottom: 20px;
    }
    .values-item .values-num {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--gold);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-heading);
      font-weight: 700;
      font-size: 1rem;
      flex-shrink: 0;
    }
    .values-item .values-content {
      flex: 1;
    }
    .values-item .values-pair {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
    }
    .values-item .values-pair strong {
      font-family: var(--font-heading);
      font-size: 1.05rem;
      color: var(--navy);
    }
    .values-item .values-pair .values-arrow {
      flex: 1;
      border-top: 2px dashed var(--gold);
      min-width: 40px;
      max-width: 80px;
      position: relative;
    }
    .values-item .values-pair .values-arrow::after {
      content: '\\25B6';
      position: absolute;
      right: -8px;
      top: -8px;
      color: var(--gold);
      font-size: 0.6rem;
    }
    .values-item .values-desc {
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.5;
    }

  </style>
</head>""",
    "Add new CSS classes"
)


# ============================================================
# HERO PHOTO REPLACEMENTS
# ============================================================
print("\n=== HERO PHOTOS ===")

heroes = [
    ("For Buyers", "fb-hero.png"),
    ("About Sells", "about-hero.png"),
    ("Our Difference", "difference-hero.png"),
    ("Leadership Team", "leadership-hero.png"),
    ("Contact Us", "contact-hero.png"),
]

for title, img in heroes:
    R(
        f'<div><h1>{title}</h1></div>\n      </div>\n      <div class="hero-right">\n        <img src="images/patterns/yellow-bar-01.png" class="hero-bar" alt="">\n        Photo placeholder\n      </div>',
        f'<div><h1>{title}</h1></div>\n      </div>\n      <div class="hero-right has-photo">\n        <img class="hero-bg" src="images/photos/{img}" alt="{title}">\n        <img src="images/patterns/yellow-bar-01.png" class="hero-bar" alt="">\n      </div>',
        f"Hero photo: {title}"
    )

# Insights hero (appears twice - listing page and blog post page)
# Insights listing page
R(
    'INSIGHTS PAGE (#/insights)\n       ============================================================ -->\n  <div class="page" id="page-insights" data-nav="insights">\n\n    <!-- === HERO === -->\n    <section class="hero">\n      <div class="hero-left">\n        <div><h1>Insights</h1></div>\n      </div>\n      <div class="hero-right">\n        <img src="images/patterns/yellow-bar-01.png" class="hero-bar" alt="">\n        Photo placeholder\n      </div>',
    'INSIGHTS PAGE (#/insights)\n       ============================================================ -->\n  <div class="page" id="page-insights" data-nav="insights">\n\n    <!-- === HERO === -->\n    <section class="hero">\n      <div class="hero-left">\n        <div><h1>Insights</h1></div>\n      </div>\n      <div class="hero-right has-photo">\n        <img class="hero-bg" src="images/photos/insights-hero.png" alt="Insights">\n        <img src="images/patterns/yellow-bar-01.png" class="hero-bar" alt="">\n      </div>',
    "Hero photo: Insights listing"
)

# Blog post page
R(
    'BLOG POST PAGE (#/insights/post)\n       ============================================================ -->\n  <div class="page" id="page-insights-post" data-nav="insights">\n\n    <!-- === HERO === -->\n    <section class="hero">\n      <div class="hero-left">\n        <div><h1>Insights</h1></div>\n      </div>\n      <div class="hero-right">\n        <img src="images/patterns/yellow-bar-01.png" class="hero-bar" alt="">\n        Photo placeholder\n      </div>',
    'BLOG POST PAGE (#/insights/post)\n       ============================================================ -->\n  <div class="page" id="page-insights-post" data-nav="insights">\n\n    <!-- === HERO === -->\n    <section class="hero">\n      <div class="hero-left">\n        <div><h1>Insights</h1></div>\n      </div>\n      <div class="hero-right has-photo">\n        <img class="hero-bg" src="images/photos/insights-hero.png" alt="Insights">\n        <img src="images/patterns/yellow-bar-01.png" class="hero-bar" alt="">\n      </div>',
    "Hero photo: Blog post"
)


# ============================================================
# FOR BUYERS PAGE
# ============================================================
print("\n=== FOR BUYERS PAGE ===")

# Item #9: Intro text + photo (replace entire intro section)
R(
    '''    <!-- === INTRO === -->
    <section class="section-white">
      <div class="container two-col">
        <div>
          <h3 class="section-heading">
            Investors: This is your story, too.
          </h3>
          <p style="color: var(--text-muted); margin-top: 12px; line-height: 1.7;">
            At Sells, we believe the best transactions happen when buyers and sellers
            share a common vision. We work with experienced investors and sponsors who
            understand that behind every business is a founder, a team, and a community
            worth protecting.
          </p>
          <p style="color: var(--text-muted); margin-top: 12px; line-height: 1.7;">
            Our approach is built on trust, transparency, and alignment&mdash;connecting
            you with opportunities that match your investment thesis and values, while
            providing the insight and access you need to make confident decisions.
          </p>
        </div>
        <div class="photo-placeholder" style="min-height: 300px;">
          Photo placeholder
        </div>
      </div>
    </section>

    <!-- === INVEST IN PEOPLE === -->
    <section class="section-white" style="padding-top: 0;">
      <div class="container text-center">
        <h2 class="section-heading">Invest in people. Invest with purpose.</h2>
        <p style="max-width: 700px; margin: 0 auto 32px; color: var(--text-muted); line-height: 1.7;">
          The investors we partner with share our commitment to principled, people-centered
          transactions. Here's what sets our buyer relationships apart.
        </p>''',
    '''    <!-- === INTRO === -->
    <section class="section-white">
      <div class="container two-col">
        <div>
          <h3 class="section-heading">
            Investors: This is your story, too.
          </h3>
          <p style="color: var(--text-muted); margin-top: 12px; line-height: 1.7;">
            Investors, buyers, and sponsors trust Sells to make thoughtful introductions to private
            business owners. We&rsquo;ve cultivated these relationships, often over years at a time. We
            know their stories and what matters to them. It means that as an investor, you&rsquo;re not
            merely pursuing a lead&mdash;you&rsquo;re connecting with purpose to create lasting value.
          </p>
        </div>
        <div>
          <img src="images/photos/fb-intro.png" alt="Investors" style="width: 100%; height: auto; border-radius: 4px;">
        </div>
      </div>
    </section>

    <!-- === INVEST IN PEOPLE === -->
    <section class="section-white" style="padding-top: 0;">
      <div class="container text-center">
        <h2 class="section-heading">Invest in people, purpose, and potential.</h2>
        <p style="max-width: 700px; margin: 0 auto 32px; color: var(--text-muted); line-height: 1.7;">
          Everything about Sells is designed to build trust that yields rewarding outcomes. It starts
          with our dedication to founders and their legacies. It informs a business model that brings
          the relational into the transactional. And it shows up in a process and an experience where
          everyone is aligned, empowered, and focused.
        </p>''',
    "For Buyers: Intro text + photo + Invest heading"
)

# Item #13: Four-column bullet content
R(
    '''        <div class="four-cols" style="text-align: left;">

          <div>
            <h4 class="gold-underline-heading">Aligned</h4>
            <ul>
              <li>Shared vision for the company's future</li>
              <li>Cultural compatibility with founders and teams</li>
              <li>Commitment to preserving legacies and communities</li>
              <li>Long-term partnership mindset over short-term returns</li>
            </ul>
          </div>

          <div>
            <h4 class="gold-underline-heading">Strategic</h4>
            <ul>
              <li>Clear investment thesis and sector expertise</li>
              <li>Value-creation plans that benefit all stakeholders</li>
              <li>Operational resources to support growth post-close</li>
              <li>Network of portfolio companies for synergies</li>
            </ul>
          </div>

          <div>
            <h4 class="gold-underline-heading">Ethical</h4>
            <ul>
              <li>Transparent communication throughout the process</li>
              <li>Fair and straightforward deal structures</li>
              <li>Respect for the seller's timeline and priorities</li>
              <li>Reputation for integrity in the market</li>
            </ul>
          </div>

          <div>
            <h4 class="gold-underline-heading">Proven</h4>
            <ul>
              <li>Track record of successful acquisitions and exits</li>
              <li>Experienced operating and management teams</li>
              <li>Strong references from founders and management</li>
              <li>Committed capital and efficient closing processes</li>
            </ul>
          </div>

        </div>''',
    '''        <div class="four-cols" style="text-align: left;">

          <div>
            <h4 class="gold-underline-heading">Aligned</h4>
            <ul>
              <li>Focused on defining success beyond the number</li>
              <li>Aligned incentives: our fee structure rewards the best outcome for you</li>
              <li>Long-term relationship mentality vs. transactional</li>
              <li>Protecting what matters: employees, culture, brand, community impact</li>
            </ul>
          </div>

          <div>
            <h4 class="gold-underline-heading">Strategic</h4>
            <ul>
              <li>Market intelligence: we know who&rsquo;s buying, what they&rsquo;re paying, and why</li>
              <li>Proactive deal positioning&mdash;getting ahead of market dynamics</li>
              <li>Sophisticated buyer targeting and qualification process</li>
              <li>Strategic storytelling: crafting the narrative that maximizes value</li>
              <li>Process tailored to your situation and goals</li>
              <li>Anticipating buyer objections and structuring around them</li>
              <li>Understanding consolidation trends and industry-specific dynamics</li>
              <li>Data-driven approach to valuation and market positioning</li>
              <li>Creating competitive tension to drive optimal terms</li>
              <li>Not just finding a buyer&mdash;finding the right buyer</li>
            </ul>
          </div>

          <div>
            <h4 class="gold-underline-heading">Ethical</h4>
            <ul>
              <li>Transparency in process, pricing, and expectations</li>
              <li>Honest about valuation&mdash;we won&rsquo;t overpromise to win business</li>
              <li>Protecting confidentiality throughout the process</li>
              <li>No pressure tactics or artificially rushed timelines</li>
              <li>Clear communication about risks, trade-offs, and deal structure implications</li>
              <li>Integrity in representing your business to buyers</li>
              <li>Fair dealings with all parties while fiercely advocating for our client</li>
              <li>Long-term reputation over short-term fees</li>
              <li>We turn down deals that aren&rsquo;t the right fit</li>
              <li>Compliance with all regulatory and professional standards</li>
            </ul>
          </div>

          <div>
            <h4 class="gold-underline-heading">Proven</h4>
            <ul>
              <li>$2B+ in closed M&amp;A transactions</li>
              <li>Track record across home services, commercial services, and related industries</li>
              <li>Repeat clients and referral-based growth</li>
              <li>Trusted by both founders and institutional investors</li>
              <li>Deep buyer network cultivated over years of relationship building</li>
              <li>Successfully navigated complex deal structures and negotiations</li>
              <li>Portfolio of closed deals that speak for themselves</li>
            </ul>
          </div>

        </div>''',
    "For Buyers: Four-column bullet content"
)

# Item #14: Why buyers trust Sells - text and photo
R(
    '''    <!-- === WHY BUYERS TRUST SELLS === -->
    <section class="section-white" style="padding-top: 0;">
      <div class="container two-col">
        <div class="photo-placeholder" style="min-height: 350px;">
          Photo placeholder
        </div>
        <div>
          <h3 class="section-heading">Why buyers trust Sells:</h3>
          <p style="color: var(--text-muted); margin-bottom: 12px; line-height: 1.7;">
            We bring differentiated deal flow, deep seller relationships, and a transparent
            process that gives you confidence at every stage.
          </p>
          <p style="color: var(--text-muted); margin-bottom: 16px; line-height: 1.7;">
            Our sellers choose to work with Sells because of trust&mdash;and that trust
            extends to the buyers and investors we introduce. You gain access to motivated,
            prepared sellers and a well-managed process designed to protect everyone's time
            and interests.
          </p>

          <h4 style="color: var(--gold); font-family: var(--font-body); font-weight: 700; margin-top: 20px; margin-bottom: 8px;">
            Optimizing Opportunity
          </h4>
          <ul style="padding-left: 20px; list-style: disc;">
            <li style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 6px; line-height: 1.5;">
              Proprietary deal flow from trusted seller relationships
            </li>
            <li style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 6px; line-height: 1.5;">
              Detailed, investor-ready marketing materials and financial models
            </li>
            <li style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 6px; line-height: 1.5;">
              Pre-qualified opportunities aligned with your investment criteria
            </li>
          </ul>

          <h4 style="color: var(--gold); font-family: var(--font-body); font-weight: 700; margin-top: 20px; margin-bottom: 8px;">
            Guiding the Process
          </h4>
          <ul style="padding-left: 20px; list-style: disc;">
            <li style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 6px; line-height: 1.5;">
              Efficient, well-organized due diligence processes
            </li>
            <li style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 6px; line-height: 1.5;">
              Direct access to management and key decision-makers
            </li>
            <li style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 6px; line-height: 1.5;">
              Transparent negotiations that build trust and accelerate close
            </li>
          </ul>
        </div>
      </div>
    </section>''',
    '''    <!-- === WHY BUYERS TRUST SELLS === -->
    <section class="section-white" style="padding-top: 0;">
      <div class="container two-col">
        <div>
          <img src="images/photos/fb-trust.png" alt="Why buyers trust Sells" style="width: 100%; height: auto; border-radius: 4px;">
        </div>
        <div>
          <h3 class="section-heading">Why buyers trust Sells:</h3>
          <p style="color: var(--text-muted); margin-bottom: 12px; line-height: 1.7;">
            Proprietary deal flow. Informed, committed founders and owners.
            A process built for efficiency&mdash;but never at the expense of
            transparency, integrity, or the human element.
          </p>
          <p style="color: var(--text-muted); margin-bottom: 16px; line-height: 1.7;">
            More than anything, investors and sponsors come back to Sells
            for a personalized experience that leaves everyone confident,
            satisfied, and energized about the future.
          </p>

          <h4 style="color: var(--gold); font-family: var(--font-body); font-weight: 700; margin-top: 20px; margin-bottom: 8px;">
            Optimizing Opportunity
          </h4>
          <ul style="padding-left: 20px; list-style: disc;">
            <li style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 6px; line-height: 1.5;">
              Sells offers access to exclusive deal flow you won&rsquo;t find on the open market
            </li>
            <li style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 6px; line-height: 1.5;">
              We foster long-term relationships with founders and owners&mdash;often over years
            </li>
            <li style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 6px; line-height: 1.5;">
              We understand sellers&rsquo; psychology and motivations
            </li>
            <li style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 6px; line-height: 1.5;">
              We maintain ongoing sourcing partnerships and retainer relationships
            </li>
          </ul>

          <h4 style="color: var(--gold); font-family: var(--font-body); font-weight: 700; margin-top: 20px; margin-bottom: 8px;">
            Guiding the Process
          </h4>
          <ul style="padding-left: 20px; list-style: disc;">
            <li style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 6px; line-height: 1.5;">
              Sells offers end-to-end buy-side representation from sourcing to close
            </li>
            <li style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 6px; line-height: 1.5;">
              We move with efficiency, precision, and professionalism
            </li>
          </ul>
        </div>
      </div>
    </section>''',
    "For Buyers: Why buyers trust Sells text + photo"
)

# Item #15: For Buyers testimonial - change from navy to light
R(
    '''    <!-- === TESTIMONIAL === -->
    <section class="testimonial-section">
      <div class="container">
        <div class="testimonial-marks">&ldquo;</div>
        <p class="testimonial-quote">
          This is where a short and powerful client testimony would go to talk about
          the success that Sells has helped this Founder during an M&amp;A process.
        </p>
        <p class="testimonial-author">Peter Parker</p>
        <p class="testimonial-company">ABC Plumbing Company, LLC</p>
        <img src="images/patterns/diamond.png" alt="" class="testimonial-diamond">
      </div>
    </section>

    <!-- === LET'S TALK === -->
    <section class="lets-talk-section">
      <div class="container two-col-40-60">
        <div class="photo-placeholder" style="min-height: 400px;">Photo placeholder</div>
        <div>
          <h2 class="section-heading-lg" style="color: #fff;">Let&rsquo;s Talk</h2>
          <p style="color: rgba(255,255,255,0.8); margin-bottom: 16px; line-height: 1.7;">
            Whether you're exploring options, preparing for a transaction, or seeking a
            trusted advisor, we're here to help. Reach out to start a confidential conversation.
          </p>
          <form class="form-grid" onsubmit="return handleFormSubmit(event)">
            <div class="form-fields">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
              <input type="text" placeholder="Title">
              <input type="text" placeholder="Company*" required>
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <div>
              <textarea placeholder="How can we help?"></textarea>
            </div>
            <div style="grid-column: 1 / -1; text-align: center; margin-top: 12px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>


''',
    '''    <!-- === TESTIMONIAL === -->
    <section class="testimonial-light">
      <div class="container">
        <div class="testimonial-marks" style="font-size: 3.5rem; color: var(--gold); font-family: var(--font-heading); line-height: 1; margin-bottom: 8px;">&ldquo;</div>
        <p class="testimonial-quote">
          This is where a short and powerful client testimony would go to talk about
          the success that Sells has helped this Founder during an M&amp;A process.
        </p>
        <p class="testimonial-author">Peter Parker</p>
        <p class="testimonial-company">ABC Plumbing Company, LLC</p>
        <img src="images/patterns/diamond.png" alt="" class="testimonial-diamond">
      </div>
    </section>

    <!-- === LET'S TALK === -->
    <section class="hp-letstalk">
      <div class="container hp-letstalk-grid">
        <div class="hp-letstalk-photo">
          <img src="images/photos/letstalk-people.png" alt="Let's Talk">
        </div>
        <div class="hp-letstalk-right">
          <h2>Let&rsquo;s Talk</h2>
          <p>
            Successful relationships begin with honest,
            straightforward conversations. Whether you&rsquo;re planning a
            capital investment or in the middle of a prospective
            transaction, we welcome the chance to meet you, listen to
            your story, and share our insights and resources.
          </p>
          <form class="form-grid" onsubmit="return handleFormSubmit(event)">
            <div class="form-fields">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
              <input type="text" placeholder="Title">
              <input type="text" placeholder="Company*" required>
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <div>
              <textarea placeholder="How can we help?"></textarea>
            </div>
            <div style="grid-column: 1 / -1; text-align: center; margin-top: 12px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>


''',
    "For Buyers: Testimonial to light + Let's Talk with photo"
)


# ============================================================
# COMPANY / ABOUT SELLS PAGE
# ============================================================
print("\n=== COMPANY PAGE ===")

# Item #16: Company intro text
R(
    '''        <h3 class="section-heading" style="max-width: 600px;">
          When it matters most, Trust Sells.
        </h3>
        <p style="color: var(--text-muted); margin-top: 12px; max-width: 800px; line-height: 1.7;">
          Sells Advisory is a middle-market investment bank dedicated to helping founders,
          owners, and investors navigate the most important transactions of their lives. We
          were founded on a simple but powerful belief: that trust is the foundation of every
          successful relationship and transaction.
        </p>
        <p style="color: var(--text-muted); margin-top: 12px; max-width: 800px; line-height: 1.7;">
          Our team brings together decades of experience across investment banking, private
          equity, finance, and entrepreneurship. We understand both sides of the table because
          we've sat in both seats. That perspective allows us to create an environment where
          open conversations lead to exceptional outcomes.
        </p>
        <p style="color: var(--text-muted); margin-top: 12px; max-width: 800px; line-height: 1.7;">
          We don't just close deals&mdash;we guide people through defining moments with care,
          expertise, and integrity. Every engagement is built on the principles that define
          who we are: empathy for sellers, alignment with buyers, and a process that brings
          it all together.
        </p>''',
    '''        <h3 class="section-heading" style="max-width: 600px;">
          When it matters most, Trust Sells.
        </h3>
        <p style="color: var(--text-muted); margin-top: 12px; max-width: 800px; line-height: 1.7;">
          Sells is the middle-market investment bank and advisory firm people trust.
          We specialize in mergers and acquisitions for Main Street, where founders, owners
          and operators of private businesses can find investors, buyers, and sponsors who
          align with their priorities and share the desire to create lasting value.
        </p>
        <p style="color: var(--text-muted); margin-top: 12px; max-width: 800px; line-height: 1.7;">
          We exist to honor the human element in every transition. We bring the relational
          back to the transactional&mdash;with an approach that fosters empathy and alignment,
          and a process that leads to mutually rewarding outcomes.
        </p>
        <p style="color: var(--text-muted); margin-top: 12px; max-width: 800px; line-height: 1.7;">
          It means that long after the event itself, both parties will feel confident, satisfied,
          and energized about their futures.
        </p>''',
    "Company: Intro text"
)

# Item #17 + #18: Trust section - text, photo, values diagram
R(
    '''    <!-- === TRUST PRINCIPLES === -->
    <section class="section-white" style="padding-top: 0;">
      <div class="container two-col">
        <div class="photo-placeholder" style="min-height: 350px;">
          Photo placeholder
        </div>
        <div>
          <h3 class="section-heading">Above all, we value trust.</h3>
          <p style="color: var(--text-muted); margin-bottom: 24px; line-height: 1.7;">
            Trust isn't just a word in our name&mdash;it's the foundation of everything we do.
            Our approach is built on three core principles that guide every relationship and
            transaction.
          </p>

          <div class="numbered-item">
            <span class="num">1.</span>
            <div>
              <strong>Dignity</strong>
              <span class="arrow">&rarr;</span>
              <strong class="text-gold">Empathy</strong>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 4px; line-height: 1.5;">
                We treat every founder, owner, and stakeholder with dignity. By truly understanding
                your goals, concerns, and values, we transform that respect into empathy&mdash;the kind
                that shapes better advice and better outcomes.
              </p>
            </div>
          </div>

          <div class="numbered-item">
            <span class="num">2.</span>
            <div>
              <strong>Honesty</strong>
              <span class="arrow">&rarr;</span>
              <strong class="text-gold">Alignment</strong>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 4px; line-height: 1.5;">
                Honest conversations create alignment between all parties. We provide candid
                assessments, transparent communication, and straightforward advice&mdash;because
                alignment is only possible when everyone sees the full picture.
              </p>
            </div>
          </div>

          <div class="numbered-item">
            <span class="num">3.</span>
            <div>
              <strong>Integrity</strong>
              <span class="arrow">&rarr;</span>
              <strong class="text-gold">Process</strong>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 4px; line-height: 1.5;">
                Integrity in every action builds a process you can count on. From preparation
                through close, we manage every detail with the highest ethical standards&mdash;creating
                a process that protects your interests at every turn.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>''',
    '''    <!-- === TRUST PRINCIPLES === -->
    <section class="section-white" style="padding-top: 0;">
      <div class="container two-col">
        <div>
          <img src="images/photos/fb-intro.png" alt="Above all, we value trust" style="width: 100%; height: auto; border-radius: 4px;">
        </div>
        <div>
          <h3 class="section-heading">Above all, we value trust.</h3>
          <p style="color: var(--text-muted); margin-bottom: 24px; line-height: 1.7;">
            Without trust, we&rsquo;re simply doing transactions. Without trust, none of this works.
            So, everything we do helps create and support an environment of trust where people feel
            safe, confident, and free to pursue mutually rewarding outcomes. We believe trust happens
            when we follow three principles:
          </p>

          <hr class="gold-dotted" style="max-width: 300px; margin: 16px 0;">

          <div class="values-item">
            <span class="values-num">1</span>
            <div class="values-content">
              <div class="values-pair">
                <strong>Dignity</strong>
                <span class="values-arrow"></span>
                <strong class="text-gold">Empathy</strong>
              </div>
              <p class="values-desc">Respect for all leads to deeper understanding and connection.</p>
            </div>
          </div>

          <div class="values-item">
            <span class="values-num">2</span>
            <div class="values-content">
              <div class="values-pair">
                <strong>Honesty</strong>
                <span class="values-arrow"></span>
                <strong class="text-gold">Alignment</strong>
              </div>
              <p class="values-desc">Transparency and communication lead to shared interests and cooperation.</p>
            </div>
          </div>

          <div class="values-item">
            <span class="values-num">3</span>
            <div class="values-content">
              <div class="values-pair">
                <strong>Integrity</strong>
                <span class="values-arrow"></span>
                <strong class="text-gold">Process</strong>
              </div>
              <p class="values-desc">Discipline and precision lead to consistent, repeatable results.</p>
            </div>
          </div>
        </div>
      </div>
    </section>''',
    "Company: Trust section text + photo + values diagram"
)

# Item #20: Company "right people" - mirror layout + fix text
R(
    '''    <!-- === RIGHT PEOPLE === -->
    <section class="section-white">
      <div class="container two-col-55-45">
        <div>
          <h3 class="section-heading">
            The right people, right when you need them.
          </h3>
          <p style="color: var(--text-muted); margin-bottom: 16px; line-height: 1.7;">
            Sells coordinates a network of specialized professionals to support every
            aspect of your transaction, ensuring nothing is overlooked.
          </p>
          <hr class="gold-dotted">
          <ul class="right-people-list">
            <li>Accounting</li>
            <li>Tax Counsel</li>
            <li>Financial Diligence</li>
            <li>General Counsel</li>
            <li>Legal Transaction</li>
            <li>Private Wealth Management</li>
          </ul>
        </div>
        <div class="photo-placeholder" style="min-height: 300px;">
          Photo placeholder
        </div>
      </div>
    </section>

    <!-- === TESTIMONIAL === -->
    <section class="testimonial-section">
      <div class="container">
        <div class="testimonial-marks">&ldquo;</div>
        <p class="testimonial-quote">
          This is where a short and powerful client testimony would go to talk about
          the success that Sells has helped this Founder during an M&amp;A process.
        </p>
        <p class="testimonial-author">Peter Parker</p>
        <p class="testimonial-company">ABC Plumbing Company, LLC</p>
        <img src="images/patterns/diamond.png" alt="" class="testimonial-diamond">
      </div>
    </section>

    <!-- === LET'S TALK === -->
    <section class="lets-talk-section">
      <div class="container two-col-40-60">
        <div class="photo-placeholder" style="min-height: 400px;">Photo placeholder</div>
        <div>
          <h2 class="section-heading-lg" style="color: #fff;">Let&rsquo;s Talk</h2>
          <p style="color: rgba(255,255,255,0.8); margin-bottom: 16px; line-height: 1.7;">
            Whether you're exploring options, preparing for a transaction, or seeking a
            trusted advisor, we're here to help.
          </p>
          <form class="form-grid" onsubmit="return handleFormSubmit(event)">
            <div class="form-fields">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
              <input type="text" placeholder="Title">
              <input type="text" placeholder="Company*" required>
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <div>
              <textarea placeholder="How can we help?"></textarea>
            </div>
            <div style="grid-column: 1 / -1; text-align: center; margin-top: 12px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>

  <!-- ============================================================
       OUR DIFFERENCE PAGE''',
    '''    <!-- === RIGHT PEOPLE === -->
    <section class="section-white">
      <div class="container two-col-55-45" style="direction: rtl;">
        <div style="direction: ltr;">
          <img src="images/photos/company-rightpeople.png" alt="The right people" style="width: 100%; height: auto; border-radius: 4px;">
        </div>
        <div style="direction: ltr;">
          <h3 class="section-heading">
            The right people, right when you need them.
          </h3>
          <p style="color: var(--text-muted); margin-bottom: 16px; line-height: 1.7;">
            To support you on the path to a rewarding outcome, Sells brings a
            network of advisors, professionals, and experts in every facet of the
            M&amp;A process. Together, we&rsquo;ll prepare your business for maximum
            valuation, facilitate a faster close, and follow through well beyond the
            transaction with guidance on wealth management, succession
            planning, and more.
          </p>
          <hr class="gold-dotted">
          <ul class="right-people-list">
            <li>Accounting</li>
            <li>Tax Counsel</li>
            <li>Financial Diligence</li>
            <li>General Counsel</li>
            <li>Legal Transaction</li>
            <li>Private Wealth Management</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- === TESTIMONIAL === -->
    <section class="testimonial-light">
      <div class="container">
        <div class="testimonial-marks" style="font-size: 3.5rem; color: var(--gold); font-family: var(--font-heading); line-height: 1; margin-bottom: 8px;">&ldquo;</div>
        <p class="testimonial-quote">
          This is where a short and powerful client testimony would go to talk about
          the success that Sells has helped this Founder during an M&amp;A process.
        </p>
        <p class="testimonial-author">Peter Parker</p>
        <p class="testimonial-company">ABC Plumbing Company, LLC</p>
        <img src="images/patterns/diamond.png" alt="" class="testimonial-diamond">
      </div>
    </section>

    <!-- === LET'S TALK === -->
    <section class="hp-letstalk">
      <div class="container hp-letstalk-grid">
        <div class="hp-letstalk-photo">
          <img src="images/photos/letstalk-people.png" alt="Let's Talk">
        </div>
        <div class="hp-letstalk-right">
          <h2>Let&rsquo;s Talk</h2>
          <p>
            Successful relationships begin with honest,
            straightforward conversations. Whether you&rsquo;re planning a
            capital investment or in the middle of a prospective
            transaction, we welcome the chance to meet you, listen to
            your story, and share our insights and resources.
          </p>
          <form class="form-grid" onsubmit="return handleFormSubmit(event)">
            <div class="form-fields">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
              <input type="text" placeholder="Title">
              <input type="text" placeholder="Company*" required>
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <div>
              <textarea placeholder="How can we help?"></textarea>
            </div>
            <div style="grid-column: 1 / -1; text-align: center; margin-top: 12px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>

  <!-- ============================================================
       OUR DIFFERENCE PAGE''',
    "Company: Right people mirror + testimonial light + Let's Talk"
)


# ============================================================
# OUR DIFFERENCE PAGE
# ============================================================
print("\n=== OUR DIFFERENCE PAGE ===")

# Item #23: "Trust is the process" intro text
R(
    '''        <h3 class="section-heading" style="max-width: 600px;">
          Trust <em>is</em> the process.
        </h3>
        <p style="color: var(--text-muted); margin-top: 12px; max-width: 800px; line-height: 1.7;">
          At Sells, trust isn't just an outcome&mdash;it's woven into every step. From our first
          conversation to closing day and beyond, our entire approach is designed to build and
          sustain the trust that makes transformative transactions possible.
        </p>
        <p style="color: var(--text-muted); margin-top: 12px; max-width: 800px; line-height: 1.7;">
          Other firms focus on the deal. We focus on the people behind the deal. That distinction
          drives everything we do and produces outcomes that look nothing like the rest of the market.
        </p>''',
    '''        <h3 class="section-heading" style="max-width: 600px;">
          Trust <em>is</em> the process
        </h3>
        <p style="color: var(--text-muted); margin-top: 12px; max-width: 800px; line-height: 1.7;">
          Sellers consistently identify trust as the deciding factor in pursuing an offer. That&rsquo;s
          why we create an environment of uncommon trust&mdash;rooted in dignity and honesty,
          and executed with the utmost integrity.
        </p>''',
    "Our Difference: Trust intro text"
)

# Items #25, #26, #27: Replace 2x2 value cards with 4-column row + split headings + new descriptions
R(
    '''    <!-- === 4 VALUE CARDS === -->
    <section class="section-white">
      <div class="container">
        <div class="value-cards">

          <div class="value-card">
            <h4>Seller <strong>Empathy</strong></h4>
            <p>
              We begin every engagement by deeply understanding the seller&mdash;their goals,
              their fears, their non-negotiables. By leading with empathy, we create an
              environment of psychological safety that allows founders to make their best
              decisions with confidence and clarity.
            </p>
          </div>

          <div class="value-card">
            <h4>Buyer <strong>Alignment</strong></h4>
            <p>
              We cultivate relationships with investors who share our values&mdash;those who
              lead with integrity, invest with purpose, and honor the legacies they acquire.
              By aligning buyer and seller values from the start, we create partnerships that
              endure well beyond the closing table.
            </p>
          </div>

          <div class="value-card">
            <h4>Clear <strong>Process</strong></h4>
            <p>
              Our process is transparent, efficient, and meticulously managed. From preparation
              through close, every step is designed to protect your interests, minimize disruption,
              and deliver outcomes that exceed expectations. No surprises, no shortcuts, no gaps.
            </p>
          </div>

          <div class="value-card">
            <h4>Rewarding <strong>Outcomes</strong></h4>
            <p>
              When empathy, alignment, and process come together, the result is a transaction
              that creates lasting value for everyone involved. Our clients don't just close
              deals&mdash;they achieve outcomes that protect their people, preserve their legacies,
              and open new chapters with optimism.
            </p>
          </div>

        </div>
      </div>
    </section>''',
    '''    <!-- === 4 VALUE CARDS === -->
    <section class="section-white">
      <div class="container">
        <div class="value-cards-row">

          <div class="value-card-slim">
            <div class="card-label">Seller</div>
            <h4>Empathy</h4>
            <p>Discreet, respectful advocacy that protects your interests</p>
          </div>

          <div class="value-card-slim">
            <div class="card-label">Buyer</div>
            <h4>Alignment</h4>
            <p>Absolute transparency about strategy and objectives</p>
          </div>

          <div class="value-card-slim">
            <div class="card-label">Clear</div>
            <h4>Process</h4>
            <p>A smooth, simple pathway to success, led with precision</p>
          </div>

          <div class="value-card-slim">
            <div class="card-label">Rewarding</div>
            <h4>Outcomes</h4>
            <p>All parties feel confident, satisfied, and energized about their futures long after closing</p>
          </div>

        </div>
      </div>
    </section>''',
    "Our Difference: Value cards 4-column + split headings + new text"
)

# Items #28, #29, #30, #32: For Sellers/Buyers Delivers sections
R(
    '''    <!-- === FOR SELLERS DELIVERS === -->
    <section class="section-white" style="padding-top: 0;">
      <div class="container two-col">
        <div>
          <h3 class="section-heading">
            What the Sells Difference delivers for <span class="text-gold">Sellers</span>:
          </h3>
          <ul style="padding-left: 20px; list-style: disc; color: var(--text-muted);">
            <li style="margin-bottom: 8px; line-height: 1.5;">
              A trusted advisor who understands your business like an insider
            </li>
            <li style="margin-bottom: 8px; line-height: 1.5;">
              Investor-level analysis and positioning to maximize value
            </li>
            <li style="margin-bottom: 8px; line-height: 1.5;">
              Access to qualified, aligned buyers who share your values
            </li>
            <li style="margin-bottom: 8px; line-height: 1.5;">
              A transparent, well-managed process from start to finish
            </li>
            <li style="margin-bottom: 8px; line-height: 1.5;">
              Protection for your team, culture, and community
            </li>
            <li style="margin-bottom: 8px; line-height: 1.5;">
              Confidence and fulfillment through your defining moment
            </li>
          </ul>
          <a href="#/for-sellers" class="pill pill-outline" style="margin-top: 16px;">
            More for Sellers
          </a>
        </div>
        <div class="photo-placeholder" style="min-height: 300px;">
          Photo placeholder
        </div>
      </div>
    </section>

    <!-- === FOR BUYERS DELIVERS === -->
    <section class="section-white" style="padding-top: 0;">
      <div class="container">
        <h3 class="section-heading">
          What the Sells Difference delivers for <span class="text-gold">Buyers</span>:
        </h3>
        <ul style="padding-left: 20px; list-style: disc; color: var(--text-muted); max-width: 700px;">
          <li style="margin-bottom: 8px; line-height: 1.5;">
            Differentiated deal flow from trusted seller relationships
          </li>
          <li style="margin-bottom: 8px; line-height: 1.5;">
            Prepared, motivated sellers with clear expectations
          </li>
          <li style="margin-bottom: 8px; line-height: 1.5;">
            Comprehensive marketing materials and financial models
          </li>
          <li style="margin-bottom: 8px; line-height: 1.5;">
            Efficient, well-organized due diligence processes
          </li>
          <li style="margin-bottom: 8px; line-height: 1.5;">
            Transparent negotiations that build trust and accelerate close
          </li>
          <li style="margin-bottom: 8px; line-height: 1.5;">
            Long-term relationships with a trusted deal source
          </li>
        </ul>
        <a href="#/for-buyers" class="pill pill-outline" style="margin-top: 16px;">
          More for Buyers
        </a>
      </div>
    </section>

    <!-- === LET'S TALK === -->
    <section class="lets-talk-section">
      <div class="container two-col-40-60">
        <div class="photo-placeholder" style="min-height: 400px;">Photo placeholder</div>
        <div>
          <h2 class="section-heading-lg" style="color: #fff;">Let&rsquo;s Talk</h2>
          <p style="color: rgba(255,255,255,0.8); margin-bottom: 16px; line-height: 1.7;">
            Whether you're exploring options, preparing for a transaction, or seeking a
            trusted advisor, we're here to help.
          </p>
          <form class="form-grid" onsubmit="return handleFormSubmit(event)">
            <div class="form-fields">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
              <input type="text" placeholder="Title">
              <input type="text" placeholder="Company*" required>
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <div>
              <textarea placeholder="How can we help?"></textarea>
            </div>
            <div style="grid-column: 1 / -1; text-align: center; margin-top: 12px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>''',
    '''    <!-- === FOR SELLERS DELIVERS === -->
    <section class="section-white" style="padding-top: 0;">
      <div class="container two-col">
        <div>
          <h3 class="section-heading">
            For Sellers, Sells Delivers:
          </h3>
          <ul style="padding-left: 20px; list-style: disc; color: var(--text-muted);">
            <li style="margin-bottom: 8px; line-height: 1.5;">Principled, Aligned Investors</li>
            <li style="margin-bottom: 8px; line-height: 1.5;">Expert Guidance</li>
            <li style="margin-bottom: 8px; line-height: 1.5;">Maximum Valuation</li>
            <li style="margin-bottom: 8px; line-height: 1.5;">Success on Your Terms</li>
            <li style="margin-bottom: 8px; line-height: 1.5;">Support Beyond the Transaction</li>
          </ul>
          <div style="display: flex; align-items: center; gap: 12px; margin-top: 16px;">
            <a href="#/for-sellers" class="pill pill-outline">More for Sellers</a>
            <img src="images/patterns/diamond.png" alt="" style="width: 12px; height: 12px;">
          </div>
        </div>
        <div>
          <img src="images/photos/diff-sellers.png" alt="For Sellers" style="width: 100%; height: auto; border-radius: 4px;">
        </div>
      </div>
    </section>

    <!-- === FOR BUYERS DELIVERS === -->
    <section class="section-white" style="padding-top: 0;">
      <div class="container">
        <h3 class="section-heading">
          For Buyers, Sells Delivers:
        </h3>
        <ul style="padding-left: 20px; list-style: disc; color: var(--text-muted); max-width: 700px;">
          <li style="margin-bottom: 8px; line-height: 1.5;">Proprietary Deal Flow</li>
          <li style="margin-bottom: 8px; line-height: 1.5;">Informed, Committed Sellers</li>
          <li style="margin-bottom: 8px; line-height: 1.5;">Strategic Alignment</li>
          <li style="margin-bottom: 8px; line-height: 1.5;">Value Beyond Price</li>
        </ul>
        <div style="display: flex; align-items: center; gap: 12px; margin-top: 16px;">
          <a href="#/for-buyers" class="pill pill-outline">More for Buyers</a>
          <img src="images/patterns/diamond.png" alt="" style="width: 12px; height: 12px;">
        </div>
      </div>
    </section>

    <!-- === LET'S TALK === -->
    <section class="hp-letstalk">
      <div class="container hp-letstalk-grid">
        <div class="hp-letstalk-photo">
          <img src="images/photos/letstalk-people.png" alt="Let's Talk">
        </div>
        <div class="hp-letstalk-right">
          <h2>Let&rsquo;s Talk</h2>
          <p>
            Successful relationships begin with honest,
            straightforward conversations. Whether you&rsquo;re planning a
            capital investment or in the middle of a prospective
            transaction, we welcome the chance to meet you, listen to
            your story, and share our insights and resources.
          </p>
          <form class="form-grid" onsubmit="return handleFormSubmit(event)">
            <div class="form-fields">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
              <input type="text" placeholder="Title">
              <input type="text" placeholder="Company*" required>
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <div>
              <textarea placeholder="How can we help?"></textarea>
            </div>
            <div style="grid-column: 1 / -1; text-align: center; margin-top: 12px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>''',
    "Our Difference: Sellers/Buyers delivers + diamond icons + photo + Let's Talk"
)


# ============================================================
# LEADERSHIP PAGE
# ============================================================
print("\n=== LEADERSHIP PAGE ===")

# Item #34: Remove period from heading
R(
    'Leading by serving.',
    'Leading by serving',
    "Leadership: Remove period from heading"
)

# Replace Leadership Let's Talk
R(
    '''    <!-- === LET'S TALK === -->
    <section class="lets-talk-section">
      <div class="container two-col-40-60">
        <div class="photo-placeholder" style="min-height: 400px;">Photo placeholder</div>
        <div>
          <h2 class="section-heading-lg" style="color: #fff;">Let&rsquo;s Talk</h2>
          <p style="color: rgba(255,255,255,0.8); margin-bottom: 16px; line-height: 1.7;">
            Whether you're exploring options, preparing for a transaction, or seeking a
            trusted advisor, we're here to help.
          </p>
          <form class="form-grid" onsubmit="return handleFormSubmit(event)">
            <div class="form-fields">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
              <input type="text" placeholder="Title">
              <input type="text" placeholder="Company*" required>
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <div>
              <textarea placeholder="How can we help?"></textarea>
            </div>
            <div style="grid-column: 1 / -1; text-align: center; margin-top: 12px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>

  <!-- ============================================================
       INSIGHTS PAGE''',
    '''    <!-- === LET'S TALK === -->
    <section class="hp-letstalk">
      <div class="container hp-letstalk-grid">
        <div class="hp-letstalk-photo">
          <img src="images/photos/letstalk-people.png" alt="Let's Talk">
        </div>
        <div class="hp-letstalk-right">
          <h2>Let&rsquo;s Talk</h2>
          <p>
            Successful relationships begin with honest,
            straightforward conversations. Whether you&rsquo;re planning a
            capital investment or in the middle of a prospective
            transaction, we welcome the chance to meet you, listen to
            your story, and share our insights and resources.
          </p>
          <form class="form-grid" onsubmit="return handleFormSubmit(event)">
            <div class="form-fields">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
              <input type="text" placeholder="Title">
              <input type="text" placeholder="Company*" required>
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <div>
              <textarea placeholder="How can we help?"></textarea>
            </div>
            <div style="grid-column: 1 / -1; text-align: center; margin-top: 12px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>

  <!-- ============================================================
       INSIGHTS PAGE''',
    "Leadership: Let's Talk with photo"
)

# Leadership "right people" photo placeholder
R(
    '''        <div class="photo-placeholder" style="min-height: 300px;">
          Photo placeholder
        </div>
      </div>
    </section>

    <!-- === LET'S TALK === -->
    <section class="hp-letstalk">
      <div class="container hp-letstalk-grid">
        <div class="hp-letstalk-photo">
          <img src="images/photos/letstalk-people.png" alt="Let\'s Talk">''',
    '''        <div>
          <img src="images/photos/company-rightpeople.png" alt="The right people" style="width: 100%; height: auto; border-radius: 4px;">
        </div>
      </div>
    </section>

    <!-- === LET'S TALK === -->
    <section class="hp-letstalk">
      <div class="container hp-letstalk-grid">
        <div class="hp-letstalk-photo">
          <img src="images/photos/letstalk-people.png" alt="Let\'s Talk">''',
    "Leadership: Right people photo"
)


# ============================================================
# INSIGHTS PAGE
# ============================================================
print("\n=== INSIGHTS PAGE ===")

# Item #42: Filter tabs - change from pills to plain text
R(
    '''        <!-- Filter tabs -->
        <div class="filter-tabs">
          <span style="font-weight: 600; font-size: 0.9rem; color: var(--text-muted);">Filter by:</span>
          <img src="images/patterns/diamond.png" alt="" style="width: 10px; height: 10px;">
          <span class="filter-tab active" data-filter="all">All</span>
          <span class="filter-tab" data-filter="sellers">Sellers</span>
          <span class="filter-tab" data-filter="buyers">Buyers</span>
          <span class="filter-tab" data-filter="news">News</span>
        </div>''',
    '''        <!-- Filter tabs -->
        <div class="filter-plain">
          <span class="filter-label">Filter by:</span>
          <span class="filter-link active" data-filter="all">All</span>
          <span class="filter-sep">/</span>
          <span class="filter-link" data-filter="sellers">Sellers</span>
          <span class="filter-sep">/</span>
          <span class="filter-link" data-filter="buyers">Buyers</span>
          <span class="filter-sep">/</span>
          <span class="filter-link" data-filter="news">News</span>
          <img src="images/patterns/diamond.png" alt="" style="width: 10px; height: 10px; margin-left: 4px;">
        </div>''',
    "Insights: Filter tabs to plain text"
)

# Replace Insights Let's Talk
R(
    '''    <!-- === LET'S TALK === -->
    <section class="lets-talk-section">
      <div class="container two-col-40-60">
        <div class="photo-placeholder" style="min-height: 400px;">Photo placeholder</div>
        <div>
          <h2 class="section-heading-lg" style="color: #fff;">Let&rsquo;s Talk</h2>
          <p style="color: rgba(255,255,255,0.8); margin-bottom: 16px; line-height: 1.7;">
            Whether you're exploring options, preparing for a transaction, or seeking a
            trusted advisor, we're here to help.
          </p>
          <form class="form-grid" onsubmit="return handleFormSubmit(event)">
            <div class="form-fields">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
              <input type="text" placeholder="Title">
              <input type="text" placeholder="Company*" required>
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <div>
              <textarea placeholder="How can we help?"></textarea>
            </div>
            <div style="grid-column: 1 / -1; text-align: center; margin-top: 12px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>

  <!-- ============================================================
       BLOG POST PAGE''',
    '''    <!-- === LET'S TALK === -->
    <section class="hp-letstalk">
      <div class="container hp-letstalk-grid">
        <div class="hp-letstalk-photo">
          <img src="images/photos/letstalk-people.png" alt="Let's Talk">
        </div>
        <div class="hp-letstalk-right">
          <h2>Let&rsquo;s Talk</h2>
          <p>
            Successful relationships begin with honest,
            straightforward conversations. Whether you&rsquo;re planning a
            capital investment or in the middle of a prospective
            transaction, we welcome the chance to meet you, listen to
            your story, and share our insights and resources.
          </p>
          <form class="form-grid" onsubmit="return handleFormSubmit(event)">
            <div class="form-fields">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
              <input type="text" placeholder="Title">
              <input type="text" placeholder="Company*" required>
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <div>
              <textarea placeholder="How can we help?"></textarea>
            </div>
            <div style="grid-column: 1 / -1; text-align: center; margin-top: 12px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>

  <!-- ============================================================
       BLOG POST PAGE''',
    "Insights: Let's Talk with photo"
)

# Blog Post Let's Talk
R(
    '''    <!-- === LET'S TALK === -->
    <section class="lets-talk-section">
      <div class="container two-col-40-60">
        <div class="photo-placeholder" style="min-height: 400px;">Photo placeholder</div>
        <div>
          <h2 class="section-heading-lg" style="color: #fff;">Let&rsquo;s Talk</h2>
          <p style="color: rgba(255,255,255,0.8); margin-bottom: 16px; line-height: 1.7;">
            Whether you're exploring options, preparing for a transaction, or seeking a
            trusted advisor, we're here to help.
          </p>
          <form class="form-grid" onsubmit="return handleFormSubmit(event)">
            <div class="form-fields">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
              <input type="text" placeholder="Title">
              <input type="text" placeholder="Company*" required>
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <div>
              <textarea placeholder="How can we help?"></textarea>
            </div>
            <div style="grid-column: 1 / -1; text-align: center; margin-top: 12px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>

  <!-- ============================================================
       CONTACT PAGE''',
    '''    <!-- === LET'S TALK === -->
    <section class="hp-letstalk">
      <div class="container hp-letstalk-grid">
        <div class="hp-letstalk-photo">
          <img src="images/photos/letstalk-people.png" alt="Let's Talk">
        </div>
        <div class="hp-letstalk-right">
          <h2>Let&rsquo;s Talk</h2>
          <p>
            Successful relationships begin with honest,
            straightforward conversations. Whether you&rsquo;re planning a
            capital investment or in the middle of a prospective
            transaction, we welcome the chance to meet you, listen to
            your story, and share our insights and resources.
          </p>
          <form class="form-grid" onsubmit="return handleFormSubmit(event)">
            <div class="form-fields">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
              <input type="text" placeholder="Title">
              <input type="text" placeholder="Company*" required>
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <div>
              <textarea placeholder="How can we help?"></textarea>
            </div>
            <div style="grid-column: 1 / -1; text-align: center; margin-top: 12px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </section>

  </div>

  <!-- ============================================================
       CONTACT PAGE''',
    "Blog Post: Let's Talk with photo"
)


# ============================================================
# CONTACT PAGE
# ============================================================
print("\n=== CONTACT PAGE ===")

# Items #48, #49: Contact form text + layout restructure
R(
    '''    <!-- === CONTACT SECTION === -->
    <section class="section-white">
      <div class="container two-col-55-45">

        <!-- Form side -->
        <div>
          <h2 class="section-heading text-gold">Let&rsquo;s Talk</h2>
          <p style="color: var(--text-muted); margin-bottom: 24px; line-height: 1.7;">
            Ready to start a conversation? Fill out the form below and a member of our
            team will be in touch within one business day. All inquiries are treated with
            the utmost confidentiality.
          </p>
          <form class="contact-form" onsubmit="return handleFormSubmit(event)">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
              <input type="text" placeholder="First Name*" required>
              <input type="text" placeholder="Last Name*" required>
            </div>
            <input type="text" placeholder="Title" style="width: 100%; margin-top: 12px;">
            <input type="text" placeholder="Company*" required style="width: 100%; margin-top: 12px;">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 12px;">
              <input type="email" placeholder="Email*" required>
              <input type="tel" placeholder="Phone*" required>
            </div>
            <textarea placeholder="How can we help?" style="width: 100%; margin-top: 12px; min-height: 120px; padding: 12px 14px; background: #f0f0f5; border: none; border-bottom: 2px solid #ccc; font-size: 0.9rem; border-radius: 2px; resize: vertical; font-family: var(--font-body);"></textarea>
            <div style="margin-top: 16px;">
              <button type="submit" class="pill pill-gold">Submit</button>
            </div>
          </form>
        </div>

        <!-- Address side -->
        <div>
          <h3 class="text-gold" style="font-family: var(--font-heading); font-size: 1.3rem; margin-bottom: 16px;">
            Address
          </h3>
          <h4 style="font-weight: 700; margin-bottom: 4px;">Headquarters</h4>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7;">
            5100 W JB Hunt Drive<br>
            STE 830<br>
            Rogers, AR 72758
          </p>
          <h3 class="text-gold" style="font-family: var(--font-heading); font-size: 1.3rem; margin-top: 24px; margin-bottom: 8px;">
            Office Line
          </h3>
          <p>
            <a href="tel:+14793343226" style="color: var(--gold); font-weight: 600; font-size: 1rem;">
              +1 (479) 334-3226
            </a>
          </p>
        </div>

      </div>
    </section>''',
    '''    <!-- === CONTACT SECTION === -->
    <section class="section-white">
      <div class="container">
        <h2 class="section-heading text-gold" style="font-style: italic;">Let&rsquo;s Talk</h2>
        <p style="color: var(--text-muted); margin-bottom: 32px; line-height: 1.7; max-width: 600px;">
          Successful relationships begin with honest, straightforward conversations.
          Whether you&rsquo;re planning a capital investment or in the middle of a prospective
          transaction, we welcome the chance to meet you, listen to your story, and share
          our insights and resources.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 32px; align-items: start;">
          <!-- Stacked fields -->
          <form class="contact-form" id="contactForm" onsubmit="return handleFormSubmit(event)" style="display: contents;">
            <div style="display: flex; flex-direction: column; gap: 12px;">
              <input type="text" placeholder="First Name*" required style="width: 100%; padding: 12px 14px; background: #f0f0f5; border: none; border-bottom: 2px solid #ccc; font-size: 0.9rem; border-radius: 2px;">
              <input type="text" placeholder="Last Name*" required style="width: 100%; padding: 12px 14px; background: #f0f0f5; border: none; border-bottom: 2px solid #ccc; font-size: 0.9rem; border-radius: 2px;">
              <input type="text" placeholder="Title" style="width: 100%; padding: 12px 14px; background: #f0f0f5; border: none; border-bottom: 2px solid #ccc; font-size: 0.9rem; border-radius: 2px;">
              <input type="text" placeholder="Company*" required style="width: 100%; padding: 12px 14px; background: #f0f0f5; border: none; border-bottom: 2px solid #ccc; font-size: 0.9rem; border-radius: 2px;">
              <input type="email" placeholder="Email*" required style="width: 100%; padding: 12px 14px; background: #f0f0f5; border: none; border-bottom: 2px solid #ccc; font-size: 0.9rem; border-radius: 2px;">
              <input type="tel" placeholder="Phone*" required style="width: 100%; padding: 12px 14px; background: #f0f0f5; border: none; border-bottom: 2px solid #ccc; font-size: 0.9rem; border-radius: 2px;">
            </div>
            <!-- Textarea -->
            <div>
              <textarea placeholder="How can we help?" style="width: 100%; height: 100%; min-height: 280px; padding: 12px 14px; background: #f0f0f5; border: none; border-bottom: 2px solid #ccc; font-size: 0.9rem; border-radius: 2px; resize: vertical; font-family: var(--font-body);"></textarea>
            </div>
          </form>
          <!-- Address side -->
          <div>
            <h3 class="text-gold" style="font-family: var(--font-heading); font-size: 1.3rem; margin-bottom: 16px;">
              Address
            </h3>
            <h4 style="font-weight: 700; margin-bottom: 4px;">Headquarters</h4>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7;">
              5100 W JB Hunt Drive, STE 830<br>
              Rogers, AR 72758
            </p>
            <h3 class="text-gold" style="font-family: var(--font-heading); font-size: 1.3rem; margin-top: 24px; margin-bottom: 8px;">
              Office Line
            </h3>
            <p>
              <a href="tel:+14793343226" style="color: var(--gold); font-weight: 600; font-size: 1rem;">
                +1 (479) 334-3226
              </a>
            </p>
          </div>
        </div>
        <div style="text-align: center; margin-top: 24px;">
          <button type="submit" form="contactForm" class="pill pill-gold">Submit</button>
        </div>
      </div>
    </section>''',
    "Contact: Form layout restructure + text change"
)


# ============================================================
# UPDATE FILTER JS (for new filter-link class)
# ============================================================
print("\n=== JS UPDATES ===")

R(
    "const filterTabs = document.querySelectorAll('.filter-tab');",
    "const filterTabs = document.querySelectorAll('.filter-tab, .filter-link');",
    "JS: Update filter selector for new class"
)

R(
    "filterTabs.forEach(function(tab) {\n      tab.addEventListener('click', function() {\n        // Update active tab styling\n        filterTabs.forEach(function(t) {\n          t.classList.remove('active');\n        });\n        this.classList.add('active');",
    "filterTabs.forEach(function(tab) {\n      tab.addEventListener('click', function() {\n        // Update active tab styling\n        document.querySelectorAll('.filter-tab, .filter-link').forEach(function(t) {\n          t.classList.remove('active');\n        });\n        this.classList.add('active');",
    "JS: Update filter click handler for new class"
)


# ============================================================
# WRITE RESULT
# ============================================================
with open(filepath, 'w') as f:
    f.write(html)

print(f"\n{'='*50}")
print(f"DONE! Applied {count} changes successfully.")
print(f"{'='*50}")
