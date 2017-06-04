
Data temp;
SET HOTEL_DATA;
numOverall = Overall * 1;
numValue = Value * 1;
numRooms = Rooms * 1;
numLoc = Location * 1;
numClean = Cleanliness * 1;
numCheck_In = Check_In * 1;
numServices = Services * 1;
numBusiness_Services = Business_Services * 1;
numSentiment = Sentiment * 1;
if Hotel_id ^= 'HotelID';
RUN;


proc contents data = temp;
run;

proc logistic data= temp;
CLASS Overall (ref = "5") Rooms (ref = "5") Location (ref = "5") Check_In (ref = "5") Services (ref = "5") Business_Services (ref = "5") Sentiment (ref = "0") /param = ref; 

model numOverall = numValue numRooms numLoc numClean numCheck_In Services numBusiness_Services numSentiment/ link= glogit;
run;

