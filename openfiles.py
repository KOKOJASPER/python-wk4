# Ask the user for the input filename
input_file = input("Enter the input filename (with full path): ")

try:
    # content of the input file
    with open(input_file, "r") as file:
        content = file.read()

    # Modify to uppercase
    modified_content = content.upper()

    #  output file
    output_file = "c:\\Users\\User\\Desktop\\python wk2\\week4-assignment\\modified_example.txt"

    #  modified output file
    with open(output_file, "w") as file:
        file.write(modified_content)

    print(f"File processed successfully. Modified content written to {output_file}")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to read the file '{input_file}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")