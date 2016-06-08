# import sublime, sublime_plugin
# import re

# Can be run using `view.run_command('hello_world')`
class HelloWorldCommand(sublime_plugin.EventListener):
  def on_load(self, view):
    mark = view.find_all(r'\/\/\s?TODO( (.+)|)')
    view.add_regions("mark", mark, "mark", "dot",
            sublime.HIDDEN | sublime.PERSISTENT)
  def on_modified(self, view):
    mark = view.find_all(r'\/\/\s?TODO( (.+)|)')
    view.add_regions("mark", mark, "mark", "dot",
            sublime.HIDDEN | sublime.PERSISTENT)
