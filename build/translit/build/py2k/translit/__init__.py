"""Transliterate between Unicode and smaller coded character sets"""

from __future__ import print_function

'''
    © 2012 spirit <hiddenspirit@gmail.com>
    https://bitbucket.org/spirit/translit/

    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU Lesser General Public License as published
    by the Free Software Foundation, either version 3 of the License,
    or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty
    of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

__all__ = ["downgrade", "upgrade", "print"]
DEFAULT_ENCODING = "latin-1"

from .downgrade import downgrade, encode, print, iconv, iconv_str
from .upgrade import upgrade, decode
from .unidecode import unidecode
from . import codec
