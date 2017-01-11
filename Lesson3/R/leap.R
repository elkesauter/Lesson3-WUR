leap<- function(x) {
  # Function to calculate if a given year(x) is a leap year
  # x (numeric) is the year you  select
  if(!is.numeric(x)) {
    warning("x must be of class numeric")
    
  } else { # x is numeric
    mod4=x%%4
    mod100=x%%100
    mod400=x%%400
    yearValue<-FALSE
    #test<-"test value"
    
    if(mod4!=0){
      yearValue<-FALSE
    }
    
    else if(mod100!=0){
      yearValue<-TRUE
    }
    else if(mod400!=0){
      yearValue<-FALSE
    }
    else{
      yearValue<-TRUE
    } 
    
  }  
  
  return(yearValue)
}


