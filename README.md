  # Clusters in directed signed networks

## Abstract : 
The authors of the paper don’t take into account the time at which the link has been created, and whether people are familiar with each other (they come from the same cluster).

Here we will try to analyze the impact of the time at which the link has been created : does it have an influence on the vote ? 
Furthermore, we will also study whether there are clusters of people in the datasets we already have : Are there people who know each other ? 
These parameters can highly impact the sign of the link between 2 people.

We also use the Reddit dataset, a signed network containing links between communities. We want to know if we can find clusters, given the links, and how we can predict the sign of a link based on the time, and based on the clusters, and compare this to the balance theory and the status theory.


## Research Questions : 

The idea is to highlight different parameters that might be important in social network edges prediction. In the original paper, they focus on balance and status theory. Here, using a new dataset, we will try to highlight the importance of other parameters.

**Groups ?**
Are people friends before voters and electors ? (for the wikipedia dataset specially)
Do there exist groups ?
Is it possible to identify groups through the voting behavior?

**From individual to communities behavior ?** 
Do networks between communities act the same way as networks between users? 
More concrete, can we see the same type of behavior in terms of the percentage of positive versus negative edges as in networks among users?
How far can we extend the methods and conclusions derived from individual behavior analysis to groups? And the reverse way, from communities to individuals?

**Importance of time?** 
Can the time affect how a user will link? 
Can we see a trend that users are more likely to create a positive or negative during a certain time of day? Does the day or week of the year influence the votes?

**Weighting of links ?**
How can we take this information into account? How important is the information given by weight of links ? How does it impact the structure network?

## Proposed dataset :
Reddit Hyperlink network (https://snap.stanford.edu/data/soc-RedditHyperlinks.html) : This dataset contains posts that creates a hyperlink from one dataset to another. There is a positive edge from page A to page B when page A is positive towards B, and there is a negative if A is negative towards B. This dataset is a tsv file, it contains the following informations :
- Name of the source reddit page
- Name of the target reddit page
- Id of the Post
- Timestamp
- Link Sentiment (+1 or -1)
- Properties (number of characters in the page, Fraction of digit, positive sentiment score, negative sentiment score, compounds sentiments score...)


## Methods : 
**Load the data :** The dataset provided is already treated, so we just have to load it using pd.read_csv(‘file’, sep = ‘\t’)<br>
**Create the network :** To create the network, we use the networkx package. We create the network using the names for the nodes, and the labeled edges (+1 or -1)<br>
**Use built-in functions :** Networkx allow us to use some clustering functions (https://networkx.org/documentation/stable/reference/algorithms/clustering.html), so we will try to use them and see if we can already draw conclusions<br>
**Compare the number of edges, nodes,.. with other datasets :** We will try to reproduce table 1 for this new dataset and compare with the ones we already have.<br>
**Implement clustering methods for all datasets :** We already used the slashdot, epinions and wikipedia datasets. So we will try to find clusters in these networks too. Specifically, for the wikipedia dataset, we can try to take into account the nominator of the election, to see if he is a friend of the editor considered for promotion, and try to find clusters of voters/nominators/editors that are close to each other. This way we can highlight biases in the elections.<br>
**Study the impact of time on the sign of the link :** We have the time information for the new dataset and the wikipedia one, so we can find the impact of time on the link and find an explanation. Example : Between 12h and 14h, the link is twice more likely to be positive -> explanation : around lunch time, people are more likely to vote positively as they are more tired, or they just ate so they’re happier/less embittered.
Use the weights of the links :  For the new dataset, we have the information about the sentiment score of the link. So a link with a higher sentiment score has more weight.

## Proposed Timeline : 
**Week 1:** Do the creation of the graphs using the new Reddit dataset, compute the equivalent of Table1 for Reddit (and other analysis that might help to know if communities results can be extended to individual or reverse, bibliography research) study the impact of time on the links, begin to implement the clustering method, begin to implement weight edges analysis (also bibliography).<br>
**Week 2:** Finish to implement the clustering methods and sentiment weighting ,compare with the others datasets. Analysis and discussion work. <br>
**Week 3:** Continuing with analysis, preparing the data story and short video.<br>

## Organization within the team : 

We don’t assign particular tasks to anyone. Whenever a person does something, he notify others through the conversation of the group. Thus we have a linear progression and everybody is involved. Plus, it allows a person to find some errors when another one doesn't find it, it allows us to optimize the code. 
In addition to the updatings on the conversation, we plan to do 2 meetings per week, to discuss our findings that need a detailed explanation, and to discuss the project.
	

## Notebook :

## Report : 
