## Github doesn't allow file commits over a certain limit
I believe the current file size limit is 500MB or 1GB. 
 

If you do accidentally commit this file, you won't be able to push it to github even if you
delete it (and commit the deletes) afterward! This is because the file history is committed
along with the file itself.

Answer from: https://stackoverflow.com/questions/19573031/cant-push-to-github-because-of-large-file-which-i-already-deleted
Locally delete large files.
Commit the local deletes.
Soft reset back X number of commits (for me it was 3): git reset
--soft HEAD~3.
Then recommit all the changes together (AKA squash) git commit -m
"New message for the combined commit"
Push squashed commit.

Special case (from user @lituo): If above doesn't work, then you may have this case. Commit 1 included the large file and Commit 1's push failed due to large file error. Commit 2 removed the large file by git rm --cached [file_name] but Commit 2's push still failed. You can follow the same steps above but instead of using HEAD~3, use HEAD~2.
