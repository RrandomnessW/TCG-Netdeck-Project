# Table from PDF to CSV
# Install tk, ghostscript, camelot-py[cv2], opencv-python
import camelot
tables = camelot.read_pdf('foo.pdf', pages='1')
print(tables[0])

# Export table to csv file. Export to file 'foo.csv', format='csv'
tables.export('foo.csv', f='csv', compress=False)

#Export the first (and only) table
tables[0].to_csv('foo.csv')

# online csv viewer: https://codebeautify.org/csv-viewer