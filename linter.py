from SublimeLinter.lint import Linter

class SublimeLinterCsl (Linter):
    cmd = 'csl-validator.sh'
    regex = r'^M="(?P<message>.+)" L=(?P<line>\d+) C=(?P<col>\d+)$'
    defaults = {
      'selector': 'source.csl, text.xml'
    }
