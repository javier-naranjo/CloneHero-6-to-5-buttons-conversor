
# CloneHero-6-to-5-buttons-conversor

This python code will help you converting your songs that only have
charts that uses a Guitar Hero Live (6 fret guitar controller) into
charts that uses the conventional Guitar Hero / Rock Band controller (5 fret: green, red, yellow, blue and orange). This only works
for CloneHero charts with '.mid' format, and only modifies the "Expert" chart of the songs.

## Screenshots


![App Screenshot](https://user-images.githubusercontent.com/52630564/210461917-a76cb6c1-0434-45f5-9ff1-ae6c002e5703.png)

Here we have an example of how this program can convert a chart
of 6 fret into a 5 fret chart. You can see the before and after
of the execution of the python script. The song is: "A-punk - Vampire Weekend"

![App Screenshot](https://user-images.githubusercontent.com/52630564/210460728-8f5c12d1-bc9e-4c0c-bd9a-978fc39c5aa1.png)

*** IT'S IMPORTANT TO RESCAN THE SONGS TO SEE THE RESULTS AFTER EXECUTING THE PROGRAM***
## Documentation

Since there is a button that is outside the range of a 5 fret guitar
when we want to play a chart of 6 frets,
I have decided to count that missing button as the red one. I think that was the 
best option to have a nice gameplay, but you can change the assignment of the 'missing button' to another one in this part of the code.

```python
    text = open("output3.csv", "r")
    text = ''.join([i for i in text]).replace(", 0, 94, 100",", 0, 96, 100").replace(", 0, 94, 0",", 0, 96, 0")
    x = open("output2.csv","w")
```

the "94" note outside the range of a 5 fret chart, and the "96" number represents
the red color in a 5 fret Guitar Hero Controller. You can replace the "96" for the midi note corresponding to the note color you think is the best if you
want to change the code.
## Installation

You can see in this youtube video how to use this program.
- [https://www.youtube.com/channel/UCnVJ0GgjLNpNJ8rov6tv6OQ](https://www.youtube.com/channel/UCnVJ0GgjLNpNJ8rov6tv6OQ)

Good luck!
    
## Authors

- [Javier Naranjo](https://github.com/javier-naranjo)
To convert a midi file into a plain text file. I used this library:
- [fourmilab | MidiCsv](https://www.fourmilab.ch/webtools/midicsv/)