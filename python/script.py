import glob
import json
import os
import sys

def parent_dir():
    # Get the parent directory of the current directory
    return os.path.dirname(os.getcwd())

def create_folder_name(idx, json_object):
    #create folder name in the format of course_number-lab-idx-last_name-first_name
    foldername = json_object["course_number"] + "-" + "lab" + idx + "-" + json_object["last_name"] + json_object["first_name"]
    # print("foldername: " + foldername)
    return foldername

def delete_folder(foldername):
    #delete folder
    os.rmdir(os.path.join(parent_dir, foldername))

def check_folder_exists(parent_dir,foldername):
    #check to see if folder already exists
    if os.path.exists(os.path.join(parent_dir, foldername)):
        print("Folder already exists")
        return True
    else:
        return False

def load_json():
    json_file = glob.glob('*.json') # get json file
    # Opening JSON file
    with open(str(json_file[0]), 'r') as json_file:
        # Reading from json file
        json_object = json.load(json_file)
    return json_object

def user_input():
    # Check if the user has provided the correct number of arguments
    if len(sys.argv) != 2:
        # get idx value from json file
        json_object = load_json()
        idx = json_object["index_number"]

        #increment idx value and add extra zero on the front if idx < 10 and save to json file
        if int(idx) < 10:
            json_object["index_number"] = "0" + str(int(idx) + 1)
        else:
            json_object["index_number"] = str(int(idx) + 1)

        json_file = glob.glob('*.json') # get json file
        #save json object to file
        with open(str(json_file[0]), "w") as outfile:
            json.dump(json_object, outfile)

        return idx

    # Check if the user has provided the help argument
    if (sys.argv[1] == "-help" or sys.argv[1] == "-h" or sys.argv[1] == "-?"):
        print("usage : " + os.path.dirname(os.getcwd()) +"\python> python3 script.py <index number>\n\
Options and arguments (and corresponding environment variables):\n\
-E     : Edit .json file\n\
-h     : print this help message and exit (also -? or --help)")
        sys.exit(0)

    if (sys.argv[1] == "-E"):
        print("Editing .json file")
        #ask for course number
        course_number = input("Enter your course number: ")
        #ask user for next index number
        index_number = input("Enter your starting idx value: ")
        #ask user for last name
        last_name = input("Enter your last name: ")
        #ask user for first name
        first_name = input("Enter your first name: ")
        
        #create json object with course number, idx value, last name, first name
        json_object = {
            "course_number": course_number,
            "index_number": index_number,
            "last_name": last_name,
            "first_name": first_name
        }

        json_file = glob.glob('*.json') # get json file

        #save json object to file
        with open(str(json_file[0]), "w") as outfile:
            json.dump(json_object, outfile)

        sys.exit(0)

    #Get the folder number from the command line
    return sys.argv[1]

def print_json(json_object):
    #print json object
    print(json_object)

def main():
    # check user input values
    idx = user_input()
    # load json file
    json_object = load_json()
    # get parent directory
    dir = parent_dir()
    # create folder name
    foldername = create_folder_name(idx, json_object)
    #check if folder name already exists
    value = check_folder_exists(dir, foldername)
    if value == True:
        print("Folder already exists... please enter a different index number")
        sys.exit(0)
    #ask the user if they are sure they want to create the folder with the given name
    answer = input("Are you sure you want to create a folder with the name: " + foldername + "? (y/n): ")
    if answer == "n":
        sys.exit(0)

    #create foldername
    os.mkdir(os.path.join(dir, foldername))
    #create docs folder within foldername
    os.mkdir(os.path.join(dir, foldername, "docs"))
    #create src folder within foldername
    os.mkdir(os.path.join(dir, foldername, "src"))
    #create README.md file within foldername
    with open(os.path.join(dir, foldername, "README.md"), "w") as f:
        #write to README.md file Lab + idx:
        f.write("Lab " + idx + ":")
        #add ========== under Lab + idx:
        f.write("\n" + "===========")
    #create TODO.md file within foldername
    with open(os.path.join(dir, foldername, "TODO.md"), "w") as f:
        #write to TODO.md file Lab + idx:
        f.write("TODO - Lab" + idx + ":")
        #add ========== under Lab + idx:
        f.write("\n" + "===========")
    sys.exit(0)

if __name__ == "__main__":
     main()






