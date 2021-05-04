import json
import requests
import socket

from SublimeLinter.lint import LintMatch, PythonLinter

def offline(host="8.8.8.8", port=53, timeout=3):
    # Adapted from https://stackoverflow.com/a/33117579
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return False
    except socket.error as ex:
        return True

class SublimeLinterContribCsl (PythonLinter):
    cmd = None
    regex = r'^M="(?P<message>.+)" L=(?P<line>\d+) C=(?P<col>\d+)$'
    defaults = {
        'selector': 'source.csl, text.xml'
    }

    def run(self, cmd, code):
        if offline():
            print("No internet. Not linting CSL.")
            return
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
        response = requests.post(url, data=data, files=files)
        return(response.text)

    def find_errors(self, output):
        try:
            content = json.loads(output)
        except ValueError:
            logger.error(
                "JSON Decode error: We expected JSON from 'csl', "
                "but instead got this:\n{}\n\n"
                .format(output)
            )
            self.notify_failure()
            return

        for error in content['messages']:
            yield LintMatch(
                match=error,
                line=error['firstLine'] - 1 if 'firstLine' in error else error['lastLine'] - 1,
                col=error['firstColumn'] if 'firstColumn' in error else 0,
                message=error['message'],
                error_type='error',
                code='',
            )

