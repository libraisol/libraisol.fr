#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'libraisol'
SITENAME = 'LIBRaiSOL'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'public'

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%d %B %Y'
DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('April', 'https://www.april.org/'),
         ('Framasoft', 'https://framasoft.org/'),
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
STATIC_PATHS = ( "doc/", )

LIBRE = 'Permettre à qui le souhaite, d\'explorer et d\'utiliser des systèmes d’exploitation informatiques non-propriétaires pour s’équiper en systèmes GNU/Linux, et en logiciels dits "libres".'
SOLIDAIRE = 'Former et équiper des populations en difficulté ou défavorisées pour permettre l\'accès à l\'informatique et à Internet à tous.'
ASSOCIATION = 'Pour bénéficier d\'un service, il est nécessaire d\'être membre de l\'association'
ABOUT_TEXT = 'LIBRAISOL (Libre Association Informatique Solidaire Linux) est une association régie par la loi du 1er juillet 1901 et le décret du 16 août 1901.'
LIBRE_LINK = 'pages/logiciel-libre.html'
LIBRE_LAB = 'Découvrir le logiciel libre'
SOLIDAIRE_LINK = 'pages/solidaire.html'
SOLIDAIRE_LAB = 'Comment bénéficier d\'un ordinateur'
ABOUT_LINK = 'pages/qui-sommes-nous.html'
PERMANENCE = 'Tous les jeudis, de 15H à 16H (voir l\'adresse ci-dessous)'
ADDRESS = 'Atrium<br/>37 avenue de Gramont<br/>03200 Vichy'
MAIL = 'libraisol@zaclys.com'
COPYRIGHT = 'Libraisol. Sauf mention contraire, le contenu est disponible sous licence <a href="https://creativecommons.org/licenses/by-sa/3.0/fr/" target="_blank">CC-BY-SA version 3.0 ou ultérieure</a>'
CODE = '<i class="icon brands fa-gitlab" aria-hidden="true"></i> Hébergé sur <a href="https://framagit.org/libraisol/www.libraisol.fr" target="_blank">Framagit</a>'
PARTNERS = (('Vichy Communauté', 'https://www.vichy-communaute.fr/'),
            ('La recyclerie', 'https://recycleriesiel.com/'),
            ('L\'Étincelle', 'https://etincelle.io/'),
            ('Fondation Orange', 'https://www.fondationorange.com/'),)
LOCALE = ('fr_FR.utf8', )
MODAL_TEXT = """\
Nous organisons le 17/10 de 15 h à 17 h, à l’Atrium de Vichy,
un atelier d’installation du système libre GNU/Linux, afin de libérer vos
machines de l’emprise des multinationales américaines.
"""
MODAL_LINK = 'install-party-17.html'
MODAL_LAB = 'Inscription'
