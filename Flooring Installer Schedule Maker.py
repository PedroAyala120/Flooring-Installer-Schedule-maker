# This program will help schedule a user inputted list of flooring installers, calculate the estimated time, and
# assign the appropriate installer for each job
# Pedro Ayala
 
def main():  # main function
    # Create a dictionary to store the estimated time for each flooring type
    job_times = {
        "hardwood": (1, 1 / 250),
        "lvp": (1, 1 / 350),
        "vinyl": (1, 1 / 350),
        "tile": (1, 1 / 150),
        "carpet": (1, 1 / 250),
        "baseboard": 1
    }

    installers = {}  # initialize installers dictionary

    create_installers(installers)  # call function to create library of installers

    # Prompt user to input number of jobs to schedule
    number_of_jobs = int(input("How many jobs are you scheduling? "))

    # Loop to assign an installer to each job
    while number_of_jobs > 0:

        # Prompt user to input job details
        flooring_type = input("What type of flooring is required for the job? (hardwood/lvp/vinyl/tile/carpet): ")
        square_footage = float(input("What is the square footage of the job? "))
        baseboards_needed = input("Are baseboards needed for the job? (yes/no): ")

        # Calculate the estimated time for the job
        prep_time, install_time = job_times[flooring_type]
        total_time = prep_time + install_time * square_footage
        if baseboards_needed == "yes":
            total_time += job_times["baseboard"]

        # Assign the job to the appropriate installer
        for installer, flooring_types in installers.items():
            if flooring_type in flooring_types:
                print(f"Job assigned to {installer}. Estimated completion time: {total_time} days")
                break

        # subtract number of jobs after each iteration of the loop
        number_of_jobs -= 1
 

# Create a dictionary to store the installer and their flooring type
def create_installers(installers):
    installers = {}  # initialize installers dictionary

    # user input installer data
    num_installers = int(input("How many installers are there? "))  # number of installers
    for i in range(num_installers):
        name = input(f"Enter the name of installer {i + 1}: ")  # input installer name
        flooring_types = []  # initialize flooring types
        num_flooring_types = int(input(f"How many flooring types can {name} install? "))  # input number of
        # for loop to input flooring type for each installer                              # floors installer can do
        for j in range(num_flooring_types):
            flooring_type = input(f"Enter flooring type {j + 1} for {name}: ")
            flooring_types.append(flooring_type)
        installers[name] = flooring_types

    return installers  # return installers' data to main
 
main()  # return to main
