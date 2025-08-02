from scub_trust_deed import scrub_document_from_content
import os

if __name__ == '__main__':
    input_file = 'assetarc/bots/Trust_Bot/templates/trust_template.docx'
    output_file = 'assetarc/bots/Trust_Bot/templates/trust_template_scrubbed.docx'

    with open(input_file, 'rb') as f:
        content = f.read()

    scrub_document_from_content(content, output_file)
    print(f"Scrubbed document saved to {output_file}")
