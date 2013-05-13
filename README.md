# Find Selected #

A plugin for Sublime Text 2 and 3 that adds an additional pair of methods for
quickly searching for text within a page.

## Details ##

Two additional search methods are available:

**find\_selected\_next** - If some text is selected then it is searched for and
the cursor highlights the next occurrence of the text. If no text is selected then
depending on the passed argument we either search for the last *Find* search term
("last_search") or the clipboard ("clipboard").

**find\_selected\_previous** - As above but we search backwards

This package doesn't really add much in the way of new functionality, it just makes
available existing functionality under one method or keypress. Previously to
search for the last search term you would call the "find\_next" method or to search
for selected text you would call the "find\_under" method. Now you can just call
the "find\_selected" method and depending on whether text is selected or not the
appropriate built-in method is called for you. It's a somewhat trivial change in
behaviour but one I found that I missed greatly when migrating from UltraEdit.
There is also the added ability to search for whatever is on the clipboard in one
keypress.

#### Important note about key bindings: ####
If you have SublimeCodeIntel installed it grabs CTRL+F3 by default. If you wish
to override this behaviour you will need to put Find Selected keys in your user
key bindings file. To do this open the default key bindings at `Preferences` ->
`Package settings` -> `Find Selected` -> `Key Bindings - Default`. Copy and paste
these into your user file at `Preferences` -> `Key Bindings - User` ensuring you
add the trailing comma as appropriate.

## Manual installation ##

At present the plugin is not in package control so you will need to install manually.

### Using GIT (recommended): ###
Go to the Packages directory (`Preferences` / `Browse Packages…`). Then clone this
repository:

    git clone git://github.com/CodeEffect/FindSelected

### Manually: ###
Downoad a zip of the project (click on the zip icon further up the page) and extract
it into your packages directory (`Preferences` / `Browse Packages…`).

## Default key bindings ##

`f3` - `find_selected_next` - If selected find next occurrence, if not then find
last search term.
`shift+f3` - `find_selected_previous` - If selected find prev occurence, if not
then find previous last search term.
`ctrl+f3` - `find_selected_next` - If selected find next occurrence, if not then
find clipboard.
`ctrl+shift+f3` - `find_selected_previous` - If selected find prev occurrence,
if not then find previous clipboard.

## License ##

Find selected is licensed under the MIT license.

  Copyright (c) 2013 Steven Perfect <steve@codeeffect.co.uk>

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
