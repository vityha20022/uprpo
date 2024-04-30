import os

def count_characters(filename):
  """Counts the number of characters in a text file.

  Args:
    filename: The name of the text file.

  Returns:
    The number of characters in the text file.
  """

  with open(filename, "r") as f:
    text = f.read()

  return len(text)


def count_words(filename):
  """Counts the number of words in a text file.

  Args:
    filename: The name of the text file.

  Returns:
    The number of words in the text file.
  """

  with open(filename, "r") as f:
    text = f.read()

  words = text.split()

  return len(words)


def count_lines(filename):
  """Counts the number of lines in a text file.

  Args:
    filename: The name of the text file.

  Returns:
    The number of lines in the text file.
  """

  with open(filename, "r") as f:
    lines = f.readlines()

  return len(lines)


if __name__ == "__main__":
  # Get the filename from the user.
  filename = input("Enter the name of the text file: ")

  # Check if the file exists.
  if not os.path.isfile(filename):
    print("The file does not exist.")
    exit()

  # Count the number of characters, words, and lines in the file.
  num_characters = count_characters(filename)
  num_words = count_words(filename)
  num_lines = count_lines(filename)

  # Print the results.
  print(f"The number of characters in the file is: {num_characters}")
  print(f"The number of words in the file is: {num_words}")
  print(f"The number of lines in the file is: {num_lines}")
