from docx import Document
import os, datetime

repoPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

document = Document('ExampleDocx/test.docx')
docText = '\n\n'.join(
    paragraph.text for paragraph in document.paragraphs
)

characters = len(docText)-docText.count('\n')
words = len(docText.replace('–','').split())

with open(repoPath+'/README.md','r') as readme:
    lines = readme.readlines()

lines[-3] = 'Update: '+str(datetime.date.today())+'  \n'
lines[-2] = 'Number of words: '+str(words)+'  \n'
lines[-1] = 'Number of characters: '+str(characters)+'  \n'

with open(repoPath+'/README.md','w') as readme:
    readme.writelines(lines)

with open(repoPath+'/LOGS.md','a') as readme:
    readme.write('\n')
    readme.write(lines[-3])
    readme.write(lines[-2])
    readme.write(lines[-1])