import pydicom

#reading files

ds1 = pydicom.dcmread("ttfm.dcm")
ds2 = pydicom.dcmread("bmode.dcm")

#getting all tag names

tag_names_1 = ds1.dir()
tag_names_2 = ds2.dir()

#writing all tags in the "output" file

with open('output', 'w') as f:

    for i in tag_names_1:
        a=ds1.data_element(i).tag
        f.write("%s\n" % a)	  	
    for i in tag_names_2:
        b=ds2.data_element(i).tag
        f.write("%s\n" % b)

