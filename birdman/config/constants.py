from collections import namedtuple

t = namedtuple("USER_TYPES", ['PERSON', 'ORG'])
USER_TYPES = t(PERSON=0, ORG=1)
