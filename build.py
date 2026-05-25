import os
import re
from datetime import datetime

def minify_html(html_string):
    """Aggressively optimizes page delivery footprint by cleaning whitespace boundaries."""
    html_string = re.sub(r'\s+', ' ', html_string)
    html_string = re.sub(r'>\s+<', '><', html_string)
    return html_string.strip()

def get_base_css():
    """Returns an optimized, high-performance typography and utility design system canvas."""
    return """<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #00c9ff; 
            --primary-gradient: linear-gradient(135deg, #00c9ff, #92fe9d);
            --secondary: #1a1a1a;
            --accent: #10b981;
            --accent-dark: #059669;
            --text-main: #333333;
            --bg-light: #f8f9fa;
            --border: #dddddd;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Plus Jakarta Sans', system-ui, sans-serif; line-height: 1.6; color: var(--text-main); background: #ffffff; -webkit-font-smoothing: antialiased; }
        .container { max-width: 1000px; margin: 0 auto; padding: 0 24px; }
        .hero { padding: 80px 0 60px 0; text-align: center; background: var(--primary-gradient); color: var(--secondary); border-radius: 0 0 24px 24px; }
        .hero h1 { font-size: 3rem; font-weight: 800; margin-bottom: 20px; letter-spacing: -0.03em; }
        .hero-lead { font-size: 1.25rem; max-width: 750px; margin: 0 auto 32px auto; font-weight: 500; }
        .cta-btn { display: inline-flex; align-items: center; background: var(--accent); color: white; padding: 16px 36px; font-size: 1.2rem; font-weight: 700; text-decoration: none; border-radius: 12px; box-shadow: 0 10px 25px rgba(16,185,129,0.35); transition: all 0.2s ease; }
        .cta-btn:hover { background: var(--accent-dark); transform: translateY(-2px); }
        .disclosure { font-size: 0.85rem; margin-top: 16px; color: #444; }
        h2 { font-size: 2.2rem; color: var(--secondary); margin: 44px 0 20px 0; letter-spacing: -0.02em; }
        .card-matrix { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin: 32px 0; }
        .feature-card { background: white; border: 1px solid var(--border); padding: 24px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
        .feature-card h3 { color: var(--secondary); font-size: 1.25rem; margin-bottom: 10px; }
        table { width: 100%; border-collapse: collapse; margin: 24px 0; font-size: 1rem; }
        th, td { border: 1px solid var(--border); padding: 14px; text-align: left; }
        th { background: #f0f0f0; color: var(--secondary); font-weight: 700; }
        .blog-list { list-style: none; margin: 24px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
        .related-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 24px 0; list-style: none; }
        @media (max-width: 768px) { .blog-list, .related-grid { grid-template-columns: 1fr; } }
        .blog-list li, .related-grid li { background: var(--bg-light); border: 1px solid var(--border); padding: 20px; border-radius: 12px; }
        .blog-list a, .related-grid a { color: var(--secondary); font-weight: 700; text-decoration: none; font-size: 1.1rem; display: block; margin-bottom: 4px; }
        .blog-list a:hover, .related-grid a:hover { color: var(--accent); }
        .affiliate-disclosure { background: #fffbeb; border-left: 4px solid #f59e0b; padding: 15px; margin: 20px 0; font-size: 0.9em; border-radius: 4px; }
        footer { border-top: 1px solid var(--border); padding: 40px 0; text-align: center; font-size: 0.9rem; color: #666; background: var(--bg-light); margin-top: 80px; }
        @media (max-width: 768px) { .hero h1 { font-size: 2.2rem; } }
    </style>"""

