import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Python27\prank") #r stands for rawpath
    print file_list
    saved_path = os.getcwd() #tells python to use the current working directory
    print ("current working directory is" +saved_path)
    '''now we see that python is looking in the folder python27,
     instead of prank, so directory change is required'''
    os.chdir(r"C:\Python27\prank") #directory is changed
    
    #(2) for each file, rename filename
    for file_name in file_list:
        print("old name - "+file_name)
        print("new name - "+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
                  
rename_files()
