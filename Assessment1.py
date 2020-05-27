import datetime
import logging
import time

start = time.time()  # Starting of time fun to measure script execution time

logging.basicConfig(level=logging.INFO)  # To log the info
logging.info("Assessment1 Script is running")

names_list = []  # creating list to store the names

with open("names.txt", "r") as file1:  # to open names file 

    names_list = file1.read().replace(" ",
                                      "_").lower().split()  # read the names from the file and coverting it to lowercase
    print(names_list)  # printing the names list


def email(names):
    """Function returns names plus domain i,e email ID's list\n"""
    return names + "@pydemo.com"


print(email.__doc__)  # docstrings

names_updated = list(map(email, names_list))  # using map function to update the email list

print(names_updated)  # printing the email list

names_updated_dup = list(set(names_updated))  # removing duplicates using set function in email list
print(names_updated_dup)  # printing the email list without duplicates

with open("namesupdated.txt", "w") as file2:  # opening the namesupdated text file
    for namesupdated in names_updated_dup:  # using for loop to write the email list to the namesupdated file
        file2.write(namesupdated + '\n')

logging.info("Assessment1 Script is Completed running with no errors")

print("Date and Time Stamp of Assessment1 script execution :", datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S"))

print("Time taken by the script to execute the Assessment1 in Seconds:{0:.4f}",
      time.time() - start)  # To print the time taken to execute script
