#YouTube Downloader
#Date: 7-12-2022   ||   Day: Wednesday

#Import Library
from pytube import YouTube

#Decleration Function
def Download(link):
  youtubeObject = YouTube(link) #Declare Object youtubeObject
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  
  #Handling Errors
  try: 
    youtubeObject.download()
  except:
    print("There has been ERROR in downloading") #If the download failed display the message for User
  print("The download Completed!") #If the download succeeded display this message for User

#Input from the User (Prompt)
#This message displays for the user in terminal or the compiler output
link = input("Put the YouTube link here URL: ")
Download(link) #Calling Function
