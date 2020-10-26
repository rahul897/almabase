# time to book uber

entry endpoint - /remind

<iframe width="720" height="400" src="https://editor.p5js.org/p5/embed/rBqmyGZlS9"></iframe>

deployed at [bookuberab.herokuapp.com](https://bookuberab.herokuapp.com/remind)

### Models
- User(email,source(lat,long),destination(lat,long),time(remind time),traveltime,Level(time offset from 1 hr),checked(whether current level is checked))
User input eg.
email = rahul@uber.com
source = 12.927880,77.627600(comma sepearate lat&long)
destination = 13.035542,77.597100(comma sepearate lat&long)
time = 18:30 (H:M notation)
- Action(email,api,time(time of action)

Was unable to setup Socketio to show action in seperate div,Instead every minute page is refreshed to show actions

Algorithm to check time
> after submitting remind form,traveltime is calculated from api and stored along with time
>
>every minute a scheduler runs and picks earliest 10 remind times and calculate
>timeleft = now - traveltime
>
>if timeleft > 1hr/pow(2,level)
>get time to get uber and check timeleft - uber ~ 1min send mail
>else
>update traveltime and decrease level
>
>make sure each level is checked only once

Currently send mail functionality is not implemented instead just shown as action in 
bottom of app.
Ideally it should be pushed to message queue and processed.

To run the server

    pip install -r requirements.txt
    #python app db init
    #python app db migrate
    python app db upgrade
    python app