def generate_programmatic_data():
    """Generates localized array targets handling individual vertical execution constraints."""
    niches = [
        {"name": "SaaS Startups", "action": "running paid beta sign-up funnels", "use": "Dynamic Text Replacement to auto-match features to search queries"},
        {"name": "Real Estate Brokers", "action": "building localized property lead capture systems", "use": "Smart Sections to scale down neighborhoods quickly"},
        {"name": "Crypto Projects", "action": "deploying fast whitepaper distribution engines", "use": "unlimited conversion layout scaling to maximize traffic drops"},
        {"name": "Roofing Companies", "action": "capturing quote requests from localized homeowners", "use": "integrated exit-intent popups to capture abandoning prospects"},
        {"name": "Digital Agencies", "action": "launching complex custom multi-client search funnels", "use": "white-label workspaces to manage client permissions cleanly"},
        {"name": "Fitness Coops", "action": "driving membership enrollments to seasonal bootcamps", "use": "A/B split testing tracks to optimize high-intent landing traffic"},
        {"name": "E-commerce Stores", "action": "scaling dedicated landing pages for social ads", "use": "seamless tracking integration loops to collect conversion tags"},
        {"name": "Legal Consultants", "action": "generating highly sensitive corporate consult inquiries", "use": "secure custom form architectures with direct webhook outputs"},
        {"name": "Financial Planners", "action": "building gated lead magnets for wealth blueprints", "use": "optimized performance delivery scripts to load profiles fast"},
        {"name": "Dental Clinics", "action": "booking local patient cosmetic dental evaluations", "use": "dynamic location maps and instant calendar scheduling tags"},
        {"name": "Online Educators", "action": "scaling evergreen webinar application sequences", "use": "automated tracking loops and countdown timer features"},
        {"name": "B2B Consultants", "action": "collecting corporate discovery call configurations", "use": "minimalist clean high-trust single page design systems"},
        {"name": "Affiliate Networks", "action": "routing paid contextual bridge traffic to offers", "use": "optimized smart sections to manage hundreds of active redirect paths"},
        {"name": "Home Inspectors", "action": "handling commercial real estate appraisal bookings", "use": "fully responsive mobile layout controls to target field users"},
        {"name": "HVAC Contractors", "action": "driving emergency repair service calls inline", "use": "sticky click-to-call integrations and conversion optimized grids"},
        {"name": "Insurance Agencies", "action": "delivering automated multi-provider coverage estimates", "use": "multi-step lead forms to handle advanced underwriting answers"},
        {"name": "Mortgage Brokers", "action": "scaling clean home refi pre-approval funnels", "use": "high-trust security layouts and rapid execution validation scripts"},
        {"name": "SaaS Advertisers", "action": "testing cold direct traffic product comparisons", "use": "modular feature comparison matrix components to convert audiences"},
        {"name": "Corporate Recruiters", "action": "attracting executive-level engineering applicants", "use": "integrated video backgrounds and immersive layout features"},
        {"name": "Medical Spas", "action": "promoting targeted aesthetics consultation bookings", "use": "high-end visual gallery blocks and seamless calendar booking apps"}
    ]
    
    topics = [
        {"pattern": "landingi-review-for-{slug}", "title": "Landingi Review 2026: Structural Optimization for {niche}"},
        {"pattern": "how-to-scale-funnels-for-{slug}", "title": "How to Automate 50+ Landing Pages for {niche} Growth"},
        {"pattern": "landingi-pricing-guide-for-{slug}", "title": "Landingi Pricing Deep-Dive: Maximizing ROI for {niche}"},
        {"pattern": "landingi-vs-unbounce-for-{slug}", "title": "Landingi vs Unbounce for {niche}: Which Option Wins?"},
        {"pattern": "smart-sections-guide-for-{slug}", "title": "How to Use Smart Sections to Scale An Active {niche}"}
    ]
    
    posts = []
    for item in niches:
        niche = item["name"]
        niche_slug = niche.lower().replace(" ", "-")
        for topic in topics:
            slug = topic["pattern"].format(slug=niche_slug)
            title = topic["title"].format(niche=niche)
            desc = f"Discover how utilizing Landingi's unmetered $29/mo page scaling tools empowers an active {niche} to bypass strict budget limits completely."
            content = (
                f"When an active, performance-driven {niche} is actively task-oriented with {item['action']}, manual asset building slows operations down to a crawl. "
                f"Switching over your landing page network architecture to Landingi allows your production team to leverage {item['use']} across every active ad set. "
                f"With standard tools capping features or charging massive overage rates as your traffic expands, Landingi's unmetered production canvas allows you to push scale limits safely. "
                f"By maintaining clean workspaces, automated responsive controls, and high-speed delivery nodes, you convert higher volumes of raw paid search traffic into actual closed revenue rows instantly."
            )
            posts.append({"slug": slug, "title": title, "desc": desc, "content": content})
    return posts

