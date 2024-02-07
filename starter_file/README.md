# Predicting Amphorae Stamps

This project explores modeling trade during the Roman Empire.  Using one of the largest datasets of open source classical ceramic data, I attempt to train machine learning models to predict stamp based on based on the distribution of Dressel-20 amphorae as they expressed in the archaeological record.    In archaeology, provenance is everything - to excavate is to destroy that data.  Fortunately, provenance is captured in this dataset by artifact coordinates.  However, many of these vessels include an alphanumeric stamp near one of their handles (Rubio-Camprillo et al., 2018).  Rubio-Campillo et al. suggested these stamps may be used as a proxy for determining trade routes and connectivity between regions of the empire, however, nearly 25% stamps and many more vessels lack stamps entirely (2018).  The ability to reconstruct missing/damaged stamps may improve our understanding and challenge assumptions regarding economic activity during this period.

## Dataset

### Overview
This dataset was uploaded to github here (https://github.com/xrubio/ecologyStamps/blob/master/data/stamps.csv)
The dataset was published to support the following article (https://www.sciencedirect.com/science/article/pii/S0305440318300463?via%3Dihub, Rubio-Camprillo et al., 2018)

stamps.csv includes coordinates ('lat', 'long'), site, province ('name') and stamp code ('code').
This dataset was filtered for Dressel-20 vessels and for stamp codes which occur at least 20 times to focus on more common economic activity.   Dressel-20 vessels were selected based on a 2017 study by  Rubio-Camprillo et. al. which tested theories regarding  Roman olive oil trade through Bayesian modeling codes associated with these vessel types found at Mount Testaccio.  This experiment essentially attempts to reverse engineer Rubio-Camprillo et al's findings.  

### Task
In archaeology, provenance is everything - to excavate is to destroy that data.  Fortunately, provenance is captured in this dataset by artifact coordinates.  However, many of these vessels include an alphanumeric stamp near one of their handles (Rubio-Camprillo et al., 2018). 


These models will predict stamp code using the following features: latitute, longitude, site, province.  

One model will bill be trained using Automated ML and the other model will explore hyerparameters of a RandomForestClassifier.  

### Access
While the data is accessable via github (see link above), my scripts will register the dataset within an Azure Workspace.

## Automated ML
The automl settings used for this experiment were:
    Primary Metric: Accuracy
    Validation: Monte Carlo Cross Validation
    Iteration timeout minutes: 25
    Experiment timeout hours: 3.5
    Early Stopping: True

Accuracy was selected as a primary metric so that the model wouldbe directly comparable with the other model.  Accuracy is appropriate because this model endeavors for overall correctness, rather than detecting a specific class or subset of data. 

Monte Carlo cross validation was selected over k-fold to add an element of randomness to the model.  Monte Carlo validations randomly select sub-samples of data for the validation set, which aptly reflects the seemingly randomness of archaeological preservation.  

Early Stopping was enabled to conserve resources such that the experiment would terminate poor performing models early and instead continue generating additional models to test.

Iteration timeout and experiment timeout limits were imposed based on resource constrictions of the environment.  

### Results
The best performing model had an accuracy of ~60.8%.
The best algorithm was voting ensemble which derrived from MaxAbsScaler, ExtremeRandomTrees and MaxAbsScaler XGBoostClassifier. 

I'm very surprised that each of these algorithms would change the directional value of coordinates, as many locations would be incorrect.  Given the landmass covered, I would expect that this error would be larger for the latitude values.  To improve this model in future, I would shift coordinates so that they were not centered around (0,0) and instead about a midpoint.  

Here are screenshots of the Run Details widget-
[!screenshot1](https://github.com/torijule/nd00333-capstone/blob/master/screenshots/AutoRunDetailsRunning.png)
[!screenshot2](https://github.com/torijule/nd00333-capstone/blob/master/screenshots/AutoMLRunDetailsComplete.png)

Model results-
Best model:
[!screenshot3](https://github.com/torijule/nd00333-capstone/blob/master/screenshots/Best%20AutoMLModel.png)

Best model algorithm:
[!screenshot4](https://github.com/torijule/nd00333-capstone/blob/master/screenshots/AutoMLDetails.png)
[!screenshot5](https://github.com/torijule/nd00333-capstone/blob/master/screenshots/AutoMLEnsembleDetails.png)

Model parameters:
[!screenshot6](https://github.com/torijule/nd00333-capstone/blob/master/screenshots/AutoMLConfigSettings.png)

## Hyperparameter Tuning
I chose to use a RandomForestClassifier to predict the stamp codes because I thought a forest classification algorithm would nicely mimic the fabric of inherant variance with regards to socioeconomic factors and various actors which influence economic activity.  Random forest classifiers are often successful in modeling consumer behavior.  These models are also highly scalable, customizable, and very efficient.  

### Results
The hyperparameter model was not as accurate as the model trained by AutoML.  This model only reported an accuracy of ~8%.   Random parameter sampling was leveraged to select hyperparameter values.  This is advantageous because it allows us to test a wide range of hyperparameters and look for quick optimization trends/opportunities, without needing to experiment with every possible parameter combination as in a GridSearch.  

The variables selected for hyperparameter turning were:
     Estimators (50 - 500)
     Leaves (1 - 20)
     Max Depth (5-500)

While a wide range of hyperparameter settings were tested, none of them performed well.  I would instead use attempt Bayesian analysis to test specific economic models, as suggested in Rubio-Camprillo, 2017, rather than looking at overarching patterns.  I additionally believe that this dataset would be much improved given a time dimension.  Stamps are associated with specific persons and therefore, specific windows in time.  An estimated timerange based on vessel matrix or disposition may aid results.

The below screeshot shows the completed hyperdrive job through the azure UI.  It displays the values used in the top performing jobs and their respective accuracies.
![screenshot10](https://github.com/torijule/nd00333-capstone/blob/master/screenshots/CompletedHyperJob.png)
![screenshot9](https://github.com/torijule/nd00333-capstone/blob/master/screenshots/HyperGraphs.png)

The best performing hyperparameter run:
![screenshot10](https://github.com/torijule/nd00333-capstone/blob/master/screenshots/BestHyperModel.png)

Run Details:
![screenshot7](https://github.com/torijule/nd00333-capstone/blob/master/screenshots/HyperRunDetails2.png)
![screenshot8](https://github.com/torijule/nd00333-capstone/blob/master/screenshots/HyperRunDetailsInProgress.png)


## Model Deployment

The best model, the AutoML model, was deployed.

The model may be queried in the following format:
{
  "data": [
    {
      "id": 0,
      "lat": 0.0,
      "long": 0.0,
      "site": "example_value",
      "province": "example_value"
    }
  ],
  "method": "predict"
}

Please see the below example for leveraging the model with sample input:
[!screenshot11](https://github.com/torijule/nd00333-capstone/blob/master/screenshots/EndpointSample.png)


## Screen Recording
Watch the video!  https://drive.google.com/file/d/1Twoxe2LmAZIfKf4xrd1I326_LfVXdk_8/view?usp=sharing

## References
Rubio-Campillo, X., Coto-Sarmiento, M., Pérez-Gonzalez, J., & Remesal Rodríguez, J. (2017). Bayesian analysis and free market trade within the Roman Empire. Antiquity, 91(359), 1241–1252. doi:10.15184/aqy.2017.131

Rubio-Campillo, X., Montanier, J. M., Rull, G., Lorenzo, J. M. B., Díaz, J. M., González, J. P., & Rodríguez, J. R. (2018). The ecology of Roman trade. Reconstructing provincial connectivity with similarity measures. Journal of Archaeological Science, 92, 37-47.


