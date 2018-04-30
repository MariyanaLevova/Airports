Airports
========

This program uses Dijkstra's shortest path algorithm to calculate the most cost-effective route an aircraft can take given a list of 5 airports and a type of aircraft. 
The program employs a greedy approach, searching for the closest non-visited neighbor that is within the aircraft's range.
The program displays the cost of eligible inputs.
The program generates images to help visualize viable paths. The origin airport node is red and arrows point the direction of travel.


Prerequisites
----------------------

This project was created in a Python 3.6 environment. 


Installation and Setup
----------------------

Run the following commands in Terminal:

```sh
git clone https://github.com/MariyanaLevova/Airports.git && cd Airports/AirportsProject/
pip install -r requirements.txt
```

Running the Program
-------------------

From within the Airports/AirportsProject/ directory (in Terminal), run this command

```sh
python run.py
```

Running the Tests
------------------

From within the Airports/AirportsProject/ directory (in Terminal), run this command

```sh
python test.py
```

Glossary
----------------------
 - Eligible entries - all entries that contain a list of unique airports and aircraft that exist in the project database (e.g. airport "DUB", aircraft "777")
 - Non-eligible entries - all entries that contain non-existing elements (e.g. airport "ABC", aircraft "77778")
 - Feasible path - an eligible entry whose itinerary complies with the rules imposed by the routing algorithm
 - Non-feasible path - an eligible entry whose itinerary does not comply with one or more of the rules imposed by the routing algorithm


