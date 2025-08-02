import zipfile

def get_docx_xml_content(docx_path):
    with zipfile.ZipFile(docx_path, 'r') as zip_ref:
        xml_content = zip_ref.read('word/document.xml')
    return xml_content

if __name__ == '__main__':
    input_file = 'assetarc/bots/Trust_Bot/templates/trust_template.docx'
    xml_content = get_docx_xml_content(input_file)
    print(xml_content.decode('utf-8'))