def build_entire_site():
    base_url = "https://brightlane.github.io/Landingi"
    affiliate_url = "https://try.landingi.com/w5farvpasbpn?utm_source=deploy"
    today_str = datetime.today().strftime('%Y-%m-%d')
    rss_date_str = datetime.today().strftime('%a, %d %b %Y 00:00:00 UT')

    blog_posts = generate_programmatic_data()
    os.makedirs("blog", exist_ok=True)
    
    urls_for_sitemap = [f"{base_url}/"]
    for post in blog_posts:
        urls_for_sitemap.append(f"{base_url}/blog/{post['slug']}.html")

    # ==========================================
    # 1. BUILD CORE HUB NODE (INDEX)
    # ==========================================
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landingi Review 2026: Best Landing Page Builder for Agencies - 14-Day Trial</title>
    <meta name="description" content="Landingi: $29/mo Core (unlimited pages), $65 Create (popups + A/B), $89 Automate. Drag-drop builder, Smart Sections, dynamic text replacement. Perfect for PPC/affiliate agencies.">
    <link rel="canonical" href="{base_url}/" />
    <link rel="alternate" type="application/rss+xml" title="Landingi Network RSS Feed" href="{base_url}/feed.xml" />
    {get_base_css()}
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Product",
      "name": "Landingi Page System",
      "description": "High-performance no-code landing page generation engine featuring Smart Sections and Dynamic Text arrays.",
      "brand": {{"@type": "Brand", "name": "Landingi"}},
      "offers": {{
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "lowPrice": "29",
        "highPrice": "89",
        "offerCount": "3"
      }}
    }}
    </script>
