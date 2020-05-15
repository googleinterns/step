#! /usr/bin/env python3

import argparse
import os
import re
import subprocess
import urllib.error
import urllib.request


SUCCESS_STRING = "\u001b[32m✓\u001b[0m"
FAIL_STRING = "\u001b[31m✗\u001b[0m"


def MoveToRoot():
  while not os.path.exists('.git'):
    os.chdir(os.pardir)
  print("Found root at", os.getcwd())


def _VerifyHelper(f, verbose, prefix):
  if f.startswith(prefix):
    f = f[len(prefix):]
    if os.path.exists(f):
      if verbose:
        print(SUCCESS_STRING, f)
    else:
      print(FAIL_STRING, f)
      return 1
  else:
    print("Unexpected path:", f)
  return 0


def VerifyFilePathMatch(f, verbose):
  return _VerifyHelper(f, verbose, "step/")


def VerifyTeachMeMatch(f, verbose):
  return _VerifyHelper(f.rstrip('`'), verbose, "~/step/")


def VerifyLinkMatch(url, verbose):
  if not url.startswith("http"):
    print("Ignoring path:", url)
    return 0

  if url == "https://translate.google.com/":
    # Can't curl translate.google.com. Believe me, it's there.
    return 0

  url = url.replace("\\(", "(").replace("\\)", ")")

  process = subprocess.run('curl -I "' + url + '"', shell=True, check=True,
      stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
      universal_newlines=True)
  code = int(process.stdout.split()[1])

  #try:
  #  code = urllib.request.urlopen(url).getcode()
  #except urllib.error.HTTPError as exception:
  #  code = exception.getcode()

  if code in [200, 301, 302]:
    if verbose:
      print(SUCCESS_STRING, url)
  else:
    print(FAIL_STRING, code, url)
    return 1
  return 0


def ProcessMdFile(filepath, verbose):
  errors = 0
  print("Checking:", filepath)
  with open(filepath) as f:
    content = f.read()
    m = re.findall('filePath=\"([^\"]+)\"', content)
    for f in m:
      errors += VerifyFilePathMatch(f, verbose)
    m = re.findall('teachme\s+(.+)', content)
    for f in m:
      errors += VerifyTeachMeMatch(f, verbose)
    m = re.findall(r'\[.*\]\(((?:\\\)|[^\)\s])+)\)', content)
    for f in m:
      errors += VerifyLinkMatch(f, verbose)
  return errors



def ProcessAllMdFiles(verbose):
  errors = 0
  for (root,dirs,files) in os.walk('.', topdown=True):
    for f in files:
      if f.endswith(".md"):
        errors += ProcessMdFile(os.path.join(root, f), verbose)
  if errors:
    print("Found", errors, "problematic link(s).")


def VerifyAllPaths(args):
  MoveToRoot()
  ProcessAllMdFiles(args.v)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Check the paths in this repo.')
  parser.add_argument('-v', action='store_true',
      help='print successful matches')
  args = parser.parse_args()
  VerifyAllPaths(args)
