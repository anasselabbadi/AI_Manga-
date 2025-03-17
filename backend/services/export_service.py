from reportlab.pdfgen import canvas

def export_to_pdf(scenario_id):
    file_path = f"exports/manga_{scenario_id}.pdf"
    c = canvas.Canvas(file_path)
    c.drawString(100, 750, f"Manga exporté - ID {scenario_id}")
    c.save()
    return file_path
