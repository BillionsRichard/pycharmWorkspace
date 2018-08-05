#coding:utf-8
from pprint import pprint as pp
import xml.etree.ElementTree as ET

tree = ET.parse('productConfig.xml')

root = tree.getroot()

# print(root.tag)

support_info_dict = {}
# for product_child in root:
#     product_name = ''
#     for child in product_child:
#         if child.tag == 'productname':
#             product_name = child.text
#         if product_name and child.tag == 'supporttypes':
#             support_info_dict[product_name] = child.text

for node in root.iter('productname'):
    print(node.text)

pp(support_info_dict)