#!/usr/bin/env python3
import os
import sys
import re
# Author: Ashkan Kiani
# Version: 0.1
# Description: Automatically generates the descriptions in this README.md by parsing scripts for "Description: *" line
def formatDescription(name, description):
  return "- `{}`: {}".format(name, description.strip())

# TODO: Support version replacement?
# lineRegex = re.compile('- `([^`]+)`-([0-9.]+)?:(.*)')
lineRegex = re.compile('- `([^`]+)`:(.*)')
def parseLine(line):
  """
  >>> parseLine('- `pbdo`:')
  ('pbdo', '')
  >>> parseLine('- `puppet`: A glorious plugin')
  ('puppet', ' A glorious plugin')
  """
  try:
    return lineRegex.findall(line)[0]
  except IndexError:
    print(line, file=sys.stderr)
    return ('', '')


def UpdateDescriptions(d):
  lines = []
  with open('./README.md') as file:
    lines = [line.rstrip() for line in file.readlines()]
  idx = 0
  for line in lines:
    if 'Descriptions' in line:
      break
    idx += 1
  header = lines[:idx+1]
  descriptions = lines[idx+1:]
  descDict = {}
  for description in descriptions:
    if description.strip() == '':
      continue
    info = parseLine(description)
    descDict[info[0]] = info[1]
  descDict.update(d)
  descriptions = [formatDescription(name, description) for name, description in descDict.items()]
  print("Descriptions:", file=sys.stderr)
  for name, desc in descDict.items():
    print("{}: {}".format(name, desc), file=sys.stderr)
  print("", file=sys.stderr)
  with open('./README.md', 'w') as file:
    file.writelines(line + "\n" for line in header + descriptions)

descriptionRegex = re.compile('Description:(.*)')
def FindDescriptions(files):
  result = {}
  for filename in files:
    with open(filename) as file:
      lines = file.readlines()
      description = None
      for line in lines:
        match = descriptionRegex.findall(line)
        if len(match) > 0:
          description = match[0]
          break
      if description is None:
        continue
      result[filename] = description.rstrip()
  return result

# TODO: Auto parse scripts for Description
def main():
  blacklist = ('^\.', 'personal', 'README.md', '\.swp$', '__pycache__')
  blacklist = [re.compile(x) for x in blacklist]
  blacklisted = lambda x: any(b.search(x) for b in blacklist)
  files = os.listdir()
  files = [file for file in files if not blacklisted(file)]
  descDict = FindDescriptions(files)
  UpdateDescriptions(descDict)

if __name__ == '__main__':
  main()
