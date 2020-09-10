# Tweet Extraction and Analysis

Extract tweets from 15 activists or political twitter handles. Twitter handles should be from 3 different countries, India, USA and Brazil. 
5 twitter handles from each country. Tweet data should contain 3 different languages, Hindi, English and Portugese with one language per set of 5. 
Each twitter handle should atleast have a 1000 tweets and should be collected from 7 consecutive days. 
The data is live streamed for 7 days and stored in the processed live stream folder. 
Atleast 3000 tweets per language. 
The collected tweets should be indexed using Apache Solr Lucene and queried to find their accuracy.
Perform sentiment analysis on the collected data judging if the tweet is positive, negetive or neutral

To run the above code, add twitter auth keys to individual codes in the code section. The code will automatically fetch tweets of 15 persons along with their replies and add it to an individual file.

### Issues handled
 Automatically restart fetching tweets from the last checkpoint when twitter api hits rate limit.
 Automate code to fetch users from JSON file instead of manually adding them to code.


