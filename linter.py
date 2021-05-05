import json
import logging
import requests
from SublimeLinter.lint import LintMatch, PythonLinter

logger = logging.getLogger('SublimeLinter.plugin.csl')

class SublimeLinterContribCsl (PythonLinter):
    cmd = None
    regex = r'^M="(?P<message>.+)" L=(?P<line>\d+) C=(?P<col>\d+)$'
    defaults = {
        'selector': 'source.csl, text.xml'
    }

    def run(self, cmd, code):
        url = "https://validator.w3.org/nu/"
        files = { 'file': ('style.csl', code) }
        data = {
            'schema': 'https://raw.githubusercontent.com/citation-style-language/schema/v1.0.1/csl.rnc https://raw.githubusercontent.com/citation-style-language/schema/602ad40976b7b455a3ce0b79f5534e8e75f088e9/csl.sch',
            'parser': 'xml',
            'laxtype': 'yes',
            'level': 'error',
            'out': 'json',
            'showsource': 'no'
        }
        try:
            response = requests.post(url, data=data, files=files, timeout=(10, 60))
        except requests.Timeout:
            logger.error("Timeout performing request to w3 nu validator.")
            self.notify_failure()
            return
        except requests.ConnectionError:
            logger.info(
                "Connection error performing request to w3 nu validator."
            )
            self.notify_failure()
            return
        return(response.text)

    def find_errors(self, output):
        try:
            content = json.loads(output)
        except ValueError:
            logger.error(
                "JSON Decode error: We expected JSON from CSL, "
                "but instead got this:\n{}\n\n"
                .format(output)
            )
            self.notify_failure()
            return

        for error in content['messages']:
            yield LintMatch(
                match=error,
                line=error['firstLine'] - self.line_col_base[0] if 'firstLine' in error else error['lastLine'] - self.line_col_base[0],
                col=error['firstColumn'] - self.line_col_base[1] if 'firstColumn' in error else 0,
                message=error['message'],
                error_type='error',
                code='',
            )

