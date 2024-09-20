#!/usr/bin/env python3

# from fpdf import FPDF

# pdf = FPDF("P", "mm", "A4")
# pdf.add_page()
# pdf.set_font("Arial", "B", 16)
# pdf.cell(40, 10, "Hello World!")
# pdf.output("tuto1.pdf", "F")


# from fpdf import FPDF


# class PDF(FPDF):
#     def header(self):
#         # Logo
#         self.image("logo.png", 10, 8, 33)
#         # Arial bold 15
#         self.set_font("Arial", "B", 15)

#         self.set_draw_color(0, 80, 180)
#         self.set_fill_color(33, 33, 33)
#         self.set_text_color(220, 50, 50)

#         # Move to the right
#         self.cell(120)
#         # Title
#         self.cell(30, 10, "Prova titolo", 1, 0, "C", 1)
#         # Line break
#         self.ln(20)

#     # Page footer
#     def footer(self):
#         # Position at 1.5 cm from bottom
#         self.set_y(-15)
#         # Arial italic 8
#         self.set_font("Arial", "I", 8)
#         # Page number
#         self.cell(0, 10, "Page " + str(self.page_no()) + "/{nb}", 0, 0, "C")


# # Instantiation of inherited class
# pdf = PDF("L")
# pdf.alias_nb_pages()
# pdf.add_page()
# pdf.set_font("Times", "", 12)
# for i in range(1, 10000):
#     pdf.cell(0, 10, "Printing line number " + str(i), 0, 1)
#     # pdf.dashed_line(10, 30, 110, 30, 1, 10)
# pdf.output("tutorial.pdf", "F")


# from fpdf import Template

# # this will define the ELEMENTS that will compose the template.
# elements = [
#     {
#         "name": "company_logo",
#         "type": "I",
#         "x1": 20.0,
#         "y1": 17.0,
#         "x2": 78.0,
#         "y2": 30.0,
#         "font": None,
#         "size": 0.0,
#         "bold": 0,
#         "italic": 0,
#         "underline": 0,
#         "foreground": 0,
#         "background": 0,
#         "align": "I",
#         "text": "logo",
#         "priority": 2,
#     },
#     {
#         "name": "company_name",
#         "type": "T",
#         "x1": 17.0,
#         "y1": 32.5,
#         "x2": 115.0,
#         "y2": 37.5,
#         "font": "Arial",
#         "size": 12.0,
#         "bold": 1,
#         "italic": 0,
#         "underline": 0,
#         "foreground": 0,
#         "background": 0,
#         "align": "I",
#         "text": "",
#         "priority": 2,
#     },
#     {
#         "name": "box",
#         "type": "B",
#         "x1": 15.0,
#         "y1": 15.0,
#         "x2": 185.0,
#         "y2": 260.0,
#         "font": "Arial",
#         "size": 0.0,
#         "bold": 0,
#         "italic": 0,
#         "underline": 0,
#         "foreground": 0,
#         "background": 0,
#         "align": "I",
#         "text": None,
#         "priority": 0,
#     },
#     {
#         "name": "box_x",
#         "type": "B",
#         "x1": 95.0,
#         "y1": 15.0,
#         "x2": 105.0,
#         "y2": 25.0,
#         "font": "Arial",
#         "size": 0.0,
#         "bold": 1,
#         "italic": 0,
#         "underline": 0,
#         "foreground": 0,
#         "background": 0,
#         "align": "I",
#         "text": None,
#         "priority": 2,
#     },
#     {
#         "name": "line1",
#         "type": "L",
#         "x1": 100.0,
#         "y1": 25.0,
#         "x2": 100.0,
#         "y2": 57.0,
#         "font": "Arial",
#         "size": 0,
#         "bold": 0,
#         "italic": 0,
#         "underline": 0,
#         "foreground": 0,
#         "background": 0,
#         "align": "I",
#         "text": None,
#         "priority": 3,
#     },
#     {
#         "name": "barcode",
#         "type": "BC",
#         "x1": 20.0,
#         "y1": 246.5,
#         "x2": 140.0,
#         "y2": 254.0,
#         "font": "Interleaved 2of5 NT",
#         "size": 0.75,
#         "bold": 0,
#         "italic": 0,
#         "underline": 0,
#         "foreground": 0,
#         "background": 0,
#         "align": "I",
#         "text": "200000000001000159053338016581200810081",
#         "priority": 3,
#     },
# ]

# # here we instantiate the template and define the HEADER
# f = Template(format="A4", elements=elements, title="Prova Titolo")
# f.add_page()

# # we FILL some of the fields of the template with the information we want
# # note we access the elements treating the template instance as a "dict"
# f["company_name"] = "CL SYSTEM"
# f["company_logo"] = "logo.png"

# # and now we render the page
# f.render("./template.pdf")


from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Logo
        self.image("cu.png", 0, 0, 200, 290)
        # Arial bold 15
        self.set_font("Arial", "B", 15)

        self.set_draw_color(0, 80, 180)
        self.set_fill_color(33, 33, 33)
        self.set_text_color(220, 50, 50)

        # Move to the right
        self.cell(120)
        # Title
        self.cell(30, 10, "Prova titolo", 1, 0, "C", 1)
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font("Arial", "I", 8)
        # Page number
        self.cell(0, 10, "Page " + str(self.page_no()) + "/{nb}", 0, 0, "C")


# Instantiation of inherited class
pdf = PDF("P")
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font("Times", "", 8)


pdf.text(40, 66, "MRCLSS85H02F952H")
pdf.text(40, 77, "CL SYSTEM INFORMATICA SRL")

# pdf.cell(58, 70, "MRCLSS85H02F952H", 0, 1, "R")

# for i in range(1, 60):
# pdf.cell(0, 10, "Printing line number " + str(i), 0, 1)

pdf.output("tutorial.pdf", "F")
