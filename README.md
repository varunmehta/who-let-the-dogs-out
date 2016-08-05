The idea is to integrate with an [Amazon Dash button](https://aws.amazon.com/iot/button/) and put an alarm for kids in the morning. 

# What is a sleep cycle ?
 For an average person a full sleep cycle lasts about 90 minutes and is normally repeated several times each night. 
 So if you want to wake up at 6:00 AM, then sleeping at 9:00 PM or 10:30 PM or 12:00 AM or 1:30 AM would allow you to 
 wake up without feeling groggy. You should sleep an average of 5-6 sleep cycles per night, in order to have proper rest.
 
 Kids need an average of 10-14 hours of sleep as per their age. For my kids around 7 sleep cycles (10.5 hours) should be 
 good, but there is a wake up time restriction around 7:00 due to school starting at 8:20. They have to leave home by 8:00. 
 Back track the wake up time is good for 7:00 AM, so the idea is to calculate a sleep cycle that let's them wake up at 7:00 AM 
 (+/- 15 minutes)   
 

# What am I trying to do ?
 My kids are small and still getting used to the idea of waking up early. The idea is to put a schedule around them to 
 sleep and wake up on time. Kids are bad at reading time, and really hate going to bed, and once they do, don't want to 
 get out! 

 Here comes the role of sleep cycles. I want my kids to wake up nice and fresh at the end of their sleep.
 
# Amazon Dash + Raspberry Pi 
 Single click the button to register the kids have slept, calculate what time the kids need to wake up and register a 
 cron job to play music at that time in the morning (more on that later)
  
 Double click to kill the music if running. 
   
 Long click for emergency music.

# Why the name  ?
 Cos that is the wake up song played :)