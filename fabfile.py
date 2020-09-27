from fabric.api import local, settings, abort
from fabric.contrib.console import confirm


def test():
  local("nosetests -v")

def commit():
  message = 'changes'
  local("git add . && git commit -am {}".format(message))

def push():
  local("git push origin master")

def prepare():
  test()
  commit()
  push()