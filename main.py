#!/usr/bin/env python3
from git import Repo #was: *
import git
import os


def get_changeset(commit):
	# @PARAM commit the commit to check
	# @return the diff (not printed)

	if (not commit.parents):
		# @FIXME: this fails for the repos first commit since there is not parent
		# @TODO find out how to tackle this
		print("WARNING: could not get diff")
		return ""

	_git = git.Git('.')
	diff = _git.diff('%s..%s' % (commit.parents[0], commit))
	return diff


repo = Repo(os.path.abspath(".")) # repo object
# print(repo.head.commit) # HEAD

#print("HEAD: ", repo.head.commit)
#git = git.Git('.')


for commit in repo.iter_commits(repo.head.commit):
	# https://gitpython.readthedocs.io/en/0.3.4/tutorial.html#the-commit-object

	print("hex: ", commit.hexsha)
	# commit.hexsha
	# commit.parents
	# commit.tree
	print("autor: ", commit.author)
	# commit.author  <-
	# commit.authored_date <-
	# commit.committer <-
	# commit-message <-
	print("message: ", commit.message)
	#print(commit)

	print("changeset:")
	print(get_changeset(commit))


# commit = commit
#parent = commit.parents[0]
#print(parent)

#print(commit.diff(commit.parents[0]))

#print("\n\n")

#obj = Wrapper(diff)
#obj.foo()



#print(repo.head.commit.diff(repo.head.commit.diff(repo.head.commit.parents[0].parents[0])))

#print(repo.index.diff(commit.parents[0].parents[0], create_patch=True))

