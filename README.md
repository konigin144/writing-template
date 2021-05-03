# writing-template                          
                      
## Source:
https://github.com/vigente/gerardus/wiki/Integrate-git-diffs-with-word-docx-files  


## How does it work?  
* Creates .md file for tracking changes in .docx  
* Appends current number of words and character to `logs.md`  
* Updates last lines of `readme.md` with current number of words and character  
                            
All above happens every time you run `git commit`.  

## Before you run:
* Paste your docx file to the repo directory  
* In `DocxCounter/counter.py` in line 6 insert docx filename  

## TODO  
- [ ] Handling more files  
- [ ] Handling files outside repo directory  
- [ ] Doing everything in one commit

~~~~
Update: 2021-05-04
Number of words: 110
Number of characters: 738
