"""
 Markdown builder
 Converts markdown files to html using the gitlab markdown API
"""

import os
import re
import json
import base64
import urllib.request
import mimetypes

BUILD_COMMAND = 'pandoc --webtex --ascii -f markdown -t html5 -o {} {}'
ROOT_DIR = '..'
TARGET_DIR = 'out' # HTML files will be created here.

IGNORE_DIRS = ['.git', 'Builder', 'out']
IGNORE_FILES = [ROOT_DIR + '\\README.md']


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def write_file(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)


def get_mime_type(file_path):
    mime_type_and_encoding = mimetypes.guess_type(file_path)
    mime_type = mime_type_and_encoding[0]
    return mime_type


def encode_base64(data):
    return base64.b64encode(data).decode('ASCII')


def get_file_base64(file_path):
    with open(file_path, 'rb') as f:
        return encode_base64(f.read())


def build_request(data):
    json_data = dict()
    json_data['text'] = data
    json_data['gfm'] = False

    headers = dict()
    headers['Content-Type'] = 'application/json'
    return headers, json.dumps(json_data)


def pandoc_convert(file_name):
    output_file = file_name + '.tmp'
    response = os.system(BUILD_COMMAND.format('"' + output_file + '"', '"' + file_name + '"'))
    if response != 0:
        raise Exception("pandoc convert failed")
    html_data = read_file(file_name + '.tmp')
    os.unlink(output_file)
    return html_data


def embed_file_in_tag(file_dir_name, tag_name, target_name, html, download=False):
    # Search for all file targets in all tags
    tag_match = re.findall(r'<' + tag_name + r'[^>]*' + target_name + r'\s*=\s*"([a-zA-Z0-9 _.]*)"', html)

    # For each file: find the target file, read the file data, and embed the file
    for tgt_name in tag_match:

        try:
            # Retrieve the file from the target directory
            tgt_base64 = get_file_base64(file_dir_name + "\\" + tgt_name)

            # Determine file type
            data_type = get_mime_type(file_dir_name + "\\" + tgt_name)

            # Replace the target in the tag with the file data
            search_regex = target_name + r'\s*=\s*"' + tgt_name + '"'
            download_string = 'download="' + tgt_name + '" ' if download else ''
            replace_string = download_string + target_name + '="data:' + data_type + ';base64, ' + tgt_base64 + '"'
            html = re.sub(search_regex, replace_string, html)
        except Exception as err:
            print(err)
    return html


def replace_img_src(img_dir, html):
    return embed_file_in_tag(img_dir, "img", "src", html)


def replace_a_href(file_dir, html):
    return embed_file_in_tag(file_dir, "a", "href", html, download=True)

# def replace_img_src(img_dir, converted_html):
#     img_match = re.findall(r'img.*src\s*=\s*"([a-zA-Z0-9 _.]*)"', converted_html)
#     for img_name in img_match:
#         img_base64 = get_file_base64(img_dir + "\\" + img_name)
#         converted_html = re.sub(r'src\s*=\s*"' + img_name + '"', 'src="data:image/png;base64, ' + img_base64 + '"',
#                                 converted_html)
#     return converted_html


def replace_img_src_ext(converted_html):
    img_match = re.findall(r'<img[^>]*src\s*=\s*"(https:[^"]*)"', converted_html, re.DOTALL)
    for img_url in img_match:
        print(img_url)
        # Retrieve the image from the URL
        contents = urllib.request.urlopen(img_url).read()
        # Convert to line base64
        img_base64 = encode_base64(contents)
        # Insert the image into the document
        converted_html = converted_html.replace(img_url, 'data:image/png;base64, ' + img_base64)
        # converted_html = re.sub('src\s*=\s*"' + img_url + '"', 'src="data:image/png;base64, ' + img_base64 + '"',
        #                          converted_html, re.DOTALL)
    return converted_html


def set_table_border(converted_html, border_width, cell_padding=0, cell_spacing=0):
    return re.sub('<table>',
                  '<table style="border-collapse:collapse"' +
                  ' border=' + str(border_width) +
                  ' cellpadding=' + str(cell_padding) +
                  ' cellspacing=' + str(cell_spacing) +
                  '>', converted_html)


def convert_file(file_name, target_dir):
    try:
        # Verify the file type
        file_dir_name = os.path.dirname(file_name)
        base_file_name = os.path.basename(file_name)
        split_file_name = os.path.splitext(base_file_name)
        if not split_file_name[1] == '.md':
            print('Error: file {} is not a markdown file (must end in .md))'.format(file_name))
            return

        print("Converting file: {}".format(base_file_name))

        # Convert the markdown to HTML using the API endpoint
        converted_html = pandoc_convert(file_name)
        converted_html = set_table_border(converted_html, 1, 10)
        # converted_html = replace_img_src(file_dir_name, converted_html)
        # converted_html = replace_a_href(file_dir_name, converted_html)
        # converted_html = converted_html = replace_img_src_ext(converted_html)

        # Save the results
        out_file_name = split_file_name[0] + '.html'
        out_file_path = target_dir + '/' + out_file_name
        write_file(out_file_path, converted_html)
        return out_file_name

    except Exception as err:
        print('Unable to convert {}: {}'.format(file_name, err))


def find_markdown_files():
    file_list = []
    for root, dirs, files in os.walk(ROOT_DIR):
        # Ignore if the directory contains an ignore string
        if any(map(lambda i: i in root, IGNORE_DIRS)): continue

        # Search the file list for markdown files
        filter_list = list(filter(lambda f: f.endswith('.md'), files))
        full_path_list = list(map(lambda f: root + '\\' + f, filter_list))

        filtered_full_path_list = list(filter(lambda f: f not in IGNORE_FILES, full_path_list))
        file_list.append(filtered_full_path_list)

    return sum(file_list, [])


converted_files = list(map(lambda f: convert_file(f, ROOT_DIR + '/' + TARGET_DIR), find_markdown_files()))
print("\nThe following files converted and saved in '{}':".format(TARGET_DIR))
print('\n'.join(converted_files))
