# 🛍️ Shopping Behavior Analysis Report

**Project:** Understanding Customer Shopping Patterns  
**Prepared by:** Hemant Dhake  
**Date:** February 14, 2026

---

## 1. Executive Summary

This report explores real shopping behavior of ~3,900 customers to answer practical business questions:

- Which product categories bring in the most money?  
- Who is actually spending — and how much?  
- Do discounts and promos really move the needle?  
- Are there clear patterns in reviews and repeat purchases?

**Main takeaways at a glance:**

- Clothing is by far the biggest revenue driver (~45–50% of total sales)  
- Middle-aged customers (35–54 years) tend to have the highest average spend  
- Discounts & promo codes are used in ~45% of purchases and clearly lift average order value  
- Repeat customers (≥10 previous purchases) contribute significantly more revenue  
- Review ratings are generally good (avg ~3.7–3.8), but some categories consistently score lower

These insights can help prioritize inventory, refine promotions, target the right age groups, and build stronger loyalty mechanics.

---

## 2. Quick Look at the Data

- **Total transactions:** 3,900  
- **Unique customers:** 3,900 (each row = one purchase)  
- **Number of columns:** 18 original + 5 engineered  
- **Time period:** not specified (cross-sectional snapshot)  
- **Missing values:** almost none after basic cleaning  
- **Duplicates removed:** 0 (clean dataset)

**Most important columns used in this analysis:**

- Age, Gender  
- Category, Item Purchased, Purchase Amount (USD)  
- Review Rating  
- Previous Purchases, Subscription Status  
- Season, Discount Applied, Promo Code Used  
- Payment Method, Frequency of Purchases

---

## 3. What We Actually Discovered

### 3.1 Gender Split – Mostly Male shoppers in this dataset

- **Male:** ~68%  
- **Female:** ~32%

Even though the dataset is male-heavy, spending behavior per purchase doesn't show dramatic differences between genders.

**Takeaway for marketing:**  
You can run mostly gender-neutral campaigns — but keep female-focused creatives / products ready, since they are underrepresented here.

### 3.2 Which Categories Make the Most Money?

**Top revenue generators (total sales):**

1. **Clothing**          – by far the leader  
2. **Footwear**  
3. **Accessories**  
4. **Outerwear**

Clothing alone usually accounts for ~45–50% of total revenue in this snapshot.

**Surprising observation:**  
Outerwear often has the **highest average order value** even though it sells fewer units.

**Actionable insight:**  
Protect and grow Clothing & Footwear inventory.  
Consider bundling Outerwear with Clothing items during fall/winter seasons.

### 3.3 Age & Spending – Who Spends the Most?

- Weak positive correlation between age and purchase amount (r ≈ 0.05–0.12)  
- Highest average spend usually comes from **35–54 year olds**  
- Young adults (18–34) buy more frequently but smaller baskets  
- Seniors (55+) tend to be very selective — high AOV when they do buy

**Business implication:**  
Middle-age segment is your sweet spot for premium / full-price products.  
Younger customers respond better to discounts, bundles, and trendy items.

### 3.4 Review Ratings – Where Are Customers Happiest?

**Average rating by category (approx):**

- Accessories   ~3.75–3.85  
- Clothing      ~3.70–3.80  
- Footwear      ~3.65–3.75  
- Outerwear     ~3.60–3.70

Interesting pattern: categories with **higher average price** (Outerwear, Footwear) tend to get slightly **lower ratings** — possibly due to fit & comfort expectations.

**Recommendation:**  
Run focused quality audits / return analysis on Outerwear and Footwear.  
Even a 0.2–0.3 point rating increase can significantly improve repeat purchase probability.

### 3.5 Loyalty & Repeat Buyers

Customers with **10+ previous purchases**:

- Represent ~35–45% of transactions  
- Usually spend 15–30% more per order  
- Much higher likelihood of using subscription status

**Quick win:**  
Launch a simple points-based loyalty program or “VIP early access” for people with ≥8–10 past purchases.

---

## 4. New Features We Created

To make analysis and future modeling easier, we added:

- `Age_Group` (Teen / Young Adult / Adult / Middle Age / Senior)  
- `Purchase_Category` (Very Low / Low / Medium / High / Very High)  
- `Discount_or_Promo` (Yes/No flag when either is used)  
- `Is_Repeat_Customer` (1 if Previous Purchases ≥ 10)  
- `Season_Category` interaction (e.g. Winter_Clothing, Summer_Footwear)

These fields make segmentation and rule-based targeting much more powerful.

---

## 5. How We Treated Outliers

Used classic **1.5 × IQR** rule and **capped** (winsorized) values for:

- Purchase Amount  
- Previous Purchases  
- Age  
- Review Rating

→ No extreme values were deleted — we just brought them in line so they don’t distort averages and models.

---

## 6. Practical Recommendations for the Business

1. **Double down on Clothing** — it’s your cash cow. Protect margin here.  
2. **Push Outerwear in colder months** — highest AOV potential.  
3. **Target 35–54 age group** with full-price / premium messaging.  
4. **Use discounts smartly for 18–34 segment** — they are price sensitive.  
5. **Improve perceived quality in Footwear & Outerwear** — ratings are dragging slightly.  
6. **Build a loyalty loop** — reward repeat buyers early (at ~8–10 purchases).  
7. **Test subscription + promo combo** — very strong signal in the data.

---

## 7. What Could We Do Next?

- Run **RFM analysis** or **K-Means clustering** to create proper customer segments  
- Build a **regression model** to predict purchase amount  
- Create **product association rules** (market basket analysis)  
- Develop **recommendation system** (collaborative filtering or content-based)  
- Build an **interactive dashboard** (Streamlit / Plotly Dash / Power BI)  
- A/B test discount messaging and loyalty reward structures

---

## 8. Final Thoughts

Even from this relatively simple dataset, clear patterns emerge:

- Clothing dominates revenue  
- Middle-age customers are high-value  
- Discounts work — but shouldn’t be everywhere  
- Quality perception in higher-price categories needs attention  
- Loyalty already exists — we just need to recognize and reward it

This kind of analysis — even at an early stage — already gives concrete direction for inventory planning, promotion strategy, and customer targeting.

Thank you for reading!  
Happy to discuss any part in more detail or help implement next steps.

Hemant Dhake  
14 February, 2026  
Pune
