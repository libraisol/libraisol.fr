#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'libraisol'
SITENAME = 'LIBRAISOL'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'public'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('April', 'https://www.april.org/'),
         ('Framasoft', 'https://www.april.org/'),
         ('ATTAC Bassin de Vichy', 'https://local.attac.org/vichy/'),)

# Social widget
"""
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
"""

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# personnalisation
THEME = 'themes/html5-dopetrope'

DEFAULT_DATE_FORMAT = ('%d %B %Y')

LIBRE = 'Permettre à qui le souhaite, d\'explorer et d\'utiliser des systèmes d’exploitation informatiques non-propriétaires pour s’équiper en systèmes GNU, Linux, et en logiciels dits "libres".'
SOLIDAIRE = 'Former et équiper des populations en difficulté ou défavorisées pour permettre l\'accès à l\'informatique et à Internet à tous.'
ASSOCIATION = 'Pour bénéficier d\'un service, il est nécessaire d\'être membre de l\'association'
ABOUT_TEXT = 'LIBRAISOL (Libre Association Informatique Solidaire Linux) est une association régie par la loi du 1er juillet 1901 et le décret du 16 août 1901.'
LIBRE_LINK = 'pages/logiciel-libre.html'
LIBRE_LAB = 'Découvrir le logiciel libre'
SOLIDAIRE_LINK = 'pages/solidaire.html'
SOLIDAIRE_LAB = 'Comment bénéficier d\'un ordinateur'
ABOUT_LINK = 'pages/qui-sommes-nous.html'
PERMANENCE = 'Les jeudi de 14H à 18H, dans la salle informatique de l’étincelle'
ADDRESS = 'Atrium<br/>37 avenue de Gramont<br/>03200 Vichy'
MAIL = 'libraisol@zaclys.com'
COPYRIGHT = 'Libraisol. Tous droits réservés'
PARTNERS = (('Vichy Communauté', 'https://www.vichy-communaute.fr/'),
            ('La recyclerie', 'https://recycleriesiel.com/'),
            ('L\'Étincelle', 'https://etincelle.io/'),)
STATIC_PATHS = ( "doc/", )
