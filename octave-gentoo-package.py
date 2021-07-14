import os
import sys
import re
import codecs
import jinja2
import urllib.request

assert sys.version_info >= (3, 9), "Python version must be at least 3.9.0"

contents = urllib.request.urlopen("http://octave.sourceforge.net/packages.php").read().decode('utf-8')

try:
    result = re.findall('<h3 class="package_name".+>(.+)</a></h3><p class="package_desc">(.+)</p><p class="deep_links.+package=(.+).tar.gz"', contents)
    print(result)
    os.makedirs('sci-mathematics', exist_ok=True)

    environment = jinja2.Environment(
        loader = jinja2.FileSystemLoader(searchpath = "./", encoding = 'utf-8', followlinks = True),
        trim_blocks = True,
        block_start_string = '<%',
        block_end_string = '%>',
        variable_start_string = '<{',
        variable_end_string = '}>',
        comment_start_string = '<#',
        comment_end_string = '#>'
    )

    for item in result:
        pn, description, p = item
        description = re.sub(' +', ' ', description.strip())
        print(pn, description, p)
        os.makedirs(os.path.join('sci-mathematics', 'octave-' + pn), exist_ok=True)

        in_file = 'metadata.xml'
        out_file = os.path.join('sci-mathematics', 'octave-' + pn, 'metadata.xml')
        print('Writting ' + out_file + ' ...')
        with codecs.open(out_file, 'w', encoding = 'utf-8') as text_file:
            text_file.write(
                environment.get_template(in_file).render({
                    'DESCRIPTION': description,
                    'PN': pn,
                    'P': p
                })
            )

        in_file = 'skel.ebuild'
        out_file = os.path.join('sci-mathematics', 'octave-' + pn, 'octave-' + p + '.ebuild')
        print('Writting ' + out_file + ' ...')
        with codecs.open(out_file, 'w', encoding = 'utf-8') as text_file:
            text_file.write(
                environment.get_template(in_file).render({
                    'DESCRIPTION': description,
                    'PN': pn,
                    'P': p
                })
            )
        
except AttributeError:
    pass
