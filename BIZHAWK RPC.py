# HELP THIS IS THE MOST HACKY AND TERRIBLE PYTHON CODE EVER I DONT EVEN KNOW WHAT HALF OF IT DOES, ITS SO SCUFFED
#neo geo pocket/color games are known to fuck up
import DiscordRPC
import ctypes

# skidded code to list all processes running and put them in a list, but i turned it into a function
EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

titles = []

def foreach_window(hwnd, lParam):
    if IsWindowVisible(hwnd):
        length = GetWindowTextLength(hwnd)
        buff = ctypes.create_unicode_buffer(length + 1)
        GetWindowText(hwnd, buff, length + 1)
        titles.append(buff.value)
    return True
EnumWindows(EnumWindowsProc(foreach_window), 0)
# end of skidded code

print(titles)
print("\n")

#bad code im not even gonna bother explaining what it does hhhhhhhh
if "BizHawk" in titles: #checks if bizhawk is in the list and gets its index number
    print("yeah biz is here")
    bizIndex = titles.index("BizHawk")
    print(bizIndex)
    print(titles[bizIndex])
    input("press enter when game open")
    # skidded code to list all processes running and put them in a list, but i turned it into a function
    EnumWindows = ctypes.windll.user32.EnumWindows
    EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    GetWindowText = ctypes.windll.user32.GetWindowTextW
    GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
    IsWindowVisible = ctypes.windll.user32.IsWindowVisible

    titles = []

    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            titles.append(buff.value)
        return True
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    # end of skidded code
    print(titles[bizIndex])
    theFuckingWindowTitle = titles[bizIndex]
#^this shit is literally a game of luck
print(theFuckingWindowTitle)

# makes it so everything that has a dash between them are different things in a list idk how to explain so just print("splitWinTit") to see. it also kinda fucks over games with -'es in their name but idk a better way to do it
splitWinTit = theFuckingWindowTitle.split("-")
print(splitWinTit)

shit = ("Playing on the " + splitWinTit[0]) # gets the console name and puts it into the variable shit
print(shit)

rpc = DiscordRPC.RPC.Set_ID(app_id=939292441285103678)

#sets up rpc
rpc.set_activity(state=splitWinTit[1],
    details=(shit),
    timestamp=rpc.timestamp(),
    large_image="biz", # Make sure you are using the same name that you used when uploading the image
    large_text="BizHawk",
    )
input() # so it doesnt close instantly after setting rpc