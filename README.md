
# CloneHero-6-to-5-buttons-conversor

This python code will help you converting your songs that only have
charts that uses a Guitar Hero Live (6 fret guitar controller) into
charts that uses the conventional Guitar Hero / Rock Band controller (5 fret: green, red, yellow, blue and orange). This only works
for CloneHero charts with '.mid' format, and works for every difficulty on each song.
***I made this specially to play the Guitar Hero TV (GHTV) setlist with a 5 fret guitar, because they are 519 amazing songs and I don't have a 6 fret guitar, and actually I don't like it!**

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
best option to have a nice gameplay, but you can change the assignment of the 'missing button' to another one.

![20230122_162820](https://user-images.githubusercontent.com/52630564/213943202-e6e66c75-ba74-4944-bfbb-144479bda4e4.jpg)

**The thing you need to know is that if in the gamemplay we see an event where the 6th note and the red note are pressed at the same time, they will be one on top of the other.**

Here we see the 6th note and the red one at the same time. One on top of the other.

![one on top](https://user-images.githubusercontent.com/52630564/210464459-474c1bd3-f0b7-44e2-9842-4fc87ae8afb0.png)
 

## Installation

*** IT'S IMPORTANT TO HAVE THE FOLDER "midicsv-1.1" IN THE SAME DIRECTORY OF THE PROGRAM, OTHERWISE ALL THE CHARTS WILL BE WIPED (PLEASE WATCH THE YOUTUBE VIDEO BELOW)... IF YOU MAKE THIS MISTAKE IS NOT A BIG DEAL ANYWAYS, YOU CAN EXECUTE "rollback.exe" AND EVERYTHING WILL BE THE SAME AGAIN.***

You can see in this youtube video how to use this program.
- [https://www.youtube.com/watch?v=XwHPXCSTVyU](https://www.youtube.com/watch?v=XwHPXCSTVyU)

But it's easy since I have made a simple GUI.

![GUI](https://user-images.githubusercontent.com/52630564/210463779-9d5da898-bd2a-4d85-b817-9dc1a4aca34c.png)

Also, to undo all the changes in the folder you have selected, feel free to use the rollback.exe. This will undo all the convertion going back to the original 6 fret charts.
    
## Authors

- [Javier Naranjo](https://github.com/javier-naranjo)
To convert a midi file into a plain text file. I used this library:
- [fourmilab | MidiCsv](https://www.fourmilab.ch/webtools/midicsv/)