from pytube import YouTube


def download_video(link):
    yt = YouTube(link)

    print("Title :", yt.title)
    print("Views :", yt.views)
    print("Duration :", yt.length)
    print("Description :", yt.description)
    print("Ratings :", yt.rating)


    stream = yt.streams.get_highest_resolution()
    stream.download()
    print("Download completed")
