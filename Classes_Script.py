""" 
Author: Rosman R. Carino
Date: 04/02/2022
Version 1.0
Description: Class Folder where this Folder contains the following sub-folders:
    Exams:
    Assignments/Homework -> Each Assignment/Homework Folder will contain 
                additional subfolders named Starter Code & Submission
    Lecture Videos: Reserved Canvas Recordings of Lecture
    Lectures: There is an Option to create subfolders for each Lecture in the 
                case there are multiple files for Lectures. Otherwise, this
                folder will just contain slides, etc.
    Section: Reserved For Section Handouts and Solutions
"""

import os

def user_input_path():
    """ 
    user_input_path: This function asks the User to enter the Directory
    Path of where to create the folder for this Class
    @return: Return Directory Path
    """
    dir_path = input("Please enter the Path to create folders: ")
    dir_path = dir_path.strip('\"')
    return dir_path

def ask_main_folder_name():
    """ 
    ask_main_folder_name: This function asks the User to enter the name of
    Path of where to create the folder for this Class
    @return: Return Directory Path
    """
    main_folder_name = input("Please enter the Main Folder Title: ")
    main_folder_name = main_folder_name.strip('\"')
    return main_folder_name

def create_main_folder(user_input_path, main_folder_title):
    """ 
    create_main_folder: This function creates the main folder of the Class
    which will then contain all the subfolders (Exams, Assignments/Homework,
    Lecture Videos, Lectures, Section) 
    @param: user_input_path, main_folder_title
    @return: main_folder_path
    """
    main_folder_path = os.path.join(user_input_path, main_folder_title)
    os.mkdir(main_folder_path)
    return main_folder_path

def homework_or_assignments_folder():
    """ 
    homework_or_assignments_folder: This function asks the User to specify
    whether to create a an Assignment Directory or a Homework Directory
    @return: Assignments(str) or Homework(str)
    """
    print("Enter the Following Choices: ")
    print("1 - Assignments")
    print("2 - Homework")
    user_input = int(input("Please enter a Choice: "))
    if user_input == 1:
        print()
        return "Assignments"
    else:
        print()
        return "Homework"
    
def create_starter_code_and_submission_folders(assign_or_hwk_path):
    """ 
    create_starter_code_and_submission_folders: This function creates
    a Starter Code and Submission Folder for each Assignment Directory in the 
    Assignment Root Directory.
    """
    #Create Starter Code and Submission Folders for Each Assignment/Homework Folder
    list_of_assign_or_hwk_folders = os.listdir(list_of_default_folder_paths[-1])
    for current_folder in list_of_assign_or_hwk_folders:
        current_folder_path = os.path.join(list_of_default_folder_paths[-1], current_folder)
        current_starter_code_path = os.path.join(current_folder_path, "Starter Code")
        current_submission_path = os.path.join(current_folder_path, "Submission")
        os.mkdir(current_starter_code_path)
        os.mkdir(current_submission_path)
     
def create_default_folders(list_of_folder_names, user_input_dir_path):
    """ 
    create_default_folders: This function creates the following directories in
    the Main Folder Root Directory: Exams, Assignments/Homework,
    Lecture Videos, Lectures, Section. This function will also return a list,
    'list_of_folder_paths' that will contain the paths for each of these
    directories.
    @param: list_of_folder_names, user_input_dir_path
    @return list_of_folder_paths
    """
    list_of_folder_paths = []
    #for current_folder in list_of_default_folders:
    for current_folder in list_of_folder_names:
        current_folder_path = os.path.join(user_input_dir_path, current_folder)
        list_of_folder_paths.append(current_folder_path)
        os.mkdir(current_folder_path)
    return list_of_folder_paths
    
def ask_number_of_folders(folder_name):
    """ 
    create_default_folders: This function asks the User to enter the number
    of folders they want to create for a given directory.
    @param: folder_name
    @return number_of_folders
    """
    print(folder_name, "Folder Creation")
    number_of_folders = int(
        input("Please enter the number of folders you want to create: "))
    print()
    return number_of_folders

def create_folders(folder_title, number_of_folders, user_input_dir_path):
    """ 
    create_folders: This function creates a given amount of directories for
    a given directory path.
    @param: folder_title, number_of_folders, user_input_dir_path
    """
    for i in range(1, number_of_folders + 1):
        current_folder_name = folder_title + " " +  str(i)
        current_folder_path = os.path.join(user_input_dir_path, 
            current_folder_name)
        os.mkdir(current_folder_path)
    
def ask_folder_creation(folder_name):
    """ 
    create_folders: This function asks a User to create additional sub-directories
    for a given directory, namely in 'folder_name'
    @param: folder_name
    @return: 
            True: User desires additional sub-directories
            False: User does not want additional sub-directories.
    """
    print("For", folder_name)
    print("Enter 1: To Create Folders for this Directory")
    print("Enter 2: To NOT create Folders for this Directory")
    user_choice = int(input("Please enter your choice: "))
    print()
    if user_choice == 1:
        return True
    else:
        return False

if __name__ == "__main__":
        #Ask User For Name of Main Folder for this Class
        main_folder_name = ask_main_folder_name()
        #Ask User For Directory Path to Create Folders for this Class
        user_input_dir_path = user_input_path()
        #Create Main Folder Path
        main_folder_path = create_main_folder(user_input_dir_path, main_folder_name)
        #Default List of Folders for Classes
        list_of_default_folders = ["Lectures", "Lecture Videos", "Exams", "Section"]
        #Ask User if to specify Assignment of Homework Folder
        homework_or_assignments = homework_or_assignments_folder()
        list_of_default_folders.append(homework_or_assignments)
        #Create Default Folders
        list_of_default_folder_paths = create_default_folders(list_of_default_folders,
                                                              main_folder_path)
        #Ask To Create Sub-Folders for Lectures from User
        lecture_folder_creation = ask_folder_creation(list_of_default_folders[0])
        if lecture_folder_creation:
            #Ask User For Number of Folders for Lectures
            number_of_lecture_folders = ask_number_of_folders("Lectures")
            #Create Lecture Sub-Folders
            create_folders("Lecture", number_of_lecture_folders, 
                                list_of_default_folder_paths[0])
        #Ask User For Number of Folders for Assignments/Homework
        number_of_assign_or_hwk_folders = ask_number_of_folders(homework_or_assignments)
        #Create Assignment/Homework Sub-Folders
        create_folders(homework_or_assignments,
                               number_of_assign_or_hwk_folders,
                               list_of_default_folder_paths[-1])
        #Create Starter Code and Submission Folders for Each Assignment/Homework Folder
        create_starter_code_and_submission_folders(list_of_default_folder_paths[-1])
        #Ask User For Number of Folders for Section
        number_of_section_folders = ask_number_of_folders("Section")
        #Creae Section Sub-Folders
        create_folders("Section",
                               number_of_section_folders,
                               list_of_default_folder_paths[3])