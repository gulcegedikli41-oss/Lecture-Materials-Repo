"""Week 3 project A: apply a transparent retail order policy."""

print("Retail Order Policy")
customer = input("Customer name: ").strip()
amount = float(input("Basket amount: "))
member = input("Member (yes/no): ").strip().lower() == "yes"
destination = input("Destination (local/national): ").strip().lower()

if amount < 0:
    print("Invalid basket amount. No quote can be produced.")
elif destination != "local" and destination != "national":
    print("Invalid destination. Choose local or national.")
else:
    if member and amount >= 1000:
        discount_rate = 0.15
        policy = "Member order of at least 1000 TRY"
    elif member:
        discount_rate = 0.05
        policy = "Member discount"
    elif amount >= 1500:
        discount_rate = 0.10
        policy = "Large order discount"
    else:
        discount_rate = 0.0
        policy = "Standard price"

    discount = amount * discount_rate
    after_discount = amount - discount
    if destination == "local":
        shipping = 0.0 if after_discount >= 500 else 35.0
    else:
        shipping = 0.0 if after_discount >= 1000 else 75.0
    total = after_discount + shipping

    print()
    print("=" * 52)
    print(f"ORDER QUOTE FOR {customer}")
    print("=" * 52)
    print(f"Policy: {policy}")
    print(f"Basket amount:  {amount:9.2f} TRY")
    print(f"Discount:      -{discount:9.2f} TRY")
    print(f"Shipping:       {shipping:9.2f} TRY")
    print(f"Total:          {total:9.2f} TRY")
    print("=" * 52)
    
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("Arial", "", "/System/Library/Fonts/Supplemental/Arial.ttf")
    pdf.add_font("Arial", "B", "/System/Library/Fonts/Supplemental/Arial Bold.ttf")

    # Başlık bandı
    pdf.set_fill_color(30, 60, 114)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", "B", 20)
    pdf.cell(0, 18, "Sipariş Teklifi", align="C", fill=True,
             new_x="LMARGIN", new_y="NEXT")

    pdf.ln(6)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Müşteri: {customer}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, f"Politika: {policy}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(4)

    # Tutar tablosu
    rows = [
        ("Sepet tutarı", f"{amount:,.2f} TRY"),
        ("İndirim", f"-{discount:,.2f} TRY"),
        ("Kargo", f"{shipping:,.2f} TRY"),
    ]
    for label, value in rows:
        pdf.cell(120, 10, label, border="B")
        pdf.cell(0, 10, value, border="B", align="R",
                 new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Arial", "B", 14)
    pdf.set_fill_color(230, 236, 245)
    pdf.cell(120, 12, "TOPLAM", fill=True)
    pdf.cell(0, 12, f"{total:,.2f} TRY", align="R", fill=True,
             new_x="LMARGIN", new_y="NEXT")

    pdf.output(f"teklif_{customer.replace(' ', '_')}.pdf")
    print("PDF oluşturuldu.")

