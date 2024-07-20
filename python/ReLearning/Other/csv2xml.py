"""This script is to create xmlfile.txt file from a given csv_to_xml_data.csv file"""
# row_list = []
# with open('csv_to_xml_data.csv', 'r') as csvfile:
#     row_list = csvfile.read().splitlines()


with open('csv_to_xml_data.csv') as f:
    lines = [line.rstrip() for line in f]
 
print(lines)


# with open('xmlfile.txt', 'w') as txtfile:
#     for row in row_list:
#         txtfile.write(f"""<Student>
#     <studentclass>8thstd</studentclass>
#     <studentsubject>math</<studentsubject>
#     <stuItem>{row}<stuItem>
#     <stuItemSting>I am {row} and I like to be {row} because I am {row}</stuItemSting>
# </Student>""")    
