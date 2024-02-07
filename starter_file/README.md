*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Predicting Amphorae Stamps

This project explores modeling trade during the Roman Empire.  Using one of the largest datasets of open source classical ceramic data, I attempt to train machine learning models to predict stamp based on based on the distribution of Dressel-20 amphorae as they expressed in the archaeological record.    In archaeology, provenance is everything - to excavate is to destroy that data.  Fortunately, provenance is captured in this dataset by artifact coordinates.  However, many of these vessels include an alphanumeric stamp near one of their handles (Rubio-Camprillo et al., 2018).  Rubio-Campillo et al. suggested these stamps may be used as a proxy for determining trade routes and connectivity between regions of the empire, however, nearly 25% stamps and many more vessels lack stamps entirely (2018).  The ability to reconstruct missing/damaged stamps may improve our understanding and challenge assumptions regarding economic activity during this period.

## Dataset

### Overview
*TODO*: Explain about the data you are using and where you got it from.
This dataset was uploaded to github here (https://github.com/xrubio/ecologyStamps/blob/master/data/stamps.csv)
The dataset was published to support the following article (https://www.sciencedirect.com/science/article/pii/S0305440318300463?via%3Dihub):
Rubio-Campillo, X., Montanier, J. M., Rull, G., Lorenzo, J. M. B., Díaz, J. M., González, J. P., & Rodríguez, J. R. (2018). The ecology of Roman trade. Reconstructing provincial connectivity with similarity measures. Journal of Archaeological Science, 92, 37-47.

stamps.csv includes coordinates ('lat', 'long'), site, province ('name') and stamp code ('code').
This dataset was filtered for Dressel-20 vessels and for stamp codes which occur at least 20 times to focus on more common economic activity.  

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.
In archaeology, provenance is everything - to excavate is to destroy that data.  Fortunately, provenance is captured in this dataset by artifact coordinates.  However, many of these vessels include an alphanumeric stamp near one of their handles (Rubio-Camprillo et al., 2018). 


These models will predict stamp code using the following features: latitute, longitude, site, province.  

One model will bill be trained using Automated ML and the other model will explore hyerparameters of a RandomForestClassifier.  

### Access
*TODO*: Explain how you are accessing the data in your workspace.



## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
Watch the video!

*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

