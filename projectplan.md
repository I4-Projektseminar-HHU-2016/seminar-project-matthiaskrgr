gitdiffbinstat project plan

What is gitdiffbinstat?

Back in 2012/2014 when I wrote the script I was active in game development.
The game source repository was a git one, source code and game assets
(textures/graphics/sounds/music) were in the same repo.
I knew that "git diff --stat" would tell me how many lines were changed
in a file, and how much bigger or smaller binary files would have become.
"git diff --shortstat", did the same but summarized as a single line,
but only for text files.
However I wanted to have this summary available binary files as well.
I wanted to know how much bigger the files in a repo got,
between two commits, branche or tags.
I could use "du" but that would require to checkout the two git refs and
I'd have to exclude the .git directory.
After some research I came to the conclusion that such a tool did no exist yet
so I started writing it myself.

The current implementatiom is done in shellscript which means
it uses a bunch of small programms
(sed, awk, cat, cut, echo, wc, grep) and as soon as some of these programs
decides to change its output, the script might break.
Rewriting the script to python should resolve this issue (hoping the module
used do not change greatly).

How does the script work?
The script takes a commit/reference or a range of commits/references as input.
Something like c2ae976 ; HEAD ; db5e40b..e0f4ce9
somebranch, HEAD..somebranch, ...master, somebranch... etc.

We check if the current repository is a initialized as git repo and make sure
git can work with the parameters (make sure they refer to some point
in the history of the repository)
Symbolic references such as HEAD, HEAD~1 or tags and branches are translated
to the underlying commit hash.
Then we generate the logs/diffs, extract the information we need do
some calculations and print out the final numbers of how many files of
what kind (text/binary) were modified and how the size changed.

Plan:
The script will be rewritten in python using modules such as
	subprocess
	sys,
	argparse
	and probably others.
I will try to generate the logs in parallel
(the bash script does that too) for good performance.
The old script writes temporary files into /tmp
I'll make use of file objects or lists instead to avoid unneccessary disk IO.

New features: Visualize repository growth
Have a plot (by matplotlib?) show how the repository grew between two points in the history.
It will be possible to set the resolution to days/weeks/months or single commits (x axis, size will be y).
Hopefully it will be possible to annotate the x axis with git tags
that happen to be the processed range (printing showing every hash is probably not a good idea).

I'd like to have some functionality accessible as some kind of object or
library so that we can
import gitdiffbinstat
and call functions inside a git repository to get specific numbers that would otherwise
be put out by the program so that other people can make better use of it.

Problems I have encountered so far:
In the bash script I can easily check an exit status of a programm
if `program` ...
discard stdout or stderr
program >1 /dev/null
program >2 /dev/null
and pipe stdout from one program into the next
foo | bar.
In python I will need less programs to do that, however haveing made bad experiences
with gitpython module, I will use subprocess to call git commands.
There were difficulties with handling stdout stderr and exit status using
the subprocess module, but in the end I got it all working, the documentation
was not perfect though.



