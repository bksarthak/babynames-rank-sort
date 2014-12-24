
import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  names = []
  
  fileRead = open(filename,'r')
  lineRead = fileRead.read()
  match = re.search(r'Popularity\sin\s(\d\d\d\d)',lineRead)
  #print match
  year = match.group(1)
  if match:
   names.append(year)
  else:
   sys.stderr.write('Year not found')
   sys.exit(1)
  
  #make a tuple of all occurences of (rank,male_name,female_name) 
  tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',lineRead)
  
  #make a dictionary having kids name as the keys and their ranks as the values
  dict_kids = {}
  for single_tuple in tuples:
   (rank,boy,girl) = single_tuple
   if boy not in dict_kids.keys():
    dict_kids[boy] = rank
   if girl not in dict_kids.keys():
    dict_kids[girl] = rank
   
  #make a sorted list from the dictionary keys
  kids_sorted = sorted(dict_kids.keys())

  #loop through the sorted list and append kids name and their ranks (from dictionary) to the list having year
  for kids in kids_sorted:
   final_dict = names.append(kids + ' '+ dict_kids[kids])

  return names

  


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)
  
  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for files in args:
   text = extract_names(files)

   complete_text = '\n'.join(text)

   if summary:
    new_file = open(files+'.summary','w')
    new_file.write(complete_text+'\n')
    new_file.close()
   else:
    print complete_text
   

  
if __name__ == '__main__':
  main()
