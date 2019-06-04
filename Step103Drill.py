import sqlite3

# Drill parameters
# The following is the list provided to use for this drill:

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

#----------------------------------------------------------------

conn = sqlite3.connect('myDatabase.db')

print("Our 'fileList' tuple has:\n\n{}\n\n".format(fileList))

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_myTxtFiles(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_textFile TEXT\
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('myDatabase.db')

with conn:
    cur = conn.cursor()
    count = 0
    print("The qualifying text files from the 'fileList' tuple are:\n")
    for file in fileList:
        if file.endswith('.txt'):
            count += 1
            print("{}) {}".format(count,file))
            cur.execute("INSERT INTO tbl_myTxtFiles(col_textFile) VALUES (?)", (file,))
    conn.commit()
conn.close()
