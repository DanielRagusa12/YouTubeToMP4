
from pytube import YouTube
from sys import argv
import os





def get_vid(tube):

    print("Title: ",tube.title)
    video = tube.streams.get_highest_resolution()


    print("------------------OUTPUT-----------------")



    current_dir = os.getcwd()
    print("1: Download to Project Directory: "+current_dir)
    print("2: Custom Directory: ")

    option = str(input())
    dir = ''

    if(option == '2'):
        print("Enter Dir: ",end='')
        dir = str(input())

    else:
        dir = current_dir



    while os.path.exists(dir) == False:
        print("Directory Invalid. Please try again.")
        print("Enter Dir: ",end='')
        dir = str(input())

 
    video.download(str(dir), skip_existing = True)


    print("------------------SUCCESS-----------------")
    print("Downloaded to: "+dir)
        


print("-----------------YOUTUBE-----------------")
print("------------------VIDEO------------------")
print("----------------DOWNLOADER---------------")
print("-----------------------------------------")
print("WARNING: You will be promted to sign into your YouTube acccount on 1st launch using OAuth")




try:
    print("video URL: ",end = '')
    link = str(input())
    tube = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    tube.check_availability()

    
    
    get_vid(tube)



except:
    print("ERROR")
    print("APP CLOSING...")
    









    

        









