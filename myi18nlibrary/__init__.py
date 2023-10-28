import gettext
import os

def configure_i18n(domain, locale_dir):
    gettext.bindtextdomain(domain, locale_dir)
    gettext.textdomain(domain)
    return gettext.gettext