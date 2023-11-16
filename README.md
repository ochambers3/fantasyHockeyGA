# fantasyHockeyGA
This is a genetic algorithm that uses last years hockey stats to learn how to draft a winning fantasy hockey league team.
The goal of this project is to help me gain insight into how I should be selecting players, and what I should be looking for in those players.

My specific league uses the following point distribution:
Goals       6
Assists     4
Power Play Points   2
Shorthanded Goals   2
Game-Winning Goals  .25
Shots on Goal       0.9
Hits        1
Blocks      0.5

Goalies:
Win         5
Saves       0.3
Shutouts    5

This is how our league determines which player in the league wins and who loses.
My theory is that if I create a mock draft with managers who learn how to weight the different categories using last years stats,
then it will give me insight into whether specific stats are overweighted or underweighted currently how the league weights them.

I also could use the help in my league, as of Nov 8 2023 I have 1 win and 2 losses.

Hockey Statistics provided by Quant Hockey at quanthockey.com

Successfully ran the first implementation with 6 hockey managers
Conclusion:
My Genetic Algorithm learned to weight assists as the most important stat and short handed goals as the least important.
After normalizing the weights and comparing them to that of my league, I discovered that (according to my GA) my league 
over-weights goals by 53%. Assists were underestimated the most at 34%, and power play points were weighted most closely to 
the found value at an underestimation of 3%. As of Nov 16, 2023 I am 1-4 in my league. I will change my team to find players who 
get more assists and see if that helps me win more weeks.
