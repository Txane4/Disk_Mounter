from os import system
def rm_no_used():
    system("del %temp%/info_to_diskpart.tmp")
    system("del %temp%/info_from_diskpart.tmp")

def ro():
    system("echo attributes volume set readonly >> %temp%/selection.tmp")
    system("echo assign >> %temp%/selection.tmp")
    system("diskpart /s %temp%/selection.tmp")

def rw():
    system("echo ATTRIBUTES VOLUME CLEAR READONLY >> %temp%/selection.tmp")
    system("echo assign >> %temp%/selection.tmp")
    system("diskpart /s %temp%/selection.tmp")

def main():
    print("Easy_Disk_mounter V.1.0")
    print("Hello there,  this software tries to detect every volume that windows can find to decide whatever you want to do.")
    system("echo List volume > %temp%/info_to_diskpart.tmp")
    system("diskpart /s %temp%/info_to_diskpart.tmp > %temp%/info_from_diskpart.tmp")

    with open('%temp%/info_from_diskpart.tmp') as f:
        lines = f.read()
        print(str(lines))

        volume = str(input("Pls select the volume number: \nWrite 'exit' to escape\nWhich one are you selecting: "))
        if volume == '1' or volume == '2' or volume == '3':
            print("BE CAREFULL IT CAN BE A VOLUME FROM YOUR SYSTEM")
        if "Volume "+ volume or "volume"+ volume in lines:
            system("echo select volume "+ volume +" > %temp%/selection.tmp")
            rwhat = str(input("Also i need to know if you want in 'ro' read-only or 'rw' with read-write permissions\nJust 'ro' or 'rw': "))
            if rwhat == "ro":
                ro()
            elif rwhat == "rw": 
                rw()
            else:
                print("You only had to write ro or rw /_ \\")
                rm_no_used()
        elif volume == "exit":
            rm_no_used()
        else:
            print("That volume doesn't exist <(_ _)>)")
            input()
    system("del %temp%/info_to_diskpart.tmp")
    system("del %temp%/selection.tmp")
    system("del %temp%/info_from_diskpart.tmp")

   
if __name__ == "__main__":
    main()