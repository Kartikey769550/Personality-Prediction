import streamlit as st
from PIL import Image

img2 = Image.open('icon2.png')
img1 = Image.open('5triats.png')
img0 = Image.open('dataflow.jpeg')
img3 = Image.open('Dataflow.png')


def app():
    st.markdown(
        '<h2 style="background-color:Grey; border-radius:5px; padding:5px 15px ; text-align:center ; font-family:arial;color:white">Personality Prediction</h2>',
        unsafe_allow_html=True)
    st.markdown(
        '<h4 style="border: inset 2px black; border-radius:4px; padding:2px 15px">Prediction-Lab : <i>Personality Predictor</i></h4>',
        unsafe_allow_html=True)
    col1, col2 = st.beta_columns((1, 2))
    with col1:
        st.text("." * 100)
        st.image(img2, width=230)
    with col2:
        st.text("." * 200)
        st.info(
            "Personality-Prediction :- Prediction-Lab a digital laboratory for Machine Learning and Artificial Intelligence")
        st.info(
            "Personality :- Style is a reflection of your attitude and your Personality")
    st.text("." * 200)
    col3 = st.beta_columns(1)
    with st.beta_expander("OCEAN PERSONALITY : OP"):
        st.write('''<p>The Big Five personality test gives you more insight into how you react in different situations, which can help you choose an occupation. 
        Career professionals and psychologists use this information in a personality career test for recruitment and candidate assessment.</p>
        <p>The big five come from the statistical study of responses to personality items. Using a technique called factor analysis researchers can look at the responses
        of people to hundreds of personality items and ask the question "what is the best was to summarize an individual?". 
        This has been done with many samples from all over the world and the general result is that, while there seem to be unlimited personality variables, five stand out from 
        the pack in terms of explaining a lot of a persons answers to questions about their personality: extraversion, neuroticism, agreeableness, conscientiousness and openness to experience. 
        The big-five are not associated with any particular test, a variety of measures have been developed to measure them. 
         </p>''', unsafe_allow_html=True)
        col1, col2, col3 = st.beta_columns((1, 2, 1))
        with col2:
            st.image(img1, use_column_width=True)
        st.write('''<pre>The theory identifies five factors :
            Following are the five factors for the personality
                • <b>openness to experience</b> (inventive/curious vs. consistent/cautious)
                • <b>conscientiousness</b> (efficient/organized vs. extravagant/careless)
                • <b>extraversion</b> (outgoing/energetic vs. solitary/reserved)
                • <b>agreeableness</b> (friendly/compassionate vs. challenging/callous)
                • <b>neuroticism</b> (sensitive/nervous vs. resilient/confident)</pre>''', unsafe_allow_html=True)
        st.write('''<pre>• Procedure :
                • The test consists of Twenty items that you must rate on how true they are 
                  about you on a five point scale where
                  1=Strongly Disagree, 2=Disagree, 3=Neutral, 4=Agree and 5=Strongly Agree. 
                  It takes most people 3-8 minutes to complete.
            </pre>''', unsafe_allow_html=True)
    with st.beta_expander(" Logistic Regression "):
        st.write('''<p>•  Logistic regression is one of the most popular Machine Learning algorithms, which comes under the <b>Supervised</b> Learning technique. It is used for predicting the categorical dependent variable using a given set of independent variables.</p>
         <p>•  Logistic regression predicts the output of a categorical dependent variable. Therefore the outcome must be a categorical or discrete value. It can be either Yes or No, 0 or 1, true or False,
          etc. but instead of giving the exact value as 0 and 1, <b>it gives the probabilistic values which lie between 0 and 1</b>.</p>
        <p>•  Logistic Regression is much similar to the Linear Regression except that how they are used. Linear Regression is used for solving Regression problems, whereas 
        <b>Logistic regression is used for solving the classification problems</b>.</p>''',
                 unsafe_allow_html=True)

        st.write('''<p><b>Logistic Function (Sigmoid Function):</b></p>
                 •  The sigmoid function is a mathematical function used to map the predicted values to probabilities.
                 <p>•  It maps any real value into another value within a range of 0 and 1.</p>             
            ''', unsafe_allow_html=True)
        st.write('''<pre><b>Logistic Regression Equation:</b>
        The Logistic regression equation can be obtained from the Linear Regression equation. The mathematical steps to get Logistic Regression equations are given below:
                    Step-1: We know the equation of the straight line can be written as:
                            y=b<sub>0</sub> + b<sub>1</sub>x<sub>1</sub> + b<sub>2</sub>x<sub>2</sub> + b<sub>3</sub>x<sub>3</sub> +....+ b<sub>n</sub>x<sub>n</sub>
                    Step-2: In Logistic Regression y can be between 0 and 1 only, so for this let's divide the above equation by (1-y):
                            y/(1-y);0 for y=0, and infinity for y=1
                    Step-3: But we need range between -[infinity] to +[infinity], then take logarithm of the equation it will become:
                            log(y/(1-y))=b<sub>0</sub> + b<sub>1</sub>x<sub>1</sub> + b<sub>2</sub>x<sub>2</sub> + b<sub>3</sub>x<sub>3</sub> +....+ b<sub>n</sub>x<sub>n</sub>
                    </pre>
                    ''', unsafe_allow_html=True)

    with st.beta_expander("Support Vector Machine"):
        st.write('''<p>Support Vector Machine or SVM is one of the most popular <b>Supervised</b> Learning algorithms, which is used for Classification as well as Regression problems.
             However, primarily, it is used for Classification problems in Machine Learning.</p>
                        <p>The goal of the SVM algorithm is to create the best line or decision boundary that can segregate n-dimensional space into classes so that we can easily put the new data point in the correct category in the future.
                         This best decision boundary is called a hyperplane.</p>
                        <p><b>SVM are of two types:</b></p>
                        <p><b>Linear SVM:</b> − Linear SVM is used for linearly separable data, which means if a dataset can be classified into two classes by using a single straight line, 
                        then such data is termed as linearly separable data, and classifier is used called as Linear SVM classifier.</p>
                        <p><b>Non-linear SVM:</b> − Non-Linear SVM is used for non-linearly separated data, which means if a dataset cannot be classified by using a straight line, 
                        then such data is termed as non-linear data and classifier used is called as Non-linear SVM classifier.</p>''',
                 unsafe_allow_html=True)
        st.write('''<pre><b>Linear Kernel:</b>
            <b>Linear Kernel</b> is used when the data is Linearly separable, that is, it can be separated using a single Line.
            It is one of the most common kernels to be used. It is mostly used when there are a Large number of Features in a particular Data Set.
            One of the examples where there are a lot of features, is Text Classification, as each alphabet is a new feature. 
            So we mostly use Linear Kernel in Text Classification.

            It can be used as a dot product between any two observations. The formula of linear kernel is as below:
                  <b>K(x,xi)=sum(x∗xi)</b></pre>''', unsafe_allow_html=True)

    with st.beta_expander("Methodology of Supervised"):
        st.write('''<p>The methodology is the core component of any research-related work. The methods used to gain the results are shown in the methodology. 
            Here, the whole research implementation is done using python. There are different steps involved to get the entire research work done which is as follows:</p>''',
                 unsafe_allow_html=True)
        col4, col5, col6 = st.beta_columns((1, 2, 1))
        with col5:
            st.image(img0, use_column_width=True)
        st.write('''<b><h4>1. Acquire Personality Dataset</h4></b>''', unsafe_allow_html=True)
        st.write('''<p>The kaggle machine learning  is a collection of datasets, data generators which are used by machine learning community for analysis purpose. 
            The personality prediction dataset is acquired from the kaggle website. This dataset was collected (2016-2018) through an interactive on-line personality test. The personality test 
            was constructed from the IPIP. The personality prediction dataset can be downloaded in zip file format just by clicking on the link available. 
             The personality prediction file consists of two subject CSV files (test.csv & train.csv). The test.csv file has 0 missing values, 7 attributes, and final label output. 
            Also, the dataset has multivariate characteristics. Here, data-preprocessing is done for checking inconsistent behaviors or trends.</p>''',
                 unsafe_allow_html=True)
        st.write('''<b><h4>2. Data preprocessing</h4></b>''', unsafe_allow_html=True)
        st.write('''<p>After, Data acquisition the next step is to clean and preprocess the data. 
            The Dataset available has numerical type features. 
            The target value is a five-level personality consisting of serious,lively,responsible,dependable & extraverted. 
            The preprocessed dataset is further split into training and testing datasets. 
            This is achieved by passing feature value, target value, test size to the train-test split method of the scikit-learn package. 
            After splitting of data, the training data is sent to the following Logistic regression & SVM design is used for training the artificial neural networks then test data is used to predict the accuracy of the trained network model.</p>''',
                 unsafe_allow_html=True)
        st.write('''<b><h4>3. Feature Extraction</h4></b>''', unsafe_allow_html=True)
        st.write('''<p>The following items were presented on one page and each was rated on a five point scale using radio buttons. The order on page was  EXT1, AGR1, CSN1, EST1, OPN1, EXT2, etc.
                    The scale was labeled 1=Disagree, 3=Neutral, 5=Agree


                    EXT1	I am the life of the party.
                    EXT2	I don't talk a lot.
                    EXT3	I feel comfortable around people.
                    EXT4	I am quiet around strangers.
                    EST1	I get stressed out easily.
                    EST2	I get irritated easily.
                    EST3	I worry about things.
                    EST4	I change my mood a lot.
                    AGR1	I have a soft heart.
                    AGR2	I am interested in people.
                    AGR3	I insult people.
                    AGR4	I am not really interested in others.
                    CSN1	I am always prepared.
                    CSN2	I leave my belongings around.
                    CSN3	I follow a schedule.
                    CSN4	I make a mess of things.
                    OPN1	I have a rich vocabulary.
                    OPN2	I have difficulty understanding abstract ideas.
                    OPN3	I do not have a good imagination.
                    OPN4	I use difficult words.
                    ''',
                 unsafe_allow_html=True)
        st.write('''<b><h4>4. Training the Model</h4></b>''', unsafe_allow_html=True)
        st.write(
            '''<p>Train/Test is a method to measure the accuracy of your model. It is called Train/Test because you split the the data set into two sets: a training set and a testing set. 80% for training, and 20% for testing.
             You train the model using the training set.In this model we trained our dataset using linear_model.LogisticRegression() & svm.SVC() from sklearn Package</p>''',
            unsafe_allow_html=True)
        st.write('''<b><h4>5. Personality Prediction Output</h4></b>''', unsafe_allow_html=True)
        st.write('''<p>After the training of the designed neural network, the testing of Logistic Regression & SVM is performed using Cohen_kappa_score & Accuracy_Score.
            </p>''',
                 unsafe_allow_html=True)
    with st.beta_expander(" K-means Clustering "):
        st.write('''<p>K-Means Clustering is an <b>Unsupervised Learning algorithm</b>, which groups the unlabeled dataset into different clusters.
           Here K defines the number of pre-defined clusters that need to be created in the process, as if K=2, there will be two clusters, and for K=3, there will be three clusters, and so on.</p>
           <p>It allows us to cluster the data into different groups and a convenient way to discover the categories of groups in the unlabeled dataset on its own without the need for any training.
              It is a centroid-based algorithm, where each cluster is associated with a centroid.The main aim of this algorithm is to minimize the sum of distances between the data point and their corresponding clusters.</p>
          <p>The algorithm takes the unlabeled dataset as input, divides the dataset into k-number of clusters, and repeats the process until it does not find the best clusters. 
          The value of k should be predetermined in this algorithm.</p>''',
                 unsafe_allow_html=True)
        st.write('''<p><b>The k-means clustering algorithm mainly performs two tasks:</b></p>
                   •  Determines the best value for K center points or centroids by an iterative process.             
                   <p>•   Assigns each data point to its closest k-center. Those data points which are near to the particular k-center, create a cluster.</p>
              ''', unsafe_allow_html=True)
        st.write('''<pre><b>K-mean Algorithm:</b>
                      Step-1: Select the number K to decide the number of clusters.
                      Step-2: Select random K points or centroids. (It can be other from the input dataset).
                      Step-3: Assign each data point to their closest centroid, which will form the predefined K clusters.
                      Step-4: Calculate the variance and place a new centroid of each cluster.
                      Step-5: Repeat the third steps, which means reassign each datapoint to the new closest centroid of each cluster.
                      Step-6: If any reassignment occurs, then go to step-4 else go to FINISH.
                      Step-7: The model is ready.
                      </pre>
                      ''', unsafe_allow_html=True)
        st.write('''<p><b>How to choose the value of "K number of clusters" in K-means Clustering?</b></p>
          The performance of the K-means clustering algorithm depends upon highly efficient clusters that it forms. But choosing the optimal number of clusters is a big task. There are some different ways to find the optimal 
          number of clusters, but here we are discussing the most appropriate method to find the number of clusters or value of K. 
          <p>The method is given below:</p>
          ''', unsafe_allow_html=True)
        st.write('''<pre><b>Elbow Method:</b>
          The Elbow method is one of the most popular ways to find the optimal number of clusters. This method uses the concept of WCSS value.
          WCSS stands for Within Cluster Sum of Squares, which defines the total variations within a cluster. The formula to calculate the value
          of WCSS (for 3 clusters) is given below:
          <p><center> WCSS= ∑P<sub>i in Cluster1</sub>distance(Pi C1)<sup>2</sup>+∑P<sub>i in Cluster2</sub>distance(Pi C2)<sup>2</sup>+∑P<sub>i in CLuster3</sub>distance(Pi C3)<sup>2</sup></center></p>
          In the above formula of WCSS:-
          ∑P<sub>i in Cluster1</sub>distance(Pi C1)<sup>2</sup>:It is the sum of the square of the distances between each data point and its centroid within a
          cluster1 and the same for the other two terms.
          To measure the distance between data points and centroid, we can use any method such as Euclidean distance or Manhattan distance.
          To find the optimal value of clusters, the elbow method follows the below steps:
          • It executes the K-means clustering on a given dataset for different K values (ranges from 1-10).
          • For each value of K, calculates the WCSS value.
          • Plots a curve between calculated WCSS values and the number of clusters K.
          • The sharp point of bend or a point of the plot looks like an arm, then that point is considered as the best value of K.
          </pre>
          ''', unsafe_allow_html=True)

    with st.beta_expander("Hierarchical Clustering"):
        st.write('''<p>Hierarchical clustering is another unsupervised learning algorithm that is used to group together the unlabeled data points having similar characteristics. Hierarchical clustering algorithms falls into following two categories.</p>
                          <p><b>Agglomerative hierarchical algorithms</b> − In agglomerative hierarchical algorithms, each data point is treated as a single cluster and then successively merge or agglomerate (bottom-up approach) the pairs of clusters. 
                          The hierarchy of the clusters is represented as a dendrogram or tree structure.</p>
                          <p><b>Divisive hierarchical algorithms</b> − On the other hand, in divisive hierarchical algorithms, all the data points are treated as one big cluster and the process of clustering involves dividing (Top-down approach) the one 
                          big cluster into various small clusters.</p>''',
                 unsafe_allow_html=True)
        st.write('''<pre><b>Steps to Perform Agglomerative Hierarchical Clustering:</b>

                                  Step-1: Treat each data point as single cluster. Hence, we will be having, say K clusters at start. 
                                          The number of data points will also be K at start.
                                  Step-2:  Now, in this step we need to form a big cluster by joining two closet datapoints.
                                           This will result in total of K-1 clusters.
                                  Step-3: Now, to form more clusters we need to join two closet clusters. This will result in total of K-2 clusters.
                                  Step-4: Now, to form one big cluster repeat the above three steps until K would become 0 
                                          i.e. no more data points left to join.
                                  Step-5: At last, after making one single big cluster, dendrograms will be used to divide into 
                                          multiple clusters depending upon the problem.
                                  </pre>
                                  ''', unsafe_allow_html=True)
        st.write('''<p>How should we Choose the Number of Clusters in Hierarchical Clustering?</p>
                          <p>To get the number of clusters for hierarchical clustering, we make use of an awesome concept called a Dendrogram.</p>
                          <p><b>A dendrogram is a diagram that shows the hierarchical relationship between objects. It is most commonly created as an output from hierarchical clustering.
                           The main use of a dendrogram is to work out the best way to allocate objects to clusters.
                           The dendrogram below shows the hierarchical clustering of six observations shown on the scatterplot to the left.</b></p>''',
                 unsafe_allow_html=True)
    with st.beta_expander("Methodology of Unsupervised"):
        st.write('''<p>The methodology is the core component of any research-related work. The methods used to gain the results are shown in the methodology. 
            Here, the whole research implementation is done using python. There are different steps involved to get the entire research work done which is as follows:</p>''',
                 unsafe_allow_html=True)
        col4, col5, col6 = st.beta_columns((2, 2, 2))
        with col5:
            st.image(img3, use_column_width=True)
        st.write('''<b><h4>1. Acquire Personality Dataset</h4></b>''', unsafe_allow_html=True)
        st.write('''<p>The kaggle machine learning  is a collection of datasets, data generators which are used by machine learning community for analysis purpose. 
            The personality prediction dataset is acquired from the kaggle website. This dataset was collected (2016-2018) through an interactive on-line personality test. The personality test 
            was constructed from the IPIP. The personality prediction dataset can be downloaded in zip file format just by clicking on the link available. 
             The personality prediction file consists of one subject CSV files (data-final.csv). The data-final.csv file has 89227 missing values, 50 attributes, and classification, regression-related tasks. 
            Also, the dataset has multivariate characteristics. Here, data-preprocessing is done for checking inconsistent behaviors or trends.</p>''',
                 unsafe_allow_html=True)
        st.write('''<b><h4>2. Data preprocessing</h4></b>''', unsafe_allow_html=True)
        st.write('''<p>After, Data acquisition the next step is to clean and preprocess the data. 
            The Dataset available has numerical type features. 
            Also, a new column Cluster have been created using all question columns. 
            The target value is a five-level classification consisting of 0 i.e. cluster '0' to 4 i.e. cluster '4'. 
            The preprocessed dataset is further split into training and testing datasets. 
            This is achieved by passing feature value, target value, test size to the train-test split method of the scikit-learn package. 
            After splitting of data, the training data is sent to the following k-mean design i.e. k-mean is used for training the artificial neural networks then test data is used to predict the accuracy of the trained network model.</p>''',
                 unsafe_allow_html=True)
        st.write('''<b><h4>3. Feature Extraction</h4></b>''', unsafe_allow_html=True)
        st.write('''<p>The following items were presented on one page and each was rated on a five point scale using radio buttons. The order on page was  EXT1, AGR1, CSN1, EST1, OPN1, EXT2, etc.
                    The scale was labeled 1=Disagree, 3=Neutral, 5=Agree


                    EXT1	I am the life of the party.
                    EXT2	I don't talk a lot.
                    EXT3	I feel comfortable around people.
                    EXT4	I keep in the background.
                    EXT5	I start conversations.
                    EXT6	I have little to say.
                    EXT7	I talk to a lot of different people at parties.
                    EXT8	I don't like to draw attention to myself.
                    EXT9	I don't mind being the center of attention.
                    EXT10	I am quiet around strangers.
                    EST1	I get stressed out easily.
                    EST2	I am relaxed most of the time.
                    EST3	I worry about things.
                    EST4	I seldom feel blue.
                    EST5	I am easily disturbed.
                    EST6	I get upset easily.
                    EST7	I change my mood a lot.
                    EST8	I have frequent mood swings.
                    EST9	I get irritated easily.
                    EST10	I often feel blue.
                    AGR1	I feel little concern for others.
                    AGR2	I am interested in people.
                    AGR3	I insult people.
                    AGR4	I sympathize with others' feelings.
                    AGR5	I am not interested in other people's problems.
                    AGR6	I have a soft heart.
                    AGR7	I am not really interested in others.
                    AGR8	I take time out for others.
                    AGR9	I feel others' emotions.
                    AGR10	I make people feel at ease.
                    CSN1	I am always prepared.
                    CSN2	I leave my belongings around.
                    CSN3	I pay attention to details.
                    CSN4	I make a mess of things.
                    CSN5	I get chores done right away.
                    CSN6	I often forget to put things back in their proper place.
                    CSN7	I like order.
                    CSN8	I shirk my duties.
                    CSN9	I follow a schedule.
                    CSN10	I am exacting in my work.
                    OPN1	I have a rich vocabulary.
                    OPN2	I have difficulty understanding abstract ideas.
                    OPN3	I have a vivid imagination.
                    OPN4	I am not interested in abstract ideas.
                    OPN5	I have excellent ideas.
                    OPN6	I do not have a good imagination.
                    OPN7	I am quick to understand things.
                    OPN8	I use difficult words.
                    OPN9	I spend time reflecting on things.
                    OPN10	I am full of ideas.
                    ''',
                 unsafe_allow_html=True)
        st.write('''<b><h4>4. Training the classifer</h4></b>''', unsafe_allow_html=True)
        st.write(
            '''<p>Kmean clustering is used for creating the cluster for which personality belongs. Kmeans is implemented using sklearn.cluster using Kmeans function accepting n_cluster as 5 since 5 personality traits are present.</p>''',
            unsafe_allow_html=True)
        st.write('''<b><h4>5. Testing and Classified Output</h4></b>''', unsafe_allow_html=True)
        st.write('''<p>After the training of the designed neural network, the testing of K-mean is performed using silhouette score. Since in our dataset labelled data is not present so silhoutte score is used for finding the compatibility and effectiveness of the model. 
            Based on silhouette score,  the accuracy of the K-mean classifier is determined. From sklearn.metric calling the silhoutte_score() function accepting parameters features , predicted labels, metrics and sample_size the score is evaluated.</p>''',
                 unsafe_allow_html=True)
