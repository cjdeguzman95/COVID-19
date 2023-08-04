# Predicting the end of the Covid-19 Pandemic in the UK

As part of our final project at Sparta Global, I analysed data from the John Hopkins API to predict when the pandemic will end in the UK using logistic regression. This theory had several assumptions, one being that the entire population is infected and therefore the pandemic will end when no new infections are reported. 

Back in May 2020 when we presented our final project, the model predicted it would be <i>3 years</i> before the UK sees the end of COVID-19. This prediction seemed unbelievable at the time however as I'm writing this description in 2023 that seemed about right!

### How it works
 1. Data is ingested from the API and saved under a CSV. You can view the code [here](https://github.com/cjdeguzman95/COVID-19/blob/master/api_data/src/covid_data_with_cumulate.py)
 2. Data is then loaded into the logistic model and a graph pops up to show when infections will plateau. You can view the code [here](https://github.com/cjdeguzman95/COVID-19/blob/master/Logistic_Model_Coloured.py)
