# Dictionaries and sets

## Dictionaries homework

Using data from [Eurostat](https://appsso.eurostat.ec.europa.eu/nui/show.do?lang=en&dataset=hlth_silc_01), create a list of tuples representing the **"Self-perceived health by country and sex, age group >16, for people living in cities"** for 2017-2018. Have at least 30 values in your dataset.

The dataset will have the following struncture:
> [
> (country, year, sex, health_index)
> ]

Example:
> [('France', 2017, M, 12), ...]

Using only comprehensions, create the following dicts:
- two dicts that group all data by country for each year
> health_index_2017 = {'France': [sex, health_index]}
>
> health_index_2018 = {'France': [sex, health_index]}
- one dict that groups all data by year for Germany
> germany = {2017: [sex, health_index]}
- one dict that grups all data by country and year, by using year in the key together with the country name
> health_index = {'France_2017': [year, sex, health_index]}
- starting from the previous **health_index** dict, display only the data where the health_index > 5
- starting from the previous **health_index** dict, display only the data where the health_index > 5 and sex is 'F'
- starting from the previous **health_index** dict, create a for loop to print the health_index


## Sets homework

Create two sets with 10 numbers each (some of the numbers should be present in both sets). With these two sets, exemplify the following basic sets operations: union, intersection, difference and symetric difference.
