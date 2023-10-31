It should describe what type of data or behavior your API can accomplish for them
- This API will provide them with the top 20 most popular last names in
America as well as the population of each name

Directions on how to access said data
- In the URL, after /users/, enter the name that you are looking for. This will return
how popular the name is and the population holding the name.

Provide an API key for authenticating their request
python3class

Should have directions for at least two routes
/users/names
/users/lastnames/{name}


<h1 align="center">
  <br>
  LastNameAPI
  <br>
</h1>
<p align="center">
  <a href="https://cdn.discordapp.com/attachments/1091738497532055573/1164400017642110976/image.png?ex=65431305&is=65309e05&hm=559c457543f5b9d672dd6998b6045cd4c474dadcf4dbaccc1c511499852e0e4e&">
    <img src="https://cdn.discordapp.com/attachments/1091738497532055573/1164400017642110976/image.png?ex=65431305&is=65309e05&hm=559c457543f5b9d672dd6998b6045cd4c474dadcf4dbaccc1c511499852e0e4e&" width="200">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •

## Key Features

* Name - Gives a list of most popular last names in the US

* Rank - Gives the rank of how popular that particular name is
  
* Total - Gives the total number of people with the name in the US


## How To Use

To run this API, you need to have an API key.

Here is the current API key:

- python3class

Then, use that API key to properly load these paths listed below.

Directions for using the API key are included in the Note at the bottom
```
# Get a list of the available last names
/names
```
```
# Get the stats of a specific last name from the list
/lastnames/{name}

# parameter {name}: this is where you put your name of choice, hopefully its on the list!
```


## Example:
```
10.6.20.72:8000/lastnames/Smith



# Will return with:

{"name":"Smith","rank":1,"total":2406257}
```



‎
> **Note**
> 
>Be sure to end your route with the API key like this: ?api_key={API_KEY}
>* If you do not use one of the API keys provided, the API will not work.


