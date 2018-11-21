"""
spaCy interface
"""

#-- Imports ---------------------------------------------------------------------
import spacy

from .parse  import parse
from .embed  import embed
from .select import select


#-- Definitions -----------------------------------------------------------------
activated  = spacy.prefer_gpu()
nlp = spacy.load('en_core_web_md')
