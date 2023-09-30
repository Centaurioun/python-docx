"""Objects shared by modules in the docx.oxml subpackage."""

from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.oxml.simpletypes import ST_DecimalNumber, ST_OnOff, ST_String
from docx.oxml.xmlchemy import BaseOxmlElement, OptionalAttribute, RequiredAttribute


class CT_DecimalNumber(BaseOxmlElement):
    """Used for ``<w:numId>``, ``<w:ilvl>``, ``<w:abstractNumId>`` and several others,
    containing a text representation of a decimal number (e.g. 42) in its ``val``
    attribute."""

    val = RequiredAttribute("w:val", ST_DecimalNumber)

    @classmethod
    def new(cls, nsptagname, val):
        """Return a new ``CT_DecimalNumber`` element having tagname `nsptagname` and
        ``val`` attribute set to `val`."""
        return OxmlElement(nsptagname, attrs={qn("w:val"): str(val)})


class CT_OnOff(BaseOxmlElement):
    """Used for ``<w:b>``, ``<w:i>`` elements and others, containing a bool-ish string
    in its ``val`` attribute, xsd:boolean plus 'on' and 'off'."""

    val = OptionalAttribute("w:val", ST_OnOff, default=True)


class CT_String(BaseOxmlElement):
    """Used for ``<w:pStyle>`` and ``<w:tblStyle>`` elements and others, containing a
    style name in its ``val`` attribute."""

    val = RequiredAttribute("w:val", ST_String)

    @classmethod
    def new(cls, nsptagname, val):
        """Return a new ``CT_String`` element with tagname `nsptagname` and ``val``
        attribute set to `val`."""
        elm = OxmlElement(nsptagname)
        elm.val = val
        return elm