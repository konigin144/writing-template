# writing-template                          
                      
## Source:
https://github.com/vigente/gerardus/wiki/Integrate-git-diffs-with-word-docx-files  


## How does it work?  
* Creates .md file for tracking changes in .docx  
* Appends current number of words and character to `logs.md`  
* Updates last lines of `readme.md` with current number of words and character  
                            
All above happens every time you run `git commit`.  

## Before you run:
* Move `pre-commit` and `post-commit` files to `.git/hooks` directory  
* Paste your docx file to the repo directory  
    If you want to leave file in your directoryfollow this:  
    * In `pre-commit` file add `cp filepath .` after `cd` command in line 101.  
    * If you don't want to keep the file copy, also add `rm filename` in the end of `pre-commit` file.  
* In `DocxCounter/counter.py` in line 6 insert docx filename  

## TODO  
- [ ] Handling more files  
- [x] Handling files outside repo directory  
    - [ ] Try to handle it better  
- [ ] Doing everything in one commit  

~~~~
Update: 2021-05-04  
Number of words: 113  
Number of characters: 750  
