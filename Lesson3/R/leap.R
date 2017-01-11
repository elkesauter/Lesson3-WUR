leap<- function(x) {
  # Function to calculate if a given year(x) is a leap year
  # x (numeric) is the year you  select
  if(!is.numeric(x)) {
    warning("x must be of class numeric")
    
  #calculation of leap year
    
  } else { # x is numeric
    
    #calculate modulus of 4,100 and 400
    mod4=x%%4
    mod100=x%%100
    mod400=x%%400
    
    #assume first all years are not leap years (common years=FALSE) 
    yearValue<-FALSE
 
    
    #if year is not divisible by 4 it is a common year 
    if(mod4!=0){
      yearValue<-FALSE
    }
    
    #if year is not divisible by 100 it is a leap year 
    else if(mod100!=0){
      yearValue<-TRUE
    }
    
    #if year is not divisible by 400 it is a common year 
    else if(mod400!=0){
      yearValue<-FALSE
    }
    
    #otherwise it is a leap year
    else{
      yearValue<-TRUE
    } 
    
  }  
  
  return(yearValue)
}


