```
 _______  _______  ______    ___   _______  _______  _______
|       ||       ||    _ |  |   | |       ||       ||       |
|  _____||       ||   | ||  |   | |    _  ||_     _||  _____|
| |_____ |       ||   |_||_ |   | |   |_| |  |   |  | |_____
|_____  ||      _||    __  ||   | |    ___|  |   |  |_____  |
 _____| ||     |_ |   |  | ||   | |   |      |   |   _____| |
|_______||_______||___|  |_||___| |___|      |___|  |_______|
```
#### Some scripts. That's it.

#### Descriptions:
##### `pastie`
Posts a file to pastie from the command line.

##### `pbdo`
Runs actions based on your clipboard using pbpaste

##### `yay-update-ignore-errors`
Wrapper script around yay to try to ignore errors.
```sh
Usage: ./yay-update-ignore-errors <package-to-ignore...>

This script will run 'yay' and ignore any package that
fails by pattern matching against the errors.

Options:
<package-to-ignore...> 		list of comma separated lists (so you can do either)
--help 				Print this help message

Examples:
	# The following are equivalent
	./yay-update-ignore-errors qemu,bluez-utils linux linux-headers
	./yay-update-ignore-errors qemu,bluez-utils,linux,linux-headers

	# Auto upgrade
	yes '' | ./yay-update-ignore-errors
	# Auto upgrade everything except linux
	yes '' | ./yay-update-ignore-errors linux

```

##### `auto_readme.py`
Automatically generates the descriptions in this README.md by parsing scripts for "Description: *" line

