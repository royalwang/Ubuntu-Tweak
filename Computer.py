import pygtk
pygtk.require('2.0')
import gtk
import os
import gobject
import gettext

from aptsources import distro
from Widgets import GConfCheckButton, ItemBox, EntryBox

UBUNTU = distro.get_distro()
DISTRIB = UBUNTU.codename

class Computer(gtk.VBox):
	"""Some options about root user"""
	def __init__(self):
		gtk.VBox.__init__(self)

		cpu = open("/proc/cpuinfo")
		cpuinfo = cpu.readlines()
		for element in cpuinfo:
			if element.split(":")[0] == "model name\t":
				cpumodel = element.split(":")[1]
		cpu.close()

		ram = open("/proc/meminfo")
		ramlines = ram.readlines()
		for element in ramlines:
			if element.split(" ")[0] == "MemTotal:":
				raminfo = element.split(" ")[-2]
		ram.close()

		box = ItemBox(_("<b>System information</b>"),(
			EntryBox(_("Hostname"),os.uname()[1]),
			EntryBox(_("Distribution"), UBUNTU.description),
			EntryBox(_("Kernel"), os.uname()[0]+" "+os.uname()[2]),
			EntryBox(_("Platform"), os.uname()[-1]),
			EntryBox(_("CPU"), cpumodel[0:-1]),
			EntryBox(_("Memory"), str(int(raminfo)/1024)+" MB"),
				))
		self.pack_start(box, False, False, 0)

		box = ItemBox(_("<b>User information</b>"),(
			EntryBox(_("Current User"), os.getenv("USER")),
			EntryBox(_("Home Directory"), os.getenv("HOME")),
			EntryBox(_("Shell"), os.getenv("SHELL")),
			EntryBox(_("Language"), os.getenv("LANG")),
				))
			
		self.pack_start(box, False, False, 0)