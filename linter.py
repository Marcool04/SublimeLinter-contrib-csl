import os
from SublimeLinter.lint import Linter

class SublimeLinterCsl (Linter):
    linter_script = os.path.join(os.path.dirname(__file__), "csl-validator.sh")
    cmd = (linter_script,) # comma is needed so that quoting is applied
    regex = r'^M="(?P<message>.+)" L=(?P<line>\d+) C=(?P<col>\d+)$'
    defaults = {
      'selector': 'source.csl, text.xml'
    }
