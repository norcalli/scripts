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

These descriptions will be auto generated (when possible), and so are
always up to date.

#### Descriptions:
##### `newest-file`
Prints the newest file whose filename matches a regex at a path
```sh
Usage: ./newest-file <path-expression> [<N>] [<finder=auto>]

Print the newest file by modification time which matches the regex
<path-expression>. The regex only applies to the basename of the file. The
path is taken as-is.

Options:
	<path-expression> 	Regex xpression passed to finder
	[<N>] 			N >= 1. Nth newest file
	[<finder=fd>] 		Which finder to use.
				    Supported: auto, find, fd
Examples:
	./newest-file '/run/user/1000/sway-ipc.*.sock'

```

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

##### `oldest-file`
Prints the oldest file whose filename matches a regex at a path
```sh
Usage: ./oldest-file <path-expression> [<N>] [<finder=auto>]

Print the oldest file by modification time which matches the regex
<path-expression>. The regex only applies to the basename of the file. The
path is taken as-is.

Options:
	<path-expression> 	Regex xpression passed to finder
	[<N>] 			N >= 1. Nth oldest file
	[<finder=fd>] 		Which finder to use.
				    Supported: auto, find, fd
Examples:
	./oldest-file '/run/user/1000/sway-ipc.*.sock'

```

##### `auto_readme.py`
Automatically generates the descriptions in this README.md by parsing scripts for "Description: *" line

##### `lua-nvim`
Use nvim as if it was a luajit executable. REPL not supported currently
```sh
Usage: lua-nvim -e <CHUNK> [arg...]
       lua-nvim <FILENAME> [arg...]

The REPL is currently not supported.

OPTIONS:
	-e <CHUNK>	Execute CHUNK as a script
	<FILENAME>	Execute FILENAME
	[arg...]	Arguments to set on 'arg'

```

