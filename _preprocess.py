from bs4 import BeautifulSoup
import re

def anchor_base_url_preprocessor(app, docname, source):
    # Get the YAML metadata from the source
    yaml_metadata = re.search(r'^\s*---([\s\S]*?)---', source, re.MULTILINE)
    if yaml_metadata:
        yaml_metadata = yaml_metadata.group(1)
    else:
        return

    # Extract the anchorBaseUrl value from YAML metadata
    match = re.search(r'^\s*anchorBaseUrl:(.*)$', yaml_metadata, re.MULTILINE)
    if match:
        anchor_base_url = match.group(1).strip()
    else:
        return

    # Parse the HTML content
    soup = BeautifulSoup(source, 'html.parser')

    # Add the script tag to set anchorBaseUrl in the head
    script_tag = soup.new_tag('script')
    script_tag.string = f'var anchorBaseUrl = "{anchor_base_url}";'
    head_tag = soup.find('head')
    if head_tag:
        head_tag.insert(0, script_tag)

    # Update the source with the modified HTML
    source_lines = source.split('\n')
    updated_html = str(soup)
    updated_lines = updated_html.split('\n')
    source_lines[:len(updated_lines)] = updated_lines
    source = '\n'.join(source_lines)

    return source
