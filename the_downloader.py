import pytube 
design = "########################"
print(f"{design * 2}\n\n")
print(("Download Your Youtube Videos And Playlist\n\n"))
print(f"{design * 2}\n\n")
qual = ""

def menu():
    while True:
        try:
            option = int(input("""
Download:
    1.Video
    2.Playlist
    3.Exit
    Input 1, 2 or 3: """))
        except:
            print("Wrong input, try again.")
            continue
        else:
            if option == 1 :
                video_downloader()
                print("Taking you back to the menu...")
            elif option == 2:
                playlist_downloader()
                print("Taking you back to the menu...")
            elif option == 3:  
                print("Bye!")
                break
            else:
                print("Input 1 ,2 or 3, please: ")
                continue
def quality():
    try: 
        user_quality = input("Input quality (720p, 480p, 360p, 240p, 144p) or press exit to Exit: ")
    except:
        print("Wrong input, try again.")
        quality()
    else:
        if user_quality == "720p" or user_quality == "720":
            qual = "720p"
        elif user_quality == "480p" or user_quality == "480":
            qual = "480p"
        elif user_quality == "360p" or user_quality == "360":
            qual = "360p"
        elif user_quality == "240p" or user_quality == "240":
            qual = "240p"
        elif user_quality == "144p" or user_quality == "144":
            qual = "144p"
        elif user_quality == "exit":
            print("Bye!")
            exit()
        else:
            qual = ""
            print("Wrong input, try again.")
            quality()
    return qual

def video_downloader():
    try:
        link = input("Input youtube video url: ")
        yt = pytube.YouTube(link)
        print(f"\nTitle: {yt.title}\n")
    except:
        print("\nInvalid url or bad network, please try again.\n")
        video_downloader()
    else:
        quality()
        print(f"Downloading {yt.title}...")
        yt.streams.get_by_resolution(qual).download()
        print(f"Downloaded {yt.title} successfully.")

def playlist_downloader():
    try:
        link = input("Input youtube playlist url: ")
        playlist = pytube.Playlist(link)
        print(f"\nTitle: {playlist.title}\n")
    except:
        print("\nInvalid url or bad network, please try again.\n")
        playlist_downloader()
    else:
        quality()
        print(f"Downloading {playlist.title}...")
        for video in playlist.videos:
            video.streams.get_by_resolution(qual).download()
        print(f"Downloaded {playlist.title} successfully.")

menu()