from website import create_app

app= create_app() 
if __name__== "__main__":
    
    app.run(debug=True)

#!line 1: I've imported my create_app whuch has be accessed by using from website which is the folder that i created.

#*line 3: I created a variable called app, then used an assignment operator and then accessed create_app and all the info inside using ()

#~line 4: then created an if statement where the name will do a comparison with the module created

#?line 6: then used the variable app and used the function run which will run the app and then enabled the debug if given.