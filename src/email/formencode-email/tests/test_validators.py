import formencode as fe
import fv_email
from nose.tools import eq_
import dns.resolver
import socket

def assert_raises(exc, method, *arg, **kwarg):
    try:
        ret = method(*arg, **kwarg)
    except exc, e:
        return e
    else:
        assert False, 'No Exception Raised'

class TestResolvingNotSupported:
    def setup(self):
        self.orighave = fv_email.have_dns
        fv_email.have_dns = False
        try:
            self.v = fv_email.Email(resolve_domain=True)
        except:
            fv_email.have_dns = self.orighave
            raise

    def teardown(self):
        fv_email.have_dns = self.orighave

    def test_init(self):
        eq_(self.v.resolve_domain, False)

class TestNonResolving:
    def setup(self):
        self.v = fv_email.Email(resolve_domain=False, not_empty=True)

    def test_empty(self):
        msg = assert_raises(fe.Invalid, self.v.to_python, '')
        assert 'Please enter an email address' in str(msg)
        msg = assert_raises(fe.Invalid, self.v.to_python, ' ')
        assert 'Please enter an email address' in str(msg)

    def test_valid(self):
        self.v.to_python('foo@example.com')
        self.v.to_python('foo-bar@example.com')
        self.v.to_python('foo+bar@example.com')
        self.v.to_python('foo_bar@example.com')
        self.v.to_python('foo@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com')

    def test_strip_whitespace(self):
        eq_('foo@example.com', self.v.to_python('fo o@ex\tam\rp\nle .com'))
        eq_('foo@example.com', self.v.to_python(u'foo@example\u200b.com'))

    def test_invalid_username(self):
        def e_test(data):
            exc = assert_raises(fe.Invalid, self.v.to_python, data)
            assert 'username portion' in str(exc)
        e_test('foo,bar@example.com')
        e_test('mailto:foo@example.com')
        e_test('mailto;foo@example.com')
        e_test('Kimme and Scott <foo@example.com>')
        e_test('"foo@example.com')
        e_test('http://mrd.mail.yahoo.com/compose?To=foo@example.com')
        e_test('foo[foo@example.com')
        e_test('foo]foo@example.com')

    def test_invalid_format(self):
        msg = assert_raises(fe.Invalid, self.v.to_python, 'foo.example.com')
        assert 'An email address must contain a single @' in str(msg)

    def test_invalid0(self):
        '''
        Test for various ways we could get a UnicodeError from idna encoding

        UnicodeError: label empty or too long
        '''
        def e_test(data):
            exc = assert_raises(fe.Invalid, self.v.to_python, data)
            assert 'domain portion of the email address is invalid' in str(exc)
        e_test('foo@example..com')
        e_test('foo@example.com.')
        e_test('foo@')
        e_test('foo@')
        e_test('foo@.com')
        e_test('foo@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com')
        e_test('foo@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com>')

    def test_invalid1(self):
        '''Other Invalid domain tests'''
        def e_test(data):
            exc = assert_raises(fe.Invalid, self.v.to_python, data)
            assert 'domain portion of the email address is invalid' in str(exc)
        e_test('foo@example.com.c')

    def test_too_many_at(self):
        def e_test(data):
            exc = assert_raises(fe.Invalid, self.v.to_python, data)
            assert 'contain more than one @' in str(exc)
        e_test('foo@ex@mple.com')
        e_test('foo@example.com@example.com')
        e_test('foo@example.com@example.com')
        e_test('foo@example.combar@')
        e_test('foo@example.com bar@example.com')
        e_test('foo@example.com,bar@example.com')

    def test_valid_intl(self):
        self.v.to_python(u'foo@\xe9xample.com')

class TestResolving:
    def dne(self, data):
        exc = assert_raises(fe.Invalid, self.v.to_python, data)
        assert 'does not exist' in str(exc)

    def setup(self):
        self.v = fv_email.Email(resolve_domain=True)

    def test_init(self):
        eq_(self.v.resolve_domain, True)

    def test_legal(self):
        self.v.to_python('webmaster@google.com')

    def test_no_answer(self):
        self.dne('webastard@mashupartistfool.com')

    def test_bad_network(self):
        orig = dns.resolver.query
        def bogus_query(domain, cls):
            raise socket.error('Bogus Error')
        dns.resolver.query = bogus_query
        try:
            exc = assert_raises(fe.Invalid, self.v.to_python, 'foo@example.com')
            assert 'connect to the server' in str(exc)
        finally:
            dns.resolver.query = orig
t = TestNonResolving()

print t