</head>
<body>
    <header class="hero">
        <div class="container">
            <h1>🎨 Landingi 2026: #1 Landing Page Builder for Agencies</h1>
            <p class="hero-lead">Drag-drop builder + Smart Sections + Dynamic Text Replacement + Popups + A/B testing. **Unlimited pages** all plans. Perfect for PPC campaigns & affiliate offers.</p>
            <div>
                <a href="{affiliate_url}" class="cta-btn" rel="sponsored">Start 14-Day Free Trial</a>
            </div>
            <p class="disclosure">Links earn commissions at no extra cost to your signup platform entry terms.</p>
        </div>
    </header>

    <main class="container">
        <div class="affiliate-disclosure">
            <strong>Affiliate Disclosure:</strong> Links earn commissions at no extra cost to your account setup parameters.
        </div>

        <h2>Why Landingi Wins for Agencies</h2>
        <p>No-code drag-drop + **Smart Sections** (update 1 element &rarr; changes everywhere) + **Dynamic Text Replacement** (auto-match Google Ads keywords). Agency plan white-label ready.</p>

        <div class="card-matrix">
            <div class="feature-card">
                <h3>✨ Smart Sections</h3>
                <p>Update header components or forms &rarr; variations push across 50+ live funnels instantly.</p>
            </div>
            <div class="feature-card">
                <h3>🔤 Dynamic Text</h3>
                <p>Auto-swap titles based on user keywords dynamically to maximize Quality Scores.</p>
            </div>
            <div class="feature-card">
                <h3>⚡ Popups + A/B Testing</h3>
                <p>Configure custom exit-intent triggers and split variants instantly from one clean hub grid.</p>
            </div>
            <div class="feature-card">
                <h3>🏢 White-Label Dashboard</h3>
                <p>Brand customer reporting dashboards, sub-accounts, and assets natively.</p>
            </div>
        </div>

        <h2>Landingi Pricing 2026</h2>
        <table>
            <tr><th>Plan</th><th>Price/mo</th><th>Key Operational Bounds</th></tr>
            <tr><td>Core Plan</td><td>$29 / mo</td><td>Perfect for scaling single-offer funnels with unlimited assets.</td></tr>
            <tr><td>Create Plan</td><td>$65 / mo</td><td>Unlocks high-conversion popup modules and standard optimization variants.</td></tr>
            <tr><td>Automate Plan</td><td>$89 / mo</td><td>Unlocks system automation scripts and complete funnel matrix data integrations.</td></tr>
            <tr><td>Agency Portal</td><td>Custom Pricing</td><td>Complete multi-seat organization matrices and full platform white-labeling.</td></tr>
        </table>
        <p style="margin-bottom: 30px;"><strong>Unlimited landing pages allowed on all tiers</strong>. 14-day tracking trial included.</p>

        <h2>Landingi vs Unbounce vs Leadpages</h2>
        <table>
            <tr><th>Feature Track</th><th>Landingi Solution</th><th>Unbounce Standard</th><th>Leadpages Core</th></tr>
            <tr><td>Starting Plan Cost</td><td>✅ $29 / mo</td><td>$99 / mo</td><td>$49 / mo</td></tr>
            <tr><td>Smart Block Swaps</td><td>✅ Yes (Global Sync)</td><td>❌ Manual Edit Only</td><td>❌ Manual Edit Only</td></tr>
            <tr><td>Dynamic Parameter Match</td><td>✅ Yes (Built-in)</td><td>Requires Pro Upgrade</td><td>❌ Limited Sets</td></tr>
            <tr><td>Page Overages</td><td>✅ Unlimited Access</td><td>Strict Visitor Caps</td><td>Standard Volume Caps</td></tr>
        </table>

        <h2>Perfect Agency Use Cases</h2>
        <ul style="margin: 20px 0; padding-left: 20px;">
            <li><strong>PPC Campaign Managers:</strong> Maximize context score matches by adjusting headlines based on ad hooks.</li>
            <li><strong>Affiliate Arbitrageurs:</strong> Launch hundreds of geo-targeted configurations without worrying about storage costs.</li>
            <li><strong>B2B Lead Generation:</strong> Collect enterprise entries and link pipelines into active CRM paths securely.</li>
        </ul>

        <div style="background: #e8f5e8; padding: 35px; text-align: center; border-radius: 16px; margin: 40px 0; border: 1px solid #c2e7c2;">
            <h2 style="margin-top: 0;">Build 10x Faster with Global Smart Sections</h2>
            <p style="margin-bottom: 20px;">Deploy conversion tracking variations at scale without standard page limit friction.</p>
            <a href="{affiliate_url}" class="cta-btn" rel="sponsored">Claim 14-Day Free Trial</a>
        </div>

        <h2>Deep-Dive Vertical Optimization Directories</h2>
        <ul class="blog-list">"""
        
    for post in blog_posts:
        index_html += f'\n            <li><a href="blog/{post["slug"]}.html">→ {post["title"]}</a><p style="color:#666; font-size:0.9rem; margin-top:4px;">{post["desc"]}</p></li>'
        
    index_html += f"""
        </ul>
    </main>

    <footer>
        <div class="container">
            <p>© 2026 Benny Palmarino | Langhorne, PA | Digital Infrastructure & Conversion Engineering</p>
        </div>
    </footer>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(minify_html(index_html))

    # ==========================================
    # 2. BUILD THE REUSE SUB-PAGE NODE STRUCTURE
    # ==========================================
    subpage_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="{base_url}/blog/{slug}.html" />
    {css}
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}",
      "description": "{desc}",
      "datePublished": "{date}",
      "author": {{
        "@type": "Person",
        "name": "Benny Palmarino"
      }}
    }}
    </script>
</head>
<body>
    <div class="container" style="padding-top: 50px;">
        <div style="margin-bottom: 24px;"><a href="../" style="color: var(--accent); text-decoration:none; font-weight:700;">&larr; Back to Performance Hub</a></div>
        <h1>{title}</h1>
        
        <article class="feature-card" style="background:#ffffff; margin-top:24px; border-left: 4px solid var(--accent); line-height:1.8;">
            <p style="font-size:1.15rem; color:var(--text-main);">{content}</p>
        </article>

        <section class="calc-box" style="text-align:center; background: var(--secondary); color: white; padding: 40px; border-radius: 24px; margin: 40px 0;">
            <h3 style="color: white; margin-bottom:12px;">Scale Your Organic Traffic Conversion Matrix</h3>
            <p style="color:#cccccc; margin-bottom:24px; max-width:600px; margin-left:auto; margin-right:auto;">Stop limiting your B2B ad strategies to high-overhead design platforms. Use Landingi's global component layouts to map custom pages fluidly.</p>
            <a href="{affiliate_url}" class="cta-btn" rel="sponsored">Claim Your Unmetered 14-Day Trial</a>
        </section>

        <h3 style="margin-top: 40px;">Related Campaign Engineering Guides</h3>
        <ul class="related-grid">
            {related_links}
        </ul>
    </div>
    <footer>
        <div class="container">
            <p>© 2026 Benny Palmarino | Langhorne, PA</p>
        </div>
    </footer>
