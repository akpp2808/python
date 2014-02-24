"""Lossy conversion from Unicode to ASCII"""
'''
    © 2012 spirit <hiddenspirit@gmail.com>
    https://bitbucket.org/spirit/translit/

    Unidecode Python package:
    Copyright 2011, Tomaž Šolc <tomaz.solc@tablix.org>
    http://pypi.python.org/pypi/Unidecode

    Text::Unidecode Perl module:
    Copyright 2001, Sean M. Burke <sburke@cpan.org>, all rights reserved.
    http://search.cpan.org/~sburke/Text-Unidecode/

    Markus Kuhn’s transtab:
    http://www.cl.cam.ac.uk/~mgk25/download/transtab.tar.gz

    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published
    by the Free Software Foundation, either version 3 of the License,
    or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty
    of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

try:
    from ._unidecode import unidecode, SOURCE_CODE_LANGUAGE
except ImportError:
    from .unidecode import unidecode, SOURCE_CODE_LANGUAGE
