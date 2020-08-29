def get_windows_disks():
        """ Return disks available on Windows machine
        
        :return: list of characters representing available disks
        """
        import string, os
        import ctypes
        disks = list()
        kernel32 = ctypes.WinDLL('kernel32')
        SEM_FAILCRITICALERRORS = 1
        SEM_NOOPENFILEERRORBOX = 0x8000
        SEM_FAIL = SEM_NOOPENFILEERRORBOX | SEM_FAILCRITICALERRORS
        oldmode = ctypes.c_uint()
        kernel32.SetThreadErrorMode(SEM_FAIL, ctypes.byref(oldmode))
        WINDOWS_DISK_SUFFIX = ":\\"
        for s in string.ascii_uppercase:
            n = s + WINDOWS_DISK_SUFFIX
            if os.path.exists(n):
                disks.append(n)

        kernel32.SetThreadErrorMode(oldmode, ctypes.byref(oldmode))
        
        return disks

print (get_windows_disks())
