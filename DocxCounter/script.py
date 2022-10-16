from fileinput import filename
from xmlrpc.client import boolean
from docx import Document
import os, datetime, sys, shutil, pypandoc

# define global variables from arguments
def defineGlobals(args):
    global REPO_PATH
    global FILE_NAME
    global FILE_PATH
    global UPDATE_README

    REPO_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\'

    try:
        FILE_PATH = args[1]
        if args[2] == "true":
            UPDATE_README = True
        else:
            UPDATE_README = False
        FILE_NAME = FILE_PATH.split("\\")[-1]
        return True
    except IndexError:
        print("Filename argument not given!")
        return False

# copy docx to repo directory
def copyFile():
    try:
        print("Copying "+FILE_NAME+" to repo...")
        dst = REPO_PATH+FILE_NAME
        shutil.copy2(FILE_PATH, dst)
        return True
    except FileNotFoundError:
        print("File does not exist")
        return False

# make md copy, update logs, update readme (optional)
def updateFile():
    try:
        logsFile = 'LOGS_'+FILE_NAME[:-4].upper() + 'md'
        mdFile = FILE_PATH[:-4] + 'md'

        # read docx
        document = Document(FILE_PATH)
        docText = '\n\n'.join(
            paragraph.text for paragraph in document.paragraphs
        )

        # make md copy
        print("Making md copy...")
        pypandoc.convert_file(REPO_PATH+FILE_NAME, 'md', outputfile=REPO_PATH+mdFile)

        # update logs
        print("Updating logs...")
        characters = len(docText)-docText.count('\n')
        words = len(docText.replace('–','').split())

        lines = dict()
        lines[0] = 'Update: '+str(datetime.date.today())+'  \n'
        lines[1] = 'Number of words: '+str(words)+'  \n'
        lines[2] = 'Number of characters: '+str(characters)+'  \n'

        with open(REPO_PATH+logsFile,'a') as readme:
            readme.write('\n')
            readme.write(lines[0])
            readme.write(lines[1])
            readme.write(lines[2])

        # update readme
        if (UPDATE_README):
            print("Updating readme...")
            with open(REPO_PATH+'README.md','r') as readme:
                readmeLines = readme.readlines()

            readmeLines[-3] = 'Update: '+str(datetime.date.today())+'  \n'
            readmeLines[-2] = 'Number of words: '+str(words)+'  \n'
            readmeLines[-1] = 'Number of characters: '+str(characters)+'  \n'

            with open(REPO_PATH+'README.md','w') as readme:
                readme.writelines(readmeLines)

        print("Done!\n")
    except Exception as e:
        print("Somethng went wrong. "+str(e))
            
def main():
    if defineGlobals(sys.argv):
        if copyFile():
            updateFile()
        
if __name__ == "__main__":
    main()