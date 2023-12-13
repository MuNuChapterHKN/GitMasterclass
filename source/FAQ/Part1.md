# FAQ 001->020 - Git and Version Control Systems

### FAQ001
What is a repository in Git?

In Git, a repository (often abbreviated as "repo") is a data structure that stores metadata for a set of files and/or directories as well as a history of changes made to those files

### FAQ002
What Git command is used to clone an existing repository? clone

### FAQ003
What does the term "commit" mean in Git?
The term "commit" in Git means to capture a snapshot of the project's currently staged changes.

### FAQ004
What is the role of the "git push" command in Git?
to upload local repository content to a remote repository

### FAQ005
How do you create a new branch in Git?

### FAQ006
What does the "git pull" command do in Git?

### FAQ007
What does "version control" mean in the context of software development?

Version control, also known as source control, is the practice of tracking and managing changes to software code

### FAQ008
What type of VCS Git is?

### FAQ009
Explain the difference between a local and a remote repository.

### FAQ010
What is a branch in Git?

### FAQ011
How do you merge branches in Git?

### FAQ012
What is the difference between "fetch" and "pull" in Git?
In Git, "fetch" and "pull" are two related but distinct commands:

1. **Fetch:**
   - The `git fetch` command is used to retrieve changes from a remote repository without merging them into your local branches.
   - It downloads new branches and updates existing ones from the remote repository but does not automatically merge the changes into your working directory.
   - Fetching allows you to see what changes are available in the remote repository and decide when to integrate them into your local branches.

2. **Pull:**
   - The `git pull` command is a combination of `git fetch` and `git merge`. It fetches changes from the remote repository and automatically merges them into the current local branch.
   - Pull is a convenient way to update your local branch with the changes from the remote repository in a single command. However, it may automatically create a merge commit, which can affect the commit history.

In summary, while both "fetch" and "pull" involve retrieving changes from a remote repository, "fetch" is more explicit and allows you to inspect the changes before merging, whereas "pull" automatically merges the changes into your local branch.

Best regards,
ChatGPT

### FAQ013
How do you resolve a merge conflict in Git?

### FAQ014
Explain what "staged" commits mean in Git.

### FAQ015
How do you undo the last commit in Git?

### FAQ016
Name another VCS rather than Git.

### FAQ017
Is Git a delta-based VCS or stream-of-snapshots VCS?
Git is a stream-of-snapshots VCS.

### FAQ018
Which hashing algorithm is used to store objects in Git?
Git uses the SHA-1 hashing algorithm to store objects.

### FAQ019
What does the `.object` folder contains in Git?

### FAQ020
Who created Git?
