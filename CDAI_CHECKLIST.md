<!doctype html><html><head><meta charset="utf-8"><title>CDAI Game Plan</title><style>body{font-family:-apple-system,Segoe UI,Helvetica,Arial,sans-serif;color:#1a1a1a;font-size:11pt;line-height:1.45;margin:0}
h1{font-size:22pt;border-bottom:3px solid #b8912f;padding-bottom:6px}h2{font-size:14pt;color:#7a5c12;margin-top:22px;border-bottom:1px solid #ddd;padding-bottom:3px}
code{background:#f3f0e8;padding:1px 4px;border-radius:3px;font-size:9.5pt}hr{display:none}ul{padding-left:22px}
li.task{list-style:none;margin-left:-20px;margin-bottom:5px}.box{display:inline-block;width:12px;height:12px;border:1.5px solid #555;border-radius:2px;margin-right:6px;vertical-align:-1px;font-size:10px;line-height:12px;text-align:center}
li.done .box{background:#b8912f;border-color:#b8912f;color:#fff}li{margin-bottom:3px}</style></head><body><h1>Allocera / CDAI: Master List</h1>
<p>Nick's running list. Claude keeps it current and checks items off as they ship.</p>
<p><strong>Rules:</strong>
- Nothing gets built until Nick has seen it and said yes.
- Every public claim must be provable, and nothing proprietary goes on a public page.
- No years or dates in titles or bylines.
- Keep the original slugs.</p>
<p><em>Last updated: Sept 26, 2026, from a full re-read of the whole chat, Sept 21 to 26.</em></p>
<hr />
<h2>A. Nick's list for tomorrow (WordPress / Google, no code)</h2>
<ol>
<li><strong>Paste the updated homepage.</strong> It's <code>website/homepage.html</code>, which is the live homepage plus the new tracking at the bottom. Nothing else changed. Paste it into the single Elementor HTML widget.</li>
<li><strong>GA4 key events.</strong> In GA4 → Admin → Events, after the first visits come in, mark these as Key events:
   - <code>generate_lead</code>
   - <code>signup_click</code>
   - <code>chat_open</code>
   - <code>calculator_code_verified</code></li>
<li><strong>Schema.</strong> Set Rank Math → Schema → <strong>Article → Blog Post</strong> on the Northbeam, Rockerbox, and validation report (contribution-margin-marketing) pages. The Pages default was already changed to "None" on Sept 26.</li>
<li><strong>Company info.</strong> Rank Math → Titles &amp; Meta → Local SEO: set Organization, "Allocera Intelligence", and the new logo.</li>
<li><strong>Comments and pings.</strong> Turn them off on every post.</li>
<li><strong>One redirect.</strong> <code>/30-day-retest-methodology-2/</code> → <code>/tag-manager-real-roi/</code> (it's an exact copy). Don't redirect <code>/seven-cost-layers/</code>; it's getting a new post.</li>
<li><strong>Delete "every two weeks"</strong> from <code>/newsletter-welcome/</code> and <code>/roas-looks-good-campaigns-lose-money/</code>. No newsletter has been sent yet.</li>
<li><strong>Turn on Rank Math → 404 Monitor.</strong></li>
<li><strong>Search Console exports.</strong> Click each reason and export its URL list:
   - "Crawled – currently not indexed" (16)
   - "noindex" (4)
   - "404" (2)
   - "Redirect error" (1)</li>
<li><strong>Rank Math titles and descriptions</strong> for the privacy, terms, and data-deletion pages. They have none.</li>
<li><strong>Categories (later).</strong> Every post is "Uncategorized". Create these and assign each post:<ul>
<li>Marketing Methodology</li>
<li>Tool Comparisons</li>
<li>Personal Injury Law</li>
<li>Home Services</li>
<li>More Industries</li>
</ul>
</li>
<li>
<p><strong><code>/home-sample/</code> pages (later, no rush).</strong> Set Parent to "(no parent)" on these 7, and add a 301 from each old URL:</p>
<ul>
<li>Northbeam</li>
<li>Rockerbox</li>
<li>validation report</li>
<li>case study</li>
<li>privacy</li>
<li>terms</li>
<li>data deletion</li>
</ul>
<p>Claude then updates every internal link.
13. <strong>Tag Manager (optional).</strong> Tracking now runs straight into GA4. If you create a GTM container, send the <code>GTM-XXXXXXX</code> ID; the events already push to <code>dataLayer</code>, so GTM picks them up too.</p>
</li>
</ol>
<p><strong>Done Sept 26:</strong> every page is on Elementor Canvas (leave it), and the schema defaults are fixed (Posts: Article → Blog Post; Pages: None).</p>
<hr />
<h2>B. Website pages (Claude builds, Nick pastes)</h2>
<p>Full page-by-page list: <strong><code>website/FIX_LIST.md</code></strong> (41 pages still carry old or false info).</p>
<table>
<thead>
<tr>
<th>#</th>
<th>Page</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><code>/net-marketing-contribution/</code></td>
<td>LIVE, <strong>91</strong></td>
</tr>
<tr>
<td>2</td>
<td><code>/calculate-contribution-margin/</code></td>
<td>LIVE, <strong>90</strong></td>
</tr>
<tr>
<td>3</td>
<td><code>/scale-hold-cut-pause-framework/</code></td>
<td>LIVE, <strong>89</strong></td>
</tr>
<tr>
<td>4</td>
<td><code>/triple-whale-vs-rockerbox-vs-allocera/</code></td>
<td>LIVE, <strong>90</strong> (optional: drop "2026" from the SEO title)</td>
</tr>
<tr>
<td>5</td>
<td><code>/home-sample/northbeam-alternative/</code></td>
<td>LIVE, <strong>90</strong></td>
</tr>
<tr>
<td>6</td>
<td><code>/home-sample/rockerbox-alternative/</code></td>
<td>LIVE (score not reported)</td>
</tr>
<tr>
<td>7</td>
<td><code>/cost-per-signed-case/</code></td>
<td>LIVE, <strong>90</strong></td>
</tr>
<tr>
<td>8</td>
<td><code>/blog/</code> (Nick's design, new content)</td>
<td>LIVE, <strong>72</strong> (normal for a directory page)</td>
</tr>
<tr>
<td>9</td>
<td>Homepage</td>
<td>LIVE. <strong>Tracking added Sept 26: paste it (A1).</strong></td>
</tr>
<tr>
<td>10</td>
<td><strong>NEXT: <code>/30-day-retest-methodology/</code></strong></td>
<td>Rebuild around the Sept 2026 validation (89.5%) and remove the fake 80%. Nick sent the current HTML. Verify every "retest" claim against the engine first.</td>
</tr>
<tr>
<td>11</td>
<td><code>/seven-cost-layers/</code></td>
<td>New post at the same URL (246 impressions). The concept is dead; the new topic is hidden marketing costs, stated plainly.</td>
</tr>
<tr>
<td>12</td>
<td><code>/55-directives-study/</code></td>
<td>301 to the validation report (the whole page is the fake 80%)</td>
</tr>
<tr>
<td>13</td>
<td><code>/tag-manager-real-roi/</code>, <code>/allocera-vs-salesforce/</code>, <code>/true-cac/</code> + <code>/true-cac-2/</code> (merge)</td>
<td>Full rebuilds (80%, seven layers, pasted head)</td>
</tr>
<tr>
<td>14</td>
<td><code>/marketing-margin-distortion-index/</code></td>
<td><strong>Nick decides:</strong> rebuild or retire (80%, Apex, "2026" in the title, unsourced stats)</td>
</tr>
<tr>
<td>15</td>
<td><code>/proof/</code>, <code>/allocera-intelligence-case-study-proof/</code>, <code>/case-study-2-oauth-validation/</code></td>
<td><strong>Nick decides:</strong> these are the Apex story. Rewrite around the validation, or retire.</td>
</tr>
<tr>
<td>16</td>
<td><code>/how-it-works/</code>, <code>/about/</code></td>
<td>Full rebuilds</td>
</tr>
<tr>
<td>17</td>
<td><code>/dashboard/</code>, validation report, terms, newsletter welcome</td>
<td>Light cleans or quick fixes</td>
</tr>
<tr>
<td>18</td>
<td><code>/pricing/</code></td>
<td><strong>ON HOLD</strong> while the free audit is worked out</td>
</tr>
<tr>
<td>19</td>
<td>22 remaining blog posts</td>
<td>Full rebuild if they have traffic, light clean if not (see FIX_LIST Tier 3)</td>
</tr>
</tbody>
</table>
<p><strong>What "light clean" means:</strong> keep the post and its design. Remove the pasted head, the seven layers, the 80%, Apex, the unsourced numbers, and the old "$2,500, don't pay if…" offer, and fix the links.</p>
<p><strong>Google index (Sept 26):</strong> 46 pages indexed, 44 not. 16 are "crawled, not indexed", which the rebuilds fix. The rest need Nick's exports (A9).</p>
<hr />
<h2>C. Homepage tracking (added Sept 26, in <code>website/homepage.html</code>)</h2>
<p>Everything reports to GA4 <code>G-29J4V3VQ7B</code>. It loads GA4 only if the site doesn't already, so page views never double-count. Every event also pushes to <code>dataLayer</code> for Tag Manager. No names, emails, or chat text are ever sent.</p>
<table>
<thead>
<tr>
<th>Event</th>
<th>When it fires</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>chat_open</code>, <code>chat_message_sent</code>, <code>chat_suggestion_click</code>, <code>chat_close</code></td>
<td>VINDEX / Ask CDAI</td>
</tr>
<tr>
<td><code>calculator_start</code>, <code>calculator_code_requested</code>, <code>calculator_code_verified</code></td>
<td>Distortion calculator</td>
</tr>
<tr>
<td><code>form_submit</code>, <code>generate_lead</code></td>
<td>Free audit / contact form (<code>generate_lead</code> fires on success)</td>
</tr>
<tr>
<td><code>signup_click</code>, <code>portal_click</code>, <code>pricing_click</code></td>
<td>Get Started, Client Portal, and any pricing link</td>
</tr>
<tr>
<td><code>button_click</code>, <code>scroll_link_click</code>, <code>email_click</code>, <code>phone_click</code>, <code>menu_open</code></td>
<td>Every other button and link, with its text and section</td>
</tr>
<tr>
<td><code>section_view</code></td>
<td>Each homepage section a visitor reaches: hero, tools, problem, how, capabilities, calculator, FAQ, intake</td>
</tr>
</tbody>
</table>
<p><strong>Views of the pricing page itself:</strong> GA4 → Reports → Pages and screens → <code>/pricing/</code>.</p>
<p>Tested in a browser Sept 26: all events fired with 0 errors.</p>
<hr />
<h2>D. Decisions for Nick (open)</h2>
<ul>
<li><strong>D2. Engine default costs.</strong> CSV uploads add a 2.9–3% platform fee, and Meta lead forms, Ringba, Boberdoo, CSV, and webhook leads add $0.25 per lead of compliance cost. Neither affects the validation or Apex. CallRail is already $0.</li>
<li><em>Recommendation:</em> default both to $0 unless the client supplies real values, before the first client who uploads a CSV.</li>
<li><strong>D3. Calculator hint.</strong> It says "default $0.25", but the calculator actually uses $0.</li>
<li><em>Recommendation:</em> reword it to "only if you pay for per-lead consent certificates".</li>
<li><strong>D4. Fake names and emails.</strong> 2,738 simulated-business lead records still hold them.</li>
<li><em>Recommendation:</em> strip them.</li>
<li><strong>D5. Sync on connect.</strong> Run the first data pull as soon as a client connects, instead of waiting for 2 AM UTC.</li>
<li><em>Recommendation:</em> yes.</li>
<li><strong>D6. AI links section</strong> (ChatGPT/Claude/Perplexity/Grok). <strong>On Sept 25 Nick said he wanted it kept.</strong> It is NOT in the current homepage.</li>
<li><em>Claude's view:</em> no proven SEO effect, and it sends visitors away.</li>
<li>Nick decides. If yes, Claude adds it back.</li>
<li><strong>D7. The intake form's job</strong> now that self-serve is live.</li>
<li><em>Recommendation:</em> free-audit request now; "Partner with us / talk to Nick" once the free audit is settled.</li>
<li><strong>D8. Apex.</strong> Still receiving leads (last one Sept 24), but 0 ad-spend rows and 0 active campaigns, so no decisions since Aug 13.</li>
<li><em>Ask Nick:</em> is their ad spend paused, or should Claude check the connection?</li>
<li><strong>Free audit credit wording.</strong> Pricing page: "first 90 days"; homepage: "100% toward a retainer". Pick one when the free audit is settled.</li>
</ul>
<hr />
<h2>E. Engine and product (Claude, after a yes)</h2>
<ul>
<li class="task"><span class="box"></span> <strong>Free Distortion Audit in Stripe.</strong> Being handled in another Claude Code session; the prompt is in <code>STRIPE_FREE_AUDIT_PROMPT.md</code>. On hold while Nick works it out.</li>
<li class="task"><span class="box"></span> <strong>Adapter fixes before turning on nightly sync</strong> (CallRail is already live, PR #28):</li>
<li>Bing puts all spend under one campaign.</li>
<li>Boberdoo's lead cost never reaches true cost.</li>
<li>Stripe assumes a 7% fee.</li>
<li>Ringba drops partner payouts.</li>
<li class="task"><span class="box"></span> <strong>Digest email logo fix.</strong> Offered, awaiting a yes.</li>
<li class="task"><span class="box"></span> <strong>Clean up the [SIM] nightly errors.</strong> Offered, awaiting a yes.</li>
<li class="task"><span class="box"></span> <strong>VINDEX live test.</strong> Ask about 15 real prospect and investor questions; Nick reviews the answers.</li>
<li>Must say: clients need HubSpot or Salesforce, and run paid ads and/or buy leads.</li>
<li>Must never contradict the validation.</li>
<li class="task"><span class="box"></span> <strong>VINDEX upgrades:</strong> streaming replies, clear hand-off-to-Nick rules, and a weekly transcript review.</li>
<li class="task"><span class="box"></span> <strong>Manuals rewrite.</strong> Remove "7 cost layers", "no self-serve", the old acronym, the stale integration counts, and the 80%.</li>
<li class="task"><span class="box"></span> <strong>VINDEX trademark check</strong> (Nick): a registered VINDEX mark exists (Vindex LLC, esports, serial 88671256).</li>
<li class="task"><span class="box"></span> <strong>Competitive research.</strong> Offered, awaiting a yes.</li>
</ul>
<hr />
<h2>F. Homepage video (Nick: "needs to be redone: good but cheap")</h2>
<ul>
<li class="task"><span class="box"></span> Claude writes the script (demo/explainer style, 90 seconds to 3 minutes). Nick approves it.</li>
<li class="task"><span class="box"></span> Nick sends a screen recording of the portal, plus the logo and screenshots.</li>
<li class="task"><span class="box"></span> Voiceover: Nick's own voice (best for trust), or free text-to-speech.</li>
<li class="task"><span class="box"></span> Claude renders a motion-graphics cut (1080p, no watermark).</li>
<li class="task"><span class="box"></span> Publish on YouTube with "Allocera" and "CDAI" in the title, then embed it at the top of the homepage. It must autoplay muted and load instantly.</li>
</ul>
<hr />
<h2>G. Growth ideas (Nick says yes or no to each)</h2>
<ul>
<li class="task"><span class="box"></span> Show the price level ("from $1,500/mo") near the main button.</li>
<li class="task"><span class="box"></span> Founder block: Nick, 3 years building, photo. Needs a photo and Nick's OK.</li>
<li class="task"><span class="box"></span> A sample report visitors can open (a clearly labeled fictional business).</li>
<li class="task"><span class="box"></span> "15 minutes with the founder" booking button (free Calendly).</li>
<li class="task"><span class="box"></span> Date the proof: "Validated Sept 2026".</li>
<li class="task"><span class="box"></span> Get the two Apex reviews onto G2.</li>
<li class="task"><span class="box"></span> YouTube channel (the video is the first upload), and founder-voice answers on Reddit (r/PPC, r/marketing, r/smallbusiness).</li>
<li class="task"><span class="box"></span> Organization + SoftwareApplication schema on the homepage.</li>
<li class="task"><span class="box"></span> Check that robots.txt allows AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended).</li>
<li class="task"><span class="box"></span> New posts for high-value keywords:</li>
<li>"google ads optimization" (390/mo)</li>
<li>"personal injury law firm marketing" (720/mo, CPC about $106)</li>
</ul>
<hr />
<h2>H. Security (Nick; important)</h2>
<ul>
<li class="task"><span class="box"></span> <strong>Supabase service-role key:</strong> it was pasted in chat on Sept 21. Rotate it in Supabase → Settings → API, then update it everywhere it's used (Render env vars).</li>
<li class="task"><span class="box"></span> <strong>Supabase database password:</strong> hardcoded in <code>run_full_directive.py</code> and <code>time_engine.py</code>, and the former cofounder may know it. Rotate it.</li>
<li class="task"><span class="box"></span> <strong>Anthropic key pasted in chat on Sept 25:</strong> make sure it's revoked in the Anthropic console. The chat bot must only use the new key stored in Render (<code>ANTHROPIC_API_KEY_chat_bot</code>).</li>
<li class="task"><span class="box"></span> Rotate other shared keys the former cofounder could have seen (Resend, Stripe, Render).</li>
<li class="task"><span class="box"></span> Check the team member lists in Render and Supabase.</li>
<li class="task"><span class="box"></span> Delete the 19 old validation cron jobs on Render (they re-run every year).</li>
</ul>
<hr />
<h2>I. Partnerships</h2>
<ul>
<li class="task done"><span class="box">&#10003;</span> CallRail email sent Sept 25, with the logo and listing description. The call with Karina and Eric is <strong>booked</strong>.</li>
<li class="task"><span class="box"></span> Before the call: be ready to explain how the integration will be promoted (pricing page, integration docs, outreach).</li>
<li class="task"><span class="box"></span> Direction: partner with companies that already have the customers (CallRail first).</li>
</ul>
<hr />
<h2>J. Access that would help Claude (Nick)</h2>
<ul>
<li class="task"><span class="box"></span> <strong>Network allowlist</strong> (cloud environment → Edit → Network access). Add your own site so Claude can check live pages, plus <code>support.google.com</code>, <code>nngroup.com</code>, <code>gartner.com</code>, <code>facebook.com</code>, and <code>wikipedia.org</code>.</li>
<li class="task"><span class="box"></span> <strong>Gmail for alloceraintelligence@gmail.com</strong>, if Claude should read the Control Tower emails. The connected Gmail is fullsendorganicks@gmail.com.</li>
<li class="task"><span class="box"></span> <strong>PageSpeed score:</strong> run pagespeed.web.dev (mobile) on the homepage and send the number.</li>
</ul>
<hr />
<h2>Done</h2>
<ul>
<li class="task done"><span class="box">&#10003;</span> <strong>Sept 26:</strong></li>
<li>8 pages rebuilt (scores above).</li>
<li>Blog rebuilt on Nick's design.</li>
<li>Every page moved to Elementor Canvas.</li>
<li>Schema defaults fixed.</li>
<li>Homepage tracking built and tested.</li>
<li>Full fix list written.</li>
<li>Stripe free-audit prompt written.</li>
<li class="task done"><span class="box">&#10003;</span> <strong>Sept 25:</strong></li>
<li>Homepage final and live: hero kept, "What CDAI does", trust FAQs, US-accurate calculator, real logos, no fake numbers.</li>
<li>VINDEX chat live.</li>
<li>Dashboard trust fix, SCALE fix (98.0%), privacy fix, CallRail nightly sync + campaign mapping, and $0 call compliance cost.</li>
<li>Math re-verified: all 1,352 validation grades reproduced exactly.</li>
<li>PAUSE 85.2%: keep quoting it (Nick).</li>
<li class="task done"><span class="box">&#10003;</span> Former cofounder fully offboarded (PR #16).</li>
</ul>
<p><strong>Verified facts to reuse:</strong>
- 89.5% overall (1,210/1,352), math 100%.
- By decision: Scale 98.0%, Hold 95.2%, Pause 85.2%, Flag 70.9% (82 neutral), Cut 55.6%, Investigate 100%, Renegotiate 100%, Quarantine 12/12 caught.
- CDAI = Capital, Decision, Accuracy, Intelligence.
- Clients need HubSpot or Salesforce, plus paid ads and/or bought leads.
- Self-serve is live.
- Retainers start at $1,500/mo.
- USA only.
- Seven cost layers is dead.</p></body></html>