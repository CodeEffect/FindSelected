# coding=utf-8
import sublime
import sublime_plugin


def removeNewlinesAndCut(text, cutTo=100):
    if "\n" in text or "\r" in text:
        text = text.replace("\n", "/CR/").replace("\r", "")
    return text[0:cutTo - 1] + u"…" if len(text) > cutTo else text


class FindSelectedNextCommand(sublime_plugin.TextCommand):
    def run(self, edit, alt="last_search"):
        """Find next instance of selected text.

If selection empty then look for the last Find command search term or the clipboard depending on the passed argument.

"""
        view = self.view
        # Get the first highlighted string to search for
        selected = view.sel()[0]
        # Note if we're searching for the clipboard or a selection
        selection = True

        # If start and end cursor points are different then we have some text selected
        if selected.a != selected.b:
            # We don't call "find_under" here as it populates the find panel and
            # so we would lose its value in case we wanted to use it later
            # Get the text of the selection
            searchText = view.substr(sublime.Region(selected.a, selected.b))
            # If we've selected right to left then ensure that we use the higher
            # of the two for comparison
            if selected.a < selected.b:
                selectedPos = selected.b
            else:
                selectedPos = selected.a
        elif alt == "last_search":
            # Run the built in find_next command from the window context
            return view.window().run_command("find_next")
        elif alt == "clipboard":
            selection = False
            # Search for what's on the clipboard
            searchText = sublime.get_clipboard()
            selectedPos = selected.a

        # Find the next instance of our search string after the cursor position
        match = view.find(searchText, selectedPos, sublime.LITERAL | sublime.IGNORECASE)

        # If nothing found underneath our cursor position
        if not match:
            # Try from the top of the page
            match = view.find(searchText, 0, sublime.LITERAL | sublime.IGNORECASE)

        # If still nothing found
        if not match:
            return sublime.status_message('''Unable to find "%s"''' % removeNewlinesAndCut(searchText))

        # If we only find our current selection then message to say only 1 found
        if selection and match.b == selectedPos:
            return sublime.status_message('''Only 1 instance of "%s" found''' % removeNewlinesAndCut(searchText))

        # Highlight it
        view.sel().clear()
        view.sel().add(match)
        # Scroll to it
        view.show(match)
        # Zoidberg eyeball, iris out!
        return sublime.status_message('''Found "%s"''' % removeNewlinesAndCut(searchText))


class FindSelectedPreviousCommand(sublime_plugin.TextCommand):
    def run(self, edit, alt="last_search"):
        """Find previous instance of selected text.

If selection empty then look for the last Find command search term or the clipboard depending on the passed argument.

"""
        view = self.view
        # Get the first highlighted string to search for
        selected = view.sel()[0]
        # Note if we're searching for the clipboard or a selection
        selection = True

        # If start and end cursor points are different then we have some text selected
        if selected.a != selected.b:
            # We don't call "find_under_previous" here as it populates the find
            # panel and so we would lose its value in case we wanted to use it later
            # Get the text of the selection
            searchText = view.substr(sublime.Region(selected.a, selected.b))
            # If we've selected right to left then ensure that we use the higher
            # of the two for comparison
            if selected.a > selected.b:
                selectedPos = selected.a
            else:
                selectedPos = selected.b
        elif alt == "last_search":
            # Run the built in find_prev command from the window context
            return view.window().run_command("find_prev")
        elif alt == "clipboard":
            # Search for what's on the clipboard
            searchText = sublime.get_clipboard()
            selectedPos = selected.b
            selection = False

        # Find all instances of our search string in order
        matches = view.find_all(searchText, sublime.LITERAL | sublime.IGNORECASE)

        # If we're searching for selected text
        if selection:
            # If we only find one match
            if len(matches) == 1:
                return sublime.status_message('''Only 1 instance of "%s" found''' % removeNewlinesAndCut(searchText))

            # If our selected text is the first found then we need the last found
            if matches[0].b == selectedPos:
                match = matches[-1]
            else:
                # Otherwise loop them until we reach our selection
                for possibleMatch in matches:
                    # We want the one before
                    if possibleMatch.b == selectedPos:
                        break
                    match = possibleMatch

        # Else we're searching for a text string
        else:
            # If not found
            if not matches:
                return sublime.status_message('''Unable to find "%s"''' % removeNewlinesAndCut(searchText))
            # If only 1 found
            if len(matches) == 1:
                match = matches[0]
            # Else find the one closest above our cursor
            else:
                # Work out the position of our cursor for later comparison
                (row, col) = view.rowcol(selectedPos)
                cursorPostition = view.text_point(row, col)
                # Work out the position of the first match
                (row, col) = view.rowcol(matches[0].b)
                possibleCursorMatch = view.text_point(row, col)
                # If the first one is further down the page than our cursor
                if cursorPostition < possibleCursorMatch:
                    # Then go to the last one
                    match = matches[-1]
                else:
                    # Nothing left but to loop all matches and calculate their positions
                    for possibleMatch in matches:
                        (row, col) = view.rowcol(possibleMatch.a)
                        possibleCursorMatch = view.text_point(row, col)
                        # We want the one before our cursor
                        if possibleCursorMatch < cursorPostition:
                            match = possibleMatch
                        else:
                            # If we match below our cursor position then stop searching
                            break

        # Highlight it
        view.sel().clear()
        view.sel().add(match)
        # Scroll to it
        view.show(match)
        # Rubber baby buggy bumpers.
        return sublime.status_message('''Found "%s"''' % removeNewlinesAndCut(searchText))
