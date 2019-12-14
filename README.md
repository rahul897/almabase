# time to book uber

entry endpoint - /remind

### Models
- User(email,source(lat,long),destination(lat,long),time(remind time),traveltime,Level(time offset from 1 hr),checked(whether current level is checked))
- Action(email,api,time(time of action)

Was unable to setup Socketio to show action in seperate div,Instead every minute page is refreshed to show actions

Algorithm to check time
> while adding remind submitted,traveltime is calculated from api and stored along with time
>
>every minute a scheduler runs and picks earliest 10 remind times and calculate
>timeleft = now - travaltime
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
    python app