# writing-template                          

## How does it work?  
* Creates .md file for tracking changes in .docx  
* Appends current number of words and character to `logs.md`  
* Updates last lines of `readme.md` with current number of words and character  
                            
All above happens every time you run script `DocxCounter/script.py`.
Arguments:
* `file` [required] - full path to your docx file  
* `updateReadme` [optional] - append logs to README file, false by default

## TODO  
- [ ] better arguments passing
- [ ] help command
- [ ] (maybe) graphical interface

~~~~
Update: 2022-10-16  
Number of words: 113  
Number of characters: 750  
