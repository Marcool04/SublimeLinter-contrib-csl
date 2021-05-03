SublimeLinter-csl
=================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-csl.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-csl)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to the [csl-validator.sh](https://github.com/citation-style-language/utilities) script. It will be used with files that have the Citation Style Language (CSL) syntax.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that the `csl-validator.sh` script from https://github.com/citation-style-language/utilities is available on your system. This further requires the `curl` and `jq` utilities.

In order for `csl-validator.sh` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

There are no specific settings for `csl-validator.sh` nor this plugin.
