from os import system
def rm_no_used(): #deletes files when u press exit
    system("del info_to_diskpart.tmp")
    system("del info_from_diskpart.tmp")
    

def ro(): #Creates readonly file to set the disk to readonly
    system("echo attributes volume set readonly >> selection.tmp")
    system("echo assign >> selection.tmp")
    system("diskpart /s selection.tmp")

def rw(): #Clears read only most likely because it has been setted in mistake.
    system("echo ATTRIBUTES VOLUME CLEAR READONLY >> selection.tmp")
    system("echo assign >> selection.tmp")
    system("diskpart /s selection.tmp")


print("Easy_Disk_mounter V.1.0")
print("Hello there,  this software tries to detect every volume that windows can find to decide whatever you want to do.")
print("Do NOT USE this script with encrypted disks!!! ")
system("echo List volume > info_to_diskpart.tmp")
system("diskpart /s info_to_diskpart.tmp > info_from_diskpart.tmp")#Takes the info of what volumes we have on the system.

with open('info_from_diskpart.tmp') as f:
    lines = f.read()
    print(str(lines))#Prints the info

    volume = str(input("Pls select the volume number: \nWrite 'exit' to escape\nWhich one are you selecting: "))#ask for what we 
    if volume == '1' or volume == '2' or volume == '3':
        print("BE CAREFULL IT CAN BE A VOLUME FROM YOUR SYSTEM")#usually on windows, are from your system and not from a external disk.
    if volume == "exit":
        rm_no_used()
    elif "Volume "+ volume or "volume"+ volume in lines:#For spanish and english systems
        system("echo select volume "+ volume +" > selection.tmp")
        rwhat = str(input("Also i need to know if you want in 'ro' read-only or 'rw' with read-write permissions\nJust 'ro' or 'rw': "))
        if rwhat == "ro":
            ro()
        elif rwhat == "rw": 
            rw()
        else:
            print("You only had to write ro or rw /_\\")
            rm_no_used()
    
    else:
        print("That volume doesn't exist <(_ _)>)")
        input()
system("del info_to_diskpart.tmp")
system("del selection.tmp")
system("del info_from_diskpart.tmp")

   
