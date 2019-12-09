# from docxtpl import DocxTemplate

# doc = DocxTemplate("LetterHead.docx")
# tpl=DocxTemplate('LetterHead.docx')
# #rt = RichText('You can add an hyperlink, here to ')
# #rt.add('google',url_id=tpl.build_url_id('http://google.com'))
# tpl.replace_pic('logo.png','sbfc.png')
# #context = { 'company_name' : "World company" }
# #doc.render(context)
# tpl.save("generated_doc.docx")

from docxtpl import DocxTemplate

headerImageUrl = './header.png'
footerImageUrl = './footer.png'
templateUrl = './LetterHeadTemplate.docx'       

docx_template = DocxTemplate('./LetterHeadTemplate.docx')

docx_template.replace_pic('header_sample.png',headerImageUrl)
docx_template.replace_pic('footer_sample.png',footerImageUrl)

docx_template.save("generated_doc.docx")