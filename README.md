# DS6014 Final Project

# Predicting Rainfall in Australia

Members: Gaurav Anand, Vasudha Manikandan, John Zhang, Summer Chambers

## Motivation   
The prediction of rainfall presents a serious concern for many entities in goverment and risk
management, as well as researchers involved in weather forecasting research in the scientific
community. Rainfall has impacts on many human industries like crop production, hydroelectric power
generation and forestry and can help mitigate forest fires which can devastate wildlife and agriculture
in many countries. This is especially true in Australia where more recently both artificial and natural
wildfires have devastated the Australian wildlife and fauna and pose a huge threat to both human
and animal lives. The 2019-2020 Australian bushfire season resulted in the loss of close to 3000
homes, deaths of 30 firefighters as well as the death of over 1.25 billion wild animals.(1) Rain has
been shown to play an important part in decreasing the chances of wildfires occuring as well as the
extent of damage caused by them.(2) Thus the forecasting of rain through the use of daily
meteorological data can be very useful for organizations involved in agricultural practises, wildfire
mitigation and control, and general weather knowledge.

## Dataset   
The dataset that we have chosen to use for this task is publicly available on [Kaggle](https://www.kaggle.com/jsphyg/weather-dataset-rattle-package). The data contains
a binary response variable on whether it will ('Yes') or won't ('No') rain the next day as well as 24
features such as location, temperature, wind speed, wind direction, etc. The data contains the
city/county as well as the date for which the data was recorded from various Australian weather
stations across the continent.

## Methods   
Our group hopes to use Bayesian Logistic Regression in order to understand the uncertainty in
predicting whether or not it will rain tomorrow. We also aim to study the uncertainty around our
parameter estimates and use them in informing future models. Based on these results, we also hope
to use Bayesian Model Averaging to select the model which performs best with a given set of
features.

## References   
1. 2019–20 Australian bushfire season. (2020, November 29). Retrieved December 01, 2020, from https://en.wikipedia.org/wiki/2019%E2%80%9320_Australian_bushfire_season   
2. Holden, Z., Swanson, A., Luce, C., Jolly, W., Maneta, M., Oyler, J., . . . Affleck, D. (2018, September
04). Decreasing fire season precipitation increased recent western US forest wildfire activity.
Retrieved December 01, 2020, from https://www.pnas.org/content/115/36/E8349.short   
3. https://www.kaggle.com/jsphyg/weather-dataset-rattle-package
4. https://stackoverflow.com/questions/44124436/python-datetime-to-season 
5. http://www.bom.gov.au/climate/glossary/seasons.shtml  