Glossary:
1. Eligible entries - all entries that contain a list of unique airports and aircraft that exist in the project database (e.g. airport "DUB", aircraft "777")
2. Non-eligible entries - all entries that contain non-existing elements (e.g. airport "ABC", aircraft "77778")
3. Feasible path - an eligible entry whose itinerary complies with the rules imposed by the routing algorithm
4. Non-feasible path - an eligible entry whose itinerary does not comply with one or more of the rules imposed by the routing algorithm

What the program does:
1. This program uses Dijkstra's shortest path algorithm to calculate the most cost-effective route an aircraft can take given a list of 5 airports and a type of aircraft.  
2. The program employs a greedy approach, searching for the closest non-visited neighbor that is within the aircraft's range.
3. The program displays the cost of eligible inputs.
4. The program generates images to help visualize viable paths. The origin airport node is red and arrows point the direction of travel.

How to run the program:
1.	Ensure you have all requirements installed (see TermProject/Project/requirements.txt)
2.	Navigate to sub-folder TermProject/Project
3.	Run the Run.py script
4.	Specify the input file to be read, and the output file to write to
5.	The program will read the input file and display the calculated path. If the path is feasible, an image to illustrate the path will be generated
6.	For all eligible entries, a summary will be printed to the specified output file
7.  For all eligible entries that are not feasible, a best case scenario path will be displayed, but no image will be generated.
8.	Non-eligible entries will be flagged as such in the console and no further action will be taken for such entries
