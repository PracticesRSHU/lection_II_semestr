import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
print(root.tag)

for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)

print(len(root)) # кількість розділів menu
print(len(root[0])) # кількість елементів hotel


"""
Для кожного елемента вкладених списків tag – це рядок тега, а attrib – це словник його атрибутів:

menu
tag: hotel attributes: {'roomnumber': '101-137'}
	tag: item attributes: {'price': '$42.60'}
	tag: item attributes: {'price': '$24.45'}
tag: campsite attributes: {'roomnumber': '201-265'}
	tag: item attributes: {'price': '$3.62'}
tag: hostel attributes: {'roomnumber': '301-312'}
	tag: item attributes: {'price': '$1.69'}
3
2

"""