</body>
</html>"""

    # Shared pre-rendering of styles to preserve processing cycles
    cached_css = get_base_css()

    for idx, post in enumerate(blog_posts):
        slug = post["slug"]
        
        related_links_list = []
        for offset in [1, 2, 3]:
            related_post = blog_posts[(idx + offset) % len(blog_posts)]
            related_links_list.append(f'<li><a href="{related_post["slug"]}.html">{related_post["title"]}</a></li>')
        related_html_str = "\n".join(related_links_list)

        rendered_subpage = subpage_template.format(
            title=post["title"],
            desc=post["desc"],
            base_url=base_url,
            slug=slug,
            css=cached_css,
            date=today_str,
            content=post["content"],
            affiliate_url=affiliate_url,
            related_links=related_html_str
        )

        with open(f"blog/{slug}.html", "w", encoding="utf-8") as f:
            f.write(minify_html(rendered_subpage))

    # ==========================================
    # 3. BUILD AUTOMATED INTERFACE DIRECTORY (LLMS.TXT)
    # ==========================================
    llms_txt = f"# Landingi Automated Asset Map Directory\n> Programmatic indexing protocols for search discovery networks and crawler engines.\n\n## Core Index Links\n"
    llms_txt += f"- [Landingi Agency Optimization Guide 2026]({base_url}/): Base features, pricing models, and system matrices.\n"
    for post in blog_posts:
        llms_txt += f"- [{post['title']}]({base_url}/blog/{post['slug']}.html): {post['desc']}\n"
    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(llms_txt.strip())

    # ==========================================
    # 4. BUILD SYNDICATION LAYER (FEED.XML)
    # ==========================================
    rss_xml = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
    <title>Landingi Review Optimization Core</title>
    <link>{base_url}/</link>
    <description>Programmatic landing page engineering feeds across complex client scaling pipelines.</description>
    <lastBuildDate>{rss_date_str}</lastBuildDate>
    <atom:link href="{base_url}/feed.xml" rel="self" type="application/rss+xml" />"""

    for post in blog_posts[:30]:  # Cap standard RSS ecosystem tracking at 30 nodes to preserve performance parameters
        rss_xml += f"""
    <item>
        <title>{post['title']}</title>
        <link>{base_url}/blog/{post['slug']}.html</link>
        <guid>{base_url}/blog/{post['slug']}.html</guid>
        <description>{post['desc']}</description>
        <pubDate>{rss_date_str}</pubDate>
    </item>"""
        
    rss_xml += "\n</channel>\n</rss>"
    with open("feed.xml", "w", encoding="utf-8") as f:
        f.write(rss_xml.strip())

    # ==========================================
    # 5. BUILD ACCESS INSTRUCTIONS (ROBOTS.TXT)
    # ==========================================
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {base_url}/sitemap.xml")

    # ==========================================
    # 6. BUILD SEARCH MAPPING ARCHIVE (SITEMAP.XML)
    # ==========================================
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls_for_sitemap:
        sitemap_xml += f"    <url>\n        <loc>{url}</loc>\n        <lastmod>{today_str}</lastmod>\n        <changefreq>daily</changefreq>\n        <priority>0.8</priority>\n    </url>\n"
    sitemap_xml += "</urlset>"
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml.strip())
        
    print(f"Success! Core Hub Node, {len(blog_posts)} minified pages, feed.xml, robots.txt, llms.txt, and sitemap.xml initialized cleanly.")

if __name__ == "__main__":
    build_entire_site()
