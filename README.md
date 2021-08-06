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

## Deep Decision Policy Gradient Network
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

## Daily NN 

To start from Chris: 
```
- Input player and output layer are fixed in size (# of stats, 1) with scalar values. 
- Hidden layers are fully connected 
- Start with 2 hidden layers 
- Start with hidden layer size = input.size / 2 

So my general plan: 
Write data gathering scrips to catalog the history of baseball to generate thousands of examples 
Write TF program to take that training set and train from it 
Evaluate test:train splits for accuracy  

Chris Stathis, 25 min
anyways, ML question?

Jeff Porzio, 25 min
Yessss ok
So this is recreational for fun
I want to do some RL with baseball players for daily draft stuff.  So the idea is I feed in a bunch of stats about a player and I want the algo to predict how "well" they'll score the following day.
I can scrub a shitton of test cases, I don't think data is going to be a problem.
But I was wondering if you have some resources / advice on how I should pick the NN and what type of NN etc... number of internal layers, etc...
The outside shape will be a bunch of inputs (I'll do some test trainings to figure out which are important?) and then output a single float "number of points" they'll be worth given those inputs.
Inputs are all floats or ints
(This is a simpler problem to the DDPGN we discussed last time.  I think that was more than I could chew)
Tensor flow in Python

Chris Stathis, 20 min
cool, yeah that sounds easy enough
sounds like you have an input and output layer with a fixed number of scalar inputs, and the hidden layers can just be fully connected
i would start small; two layers is probably enough

Jeff Porzio, 17 min
Two hidden layers?

Chris Stathis, 15 min
yeah
and start with hidden layer size = input layer size / 2 or something like that

Chris Stathis, 13 min
the more neurons you have the more training data you need, and since your problem is fairly simple / low-dimensional I would err on the side of a smaller net

Jeff Porzio, 12 min
Perfection. These are the sorts of rules of thumb I was looking for 😀
What are some signs that I need more complexity / a different set up?

Chris Stathis, 11 min
overfitting to training data
or otherwise inability to generalize
think of it like terms in a n-D polynomial fit... if the function has really high dimension and high order terms you need more neurons or you'll only be able to fit to the region of the state space that your training data covers well

Jeff Porzio, 9 min
but an N-d polynomial can also fix the noise if N is too high ... which is over training?
fit*

Chris Stathis, 5 min
if you have good performance on a large training set but bad performance on the test set its usually better to tweak the learning rate etc. than actually change the network structure
if you can't even get good performance on the training set as you increase the size of it, then it might mean the network isn't generalizing well enough

Jeff Porzio, 3 min
Ok, gotcha.  So I am going to write a script to generate as close to the history of baseball as I can get (I've got this mostly tooled out, just need to figure out how to transform it into something savable, probs just a spreadsheet?).  I'll train using a subset of that and see how performance changes based on including more/less of that entire data set?
Any hardware things I should aim for from the get go?  Do I want a GPU implementation from the start or is a CPU start ok?

Chris Stathis, 1 min
CPU is fine
If you're using keras/tf you should be able to get GPU acceleration for free as long as you can figure out how to install it correctly

Jeff Porzio, 1 min
Sweet.
Thank you, sir 😀

```


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