# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

import logging

import click

__version__ = '1.0.0'

__notice__ = '''%(prog)s, version %(version)s

Acsone Odoo Development Tools.

Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).'''


@click.group()
@click.version_option(version=__version__, message=__notice__)
@click.option('-v', '--verbose', count=True)
def main(verbose):
    if verbose > 1:
        level = logging.DEBUG
    elif verbose > 0:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format='%(message)s', level=level)
