from website import myweb
from website import db
from website.models import City
from flask import render_template, flash, redirect
from website.forms import TopCities


@myweb.route("/all")
def all():
    allCity = City.query.all()
    return render_template('allcities.html', allCity = allCity) 



@myweb.route("/visited")
def visited():
    visitedCity = []
    allCity = City.query.all() 
    for city in allCity:
        if city.visited:
             visitedCity.append(city.cityname)

    return render_template('visited.html', visitedCity = visitedCity)

@myweb.route("/", methods = ['GET', 'POST'])
def home():
    title = 'Top Cities'
    top_cities = ["Paris", "London", "Rome", "Kathmandu"]
    form = TopCities()

    #check to see if user-input is already in the database



    #if form is validated and there is no duplicate in city name
    if form.validate_on_submit() and (not alreadyInDatabase(form.cityname.data) and validCityName(form.cityname.data)):

        #then add the city into the DataBase
        addcity = City(cityname = form.cityname.data, cityrank = form.cityrank.data, visited = form.visited.data)
        db.session.add(addcity)
        db.session.commit()
        flash(f'{form.cityname.data} was added as rank {form.cityrank.data} and Visited = {form.visited.data}')
    
    elif (form.cityname.data == None and form.cityrank.data == None and form.visited.data == None):
        redirect('/')
    
    elif alreadyInDatabase(form.cityname.data):
        flash(f'{form.cityname.data} was NOT added as it is a duplicate.')

    redirect('/')
    return render_template('home.html', title = title, top_cities = top_cities, form = form)

def alreadyInDatabase(inputValue):
    dbCity = City.query.all()

    for c in dbCity:
        if c == None or inputValue == None:
            return False
        if c.cityname.lower() == inputValue.lower():
            return True

def validCityName(inputValue):
    if inputValue == None:
        return True
        
    return inputValue.isalpha()