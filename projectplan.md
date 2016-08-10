Project plan:

* Port the project to python, remove awk/sed/echo/cat dependencies
  * (which will hopefully improve performance a bit)
* Make sure we no longer write temporary files into /tmp (use lists or whatever instead)

New features:
* visualize/plot size growth between git objects (commits/tags/branches)
  * via matplotlib?
  * set plot resolution (one data point per: day/commit etc..) 
