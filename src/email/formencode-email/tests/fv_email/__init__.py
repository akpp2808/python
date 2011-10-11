import formencode
import formencode.validators
import socket
import re
from encodings import idna

_ = lambda s: s

try:
    import dns.resolver
    import dns.exception
    have_dns=True
except ImportError:
    have_dns=False

class Email(formencode.validators.Email):
    # Uses dnspython rather than pyDNS for domain resolution
    # Makes use of the patch at http://pythonpaste.org/archives/message/20081015.191555.f6252ba5.en.html
    # Also adds ",:;'"" to the illegal characters; see http://sourceforge.net/tracker/?func=detail&aid=2788489&group_id=91231&atid=596416
    usernameRE = re.compile(r"""^[^'";:,\t\n\r@<>()\[\]]+$""", re.I)
    predomainRE = re.compile(r"^\.|\.\.|\.$|\w{64,}", re.I)

    messages = {'multipleAt': _('The email address may not contain more than one @')}

    def __init__(self, *args, **kw):
        global have_dns
        formencode.FancyValidator.__init__(self, *args, **kw)
        if self.resolve_domain:
            if not have_dns:
                import warnings
                warnings.warn(
                    "dnspython <http://www.dnspython.org/> is not installed "
                    "on your system (or the dns.resolver package cannot be "
                    "found). I cannot resolve domain names in addresses.  The "
                    "resolve_domain setting has been set to False.")
                self.resolve_domain = False

    def validate_python(self, value, state):
        if not value:
            raise formencode.Invalid(
                self.message('empty', state),
                value, state)
        split = value.split('@')
        if len(split) > 2:
            raise formencode.Invalid(
                self.message('multipleAt', state), value, state)
        if len(split) < 2:
            raise formencode.Invalid(
                self.message('noAt', state),
                value, state)
        username, domain=split
        if not self.usernameRE.search(username):
            raise formencode.Invalid(
                self.message('badUsername', state,
                             username=username),
                value, state)
        if self.predomainRE.search(domain) or not domain.strip():
            raise formencode.Invalid(
                self.message('badDomain', state,
                             domain=domain),
                value, state)
        idna_domain = '.'.join([idna.ToASCII(l) for l in domain.split('.')])
        if not self.domainRE.search(idna_domain):
            raise formencode.Invalid(
                self.message('badDomain', state, domain=domain),
                value, state)
        if self.resolve_domain:
            assert have_dns, "dnspython should be available"
            try:
                try:
                    a = dns.resolver.query(domain, 'MX')
                except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer), e:
                    try:
                        a = dns.resolver.query(domain, 'A')
                    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer), e:
                        raise formencode.Invalid(
                            self.message('domainDoesNotExist', state,
                                domain=domain),
                            value, state)
            except (socket.error, dns.exception.DNSException), e:
                raise formencode.Invalid(
                    self.message('socketError', state, error=e),
                    value, state)

    def _to_python(self, value, state):
        return re.sub(re.compile(u'\s', re.UNICODE), u'', value)

