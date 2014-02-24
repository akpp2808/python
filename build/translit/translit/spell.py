# Mostly for fixing typographic apostrophe issues with PyEnchant.
import re
from collections import defaultdict

from enchant import * #@UnusedWildImport
import translit


AUTOFIX_WHITELIST = defaultdict(set, {
    "fr": {"ça"},
})

AUTOFIX_WORD_RE = re.compile("[\w'’]+")


class Dict(Dict):
    def __init__(self, tag=None, broker=None):
        super().__init__(tag, broker)
        self.short_tag = self.tag.split("_")[0]
        self._autofix_whitelist = AUTOFIX_WHITELIST[self.short_tag]

    def check(self, word):
        return super().check(word.replace("’", "'"))

    def suggest(self, word):
        suggestions = super().suggest(word.replace("’", "'"))
        return [s.replace("'", "’") for s in suggestions]

    def autofix(self, text):
        """Fix unambiguous spelling errors.
        """
        def word_repl(match):
            def normalize(word):
                return translit.downgrade(word.lower(), "ascii")
            word = match.group(0)
            if len(word) > 1 and not self.check(word):
                normalized_word = normalize(word)
                found = None
                for suggestion in self.suggest(word):
                    if normalized_word == normalize(suggestion):
                        if suggestion.lower() in self._autofix_whitelist:
                            return suggestion
                        if found is not None:
                            break
                        found = suggestion
                else:
                    if found:
                        return found
            return word
        return AUTOFIX_WORD_RE.sub(word_repl, text)
