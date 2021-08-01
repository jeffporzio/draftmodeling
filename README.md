 # To install... 

```
conda install python=3.9.4
pip install pybaseball
pip install baseball-scraper
```

Other packages: 
- Numpy
- Pandas


# dailydraft/
Either generic algorithm to "optimize" the team 
Or NN to make thousands of examples every day, then train with the "answers" the next day? 
 - Can this be done retroactively using the daily data? I think so. 
Probably too large of a parameter space

Code Approach 1, eventually generate enough datat to try Approach 2
## Approach 1: 
Use genetic algo to pick optimal team based on raw data
Pros: Easy, fast 
Cons: Doesn't have a way to account for randomness in player performance
player data --> projections to points conversion --> build a team based on those points

## Approach 2: 
Train NN to predict player's values based on raw data and use that as an input to the optimization problem 
Pros: Allows us to try and predict player performance somehow.  
Cons: Requires learning TF. Not entierly sure the NN will be successful. 
Training:
players data --> NN which predicts points for that player that day
actual next day data --> Used to construct training data 
Usage: 
Replace "projections to points conversion" in approach 1 with the predictive algorithm

## Approach 3: 
Train NN to pick an entire team based on the raw data 
Pros: Probably the most promising. 
Cons: Too large of a parameter space.

# seasondraft/ 
Contains some initial sketches for classes I wanted to keep.  Originally from the DDPGN idea of picking a team for a season. 
Some classes are missing and the code is not in a "nice" shape. 







# Hosting a webiste 
- Droplet from digital ocean $5/mo (get the smallest one for now)
- Google Domains One time cost + $5/yr
- VMWare for sshing into the container
- Google: "Digital Ocean Nginx guide"

Plan is to use Flask + Jinja2 for the website?







# LearningTF/
Contains some code examples for doing a DDPGN in Tensor Flow.  No original content yet. 

To decide value: 
    use data from MC sims to know what 1st, 2nd, 3rd, thresholds are for each category to predice the 
    increased value that player adds to the team. 

NN: 
    Use NN to predict value of a player based on all the data we have 
        (Player stats, team's current stats, money, number of players, 
            maybe historical data about each threshhold
            Other team's stats? Probably.
        )

    Rough flow: 
    while true: 
        Do draft with NN deciding value of each player
        Do a league to see how each team scores
        Organize the results of the league's scores into training set data
        Train NN with that data, repeat

    Things we need: 
    - Idea of what the NN should use
    - Tools to convert the league results into training data
        + What training data it needs 
    -  Can I turn the 23+ decisions the NN made into useful data? Q-Learning?

    - Decide who wins what points for a league and report that 

    - Better to have the NN predict value and have a separate algo do the auctioning? I think yes.

    - Separate agents for valuing the next player to pick when it's our turn?

https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-4-deep-q-networks-and-beyond-8438a3e2b8df

https://github.com/awjuliani/DeepRL-Agents/blob/master/Double-Dueling-DQN.ipynb

https://www.tensorflow.org/agents/tutorials/0_intro_rl DQN Not suitable to problem 

https://pemami4911.github.io/blog/2016/08/21/ddpg-rl.html


# flaskapp/

## Running the app
```
set FLASK_APP=flaskapp.py
set FLASK_DEBUG=1
flask run
```
Default port is 5000.  I have it set to run on 8080 if you run the flaskapp.py script 
```
python flaskapp.py
```

The above is probably how to do this in production.  It can also be run by running the flaskapp.py script. 

Trying to figure out how to make this as close to a web components architecture as possible... I really donn't want to learn REACT or something.  Typescript WC might be better but missing some tools I am used to working with for those. 
Each tempalte can be a "component" and we can include them as blocks, however I am not yet sure how to handle passing information to and from the components that need to agree on the same data. 

## Todo:

 Put each component behind a (singlton?) factory so I can create multiple instances of them easily, without importing an instance. 

Make a generic store class with pub/sub behavior so components can be dynamically updated as the state changes. 


# Road Map: 

Create a "data" page where we just display the statistics for hitter and pitchers in tables for the given input range of dates.  This lets us figure out the back end problems of getting all the data we need.  It also gives us a simple front end problem to solve to build up a framework. 

Once we have all the data we need, we can work on actually doing the draft prediction algorithms for the daily draft team. 