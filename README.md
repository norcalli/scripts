```
 _______  _______  ______    ___   _______  _______  _______
|       ||       ||    _ |  |   | |       ||       ||       |
|  _____||       ||   | ||  |   | |    _  ||_     _||  _____|
| |_____ |       ||   |_||_ |   | |   |_| |  |   |  | |_____
|_____  ||      _||    __  ||   | |    ___|  |   |  |_____  |
 _____| ||     |_ |   |  | ||   | |   |      |   |   _____| |
|_______||_______||___|  |_||___| |___|      |___|  |_______|
```
####Some scripts. That's it.

####Descriptions:
- `pbdo`: Runs actions based on your clipboard using pbpaste
- `pastie`: Posts a file to pastie from the command line.
- `auto_readme.py`: Automatically generates the descriptions in this README.md by parsing scripts for "Description: *" line
- `nvas`: Opens the filenames provided in the args inside of a **running** Neovim by detecting $NVIM_LISTENER_ADDR. This is useful for the new :terminal mode, so that you can open a file in the current neovim without leaving terminal mode. It also waits for the buffer to be closed/detached before exiting, which allows it to be used for commands which call to `$EDITOR` for input, such as `git commit -v`.
