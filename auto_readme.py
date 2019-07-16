#!/usr/bin/env python3
# vim:ts=4 noet sw=4 cc=80
# Author: Ashkan Kiani
# Version: 0.1
# Description: Automatically generates the descriptions in this README.md by parsing scripts for "Description: *" line

import os
import sys
import re

TITLE_HEADER_LEVEL = "####"
SCRIPT_HEADER_LEVEL = TITLE_HEADER_LEVEL+"#"


def format_description(name, description, help_text):
		if help_text is not None:
				# return "- `{}`: {}\n	- ```\n{}\n```".format(name, description.strip(), help_text)
				return SCRIPT_HEADER_LEVEL+" `{}`\n{}\n```sh\n{}\n```\n".format(name, description.strip(), help_text)
		else:
				return SCRIPT_HEADER_LEVEL+" `{}`\n{}\n".format(name, description.strip())

# TODO: Support version replacement?

# Run the script to generate help text.
# However, if I didn't actually implement a --help flag case,
# then kill it just in case it starts to do things in as little
# time as possible. It turns out that takes about 0.005-0.01 seconds
# for a simple bash script.
def get_help_text(script_file_name):
		import subprocess
		result = subprocess.run(["timeout", "-sKILL", "0.01", script_file_name, "--help"], capture_output=True)
		help_text = result.stderr.decode("utf-8")
		if not help_text.lower().startswith("usage:"):
				print(script_file_name, "invalid help text, skipping.", help_text)
				return None
		return help_text

SCRIPT_NAME_REGEX = re.compile(SCRIPT_HEADER_LEVEL+' `([^`]+)`')

def parse_descriptions(lines):
	description_dictionary = {}
	while len(lines) > 0:
		line = lines.pop()
		if line.strip() == '':
			continue
		# Parse the lines of existing descriptions, which may include
		# manually added descriptions
		try:
			script_name = SCRIPT_NAME_REGEX.findall(line)[0]
			line = lines.pop()
			script_description = []
			while not line.startswith("```") and not line.startswith(SCRIPT_HEADER_LEVEL+" "):
				script_description.push(line)
				try:
					line = lines.pop()
				except IndexError:
					break
			description_dictionary[script_name] = script_description
		except IndexError:
			pass
		return description_dictionary


# Parse the existing README and find descriptions
# Update them with new descriptions from the passed in
# dictionary. Leave anything before the line "#### Descriptions"
def update_descriptions(new_descriptions):
	lines = []
	with open('./README.md') as file:
		lines = [line.rstrip() for line in file.readlines()]
	idx = 0
	for line in lines:
		if line.startswith(TITLE_HEADER_LEVEL+' Descriptions'):
			break
		idx += 1
	# Up to and including "#### Descriptions"
	header = lines[:idx+1]

	# Everything after.
	description_dictionary = parse_descriptions(lines[idx+1:])

	description_dictionary.update(new_descriptions)

	descriptions = [
		format_description(
			name,
			description,
			get_help_text("./" + name),
		)
		for name, description in description_dictionary.items()]

	sys.stderr.writelines(line + "\n" for line in header + descriptions)

	with open('./README.md', 'w') as file:
		file.writelines(line + "\n" for line in header + descriptions)


description_regex = re.compile('Description:(.*)')


def find_descriptions(files):
	result = {}
	for filename in files:
		with open(filename) as file:
			lines = file.readlines()
			description = None
			for line in lines:
				match = description_regex.findall(line)
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
	new_descriptions = find_descriptions(files)
	update_descriptions(new_descriptions)


if __name__ == '__main__':
	main()
