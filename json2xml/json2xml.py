# -*- coding: utf-8 -*-
from xml.dom.minidom import parseString
import dicttoxml


class Json2xml:
    def __init__(
        self,
        data: str,
        wrapper: str = "all",
        pretty: bool = True,
        attr_type: bool = True,
        item_name: str = "item",
    ):
        self.data = data
        self.pretty = pretty
        self.wrapper = wrapper
        self.attr_type = attr_type
        self.item_name_func = lambda _: item_name

    def to_xml(self):
        """
        Convert to xml using dicttoxml.dicttoxml and then pretty print it.
        """
        if self.data:
            xml_data = dicttoxml.dicttoxml(
                self.data,
                custom_root=self.wrapper,
                attr_type=self.attr_type,
                item_func=self.item_name_func,
            )
            if self.pretty:
                return parseString(xml_data).toprettyxml()
            return xml_data
        return None
