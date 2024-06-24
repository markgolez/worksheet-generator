from lxml import etree
from docx import Document
from sympy import *
from lxml.etree import XMLSyntaxError

# create expression
x, y = symbols('x y')
expr1 = 64*x**6 - 280*x**3 + 216

# create MathML structure
expr1xml = mathml(expr1, printer='presentation')
tree = etree.fromstring(
    '<math xmlns="http://www.w3.org/1998/Math/MathML">'+expr1xml+'</math>')

# convert to MS Office structure
xslt = etree.parse('MML2OMML.XSL')
transform = etree.XSLT(xslt)
new_dom = transform(tree)

# write to docx
document = Document()
p = document.add_paragraph()
p._element.append(new_dom.getroot())
document.save("simpleEq.docx")
