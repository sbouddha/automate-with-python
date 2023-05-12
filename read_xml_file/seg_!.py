import xml.etree.ElementTree as ET

file = r"C:\Without_Sync\Py\automate-with-python\read_xml_file\xml_file.xml"
# Parse the XML file
tree = ET.parse(file)
root = tree.getroot()

# Set the XML namespace prefix
namespace = {'NS3': 'http://xmlns.xyz.com/integration/dopa/customer'}

# Find all "CustomerId" elements and extract their values
customer_ids = []
for customer_id_element in root.findall(".//NS3:CoverageId", namespace):
    customer_id = customer_id_element.text
    customer_ids.append(customer_id)

# Print the extracted "CustomerId" values
for customer_id in customer_ids:
    print(customer_id)
