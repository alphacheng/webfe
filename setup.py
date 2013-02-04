# ======================================================#
# File automagically generated by GUI2Exe version 0.3
# Andrea Gavana, 01 April 2007
# ======================================================#

# Let's start with some default (for me) imports...

from distutils.core import setup
import py2exe
import glob
import os
import zlib
import shutil
import matplotlib
#import OpenGL
import threading
from ctypes import util
try:
    from OpenGL.platform import win32
except AttributeError:
    pass
        

# Remove the build folder
shutil.rmtree("build", ignore_errors=True)

# do the same for dist folder
shutil.rmtree("dist", ignore_errors=True)

MANIFEST_TEMPLATE = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="x86"
    name="%(prog)s"
    type="win32"
  />
  <description>%(prog)s</description>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel
            level="asInvoker"
            uiAccess="false">
        </requestedExecutionLevel>
      </requestedPrivileges>
    </security>
  </trustInfo>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity
            type="win32"
            name="Microsoft.VC90.CRT"
            version="9.0.21022.8"
            processorArchitecture="x86"
            publicKeyToken="1fc8b3b9a1e18e3b">
      </assemblyIdentity>
    </dependentAssembly>
  </dependency>
  <dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
  </dependency>
</assembly>
"""

class Target(object):
    """ A simple class that holds information on our executable file. """
    def __init__(self, **kw):
        """ Default class constructor. Update as you need. """
        self.__dict__.update(kw)


# Ok, let's explain why I am doing that.
# Often, data_files, excludes and dll_excludes (but also resources)
# can be very long list of things, and this will clutter too much
# the setup call at the end of this file. So, I put all the big lists
# here and I wrap them using the textwrap module.

data_files = []

includes = ["wx.lib.pubsub.*", "wx.lib.pubsub.core.*", "wx.lib.pubsub.pubsub1.*", "wx.lib.pubsub.pubsub2.*", "wx.lib.pubsub.utils.*" ,"ctypes", "logging","threading"]
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = ['matplotlib', 'pytz','wx.lib.pubsub','OpenGL']
dll_excludes = ['libgdk-win32-2.0-0.dll','libgdk_pixbuf-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll',
                'MSVCP90.dll', 'mswsock.dll', 'powrprof.dll']
icon_resources = []
bitmap_resources = []
other_resources = []
other_resources = [(24, 1, MANIFEST_TEMPLATE % dict(prog="MyAppName"))]


# This is a place where the user custom code may go. You can do almost
# whatever you want, even modify the data_files, includes and friends
# here as long as they have the same variable name that the setup call
# below is expecting.


#
# The following will copy the MSVC run time dll's
# (msvcm90.dll, msvcp90.dll and msvcr90.dll) and
# the Microsoft.VC90.CRT.manifest which I keep in the
# "Py26MSdlls" folder to the dist folder
#
# depending on wx widgets you use, you might need to add
# gdiplus.dll to the above collection



# I found on some systems one has to put them into sub-folders.
##data_files += [("Microsoft.VC90.CRT", py26MSdll),
##               ("lib\Microsoft.VC90.CRT", py26MSdll)]
import matplotlib
from distutils.filelist import findall

matplotlibdatadir = matplotlib.get_data_path()
matplotlibdata = findall(matplotlibdatadir)
matplotlibdata_files = []
for f in matplotlibdata:
    dirname = os.path.join('mpl-data', f[len(matplotlibdatadir)+1:])
    matplotlibdata_files.append((os.path.split(dirname)[0], [f]))

data_files.extend(matplotlibdata_files)


py26MSdll = glob.glob(r"c:\Dev\Py26MSdlls-9.0.21022.8\msvc\*.*")
# install the MSVC 9 runtime dll's into the application folder
data_files += [("", py26MSdll)]

# Ok, now we are going to build our target class.
# I chose this building strategy as it works perfectly for me :-D


GUI2Exe_Target_1 = Target(
    # what to build
    script = "main.py",
    icon_resources = icon_resources,
    bitmap_resources = bitmap_resources,
    other_resources = other_resources,
    dest_base = "webfe",
    version = "0.1",
    company_name = "No Company",
    copyright = "No Copyrights",
    name = "Py2Exe Sample File"
    )



# That's serious now: we have all (or almost all) the options py2exe
# supports. I put them all even if some of them are usually defaulted
# and not used. Some of them I didn't even know about.

setup(

    data_files = data_files,

    options = {"py2exe": {"compressed": 2,
                          "optimize": 2,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 2,
                          "dist_dir": "dist",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },

    zipfile = "lib\library.zip",
    console = [GUI2Exe_Target_1],
    windows = []#GUI2Exe_Target_1]
    )

# This is a place where any post-compile code may go.
# You can add as much code as you want, which can be used, for example,
# to clean up your folders or to do some particular post-compilation
# actions.

# And we are done. That's a setup script :-D

#========== additional cleanup =====================
