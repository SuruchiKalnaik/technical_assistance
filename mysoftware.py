import os
print("Welcome to your personal technical assistance")
while True:
    print("What you would like to do: ", end="")
    p = input()
    if (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and (("chrome" in p) or ("browser" in p) or ("engine" in p)):
        print("Opening chrome")
        os.system("start chrome")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and (("notepad" in p) or ("editor" in p)):
        print("Opening notepad")
        os.system("start notepad")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and (("explorer" in p) or ("edge" in p)):
        print("Opening internet explorer")
        os.system("start iexplore")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and (("mozilla" in p) or ("firefox" in p)):
        print("Opening firefox")
        os.system("start firefox")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("create" in p)) and (("powerpoint" in p) or ("ppt" in p)):
        print("Opening powerpoint")
        os.system("start powerpnt")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("do" in p) or ("paint") in p) and (("paint" in p) or ("picture" in p) or ("drawing" in p) or ("painting" in p)):
        print("Opening paint")
        os.system("start mspaint")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("adjust" in p) or("set" in p)) and (("setting" in p) or ("environment" in p)):
        print("Opening setting")
        os.system("start ms-settings:")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and ("powershell" in p):
        prit("Opening powershell")
        os.system("start powershell")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and ("store" in p):
        print("Opening microsoft store")
        os.system("start ms-windows-store:")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("create" in p)) and (("word" in p) or ("document" in p)):
        print("Opening word")
        os.system("start winword")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("create" in p)) and ("excel" in p):
        print("Opening excel")
        os.system("start excel")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or("do" in p) or ("perform" in p)) and (("calculator" in p) or ("calculation" in p)):
        print("Opening calculator")
        os.system("start calc")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("click" in p)) and (("camera" in p) or ("photo" in p) or ("picture" in p)):
        print("Opening camera")
        os.system("start microsoft.windows.camera:")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p)) and (("control" in p) or ("pannel" in p)):
        print("Opening control pannel")
        os.system("start control")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("set" in p)) and (("alarm" in p) or ("clock" in p) or ("stopwatch" in p) or ("timer" in p)):
        print("Opening alarm and clock")
        os.system("start explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App")
    elif (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p) or ("start" in p) or ("play" in p)) and ("km" in p):
        print("Opening KMPlayer")
        os.system("start kmplayer")
    elif (("exit" in p) or ("quit" in p)):
        print("Goodbye! Have a nice day...")
        break
    else:
        print("Your system does not support this program.")
    print("*"*40)