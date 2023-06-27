# MorseCodeConverter

This is a simple command-line Python program to convert alphanumeric characters into Morse Code.

## Usage

1. Clone this repository
git clone https://github.com/yourusername/MorseCodeConverter.git

2. Navigate into the MorseCodeConverter directory
cd MorseCodeConverter

3. Run the program with Python
python morse_converter.py

4. When prompted, enter the string you want to convert into Morse Code.

## How It Works

The program uses a dictionary to map alphanumeric characters (both uppercase and lowercase) to their equivalent Morse Code. When a string is entered by the user, the program iterates over each character in the string. If the character is alphanumeric, it converts it into Morse Code using the dictionary and adds it to the final output string. Spaces in the input are also handled and represented as '/ ' in Morse Code.

## Limitations

This program only converts alphanumeric characters (letters and numbers). Special characters are not supported.

## Contribution

Feel free to fork this project, modify it and create pull requests to improve the functionality.

## License

This project is licensed under the MIT License.
