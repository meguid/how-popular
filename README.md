# how-popular
Using Machine Learning to predict how popular would you be based on your body measurements data compared to 8000 celebrities real data

## To-Do:

- [x] Parsing Data
  - [x] Celebrities
  - [x] Celebrities biography
  - [x] Body measurements
  - [x] Popularity
- [x] Prediction
  - [x] Calculating features impressions
  - [x] Calculate Score
  - [x] Calculate ranks
  - [x] Compete with other celebrities
- [x] Plotting Data
  - [x] Generate training sets as vectors
  - [x] Plotting celebrities data
  - [x] Plotting top 200 (in no. of fans) celebrities data
- [x] Linear Regression (so far not the best option for accurate results, still searching!!!)
- [ ] Apply more examples using other celebrities data that we already parsed

## Requirements
- [x] Python
- [x] Octave-GUI
- [x] Selenium
- [x] lxml
- [x] requests


## Installation

  ```bash
  sudo pip install selenium
  sudo apt-get install python-lxml
  sudo pip install requests
  ```
  
## Usage
  **`First run the prediction algorithm and enter your measurements.`** 
  ```
  python predict.py
  Please enter your body measurments in this order [Cup Bust Waist Hip]
  B 34 26 32
  ```
  
  **`Your Results`** 
  
  GOOO GIRL, You scored 59%. You're in the top 62% of all celebrities and ranked with propability higher than or equal to Beyonce Knowles, Kim Kardashian West, Ariana Grande, Amanda Bynes, and Jennifer Lopez

## Plots 
  **`We can easily see the pop culture effect on women body image through this charts.`** 

- Bust Size against popularity.
<img src="/Assets/bust.png">

- Bust Size against popularity. (Data for top 200 celebrities in number of fans)

  **`Every female celebrity in the 200 most popular has a range of 30:38 inches Bust size.`** 

<img src="/Assets/bust200.png">

- Waist Size against popularity.
<img src="/Assets/waist.png">

- Waist Size against popularity. (Data for top 200 celebrities in number of fans)

  **`Every female celebrity in the 200 most popular has a range of 20:30 inches Waist size.`** 

<img src="/Assets/waist200.png">

- Hip Size against popularity.
<img src="/Assets/hip.png">

- Hip Size against popularity. (Data for top 200 celebrities in number of fans)

  **`Kinda Every female celebrity in the 200 most popular has a range of 30:40 inches Hip size.`** 

<img src="/Assets/hip200.png">

  **`Nicki Minaj Breaking The Norm.`** 

<img src="/Assets/nicki.png">

- Cup Size against popularity.
<img src="/Assets/cup.png">

- Cup Size against popularity. (Data for top 200 celebrities in number of fans)

  **`C is taking over.`** 

<img src="/Assets/cup200.png">

- Ethnicity against popularity.
<img src="/Assets/ethnicity.png">

- Ethnicity against popularity. (Data for top 200 celebrities in number of fans)

  **`White domination?`** 

<img src="/Assets/ethnicity200.png">
