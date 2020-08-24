import zipfile

my_zip = zipfile.ZipFile('files.zip', 'w')
my_zip.write('t1.txt')
my_zip.write('t2.txt')
my_zip.write('hummer.jpg')
my_zip.close()