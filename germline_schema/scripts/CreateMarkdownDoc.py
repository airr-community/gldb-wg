# Copyright (c) 2018 William Lees

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Create an Excel-based Submission Sheet from the yaml schema

import yaml
from jinja2 import Environment, FileSystemLoader, Template
import yamlordereddictloader
import argparse
import sys

import textwrap


def main(argv):
    parser = argparse.ArgumentParser(description='Create a Markdown document from a yaml schema, preserving declaration order in the yaml dictionaries.')
    parser.add_argument('schemafile', help='Schema file (.yaml)')
    parser.add_argument('outfile', help='Output file (.xlsx)')
    parser.add_argument('templatedir', help='Template directory (.xlsx)')
    parser.add_argument('template', help='Template file (.xlsx)')
    args = parser.parse_args()


    simple =  yaml.load(open(args.schemafile, 'r'), Loader=yamlordereddictloader.Loader)
    ENV = Environment(loader=FileSystemLoader(args.templatedir))
    template = ENV.get_template(args.template)

    with open(args.outfile, 'w') as fo:
        fo.write(template.render(simple))



if __name__=="__main__":
    main(sys.argv)
